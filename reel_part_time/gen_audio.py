# -*- coding: utf-8 -*-
"""
Genera la voce narrante e la timeline delle battute.

Motori:
  --engine piper   : Piper, TTS neurale offline, voce italiana maschile (default)
  --engine eleven  : ElevenLabs REST, voce più naturale  [richiede ELEVENLABS_API_KEY]
  --engine espeak  : espeak-ng + mbrola it4 (ultima spiaggia, molto robotica)

Per ogni battuta produce audio/<id>.wav (44.1 kHz stereo, normalizzato) e
misura dove inizia e dove finisce il parlato: il template usa questi istanti
per far comparire il testo "a macchina" insieme alla voce.
Scrive timeline.json e audio/voiceover.wav.
"""
import os, sys, json, argparse, subprocess, wave, array, contextlib, urllib.request
from scenes import BEATS

OUT = "audio"
GAP_BEFORE = 0.10   # silenzio prima della battuta: ritmo da reel, stacchi stretti
GAP_AFTER  = 0.32   # coda: il testo completo resta un attimo a schermo

PIPER_BIN   = os.path.join("tts", "piper", "piper")
PIPER_MODEL = os.path.join("tts", "it-riccardo_fasol-x-low.onnx")
PIPER_SPEED = 0.88  # length_scale < 1 = più veloce

EL_MODEL = "eleven_multilingual_v2"
EL_BASE  = "https://api.elevenlabs.io/v1"


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, **kw)


def dur_wav(path):
    with contextlib.closing(wave.open(path, "r")) as w:
        return w.getnframes() / float(w.getframerate())


def speech_bounds(path, thr_db=-38.0):
    """Primo e ultimo istante in cui il segnale supera la soglia (finestre da 10 ms)."""
    with contextlib.closing(wave.open(path, "r")) as w:
        sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
        assert sw == 2, "atteso PCM 16 bit"
        data = array.array("h", w.readframes(w.getnframes()))
    win = int(sr * 0.01) * ch
    thr = 32768 * 10 ** (thr_db / 20.0)
    loud = []
    for i in range(0, len(data), win):
        chunk = data[i:i + win]
        if chunk and max(abs(min(chunk)), abs(max(chunk))) > thr:
            loud.append(i / ch / sr)
    if not loud:
        return 0.0, len(data) / ch / sr
    return loud[0], loud[-1] + 0.01


# ---------------------------------------------------------------- ElevenLabs
def el_request(path, key, data=None, method="GET"):
    req = urllib.request.Request(EL_BASE + path, method=method)
    req.add_header("xi-api-key", key)
    if data is not None:
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(data).encode("utf-8")
    return urllib.request.urlopen(req, timeout=120)


def el_pick_voice(key):
    forced = os.environ.get("ELEVENLABS_VOICE_ID")
    if forced:
        return forced
    voices = json.loads(el_request("/voices", key).read())["voices"]

    def score(v):
        labels = {k: (val or "").lower() for k, val in (v.get("labels") or {}).items()}
        s = 10 if labels.get("gender") == "male" else 0
        s += 8 if labels.get("accent") == "italian" else 0
        s += 6 if labels.get("use_case") in ("narration", "informative_educational") else 0
        return s
    return sorted(voices, key=score, reverse=True)[0]["voice_id"]


def el_tts(key, voice_id, text, dest):
    body = {"text": text, "model_id": EL_MODEL,
            "voice_settings": {"stability": 0.42, "similarity_boost": 0.80,
                               "style": 0.35, "use_speaker_boost": True}}
    r = el_request(f"/text-to-speech/{voice_id}?output_format=mp3_44100_128", key, body, "POST")
    with open(dest, "wb") as f:
        f.write(r.read())


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["piper", "eleven", "espeak"], default="piper")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    key = voice_id = None
    if args.engine == "eleven":
        key = os.environ.get("ELEVENLABS_API_KEY") or sys.exit("ELEVENLABS_API_KEY non presente.")
        voice_id = el_pick_voice(key)
    if args.engine == "piper" and not os.path.exists(PIPER_BIN):
        sys.exit("Piper non installato: lancia prima ./setup_tts.sh")

    timeline, t = [], 0.0
    for b in BEATS:
        raw = os.path.join(OUT, b["id"] + ("_raw.mp3" if args.engine == "eleven" else "_raw.wav"))
        final = os.path.join(OUT, b["id"] + ".wav")

        if args.engine == "piper":
            run([PIPER_BIN, "-q", "--model", PIPER_MODEL, "--length_scale", str(PIPER_SPEED),
                 "--sentence_silence", "0.12", "--output_file", raw],
                input=b["say"].encode("utf-8"))
        elif args.engine == "eleven":
            el_tts(key, voice_id, b["say"], raw)
        else:
            run(["espeak-ng", "-v", "mb-it4", "-s", "160", "-p", "50", b["say"], "-w", raw])

        # taglia i silenzi del motore, poi rimette pause uguali per tutte le battute
        tmp = os.path.join(OUT, b["id"] + "_trim.wav")
        run(["ffmpeg", "-y", "-i", raw, "-ac", "1", "-ar", "44100", "-c:a", "pcm_s16le", tmp])
        s0, s1 = speech_bounds(tmp)
        speech = s1 - s0
        ms = int(GAP_BEFORE * 1000)
        run(["ffmpeg", "-y", "-i", tmp,
             "-af", (f"atrim={max(0, s0 - 0.02):.3f}:{s1 + 0.04:.3f},asetpts=PTS-STARTPTS,"
                     "highpass=f=70,equalizer=f=3200:t=q:w=1.2:g=2.5,"
                     "acompressor=threshold=-20dB:ratio=3:attack=5:release=80,"
                     f"loudnorm=I=-15:TP=-1.5:LRA=9,aresample=44100,"
                     f"adelay={ms}|{ms},apad=pad_dur={GAP_AFTER}"),
             "-ac", "2", "-ar", "44100", final])
        os.remove(tmp)

        d = dur_wav(final)
        timeline.append({
            "id": b["id"], "visual": b["visual"], "say": b["say"], "text": b["text"],
            "start": round(t, 3), "end": round(t + d, 3), "dur": round(d, 3),
            # istanti assoluti in cui la voce parla (per il testo a macchina)
            "s0": round(t + GAP_BEFORE + 0.02, 3), "s1": round(t + GAP_BEFORE + 0.02 + speech, 3),
        })
        t += d

    with open("timeline.json", "w") as f:
        json.dump({"total": round(t, 3), "engine": args.engine, "beats": timeline},
                  f, indent=2, ensure_ascii=False)

    with open(os.path.join(OUT, "concat.txt"), "w") as f:
        for b in timeline:
            f.write(f"file '{b['id']}.wav'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(OUT, "concat.txt"),
         "-c", "copy", os.path.join(OUT, "voiceover.wav")])

    print("DURATA TOTALE: %.2fs  (%d battute, motore %s)" % (t, len(timeline), args.engine))
    for b in timeline:
        print(f"  {b['id']}  {b['visual']:9s} {b['dur']:5.2f}s  [{b['start']:6.2f} → {b['end']:6.2f}]")


if __name__ == "__main__":
    main()
