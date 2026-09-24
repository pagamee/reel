# Reel "Part-time sulla carta" — stile doodle con testo a macchina (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 1**.

Stile ripreso dai reel "omino con occhiali e cravatta": fondo chiaro, disegni a
tratto nero con pochi accenti di colore, testo in alto in stampatello scritto a
mano che compare **lettera per lettera insieme alla voce**, parole chiave in
verde/rosso, stacco secco a ogni cambio di illustrazione.

Output: `out/reel.mp4` — 1080×1920, H.264 yuv420p, 30 fps, AAC stereo.

## Rigenerare

Servono `ffmpeg`, Node 18+ e Python 3.10–3.12 (in una sessione nuova: `apt-get install -y ffmpeg`).

```bash
npm install
./build.sh                    # voce Kokoro offline (al primo giro la installa con ./setup_tts.sh)
./build.sh eleven             # voce ElevenLabs (vedi sotto)
./build.sh rec                # la tua registrazione (vedi sotto)
./build.sh take               # lettura continua già pronta in rec_src/ (versione attuale, ElevenLabs)
./build.sh kokoro --music traccia.mp3 --music-db -24   # con musica, abbassata sotto la voce
```

## La voce

**Motore predefinito: Kokoro-82M** (`kokoro-onnx` 0.6.1, voce italiana maschile
`im_nicola`, velocità 1,0), tutto offline sulla CPU (~30 s per l'intero copione).
`./setup_tts.sh` crea `tts/venv` e scarica il modello dalle release GitHub di
`thewh1teagle/kokoro-onnx` (`model-files-v1.1`, ~350 MB, con checksum); `tts/` non
va nel repo. `gen_audio.py` si rilancia da solo dentro `tts/venv`.

- **Narrazione continua.** Il copione intero è letto in UNA sintesi: l'intonazione
  scorre da una battuta all'altra e le battute che spezzano una frase (b16→b17,
  b23→b24) sono lette come una frase sola. Le pause sono quelle del parlato
  (~0,1 s a virgole e due punti, un respiro di 0,25–0,45 s a fine frase); solo quelle
  oltre 0,45 s vengono accorciate, tagliando al centro del silenzio.
- **Confini delle battute** dalle durate per fonema che il modello restituisce,
  rifiniti sulle pause reali dell'audio: il cambio di battuta (e di disegno) cade
  sempre dentro una pausa, al più 0,1 s prima che parta la frase successiva.
  `s0`/`s1` = inizio/fine del parlato della battuta (testo a macchina).
- **Pronuncia**: correzioni solo per il TTS in `KOKORO_RESPELL`/`KOKORO_PHONFIX`
  dentro `gen_audio.py` (es. "WhatsApp", "ségnati", il verbo "è" accentato); il
  testo a schermo non cambia.
- **Uscite**: `audio/voiceover.wav` (traccia unica, 44,1 kHz stereo, −15 LUFS,
  elaborazione leggera: passa-alto, +1,5 dB di presenza, compressione 2:1, limitatore
  a −1,5 dBFS), `timeline.json`, e `audio/voice_report.json` con pause, energia ai
  confini e loudness.
- **Ripetibile**: la sintesi usa un seed fisso (`KOKORO_SEED`, predefinito 1234), quindi
  la stessa build dà sempre lo stesso audio e la stessa timeline; cambiando seed si
  ottiene un'altra "ripresa" della stessa lettura.
- Altre voci/velocità: `KOKORO_VOICE=if_sara KOKORO_SPEED=0.9 ./build.sh`
  (oppure `python3 gen_audio.py --voice if_sara --speed 0.9`).

Limite onesto: è una voce sintetica. Molto più fluida della vecchia (Piper x_low a
battute separate), ma nessuna voce offline disponibile qui è indistinguibile da una
persona. Per una resa "umana al 100%" ci sono ElevenLabs o una registrazione vera.

### Passare a ElevenLabs

1. Nelle impostazioni dell'ambiente imposta la variabile `ELEVENLABS_API_KEY`
   e consenti nella rete l'host `api.elevenlabs.io`.
2. `./build.sh eleven`

Il copione parte in **una sola richiesta** a `/v1/text-to-speech/{voice_id}/with-timestamps`
(a paragrafi con `previous_text`/`next_text` solo se superasse `ELEVENLABS_MAX_CHARS`),
e i tempi delle battute vengono dall'allineamento per carattere della risposta.
Opzionali: `ELEVENLABS_VOICE_ID` (altrimenti sceglie da solo una voce maschile,
italiana se l'account ne ha una), `ELEVENLABS_MODEL` (predefinito
`eleven_multilingual_v2`), `ELEVENLABS_OUTPUT_FORMAT` (predefinito `mp3_44100_128`),
`ELEVENLABS_SPEED`. Impostazioni voce: stability 0,48, similarity 0,75, style 0,25,
speaker boost. Prova offline del percorso (risposta simulata, niente rete):
`python3 gen_audio.py --selftest`.

### Lettura continua già pronta (motore "take") — versione attuale

Il video attuale usa la voce ElevenLabs "Chris Basetta – Social Media" (modello
eleven_multilingual_v2), generata col connettore ElevenLabs in un'unica lettura:
`rec_src/eleven_full.mp3`. È accelerata ×1,2 (`atempo`, stesso tono) in
`rec_src/take.flac`; `rec_src/align_take.py` sceglie i confini delle battute tra le
pause reali (programmazione dinamica, durate attese dalla timeline Kokoro in
`rec_src/kokoro_timeline.json`) e scrive `rec_src/take_spans.json`, verificato con
trascrizione automatica battuta per battuta. Poi `./build.sh take`.
Funziona allo stesso modo con una tua registrazione unica di tutto il copione.

### Registrazione propria

Un file per battuta in `rec/<id>.wav` (anche `.mp3`, `.m4a`: `rec/b01.wav` …
`rec/b25.wav`), letto con il testo del campo `say`; poi `./build.sh rec`. Il silenzio
ai bordi viene tolto e le battute sono unite con pause secondo la punteggiatura
(0,14 s dopo una virgola, 0,2 s dopo i due punti, 0,36 s a fine frase).

## Copertina

`node render.mjs cover` → `out/cover.png` (1080×1920) più i ritagli di controllo
`out/cover_griglia_3x4.png` (griglia del profilo) e `out/cover_feed_4x5.png` (feed).
Titolo e disegno stanno nella fascia centrale (y 285–1635), l'unica sempre visibile.
Testo e righe in `COVER` dentro `reel_template.html`. Su Instagram: "Modifica
copertina" → "Aggiungi dal rullino".

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
