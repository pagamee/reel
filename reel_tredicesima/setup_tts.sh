#!/usr/bin/env bash
# Installa in ./tts/ il motore della voce narrante. Serve una volta sola; niente
# file pesanti nel repo (tts/ è in .gitignore).
#
#   ./setup_tts.sh            Kokoro-82M, voce "im_nicola" (PREDEFINITO)
#   ./setup_tts.sh piper      Piper + voce "riccardo" x_low (alternativa, più robotica)
#   ./setup_tts.sh all        entrambi
#
# Kokoro: venv Python in tts/venv con kokoro-onnx 0.6.1 + misaki (G2P espeak-ng:
# la libreria e i dati arrivano col pacchetto espeakng-loader, nessun pacchetto di
# sistema). Modello dalle release GitHub di thewh1teagle/kokoro-onnx, cartella
# "model-files-v1.1": è l'export fp32 CON l'uscita "duration", indispensabile per
# sapere quando inizia e finisce ogni battuta (quello di model-files-v1.0 non ce l'ha).
# Spazio: ~220 MB di venv + 354 MB di modello.
set -euo pipefail
cd "$(dirname "$0")"
WHAT="${1:-kokoro}"
PY="${PYTHON:-python3}"
mkdir -p tts

sha256() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -d' ' -f1
  else shasum -a 256 "$1" | cut -d' ' -f1; fi
}

# fetch URL DEST SHA256 : scarica solo se manca o è diverso, e verifica il checksum
fetch() {
  local url="$1" dest="$2" sum="$3"
  if [ -f "$dest" ] && [ "$(sha256 "$dest")" = "$sum" ]; then return 0; fi
  echo "  scarico $(basename "$dest") ..."
  curl -fsSL --retry 3 --retry-delay 3 -o "$dest.part" "$url"
  local got; got="$(sha256 "$dest.part")"
  if [ "$got" != "$sum" ]; then
    rm -f "$dest.part"
    echo "ERRORE: checksum di $(basename "$dest") diverso da quello atteso ($got)" >&2
    exit 1
  fi
  mv "$dest.part" "$dest"
}

setup_kokoro() {
  echo "== Kokoro (voce predefinita)"
  local V=tts/venv
  if ! "$V/bin/python" -c "import kokoro_onnx, misaki.espeak, soundfile" >/dev/null 2>&1; then
    # misaki-fork 0.9.6 richiede Python 3.10-3.12
    local OKPY='import sys; sys.exit(not (3, 10) <= sys.version_info[:2] <= (3, 12))'
    "$PY" -c "$OKPY" || { echo "ERRORE: serve Python 3.10-3.12 (es. PYTHON=python3.12 $0)" >&2; exit 1; }
    # venv lasciato a metà da un tentativo precedente (senza pip o con un altro Python): si rifà
    if ! "$V/bin/python" -c "$OKPY" 2>/dev/null || ! "$V/bin/python" -m pip --version >/dev/null 2>&1; then
      rm -rf "$V"
      "$PY" -m venv "$V"
    fi
    "$V/bin/python" -m pip install -q -U pip
    # misaki-fork senza extra: niente torch né spacy
    "$V/bin/python" -m pip install -q "kokoro-onnx==0.6.1" "misaki-fork==0.9.6" "soundfile>=0.12"
  fi
  mkdir -p tts/kokoro
  local REL=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1
  fetch "$REL/kokoro-v1.0.onnx" tts/kokoro/kokoro-v1.0.onnx \
        beb0d1848dee9a49da392cc3df26958d46cfa35d321edf434f52949153f0df3a
  fetch "$REL/voices-v1.0.bin" tts/kokoro/voices-v1.0.bin \
        bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d
  # prova: il modello deve dare le durate per fonema e la voce deve esserci
  "$V/bin/python" - <<'EOF'
from kokoro_onnx import Kokoro
from misaki.espeak import EspeakG2P
k = Kokoro("tts/kokoro/kokoro-v1.0.onnx", "tts/kokoro/voices-v1.0.bin")
assert k.has_timings, "il modello non ha l'uscita 'duration'"
assert "im_nicola" in k.get_voices(), "voce im_nicola assente"
ps, _ = EspeakG2P(language="it")("Prova della voce.")
audio, sr, tim = k.create_timed(ps, "im_nicola", 1.0, is_phonemes=True)
print(f"  Kokoro pronto: {len(audio) / sr:.2f}s di prova, {len(tim)} fonemi con i tempi")
EOF
}

setup_piper() {
  echo "== Piper (alternativa)"
  local REL=https://github.com/rhasspy/piper/releases/download
  if [ ! -x tts/piper/piper ]; then
    curl -sSLf -o tts/piper.tgz "$REL/2023.11.14-2/piper_linux_x86_64.tar.gz"
    tar xzf tts/piper.tgz -C tts && rm tts/piper.tgz
  fi
  if [ ! -f tts/it-riccardo_fasol-x-low.onnx ]; then
    curl -sSLf -o tts/voice.tgz "$REL/v0.0.2/voice-it-riccardo_fasol-x-low.tar.gz"
    tar xzf tts/voice.tgz -C tts && rm tts/voice.tgz
  fi
  echo "  Piper pronto: tts/piper/piper  voce: it-riccardo_fasol-x-low"
}

case "$WHAT" in
  kokoro) setup_kokoro ;;
  piper)  setup_piper ;;
  all)    setup_kokoro; setup_piper ;;
  *) echo "uso: $0 [kokoro|piper|all]" >&2; exit 2 ;;
esac
