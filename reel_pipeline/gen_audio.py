# -*- coding: utf-8 -*-
"""
Genera la voce narrante e la timeline delle scene.

Due motori:
  --engine eleven  : ElevenLabs REST (voce naturale)  [richiede ELEVENLABS_API_KEY]
  --engine espeak  : espeak-ng + mbrola it4 (offline, fallback)

Per ogni scena produce audio/<id>.wav (44.1 kHz stereo, loudnorm, con
lead-in/tail di silenzio) e scrive timeline.json con start/end/dur.
Infine concatena tutto in audio/voiceover.wav.
"""
import os, sys, json, argparse, subprocess, wave, contextlib, urllib.request, urllib.error
from scenes import SCENES

OUT = "audio"
GAP_BEFORE = 0.30   # silenzio prima della battuta
GAP_AFTER  = 0.55   # coda: il testo resta ancora un attimo a schermo

# --- espeak/mbrola ---
ESPEAK_VOICE = "mb-it4"
ESPEAK_SPEED = 148
ESPEAK_PITCH = 52

# --- ElevenLabs ---
EL_MODEL = "eleven_multilingual_v2"
EL_BASE  = "https://api.elevenlabs.io/v1"


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, **kw)


def dur_wav(path):
    with contextlib.closing(wave.open(path, "r")) as w:
        return w.getnframes() / float(w.getframerate())


# ---------------------------------------------------------------- ElevenLabs
def el_request(path, key, data=None, method="GET"):
    req = urllib.request.Request(EL_BASE + path, method=method)
    req.add_header("xi-api-key", key)
    if data is not None:
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(data).encode("utf-8")
    return urllib.request.urlopen(req, timeout=120)


def el_pick_voice(key):
    """Sceglie una voce femminile adatta all'italiano."""
    forced = os.environ.get("ELEVENLABS_VOICE_ID")
    if forced:
        return forced, "(da ELEVENLABS_VOICE_ID)"
    voices = json.loads(el_request("/voices", key).read())["voices"]

    def score(v):
        labels = {k: (val or "").lower() for k, val in (v.get("labels") or {}).items()}
        s = 0
        if labels.get("gender") == "female":
            s += 10
        if "italian" in (v.get("fine_tuning", {}).get("language") or "").lower():
            s += 8
        if labels.get("use_case") in ("narration", "narrative_story", "informative_educational", "news"):
            s += 6
        if labels.get("age") in ("middle_aged", "middle-aged", "young"):
            s += 2
        if labels.get("accent") in ("italian",):
            s += 8
        return s

    voices.sort(key=score, reverse=True)
    best = voices[0]
    return best["voice_id"], best.get("name", "?")


def el_tts(key, voice_id, text, dest_mp3, style=0.30, stability=0.45):
    body = {
        "text": text,
        "model_id": EL_MODEL,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": 0.80,
            "style": style,
            "use_speaker_boost": True,
        },
    }
    r = el_request(
        f"/text-to-speech/{voice_id}?output_format=mp3_44100_128", key, body, "POST"
    )
    with open(dest_mp3, "wb") as f:
        f.write(r.read())


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["eleven", "espeak"], default="espeak")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    key = voice_id = None
    if args.engine == "eleven":
        key = os.environ.get("ELEVENLABS_API_KEY")
        if not key:
            sys.exit("ELEVENLABS_API_KEY non presente in ambiente.")
        voice_id, vname = el_pick_voice(key)
        print(f"ElevenLabs voice: {vname} ({voice_id})  model={EL_MODEL}")

    timeline, t = [], 0.0
    for sc in SCENES:
        raw = os.path.join(OUT, sc["id"] + ("_raw.mp3" if args.engine == "eleven" else "_raw.wav"))
        final = os.path.join(OUT, sc["id"] + ".wav")

        if args.engine == "eleven":
            # la scena 9 e la 10 sono l'avvocata: un filo più "calda"/espressiva
            style = 0.42 if sc["id"] in ("s9_lesson", "s10_cta") else 0.30
            el_tts(key, voice_id, sc["narration"], raw, style=style)
        else:
            run(["espeak-ng", "-v", ESPEAK_VOICE, "-s", str(ESPEAK_SPEED),
                 "-p", str(ESPEAK_PITCH), sc["narration"], "-w", raw])

        ms = int(GAP_BEFORE * 1000)
        run(["ffmpeg", "-y", "-i", raw,
             "-af", (f"aresample=44100,loudnorm=I=-16:TP=-1.5:LRA=11,"
                     f"adelay={ms}|{ms},apad=pad_dur={GAP_AFTER}"),
             "-ac", "2", "-ar", "44100", final])

        d = dur_wav(final)
        timeline.append({
            "id": sc["id"], "visual": sc["visual"], "narration": sc["narration"],
            "start": round(t, 3), "end": round(t + d, 3), "dur": round(d, 3),
        })
        t += d

    with open("timeline.json", "w") as f:
        json.dump({"total": round(t, 3), "engine": args.engine, "scenes": timeline},
                  f, indent=2, ensure_ascii=False)

    # voiceover unico
    with open(os.path.join(OUT, "concat.txt"), "w") as f:
        for s in timeline:
            f.write(f"file '{s['id']}.wav'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0",
         "-i", os.path.join(OUT, "concat.txt"), "-c", "copy",
         os.path.join(OUT, "voiceover.wav")])

    print("TOTAL DURATION: %.2fs" % t)
    for s in timeline:
        print(f"  {s['id']:12s} {s['dur']:5.2f}s  [{s['start']:6.2f} -> {s['end']:6.2f}]")


if __name__ == "__main__":
    main()
