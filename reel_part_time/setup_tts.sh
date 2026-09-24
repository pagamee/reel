#!/usr/bin/env bash
# Scarica Piper (TTS neurale offline) e la voce italiana "riccardo" in ./tts/
# Serve solo una volta. Tutto arriva dalle release GitHub di rhasspy/piper.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p tts
cd tts
REL=https://github.com/rhasspy/piper/releases/download
if [ ! -x piper/piper ]; then
  curl -sSLf -o piper.tgz "$REL/2023.11.14-2/piper_linux_x86_64.tar.gz"
  tar xzf piper.tgz && rm piper.tgz
fi
if [ ! -f it-riccardo_fasol-x-low.onnx ]; then
  curl -sSLf -o voice.tgz "$REL/v0.0.2/voice-it-riccardo_fasol-x-low.tar.gz"
  tar xzf voice.tgz && rm voice.tgz
fi
echo "Piper pronto: $(pwd)/piper/piper  voce: it-riccardo_fasol-x-low"
