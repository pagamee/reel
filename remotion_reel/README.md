# Reel TFR in nero — pipeline Remotion

Versione del reel costruita con [Remotion](https://www.remotion.dev/) (React → video).
Riproduce le stesse 10 scene doodle del pipeline `../reel_pipeline`, con il
voiceover sincronizzato dalla `timeline.json`.

## Struttura

- `src/figure.ts` — builder SVG dello stick-figure (estratti verbatim dal pipeline originale)
- `src/scenes.ts` — le 10 scene (testi + pose) in forma dichiarativa
- `src/Scene.tsx` — rendering di una scena: auto-fit del testo, codina dei fumetti, animazioni per-frame (pop/rise)
- `src/Reel.tsx` — sequenze dalla timeline + `<Audio>` voiceover, caricamento font locali
- `src/Root.tsx` — composizione `Reel` (1080×1920, 30 fps, durata dalla timeline)
- `public/fonts/` — Humor Sans + Comic Neue (per il glifo €)
- `public/voiceover.wav` — traccia voce (non versionata; copiala da `../reel_pipeline/audio/voiceover.wav`)

## Build offline

Remotion di norma scarica un Chrome Headless Shell al primo render. In un
ambiente senza egress verso i server di Google/Remotion si usa il Chromium
già presente (qui quello di Playwright) via `--browser-executable`, che deve
puntare a un **chrome-headless-shell** (il Chrome completo non supporta più la
vecchia headless mode).

```bash
npm install
cp ../reel_pipeline/audio/voiceover.wav public/voiceover.wav

SHELL=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
npx remotion render Reel out/reel_remotion.mp4 \
  --browser-executable="$SHELL" --codec=h264 --crf=18

# still singolo per debug:
npx remotion still Reel out/frame.png --frame=340 --browser-executable="$SHELL"
```

## Rigenerare il voiceover

Il voiceover attuale è offline (espeak). Per la voce naturale ElevenLabs, una
volta abilitato `api.elevenlabs.io` nella network policy dell'ambiente:

```bash
cd ../reel_pipeline
ELEVENLABS_API_KEY=... ./build.sh eleven   # rigenera timeline.json + voiceover.wav
cp audio/voiceover.wav ../remotion_reel/public/voiceover.wav
cp timeline.json ../remotion_reel/src/timeline.json
```

poi ri-renderizza con Remotion.
