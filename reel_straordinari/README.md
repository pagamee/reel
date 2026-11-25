# Reel "Fai 50 ore, te ne pagano 40" — piano n. 1, straordinari (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, piano editoriale n. 1.
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

Contenuto giuridico semplificato: orario normale 40 ore settimanali o meno da CCNL
(art. 3 d.lgs. 66/2003); straordinario compensato con le maggiorazioni dei contratti
collettivi (art. 5); lavoro in più noto e accettato dal datore; prove; prescrizione
quinquennale che, secondo la Cassazione (2022), di regola decorre dalla fine del rapporto.
Video da pubblicare: `out/reel_musica.mp4` (con la base di `../music/`).

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
