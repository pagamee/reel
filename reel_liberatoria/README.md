# Reel "Firma la liberatoria o non ti pago" — parte 6 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 6**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (17 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti precedenti; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (liberatoria, catena, cartellina "copia"…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`; confine b06/b07 corretto a mano
  sulla pausa reale), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico semplificato per un reel: retribuzione, TFR e ferie non godute non
possono essere condizionati a una rinuncia; rinunce e transazioni su diritti inderogabili
impugnabili entro 6 mesi (art. 2113 c.c.), salvo quelle in sede protetta (Ispettorato,
sede sindacale…); la quietanza liberatoria generica di regola vale come dichiarazione di
scienza, non come rinuncia; messa in mora e decreto ingiuntivo per il recupero, con
interessi.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
