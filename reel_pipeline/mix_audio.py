# -*- coding: utf-8 -*-
"""
Mixa la traccia audio finale:
  voce narrante (audio/voiceover.wav)
  + un leggero "whoosh" a ogni cambio scena
  + eventuale musica di sottofondo (--music FILE) tenuta bassa e "duckata" sotto la voce.
Esce in audio/final.wav.
"""
import json, os, subprocess, argparse

OUT = "audio"

def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--music", help="file musicale opzionale per il sottofondo")
    ap.add_argument("--music-db", type=float, default=-26.0, help="volume del sottofondo in dB")
    args = ap.parse_args()

    tl = json.load(open("timeline.json"))
    total = tl["total"]

    # --- whoosh: breve soffio di rumore filtrato, per i cambi scena ---
    whoosh = os.path.join(OUT, "whoosh.wav")
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anoisesrc=d=0.34:c=pink:a=0.5:r=44100",
         "-af", ("highpass=f=260,lowpass=f=5200,"
                 "afade=t=in:st=0:d=0.06,afade=t=out:st=0.10:d=0.24,"
                 "volume=0.30,aformat=channel_layouts=stereo"),
         "-ar", "44100", whoosh])

    # un whoosh su ogni stacco (non sul primo fotogramma)
    starts = [s["start"] for s in tl["scenes"][1:]]
    inputs, filters, labels = ["-i", os.path.join(OUT, "voiceover.wav")], [], ["[0:a]"]
    for i, st in enumerate(starts):
        inputs += ["-i", whoosh]
        # il whoosh parte poco prima dello stacco, così "copre" il taglio
        delay = max(0, int((st - 0.12) * 1000))
        filters.append(f"[{i+1}:a]adelay={delay}|{delay}[w{i}]")
        labels.append(f"[w{i}]")

    chain = ";".join(filters)
    mix = f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0[voxw]"
    graph = (chain + ";" if chain else "") + mix
    last = "[voxw]"

    if args.music:
        inputs += ["-i", args.music]
        mi = len(starts) + 1
        gain = 10 ** (args.music_db / 20.0)
        # la musica scende automaticamente quando parla la voce (sidechaincompress)
        graph += (f";[{mi}:a]aformat=channel_layouts=stereo,aloop=loop=-1:size=2e9,"
                  f"atrim=0:{total:.3f},volume={gain:.4f}[bed]")
        graph += f";[bed][0:a]sidechaincompress=threshold=0.03:ratio=8:attack=25:release=350[ducked]"
        graph += f";[voxw][ducked]amix=inputs=2:duration=first:normalize=0[mixed]"
        last = "[mixed]"

    graph += f";{last}alimiter=limit=0.95,aresample=44100[out]"

    final = os.path.join(OUT, "final.wav")
    run(["ffmpeg", "-y"] + inputs +
        ["-filter_complex", graph, "-map", "[out]",
         "-t", f"{total:.3f}", "-ac", "2", "-ar", "44100", final])
    print(f"audio/final.wav  ({total:.2f}s, {len(starts)} whoosh"
          + (", musica in sottofondo" if args.music else "") + ")")

if __name__ == "__main__":
    main()
