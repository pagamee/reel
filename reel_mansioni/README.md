# Reel "Mansioni superiori" — parte 3 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 3**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (21 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti 1 e 2; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (portablocco, targa "responsabile", calendario dei mesi,
  scalini dei livelli, bilancia, annaffiatoio…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`; b13–b19 corrette a mano sulle
  pause reali), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico (art. 2103 c.c.) semplificato per un reel: paga del livello
superiore per il periodo in cui si svolgono le mansioni; assegnazione definitiva dopo
il periodo del CCNL o, in mancanza, 6 mesi continuativi, salvo sostituzione di un
collega con diritto alla conservazione del posto; mansioni superiori prevalenti.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
