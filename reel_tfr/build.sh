#!/usr/bin/env bash
# Pipeline completa: voce -> timeline -> HTML -> controlli -> anteprime -> video.
# Uso:  ./build.sh [kokoro|eleven|piper|espeak|rec] [--music traccia.mp3 --music-db -24]
#   kokoro (predefinito)  voce offline continua, installata da ./setup_tts.sh
#   eleven                ElevenLabs (serve ELEVENLABS_API_KEY e api.elevenlabs.io raggiungibile)
#   rec                   registrazione propria, un file per battuta in rec/<id>.wav
set -euo pipefail
cd "$(dirname "$0")"
ENGINE="${1:-kokoro}"

for tool in ffmpeg ffprobe node; do
  command -v "$tool" >/dev/null 2>&1 || {
    echo "ERRORE: manca $tool. In una sessione nuova: apt-get install -y ffmpeg (node: npm install richiede Node 18+)" >&2
    exit 1
  }
done
[ -d node_modules/playwright ] || npm install --silent

if [ "$ENGINE" = "kokoro" ] && { [ ! -x tts/venv/bin/python ] || [ ! -f tts/kokoro/kokoro-v1.0.onnx ]; }; then
  ./setup_tts.sh kokoro
fi
if [ "$ENGINE" = "piper" ] && { [ ! -x tts/piper/piper ] || [ ! -f tts/it-riccardo_fasol-x-low.onnx ]; }; then
  ./setup_tts.sh piper
fi

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
