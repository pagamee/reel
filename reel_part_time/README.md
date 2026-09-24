# Reel "Part-time sulla carta" — stile doodle con testo a macchina (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 1**.

Stile ripreso dai reel "omino con occhiali e cravatta": fondo chiaro, disegni a
tratto nero con pochi accenti di colore, testo in alto in stampatello scritto a
mano che compare **lettera per lettera insieme alla voce**, parole chiave in
verde/rosso, stacco secco a ogni cambio di illustrazione.

Output: `out/reel.mp4` — 1080×1920, H.264 yuv420p, 30 fps, AAC stereo.

## Rigenerare

```bash
npm install
./build.sh                    # voce Piper offline (la scarica al primo giro con setup_tts.sh)
./build.sh eleven             # voce ElevenLabs (serve ELEVENLABS_API_KEY; ELEVENLABS_VOICE_ID opzionale)
./build.sh piper --music traccia.mp3 --music-db -24   # con musica, abbassata sotto la voce
```

In alternativa si registra la propria voce: un file per battuta in `audio/<id>.wav`,
poi si adattano a mano `timeline.json` e `audio/voiceover.wav` (vedi `gen_audio.py`).

## I pezzi

| file | cosa fa |
|---|---|
| `scenes.py` | copione: 25 battute, ognuna con `visual`, `say` (voce) e `text` (schermo) |
| `setup_tts.sh` | scarica Piper e la voce italiana `riccardo` dalle release GitHub |
| `gen_audio.py` | una traccia per battuta, misura inizio/fine del parlato, scrive `timeline.json` |
| `mix_audio.py` | voce + "pop" leggero a ogni cambio di illustrazione (+ musica opzionale) |
| `reel_template.html` | personaggi, oggetti e le 18 illustrazioni (`ART.<visual>`), testo a macchina |
| `build_html.py` | inietta `timeline.json` nel template → `reel.html` |
| `render.mjs` | `check` (layout), `preview` (1 PNG per battuta + `preview/sheet.png`), `full` (video), `still <t>` |

## Come funziona il copione

- Battute consecutive con lo **stesso `visual`** restano sulla stessa illustrazione:
  cambia solo il testo (come nel riferimento, dove un disegno regge più frasi).
- Nel `text` i marcatori `[g]…[/g]`, `[r]…[/r]`, `[i]…[/i]` colorano le parole
  in verde, rosso, indaco Pagamee.
- Nel `say` i numeri vanno in lettere ("ventiquattro"), così il TTS non sbaglia;
  a schermo restano in cifre ("24").
- Gli elementi dei disegni possono entrare **quando il testo arriva a una parola**:
  `A(elemento, {from:"b21:WHATSAPP"})`. Oppure a inizio battuta (`from:"b05"`),
  con ritardo (`from:"b01+0.5"`), e sparire con `until`. Entrate: `pop`, `stamp`,
  `drop`, `slide`, `fade`, `rise`, `draw`, `write`; animazioni continue con `loop`
  (`spin`, `bob`, `shake`, `blink`, `twinkle`, `flutter`).

## Controlli automatici (`node render.mjs check`)

- didascalia oltre 4 righe, o rimpicciolita sotto 56 px perché troppo lunga;
- disegno che parte sotto il testo o esce dai bordi;
- parola-cue non trovata nel testo della battuta (errore JS, blocca il render).

## Note di stile

- Font: **Walter Turncoat** (testo, etichette; Apache 2.0) e **Inter 700** solo per
  il wordmark Pagamee (OFL). File e licenze in `fonts/`.
- Colori: inchiostro `#18181b`, fondo `#fafafa`, verde `#059669`, rosso `#dc2626`,
  indaco Pagamee `#4f46e5` (cravatta `#3730a3`, marchio con gradiente `#6366f1 → #8b5cf6`).
- I disegni sono progettati sul 1080×1920 e poi scalati a 0,86 verso l'alto
  (`ART_SCALE`): su Instagram il fondo dello schermo è coperto da didascalia e pulsanti.
- Il personaggio (`guy()`) ha pose per mano (`l`, `r` rispetto alla spalla), faccia
  (`smile`, `smirk`, `flat`, `sad`, `o`, `grin`, `wavy`, `shh`), occhi, sopracciglia,
  sudore, rossore. `boss()` è la variante del capo (completo scuro, baffi).

## Fare la parte 2

1. Riscrivi `BEATS` in `scenes.py` (tema nuovo, stessa struttura).
2. Aggiungi/riusa le illustrazioni in `ART` dentro `reel_template.html`.
3. `./build.sh` — `check` segnala subito testi troppo lunghi o disegni fuori posto.
