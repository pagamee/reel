#!/usr/bin/env bash
# Pipeline completa: voce -> timeline -> HTML -> controlli -> video.
# Uso:  ./build.sh [espeak|eleven]   (default: espeak)
set -euo pipefail
ENGINE="${1:-espeak}"

echo "== 1/5  voce narrante + timeline (motore: $ENGINE)"
python3 gen_audio.py --engine "$ENGINE"

echo "== 2/5  mix audio (voce + whoosh ai cambi scena)"
python3 mix_audio.py "${@:2}"

echo "== 3/5  costruzione reel.html"
python3 build_html.py

echo "== 4/5  controlli di layout su tutte le scene"
node render.mjs check

echo "== 5/5  render video 1080x1920 @30fps"
node render.mjs full 30

echo
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt \
        -show_entries format=duration -of default=nw=1 out/reel.mp4
