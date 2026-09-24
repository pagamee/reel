# Reel "Turni di notte con un figlio piccolo" — parte 8 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 8**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (17 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti precedenti; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (bambino, lettino, luna, carrozzina, turni di notte…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico semplificato per un reel: non sono obbligati al lavoro notturno la
madre di un figlio sotto i 3 anni o, in alternativa, il padre convivente; il genitore unico
affidatario di un figlio convivente sotto i 12 anni; chi ha a carico una persona con
disabilità ai sensi della L. 104/1992 (art. 11 d.lgs. 66/2003, art. 53 d.lgs. 151/2001);
divieto di lavoro dalle 24 alle 6 dalla gravidanza a un anno del bambino. Il copione letto
è stato accorciato di poche parole per stare nei crediti ElevenLabs rimasti.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
