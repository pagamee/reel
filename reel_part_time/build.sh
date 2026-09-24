#!/usr/bin/env bash
# Pipeline completa: voce -> timeline -> HTML -> controlli -> anteprime -> video.
# Uso:  ./build.sh [piper|eleven|espeak] [--music traccia.mp3 --music-db -24]
set -euo pipefail
cd "$(dirname "$0")"
ENGINE="${1:-piper}"

[ "$ENGINE" = "piper" ] && [ ! -x tts/piper/piper ] && ./setup_tts.sh

echo "== 1/6  voce + timeline (motore: $ENGINE)"
python3 gen_audio.py --engine "$ENGINE"

echo "== 2/6  mix audio"
python3 mix_audio.py "${@:2}"

echo "== 3/6  reel.html"
python3 build_html.py

echo "== 4/6  controlli di layout"
node render.mjs check

echo "== 5/6  anteprime"
node render.mjs preview

echo "== 6/6  video 1080x1920 @30fps"
node render.mjs full 30

ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate \
        -show_entries format=duration -of default=nw=1 out/reel.mp4
