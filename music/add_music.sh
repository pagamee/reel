#!/usr/bin/env bash
# Aggiunge la base musicale sotto la voce di un reel già finito (video copiato, solo l'audio cambia).
# Uso: ./add_music.sh <reel.mp4> <musica.wav> <uscita.mp4> [dB musica, predefinito -22]
set -euo pipefail
IN="$1"; MUS="$2"; OUT="$3"; DB="${4:--22}"
ffmpeg -loglevel error -y -i "$IN" -stream_loop -1 -i "$MUS" -filter_complex \
 "[0:a]asplit=2[v][sc];[1:a]volume=${DB}dB,aformat=channel_layouts=stereo[m];\
  [m][sc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];\
  [v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$OUT"
