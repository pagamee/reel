# -*- coding: utf-8 -*-
"""
Traccia audio finale:
  voce (audio/voiceover.wav)
  + un "pop" leggero a ogni cambio di illustrazione (non a ogni battuta)
  + musica di sottofondo opzionale (--music FILE), bassa e abbassata sotto la voce.
Esce in audio/final.wav.
"""
import json, os, subprocess, argparse

OUT = "audio"


def run(cmd):
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--music", help="file musicale opzionale")
    ap.add_argument("--music-db", type=float, default=-24.0, help="volume della musica in dB")
    args = ap.parse_args()

    tl = json.load(open("timeline.json"))
    total = tl["total"]

    # "pop" morbido: sinusoide in discesa con attacco rapido
    pop = os.path.join(OUT, "pop.wav")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", "sine=f=620:d=0.14:r=44100",
         "-af", ("vibrato=f=18:d=0.25,afade=t=in:st=0:d=0.006,afade=t=out:st=0.02:d=0.12,"
                 "lowpass=f=2400,volume=0.20,aformat=channel_layouts=stereo"), pop])

    cuts, prev = [], None
    for b in tl["beats"]:
        if prev is not None and b["visual"] != prev:
            cuts.append(b["start"])
        prev = b["visual"]

    inputs, filters, labels = ["-i", os.path.join(OUT, "voiceover.wav")], [], ["[0:a]"]
    for i, st in enumerate(cuts):
        inputs += ["-i", pop]
        d = int(st * 1000)
        filters.append(f"[{i+1}:a]adelay={d}|{d}[p{i}]")
        labels.append(f"[p{i}]")
    graph = ";".join(filters) + (";" if filters else "")
    graph += f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0[vox]"
    last = "[vox]"

    if args.music:
        inputs += ["-i", args.music]
        mi = len(cuts) + 1
        gain = 10 ** (args.music_db / 20.0)
        graph += (f";[{mi}:a]aformat=channel_layouts=stereo,aloop=loop=-1:size=2e9,"
                  f"atrim=0:{total:.3f},afade=t=out:st={max(0, total-1.5):.3f}:d=1.5,volume={gain:.4f}[bed]")
        graph += ";[bed][0:a]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=300[duck]"
        graph += ";[vox][duck]amix=inputs=2:duration=first:normalize=0[mix]"
        last = "[mix]"
    # level=0: col default alimiter moltiplica tutto per 1/limit, e i picchi limitati finiscono a 0 dBFS
    graph += f";{last}alimiter=limit=0.89:level=0:latency=1,aresample=44100[out]"

    run(["ffmpeg", "-y"] + inputs + ["-filter_complex", graph, "-map", "[out]",
         "-t", f"{total:.3f}", "-ac", "2", "-ar", "44100", os.path.join(OUT, "final.wav")])
    print(f"audio/final.wav  ({total:.2f}s, {len(cuts)} stacchi"
          + (", con musica" if args.music else "") + ")")


if __name__ == "__main__":
    main()
