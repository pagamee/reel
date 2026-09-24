# Reel "Turno cambiato all'ultimo minuto" — parte 7 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 7**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (18 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti precedenti; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (barre delle ore di riposo, cartello di divieto,
  infinito barrato, chat grandi…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico semplificato per un reel: turni programmati e modifiche con
preavviso ragionevole (spesso fissato dal CCNL); riposo giornaliero di 11 ore consecutive
ogni 24 (art. 7 d.lgs. 66/2003), salvo deroghe della contrattazione collettiva (art. 17);
esercizio della flessibilità secondo correttezza e buona fede. Nel video Andrea stacca
alle 22 e il capo gli chiede di rientrare alle 6.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
