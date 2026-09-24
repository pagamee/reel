# Reel "TFR e fuori busta" — parte 4 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 4**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (20 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti precedenti; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (scatolone, busta paga, chat, manette, aureola,
  ricevute…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`; confine b13/b14 corretto a mano
  sulla pausa reale), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico semplificato per un reel: TFR calcolato su tutte le somme corrisposte
in dipendenza del rapporto a titolo non occasionale (art. 2120 c.c.), quindi anche sulla
parte pagata fuori busta, se provata; contributi e relative sanzioni a carico del datore;
segnalazione a Ispettorato del lavoro e INPS; prescrizione del TFR in 5 anni dalla
cessazione. La cifra "circa 2.000 €" è 800 € × 36 mesi ÷ 13,5, senza rivalutazione.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
