# -*- coding: utf-8 -*-
"""
Voce narrante + timeline delle battute.

La voce NON è più fatta di battute sintetizzate una per una e unite con pause
fisse: il copione viene letto come UN testo continuo, così l'intonazione scorre
da una battuta all'altra (b16→b17 e b23→b24 sono una frase sola) e le pause sono
quelle del parlato: brevi dove la frase continua, un respiro a fine frase.
Pause oltre MAX_PAUSE vengono accorciate tagliando al centro del silenzio.
I confini delle battute si ricavano dai tempi che il motore restituisce (durate
per fonema di Kokoro, allineamento per carattere di ElevenLabs), rifiniti sulle
pause reali dell'audio: il cambio di battuta cade sempre dentro una pausa.

Motori (--engine):
  kokoro  PREDEFINITO. Kokoro-82M offline, voce italiana maschile "im_nicola",
          sintesi continua di tutto il copione. Installazione: ./setup_tts.sh
          (venv in tts/venv, modello in tts/kokoro). Variabili: KOKORO_VOICE, KOKORO_SPEED.
  eleven  ElevenLabs: UNA richiesta /with-timestamps per tutto il copione (o poche,
          per paragrafi, con previous_text/next_text). Serve ELEVENLABS_API_KEY;
          opzionali ELEVENLABS_VOICE_ID, ELEVENLABS_MODEL (default eleven_multilingual_v2),
          ELEVENLABS_OUTPUT_FORMAT (default mp3_44100_128).
  piper   Piper offline (voce riccardo x_low), una battuta alla volta (./setup_tts.sh piper).
  espeak  espeak-ng + mbrola, una battuta alla volta (ultima spiaggia, molto robotica).
  rec     registrazione propria: un file per battuta in rec/<id>.wav (o .mp3/.m4a...).

Uscite:
  audio/voiceover.wav  traccia unica, 44,1 kHz stereo, ~-15 LUFS integrati
  timeline.json        {"total", "engine", "beats": [{"id","visual","say","text",
                        "start","end","dur","s0","s1"}]}
     start/end : quando la battuta è a schermo; contigui (start_i = end_{i-1}),
                 il confine cade nella pausa, poco prima che parta la battuta dopo
     s0/s1     : istanti assoluti in cui la voce pronuncia la battuta (testo a macchina)
  audio/voice_report.json  pause, energia ai confini, loudness (per controllo)

Prova offline dei percorsi ElevenLabs e "rec" (risposte simulate, nessuna rete):
  python3 gen_audio.py --selftest
"""
import argparse
import array
import base64
import difflib
import glob
import json
import math
import operator
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scenes import BEATS  # noqa: E402

# ---------------------------------------------------------------- parametri comuni
LEAD = 0.12          # silenzio prima della prima parola
TAIL = 0.70          # dopo l'ultima parola: il testo finale resta un attimo a schermo
MAX_PAUSE = 0.45     # pause più lunghe vengono accorciate (al centro del silenzio)
FRAME = 0.01         # finestre da 10 ms per l'analisi dell'energia
QUIET_DB = -40.0     # "pausa" = frame almeno 40 dB sotto il frame più forte del file
QUIET_DB_2 = -30.0   # seconda soglia, per pause con respiro/rumore (ElevenLabs)
BOUNDARY_LEAD = 0.10  # il cambio di battuta cade al più 0,10 s prima dell'attacco successivo
TARGET_LUFS = -15.0
PEAK_LIMIT = 0.84    # -1,5 dBFS
SR_OUT = 44100
PUNCT = set(".,;:!?…—-\"'«»“”()")

# elaborazione leggera: niente compressione aggressiva (rende la voce metallica)
VOICE_CHAIN = ("highpass=f=60:p=2,"
               "equalizer=f=3500:t=q:w=0.9:g=1.5,"
               "acompressor=threshold=-24dB:ratio=2:knee=6:attack=15:release=250,"
               f"aresample={SR_OUT}:resampler=soxr:precision=28")

# ---------------------------------------------------------------- Kokoro
VENV = os.path.join(HERE, "tts", "venv")
KOKORO_MODEL = os.path.join(HERE, "tts", "kokoro", "kokoro-v1.0.onnx")
KOKORO_VOICES = os.path.join(HERE, "tts", "kokoro", "voices-v1.0.bin")
KOKORO_VOICE = os.environ.get("KOKORO_VOICE", "im_nicola")
KOKORO_SPEED = float(os.environ.get("KOKORO_SPEED", "1.0"))
KOKORO_S0_BIAS = 0.05  # l'inizio dato dal modello arriva in media ~50 ms dopo l'attacco reale
# Grafie usate SOLO per la sintesi Kokoro (G2P espeak-ng): il testo a schermo non cambia.
KOKORO_RESPELL = [
    (r"\bWhatsApp\b", "uotsàpp"),            # wˈɔʦ ˈapː (due parole) -> wotsˈapː
    (r"\bsegnati\b", "ségnati"),             # segnàti (participio) -> ségnati (imperativo)
    (r"\bAttenzione\b", "Attenzióne"),       # iato zi-o (5 sillabe) -> dittongo
    (r"\bmaggiorazione\b", "maggiorazióne"),  # idem
    (r"\bc'è\b", "cè"),                      # ʧe atona -> ʧˈɛ
    (r"\bpiù\b", "piú"),                     # pjʊ atona -> pjˈu
    (r"\bfai\b", "fài"),                     # fˈaːi -> dittongo
    (r"\bstipendio\b", "stipèndio"),         # e aperta
    (r"(?<![\w'])è\b", "èh"),                  # verbo "è": espeak lo fa atono (e), così è ˈɛ
]
# Correzioni sui fonemi: con le ɪ finali di espeak "Scrivici" viene capito "scriveci"
KOKORO_PHONFIX = {"skrˈiːvɪʧɪ": "skrˈiviʧi"}

# ---------------------------------------------------------------- Piper / espeak / rec
PIPER_BIN = os.path.join(HERE, "tts", "piper", "piper")
PIPER_MODEL = os.path.join(HERE, "tts", "it-riccardo_fasol-x-low.onnx")
PIPER_SPEED = 0.88   # length_scale < 1 = più veloce
# motori a battute separate: pausa dopo la battuta secondo la punteggiatura finale
GAP_BY_MARK = {",": 0.14, ";": 0.20, ":": 0.20, ".": 0.36, "?": 0.36, "!": 0.36, "…": 0.36}
GAP_DEFAULT = 0.14

# ---------------------------------------------------------------- ElevenLabs
EL_BASE = os.environ.get("ELEVENLABS_BASE_URL", "https://api.elevenlabs.io")
EL_DEFAULT_MODEL = "eleven_multilingual_v2"
EL_DEFAULT_FORMAT = "mp3_44100_128"
EL_MAX_CHARS = 4500  # sotto il limite per richiesta; il copione (~1.400 caratteri) sta in una
EL_LANG_MODELS = ("eleven_turbo_v2_5", "eleven_flash_v2_5")  # accettano language_code


def el_settings():
    """Impostazioni per una lettura naturale (non piatta, non teatrale)."""
    return {"stability": 0.48, "similarity_boost": 0.75, "style": 0.25,
            "use_speaker_boost": True,
            "speed": float(os.environ.get("ELEVENLABS_SPEED", "1.0"))}


# ================================================================ utilità audio (solo stdlib)
def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, **kw)


def db2lin(db):
    return 10 ** (db / 20.0)


def lin2db(v):
    return 20 * math.log10(max(v, 1e-9))


def read_wav(path):
    """WAV PCM 16 bit -> (array 'h' mono, sr). I canali vengono mediati."""
    with wave.open(path, "rb") as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        if sw != 2:
            raise ValueError(f"{path}: atteso PCM 16 bit")
        data = array.array("h", w.readframes(w.getnframes()))
    if sys.byteorder == "big":
        data.byteswap()
    if ch > 1:
        data = array.array("h", (int(sum(data[i:i + ch]) / ch) for i in range(0, len(data), ch)))
    return data, sr


def write_wav(path, x, sr):
    y = array.array("h", x)
    if sys.byteorder == "big":
        y.byteswap()
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(y.tobytes())


def to_mono_wav(src, dst, sr=None, extra_in=()):
    cmd = ["ffmpeg", "-y", "-v", "error", *extra_in, "-i", src, "-ac", "1"]
    if sr:
        cmd += ["-ar", str(sr)]
    run(cmd + ["-c:a", "pcm_s16le", dst])


def frame_rms(x, sr, frame=FRAME):
    n = max(1, int(round(sr * frame)))
    mul = operator.mul
    out = []
    for i in range(0, len(x) - n + 1, n):
        c = x[i:i + n]
        out.append(math.sqrt(sum(map(mul, c, c)) / n))
    return out or [0.0]


def runs_of(mask):
    """[(k0, k1)] delle sequenze True, k1 escluso."""
    out, start = [], None
    for k, q in enumerate(mask):
        if q and start is None:
            start = k
        elif not q and start is not None:
            out.append((start, k))
            start = None
    if start is not None:
        out.append((start, len(mask)))
    return out


def fade(x, n, out=False):
    n = min(n, len(x))
    for j in range(n):
        g = (j + 0.5) / n
        k = len(x) - n + j if out else j
        x[k] = int(x[k] * ((1 - g) if out else g))
    return x


def splice(x, cuts, fade_n):
    """Toglie i tratti [a, b) (campioni), con dissolvenza incrociata breve."""
    out, pos = array.array("h"), 0
    for a, b in cuts:
        f = max(0, min(fade_n, a - pos, b - a))
        out.extend(x[pos:a - f])
        for j in range(f):
            r = (j + 0.5) / f
            out.append(int(round(x[a - f + j] * (1 - r) + x[b - f + j] * r)))
        pos = b
    out.extend(x[pos:])
    return out


def cut_mapper(cuts, sr):
    """Tempo originale -> tempo dopo aver tolto i tratti `cuts`."""
    def m(t):
        s = t * sr
        removed = 0
        for a, b in cuts:
            if s >= b:
                removed += b - a
            elif s > a:
                return (a - removed) / sr
        return (s - removed) / sr
    return m


# ================================================================ motori
def phonemizer_kokoro(k):
    from misaki.espeak import EspeakG2P
    g2p = EspeakG2P(language="it")
    vocab = k.tokenizer.vocab

    def phon(text):
        for pat, rep in KOKORO_RESPELL:
            text = re.sub(pat, rep, text)
        ps, _ = g2p(text)
        ps = " ".join("".join(c for c in ps if c in vocab).split())
        for a, b in KOKORO_PHONFIX.items():
            ps = ps.replace(a, b)
        return ps
    return phon


def synth_kokoro(out_dir, voice, speed):
    """Tutto il copione in UNA sintesi continua; tempi per battuta dalle durate del modello."""
    import numpy as np
    from kokoro_onnx import Kokoro
    for p in (KOKORO_MODEL, KOKORO_VOICES):
        if not os.path.exists(p):
            sys.exit(f"Manca {p}: lancia prima ./setup_tts.sh")
    k = Kokoro(KOKORO_MODEL, KOKORO_VOICES)
    if not k.has_timings:
        sys.exit("Il modello Kokoro non restituisce le durate: serve model-files-v1.1 (./setup_tts.sh)")
    if voice not in k.get_voices():
        sys.exit(f"Voce Kokoro '{voice}' assente. Voci italiane: if_sara, im_nicola")
    phon = phonemizer_kokoro(k)
    parts = [phon(b["say"]) for b in BEATS]
    offs, pos = [], 0
    for p in parts:
        offs.append(pos)
        pos += len(p) + 1
    full = " ".join(parts)
    t0 = time.time()
    audio, sr, tim = k.create_timed(full, voice, speed, is_phonemes=True, continuous=True,
                                    sentence_pause=0.25, clause_pause=0.1)
    calc = time.time() - t0
    if len(tim) != len(full):
        sys.exit(f"Kokoro: {len(tim)} tempi per {len(full)} fonemi, allineamento impossibile")
    spans = []
    for p, off in zip(parts, offs):
        a, b = off, off + len(p) - 1
        while b > a and (tim[b].phoneme in PUNCT or tim[b].phoneme == " "):
            b -= 1
        spans.append((tim[a].start, tim[b].end))
    pcm = (np.clip(audio, -1.0, 1.0) * 32767.0).round().astype("<i2")
    x = array.array("h")
    x.frombytes(pcm.tobytes())
    if sys.byteorder == "big":
        x.byteswap()
    info = {"engine": "kokoro", "voice": voice, "speed": speed, "model": os.path.basename(KOKORO_MODEL),
            "native_sr": sr, "compute_s": round(calc, 1), "phonemes": dict(zip((b["id"] for b in BEATS), parts))}
    print(f"Kokoro {voice} @ {speed}: {len(audio) / sr:.1f}s di parlato continuo in {calc:.1f}s "
          f"({len(full)} fonemi)")
    return x, sr, spans, info


def trim_quiet(x, sr, rel_db=QUIET_DB):
    """Toglie il silenzio in testa e in coda (soglia relativa al frame più forte)."""
    rms = frame_rms(x, sr)
    thr = max(rms) * db2lin(rel_db)
    loud = [k for k, v in enumerate(rms) if v > thr]
    if not loud:
        return x[:0], 0
    fs = int(round(sr * FRAME))
    a = max(0, loud[0] * fs - int(0.02 * sr))
    b = min(len(x), (loud[-1] + 1) * fs + int(0.06 * sr))
    y = array.array("h", x[a:b])
    fade(y, int(0.005 * sr))
    fade(y, int(0.01 * sr), out=True)
    return y, a


def synth_per_beat(engine, out_dir, rec_dir):
    """Una battuta alla volta (piper, espeak, rec), unite con pause secondo la punteggiatura."""
    sr = SR_OUT
    if engine == "piper" and not os.path.exists(PIPER_BIN):
        sys.exit("Piper non installato: lancia prima ./setup_tts.sh piper")
    x, spans = array.array("h"), []
    for i, b in enumerate(BEATS):
        mono = os.path.join(out_dir, f"_{b['id']}_mono.wav")
        if engine == "rec":
            found = sorted(glob.glob(os.path.join(rec_dir, b["id"] + ".*")))
            if not found:
                sys.exit(f"Manca la registrazione {rec_dir}/{b['id']}.wav")
            to_mono_wav(found[0], mono, sr)
        else:
            raw = os.path.join(out_dir, f"_{b['id']}_raw.wav")
            if engine == "piper":
                run([PIPER_BIN, "-q", "--model", PIPER_MODEL, "--length_scale", str(PIPER_SPEED),
                     "--sentence_silence", "0.12", "--output_file", raw], input=b["say"].encode("utf-8"))
            else:
                run(["espeak-ng", "-v", "mb-it4", "-s", "160", "-p", "50", b["say"], "-w", raw])
            to_mono_wav(raw, mono, sr)
            os.remove(raw)
        y, _ = trim_quiet(read_wav(mono)[0], sr)
        os.remove(mono)
        t0 = len(x) / sr
        x.extend(y)
        spans.append((t0, len(x) / sr))
        if i + 1 < len(BEATS):
            mark = b["say"].rstrip()[-1:]
            x.extend(array.array("h", bytes(2 * int(GAP_BY_MARK.get(mark, GAP_DEFAULT) * sr))))
    return x, sr, spans, {"engine": engine}


# ---------------------------------------------------------------- ElevenLabs
def el_http(method, path, key, body=None, query=None, timeout=300):
    """Chiamata REST ElevenLabs (sostituibile nei test). Ritorna il corpo in bytes."""
    url = EL_BASE + path + ("?" + urllib.parse.urlencode(query) if query else "")
    data = json.dumps(body).encode("utf-8") if body is not None else None
    for attempt in range(4):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("xi-api-key", key)
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read()[:600].decode("utf-8", "replace")
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(3 * 2 ** attempt)
                continue
            sys.exit(f"ElevenLabs {method} {path}: HTTP {e.code}\n{msg}")
        except urllib.error.URLError as e:
            if attempt < 3:
                time.sleep(3 * 2 ** attempt)
                continue
            sys.exit(f"ElevenLabs non raggiungibile ({e.reason}): la rete deve consentire api.elevenlabs.io")
    raise AssertionError("non raggiunto")


def el_pick_voice(key):
    forced = os.environ.get("ELEVENLABS_VOICE_ID")
    if forced:
        return forced, "ELEVENLABS_VOICE_ID"
    voices = json.loads(el_http("GET", "/v1/voices", key)).get("voices") or []
    if not voices:
        sys.exit("Nessuna voce nell'account ElevenLabs: imposta ELEVENLABS_VOICE_ID")

    def italian(v):
        labels = {str(k).lower(): str(val or "").lower() for k, val in (v.get("labels") or {}).items()}
        langs = {str(x.get("language", "")).lower() for x in (v.get("verified_languages") or [])}
        return ("italian" in labels.get("accent", "") or labels.get("language") in ("it", "italian")
                or "it" in langs or "italian" in langs)

    def score(v):
        labels = {str(k).lower(): str(val or "").lower() for k, val in (v.get("labels") or {}).items()}
        s = {"male": 10, "female": -10}.get(labels.get("gender"), 0)
        s += 8 if italian(v) else 0
        use = labels.get("use_case", labels.get("use case", "")).replace(" ", "_")
        s += 4 if use in ("narration", "narrative_story", "informative_educational",
                          "conversational", "social_media") else 0
        return s
    best = max(voices, key=score)
    if not italian(best):
        print("ATTENZIONE: nessuna voce italiana nell'account; uso "
              f"'{best.get('name')}'. Meglio scegliere una voce italiana nella Voice Library "
              "e impostare ELEVENLABS_VOICE_ID.")
    return best["voice_id"], best.get("name", "?")


def el_groups(says, max_chars):
    """Battute consecutive raggruppate entro max_chars, spezzando solo a fine frase."""
    groups, cur, size = [], [], 0
    for i, s in enumerate(says):
        n = len(s) + 1
        if cur and size + n > max_chars and says[cur[-1]].rstrip()[-1:] in ".?!…":
            groups.append(cur)
            cur, size = [], 0
        cur.append(i)
        size += n
    if cur:
        groups.append(cur)
    return groups


def el_char_times(text, alignment):
    """Per ogni carattere di `text`: (inizio, fine) dall'allineamento ElevenLabs."""
    chars = alignment["characters"]
    st = alignment["character_start_times_seconds"]
    en = alignment["character_end_times_seconds"]
    got = "".join(chars)
    if got == text and len(chars) == len(text):
        return list(zip(st, en))
    # testo restituito diverso (normalizzazione): mappa carattere per carattere
    idx = [None] * len(text)
    sm = difflib.SequenceMatcher(None, text, got, autojunk=False)
    # indice nel testo restituito -> indice nella lista dei caratteri
    ci, pos = [], 0
    for j, c in enumerate(chars):
        ci += [j] * len(c)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            idx[a + k] = ci[b + k]
    known = [i for i, v in enumerate(idx) if v is not None]
    if not known:
        raise ValueError("allineamento ElevenLabs non confrontabile col testo")
    out = []
    for i in range(len(text)):
        if idx[i] is None:  # prende il vicino noto più prossimo
            j = min(known, key=lambda k: abs(k - i))
            out.append((st[idx[j]], en[idx[j]]))
        else:
            out.append((st[idx[i]], en[idx[i]]))
    return out


def el_decode(audio_bytes, fmt, dst_wav, tmp):
    """Audio della risposta -> WAV mono 16 bit alla frequenza nativa del formato."""
    if fmt.startswith("pcm_"):
        sr = int(fmt.split("_")[1])
        x = array.array("h")
        x.frombytes(audio_bytes[:len(audio_bytes) // 2 * 2])
        if sys.byteorder == "big":
            x.byteswap()
        write_wav(dst_wav, x, sr)
        return
    src = tmp + "." + fmt.split("_")[0]
    with open(src, "wb") as f:
        f.write(audio_bytes)
    to_mono_wav(src, dst_wav)


def synth_eleven(out_dir):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY non presente: impostala nelle variabili d'ambiente.")
    model = os.environ.get("ELEVENLABS_MODEL", EL_DEFAULT_MODEL)
    fmt = os.environ.get("ELEVENLABS_OUTPUT_FORMAT", EL_DEFAULT_FORMAT)
    max_chars = int(os.environ.get("ELEVENLABS_MAX_CHARS", EL_MAX_CHARS))
    voice_id, voice_name = el_pick_voice(key)
    says = [b["say"].strip() for b in BEATS]
    groups = el_groups(says, max_chars)
    x, sr, spans = array.array("h"), None, []
    align_dump = []
    for gi, g in enumerate(groups):
        text = " ".join(says[i] for i in g)
        body = {"text": text, "model_id": model, "voice_settings": el_settings(),
                "seed": int(os.environ.get("ELEVENLABS_SEED", "1234"))}
        if gi > 0:
            body["previous_text"] = " ".join(says[:g[0]])[-1500:]
        if gi + 1 < len(groups):
            body["next_text"] = " ".join(says[g[-1] + 1:])[:1500]
        if model in EL_LANG_MODELS:
            body["language_code"] = "it"
        resp = json.loads(el_http("POST", f"/v1/text-to-speech/{voice_id}/with-timestamps", key,
                                  body, {"output_format": fmt}))
        al = resp.get("alignment") or resp.get("normalized_alignment")
        if not al:
            sys.exit("Risposta ElevenLabs senza allineamento")
        wav = os.path.join(out_dir, f"_eleven_{gi:02d}.wav")
        el_decode(base64.b64decode(resp["audio_base64"]), fmt, wav, os.path.join(out_dir, f"_eleven_{gi:02d}"))
        y, ysr = read_wav(wav)
        os.remove(wav)
        if sr is None:
            sr = ysr
        elif ysr != sr:
            sys.exit("ElevenLabs: frequenze diverse tra le parti")
        ct = el_char_times(text, al)
        base = len(x) / sr
        pos = 0
        for i in g:
            a, b = pos, pos + len(says[i])
            letters = [j for j in range(a, b) if says[i][j - a].isalnum()]
            spans.append((base + ct[letters[0]][0], base + ct[letters[-1]][1]))
            pos = b + 1
        x.extend(y)
        align_dump.append({"text": text, "alignment": al})
    with open(os.path.join(out_dir, "eleven_alignment.json"), "w") as f:
        json.dump(align_dump, f, ensure_ascii=False)
    print(f"ElevenLabs: voce {voice_name} ({voice_id}), modello {model}, {len(groups)} richieste")
    return x, sr, spans, {"engine": "eleven", "voice_id": voice_id, "voice": voice_name,
                          "model": model, "format": fmt, "requests": len(groups)}


# ================================================================ pause, confini, timeline
def shape(x, sr, spans, max_pause):
    """Accorcia le pause troppo lunghe, toglie il silenzio ai bordi, aggiunge attacco e coda."""
    rms = frame_rms(x, sr)
    thr = max(rms) * db2lin(QUIET_DB)
    n = len(rms)
    fs = int(round(sr * FRAME))
    cuts, capped = [], []
    for k0, k1 in runs_of([v <= thr for v in rms]):
        if k0 == 0 or k1 >= n:
            continue  # testa e coda: gestite sotto
        length = (k1 - k0) * FRAME
        if length > max_pause + 1e-6:
            half = int(max_pause / 2 * sr)
            cuts.append((k0 * fs + half, k1 * fs - half))
            capped.append((round(k0 * FRAME, 3), round(length, 3)))
    y = splice(x, cuts, int(0.005 * sr))
    cmap = cut_mapper(cuts, sr)
    y, head = trim_quiet(y, sr)
    lead = array.array("h", bytes(2 * int(LEAD * sr)))
    tail = array.array("h", bytes(2 * int(TAIL * sr)))
    out = lead + y + tail
    dur = len(y) / sr

    def m(t):
        return LEAD + min(max(cmap(t) - head / sr, 0.0), dur)
    return out, [(m(a), m(b)) for a, b in spans], capped


def place_beats(x, sr, spans, s0_bias):
    """s0/s1 per battuta e confini, dentro le pause reali dell'audio."""
    rms = frame_rms(x, sr)
    ref = max(rms)
    nfr = len(rms)
    runs40 = runs_of([v <= ref * db2lin(QUIET_DB) for v in rms])
    runs30 = runs_of([v <= ref * db2lin(QUIET_DB_2) for v in rms])

    def best_run(runs, lo, hi):
        k_lo, k_hi = int(lo / FRAME), int(math.ceil(hi / FRAME))
        best, score = None, (0, 0)
        for k0, k1 in runs:
            ov = min(k1, k_hi) - max(k0, k_lo)
            if ov > 0 and (ov, k1 - k0) > score:
                best, score = (k0, k1), (ov, k1 - k0)
        return best

    def level_at(t):
        k = min(nfr - 1, max(0, int(t / FRAME)))
        return lin2db(max(rms[max(0, k - 1):k + 2]) / ref)

    n = len(spans)
    s0 = [a - s0_bias for a, _ in spans]
    s1 = [b for _, b in spans]
    loud = [k for k, v in enumerate(rms) if v > ref * db2lin(QUIET_DB)]
    first_on, last_off = loud[0] * FRAME, (loud[-1] + 1) * FRAME
    if abs(first_on - s0[0]) <= 0.25:
        s0[0] = first_on
    s1[-1] = min(s1[-1], last_off)
    bounds, info = [], []
    for i in range(n - 1):
        a_next, b_cur = spans[i + 1][0], spans[i][1]
        lo, hi = min(a_next, b_cur) - 0.06, max(a_next, b_cur) + 0.06
        run_ = best_run(runs40, lo, hi) or best_run(runs30, lo, hi)
        if run_:
            q0, q1 = run_[0] * FRAME, run_[1] * FRAME
            if abs(q1 - s0[i + 1]) <= 0.25:
                s0[i + 1] = q1  # attacco acustico della battuta successiva
            bnd = max((q0 + q1) / 2, q1 - BOUNDARY_LEAD)
            s1[i] = min(s1[i], q0 + 0.05)
            pause = q1 - q0
        else:  # nessuna pausa: il punto più silenzioso tra le due battute
            k_lo, k_hi = int(lo / FRAME), max(int(lo / FRAME) + 1, int(math.ceil(hi / FRAME)))
            k = min(range(k_lo, min(k_hi, nfr)), key=lambda j: rms[j])
            bnd, pause = (k + 0.5) * FRAME, 0.0
        s1[i] = min(s1[i], bnd - 0.02)
        s0[i + 1] = max(s0[i + 1], bnd + 0.01)
        bounds.append(bnd)
        info.append({"after": BEATS[i]["id"], "boundary": round(bnd, 3), "pause": round(pause, 3),
                     "energy_db": round(level_at(bnd), 1), "fallback": not run_})
    return s0, s1, bounds, info


def loudness(path, af=None):
    """Loudness integrata (LUFS), LRA e true peak con il filtro ebur128 di ffmpeg."""
    chain = (af + "," if af else "") + "ebur128=peak=true:framelog=verbose"
    p = subprocess.run(["ffmpeg", "-nostats", "-v", "info", "-i", path, "-af", chain, "-f", "null", "-"],
                       capture_output=True, text=True, check=True)
    summ = p.stderr[p.stderr.rfind("Summary:"):]
    get = lambda pat: float(re.search(pat, summ).group(1))  # noqa: E731
    return {"I": get(r"I:\s+(-?[\d.]+) LUFS"), "LRA": get(r"LRA:\s+(-?[\d.]+) LU"),
            "peak": get(r"Peak:\s+(-?[\d.]+|-inf) dBFS")}


def master(src, dst):
    """Catena leggera + guadagno per -15 LUFS integrati + limitatore trasparente."""
    pre = loudness(src, VOICE_CHAIN)
    gain = TARGET_LUFS - pre["I"]
    for _ in range(3):
        af = (f"{VOICE_CHAIN},volume={gain:.2f}dB,"
              f"alimiter=limit={PEAK_LIMIT}:attack=5:release=60:level=0:latency=1")
        run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", af, "-ac", "2", "-ar", str(SR_OUT),
             "-c:a", "pcm_s16le", dst])
        post = loudness(dst)
        if abs(post["I"] - TARGET_LUFS) <= 0.3:
            break
        gain += TARGET_LUFS - post["I"]
    return post


def wav_duration(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def generate(engine, out_dir="audio", timeline_path="timeline.json", voice=KOKORO_VOICE,
             speed=KOKORO_SPEED, rec_dir="rec", max_pause=MAX_PAUSE, quiet=False):
    os.makedirs(out_dir, exist_ok=True)
    for old in glob.glob(os.path.join(out_dir, "b[0-9][0-9]*.wav")) + [os.path.join(out_dir, "concat.txt")]:
        if os.path.exists(old):
            os.remove(old)  # tracce per battuta del vecchio sistema: non servono più
    if engine == "kokoro":
        x, sr, spans, info = synth_kokoro(out_dir, voice, speed)
        bias = KOKORO_S0_BIAS
    elif engine == "eleven":
        x, sr, spans, info = synth_eleven(out_dir)
        bias = 0.0
    else:
        x, sr, spans, info = synth_per_beat(engine, out_dir, rec_dir)
        bias = 0.0

    y, spans, capped = shape(x, sr, spans, max_pause)
    s0, s1, bounds, binfo = place_beats(y, sr, spans, bias)
    edit = os.path.join(out_dir, "voice_edit.wav")
    write_wav(edit, y, sr)
    vo = os.path.join(out_dir, "voiceover.wav")
    loud = master(edit, vo)
    total = round(wav_duration(vo), 3)

    edges = [0.0] + [round(b, 3) for b in bounds] + [total]
    timeline = []
    for i, b in enumerate(BEATS):
        st, en = edges[i], edges[i + 1]
        timeline.append({"id": b["id"], "visual": b["visual"], "say": b["say"], "text": b["text"],
                         "start": st, "end": en, "dur": round(en - st, 3),
                         "s0": round(min(max(s0[i], st), en), 3), "s1": round(min(max(s1[i], st), en), 3)})
    tag = engine if engine != "kokoro" else f"kokoro-{voice}-{speed:.2f}"
    with open(timeline_path, "w") as f:
        json.dump({"total": total, "engine": tag, "beats": timeline}, f, indent=2, ensure_ascii=False)

    # pause interne tra una parola e l'altra (sul file finale, prima del mastering)
    rms = frame_rms(y, sr)
    thr = max(rms) * db2lin(QUIET_DB)
    pauses = [(k1 - k0) * FRAME for k0, k1 in runs_of([v <= thr for v in rms])[1:-1]]
    long_p = [p for p in pauses if p >= 0.2]
    report = {"engine": tag, **info, "total": total, "loudness": loud, "max_pause": max_pause,
              "capped_pauses": capped, "boundaries": binfo,
              "pauses_ge_200ms": {"n": len(long_p), "mean": round(sum(long_p) / max(1, len(long_p)), 3),
                                  "max": round(max(long_p or [0]), 3)}}
    with open(os.path.join(out_dir, "voice_report.json"), "w") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)

    if not quiet:
        print("DURATA TOTALE: %.2fs  (%d battute, motore %s)" % (total, len(timeline), tag))
        print(f"  loudness {loud['I']:.1f} LUFS, true peak {loud['peak']:.1f} dBFS, LRA {loud['LRA']:.1f} LU;"
              f" pause accorciate a {max_pause}s: {len(capped)}")
        for i, b in enumerate(timeline):
            extra = ""
            if i < len(binfo):
                bi = binfo[i]
                extra = f"  pausa dopo {bi['pause']:.2f}s, energia al confine {bi['energy_db']:6.1f} dB"
                extra += "  [NESSUNA PAUSA]" if bi["fallback"] else ""
            print(f"  {b['id']}  {b['visual']:9s} [{b['start']:6.2f} → {b['end']:6.2f}]"
                  f"  voce {b['s0']:6.2f}–{b['s1']:6.2f}{extra}")
    return timeline, report


# ================================================================ prova offline (ElevenLabs simulato, rec)
def _tone_power(x, sr, f):
    """Potenza a frequenza f (Goertzel con finestra di Hann)."""
    n = len(x)
    if n < 2:
        return 0.0
    w = 2 * math.cos(2 * math.pi * f / sr)
    s1 = s2 = 0.0
    c = 2 * math.pi / (n - 1)
    for i, v in enumerate(x):
        s = v * (0.5 - 0.5 * math.cos(c * i)) + w * s1 - s2
        s2, s1 = s1, s
    return s1 * s1 + s2 * s2 - w * s1 * s2


def _selftest_signal(sr, lead=0.3, long_gap_after=5, short_gap_after=12):
    """Una 'voce' finta: ogni battuta è un tono con frequenza propria, pause note."""
    freqs = [310 + 67 * i for i in range(len(BEATS))]
    layout, t = [], lead
    for i, b in enumerate(BEATS):
        d = max(0.6, 0.03 * len(b["say"]))
        layout.append((t, t + d))
        t += d
        mark = b["say"].rstrip()[-1:]
        t += 0.9 if i == long_gap_after else 0.05 if i == short_gap_after else GAP_BY_MARK.get(mark, 0.14)
    n = int((t + 0.4) * sr)
    x = array.array("h", bytes(2 * n))
    for (a, b), f in zip(layout, freqs):
        i0, i1 = int(a * sr), int(b * sr)
        nf = int(0.01 * sr)
        for i in range(i0, i1):
            tt = (i - i0) / sr
            env = 0.55 + 0.45 * math.sin(2 * math.pi * 3.3 * tt) ** 2
            g = min(1.0, (i - i0) / nf, (i1 - i) / nf)
            x[i] = int(8000 * env * g * math.sin(2 * math.pi * f * tt))
    return x, layout, freqs


def _fake_alignment(text_parts, layout, t_offset):
    chars, st, en = [], [], []
    for k, (s, (a, b)) in enumerate(zip(text_parts, layout)):
        if k:
            chars.append(" ")
            st.append(layout[k - 1][1] - t_offset)
            en.append(a - t_offset)
        dt = (b - a) / len(s)
        for j, c in enumerate(s):
            chars.append(c)
            st.append(round(a + j * dt - t_offset, 3))
            en.append(round(a + (j + 1) * dt - t_offset, 3))
    return {"characters": chars, "character_start_times_seconds": st, "character_end_times_seconds": en}


def _check_output(tl_path, out_dir, freqs, long_gap_after, errs, label):
    tl = json.load(open(tl_path))
    beats = tl["beats"]
    keys = ["id", "visual", "say", "text", "start", "end", "dur", "s0", "s1"]
    if set(tl) != {"total", "engine", "beats"}:
        errs.append(f"{label}: chiavi timeline {sorted(tl)}")
    vo = os.path.join(out_dir, "voiceover.wav")
    if abs(wav_duration(vo) - tl["total"]) > 0.002:
        errs.append(f"{label}: total {tl['total']} diverso dalla durata del wav {wav_duration(vo):.3f}")
    with wave.open(vo, "rb") as w:
        if (w.getframerate(), w.getnchannels()) != (SR_OUT, 2):
            errs.append(f"{label}: voiceover non 44,1 kHz stereo")
    if beats[0]["start"] != 0 or beats[-1]["end"] != tl["total"]:
        errs.append(f"{label}: start iniziale/end finale sbagliati")
    for i, b in enumerate(beats):
        if list(b) != keys:
            errs.append(f"{label}: chiavi battuta {b['id']}: {list(b)}")
        if i and b["start"] != beats[i - 1]["end"]:
            errs.append(f"{label}: {b['id']} non contigua")
        if not (b["start"] <= b["s0"] < b["s1"] <= b["end"]):
            errs.append(f"{label}: {b['id']} s0/s1 fuori da start/end")
    tmp16 = os.path.join(out_dir, "_check16k.wav")
    to_mono_wav(vo, tmp16, 16000)
    x, sr = read_wav(tmp16)
    os.remove(tmp16)
    rms = frame_rms(x, sr)
    ref = max(rms)
    for i, b in enumerate(beats):
        k0, k1 = int(b["start"] / FRAME), int(b["end"] / FRAME)
        loud = [k for k in range(k0, min(k1, len(rms))) if rms[k] > ref * db2lin(-30)]
        if not loud:
            errs.append(f"{label}: {b['id']} senza audio in [{b['start']}, {b['end']}]")
            continue
        on, off = loud[0] * FRAME, (loud[-1] + 1) * FRAME
        if abs(b["s0"] - on) > 0.04 or abs(b["s1"] - off) > 0.06:
            errs.append(f"{label}: {b['id']} s0/s1 {b['s0']}/{b['s1']} contro tono {on:.2f}/{off:.2f}")
        seg = x[int(b["start"] * sr):int(b["end"] * sr)]
        own = _tone_power(seg, sr, freqs[i])
        for j in (i - 1, i + 1):
            if 0 <= j < len(freqs):
                leak = _tone_power(seg, sr, freqs[j])
                if leak > own * 1e-3:
                    errs.append(f"{label}: {b['id']} contiene audio di {beats[j]['id']} "
                                f"({10 * math.log10(leak / own):.1f} dB)")
        if i + 1 < len(beats):
            k = int(b["end"] / FRAME)
            lev = lin2db(max(rms[max(0, k - 1):k + 2]) / ref)
            if lev > -35:
                errs.append(f"{label}: energia al confine {b['id']}|{beats[i + 1]['id']} {lev:.1f} dB")
    if long_gap_after is not None:
        gap = beats[long_gap_after + 1]["s0"] - beats[long_gap_after]["s1"]
        if gap > MAX_PAUSE + 0.08:
            errs.append(f"{label}: pausa lunga non accorciata ({gap:.2f}s)")
    return tl


def selftest():
    """Prova offline: ElevenLabs (1 richiesta mp3, più richieste mp3, pcm) e registrazioni."""
    g = globals()
    real_http, env0 = g["el_http"], dict(os.environ)
    tmp = tempfile.mkdtemp(prefix="gen_audio_selftest_")
    errs = []
    says = [b["say"].strip() for b in BEATS]
    voices = {"voices": [
        {"voice_id": "f_en", "name": "Anna", "labels": {"gender": "female", "accent": "american"}},
        {"voice_id": "m_it", "name": "Marco", "labels": {"gender": "male", "accent": "italian",
                                                          "use_case": "narrative_story"}},
        {"voice_id": "m_en", "name": "Bob", "labels": {"gender": "male", "accent": "british"}}]}
    try:
        for label, fmt, max_chars in (("eleven-1-richiesta", "mp3_44100_128", None),
                                      ("eleven-4-richieste", "mp3_44100_128", "420"),
                                      ("eleven-pcm", "pcm_24000", None)):
            sr = int(fmt.split("_")[1])
            sig, layout, freqs = _selftest_signal(sr)
            calls = []

            def fake(method, path, key, body=None, query=None, timeout=0):
                calls.append({"method": method, "path": path, "body": body, "query": query})
                if path == "/v1/voices":
                    return json.dumps(voices).encode()
                m = re.fullmatch(r"/v1/text-to-speech/([^/]+)/with-timestamps", path)
                assert m and method == "POST" and key == "chiave-finta", (method, path, key)
                # quali battute contiene la richiesta
                rng = next((a, b) for a in range(len(says)) for b in range(a + 1, len(says) + 1)
                           if " ".join(says[a:b]) == body["text"])
                # ogni risposta ha un po' di silenzio ai bordi, mai audio delle battute vicine
                t0 = max(0.0, layout[rng[0]][0] - 0.25, layout[rng[0] - 1][1] + 0.01 if rng[0] else 0.0)
                t1 = layout[rng[1] - 1][1] + 0.3
                if rng[1] < len(layout):
                    t1 = min(t1, layout[rng[1]][0] - 0.01)
                piece = sig[int(t0 * sr):int(t1 * sr)]
                if fmt.startswith("pcm_"):
                    audio = piece.tobytes()
                else:
                    w = os.path.join(tmp, "_piece.wav")
                    write_wav(w, piece, sr)
                    run(["ffmpeg", "-y", "-v", "error", "-i", w, "-c:a", "libmp3lame", "-b:a", "128k",
                         w[:-4] + ".mp3"])
                    audio = open(w[:-4] + ".mp3", "rb").read()
                al = _fake_alignment(says[rng[0]:rng[1]], layout[rng[0]:rng[1]], t0)
                return json.dumps({"audio_base64": base64.b64encode(audio).decode(),
                                   "alignment": al, "normalized_alignment": al}).encode()

            g["el_http"] = fake
            os.environ.update({"ELEVENLABS_API_KEY": "chiave-finta", "ELEVENLABS_OUTPUT_FORMAT": fmt})
            os.environ.pop("ELEVENLABS_VOICE_ID", None)
            os.environ.pop("ELEVENLABS_MODEL", None)
            if max_chars:
                os.environ["ELEVENLABS_MAX_CHARS"] = max_chars
            else:
                os.environ.pop("ELEVENLABS_MAX_CHARS", None)
            if label == "eleven-pcm":
                os.environ["ELEVENLABS_MODEL"] = "eleven_turbo_v2_5"
            d = os.path.join(tmp, label)
            generate("eleven", d, os.path.join(d, "timeline.json"), quiet=True)
            tts = [c for c in calls if c["path"] != "/v1/voices"]
            if not tts or any(c["path"] != "/v1/text-to-speech/m_it/with-timestamps" for c in tts):
                errs.append(f"{label}: voce scelta sbagliata: {[c['path'] for c in tts]}")
            want_model = "eleven_turbo_v2_5" if label == "eleven-pcm" else EL_DEFAULT_MODEL
            for k, c in enumerate(tts):
                bd = c["body"]
                if bd["model_id"] != want_model or c["query"] != {"output_format": fmt}:
                    errs.append(f"{label}: modello/formato {bd['model_id']} {c['query']}")
                vs = bd["voice_settings"]
                if not (0.45 <= vs["stability"] <= 0.5 and vs["similarity_boost"] == 0.75
                        and 0.2 <= vs["style"] <= 0.3 and vs["use_speaker_boost"] is True):
                    errs.append(f"{label}: voice_settings {vs}")
                if ("previous_text" in bd) != (k > 0) or ("next_text" in bd) != (k + 1 < len(tts)):
                    errs.append(f"{label}: previous_text/next_text sbagliati nella richiesta {k}")
                if ("language_code" in bd) != (want_model in EL_LANG_MODELS):
                    errs.append(f"{label}: language_code inatteso")
            if label == "eleven-1-richiesta" and len(tts) != 1:
                errs.append(f"{label}: {len(tts)} richieste invece di 1")
            if label == "eleven-4-richieste" and len(tts) < 3:
                errs.append(f"{label}: attese più richieste, fatte {len(tts)}")
            if " ".join(c["body"]["text"] for c in tts) != " ".join(says):
                errs.append(f"{label}: il testo inviato non è il copione intero")
            tl = _check_output(os.path.join(d, "timeline.json"), d, freqs, 5, errs, label)
            print(f"  {label}: {len(tts)} richieste TTS, total {tl['total']:.2f}s, "
                  f"{'OK' if not [e for e in errs if e.startswith(label)] else 'ERRORI'}")

        # registrazione propria: un file per battuta
        sig, layout, freqs = _selftest_signal(SR_OUT)
        rec = os.path.join(tmp, "rec_in")
        os.makedirs(rec)
        for b, (a, e) in zip(BEATS, layout):
            write_wav(os.path.join(rec, b["id"] + ".wav"),
                      array.array("h", bytes(2 * int(0.2 * SR_OUT))) + sig[int(a * SR_OUT):int(e * SR_OUT)]
                      + array.array("h", bytes(2 * int(0.3 * SR_OUT))), SR_OUT)
        d = os.path.join(tmp, "rec")
        generate("rec", d, os.path.join(d, "timeline.json"), rec_dir=rec, quiet=True)
        rec_errs = []
        tl = _check_output(os.path.join(d, "timeline.json"), d, freqs, None, rec_errs, "rec")
        errs += rec_errs
        print(f"  rec: total {tl['total']:.2f}s, {'OK' if not rec_errs else 'ERRORI'}")
    finally:
        g["el_http"] = real_http
        os.environ.clear()
        os.environ.update(env0)
    if errs:
        print("SELFTEST FALLITO:\n  " + "\n  ".join(errs))
        print("file in", tmp)
        return 1
    shutil.rmtree(tmp, ignore_errors=True)
    print("SELFTEST OK")
    return 0


# ================================================================ main
def ensure_venv():
    """Kokoro gira nel venv tts/venv: se serve, lo script si rilancia da solo lì dentro."""
    if os.path.realpath(sys.prefix) == os.path.realpath(VENV):
        return
    py = os.path.join(VENV, "bin", "python")
    if not os.path.exists(py):
        sys.exit("Kokoro non installato: lancia prima ./setup_tts.sh")
    os.execv(py, [py, os.path.abspath(__file__)] + sys.argv[1:])


def main():
    ap = argparse.ArgumentParser(description="Voce narrante continua + timeline delle battute")
    ap.add_argument("--engine", choices=["kokoro", "eleven", "piper", "espeak", "rec"], default="kokoro")
    ap.add_argument("--voice", default=KOKORO_VOICE, help="voce Kokoro (im_nicola, if_sara)")
    ap.add_argument("--speed", type=float, default=KOKORO_SPEED, help="velocità Kokoro (1.0 = naturale)")
    ap.add_argument("--max-pause", type=float, default=MAX_PAUSE, help="pausa massima in secondi")
    ap.add_argument("--rec-dir", default="rec", help="cartella delle registrazioni (--engine rec)")
    ap.add_argument("--selftest", action="store_true", help="prova offline ElevenLabs simulato + rec")
    args = ap.parse_args()
    os.chdir(HERE)
    if args.selftest:
        sys.exit(selftest())
    if args.engine == "kokoro":
        ensure_venv()
    generate(args.engine, voice=args.voice, speed=args.speed, rec_dir=args.rec_dir,
             max_pause=args.max_pause)


if __name__ == "__main__":
    main()
