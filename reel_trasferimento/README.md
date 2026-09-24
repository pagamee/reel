# Reel "Trasferimento da un giorno all'altro" — parte 5 (1080×1920)

Serie *"Cose sul lavoro che il tuo capo spera che tu non scopra mai"*, **parte 5**.
Stessa pipeline, stesso stile e stesso protagonista (Andrea) della parte 1 in
`../reel_part_time/` (vedi il suo README per i dettagli tecnici).

- `scenes.py`: copione (18 battute) e `SERIES_PART`.
- `reel_template.html`: stesso motore delle parti precedenti; cambiano le scene (`ART.*`),
  gli oggetti di questa puntata (valigia, cartello stradale, casa, assegno in bianco,
  maschera, scudo "104"…) e la copertina (`COVER`, `SERIES_PART`).
- Voce: ElevenLabs "Chris Basetta – Social Media" (eleven_multilingual_v2), una lettura
  continua in `rec_src/eleven_full.mp3`, accelerata ×1,2 in `rec_src/take.flac`;
  confini delle battute in `rec_src/take_spans.json` (`rec_src/align_take.py`, guida:
  timeline Kokoro in `rec_src/kokoro_timeline.json`), verificati battuta per battuta con trascrizione automatica.
  Rigenerare: `./build.sh take`.
- Copertina: `node render.mjs cover` → `out/cover.png` (+ ritagli 3:4 e 4:5).

Contenuto giuridico semplificato per un reel: trasferimento ad altra unità produttiva solo
per comprovate ragioni tecniche, organizzative e produttive (art. 2103, comma 8, c.c.);
forma scritta e preavviso secondo il CCNL; consenso necessario per chi usa i permessi
per assistere un familiare (art. 33, comma 5, L. 104/1992); impugnazione stragiudiziale
entro 60 giorni dalla comunicazione (art. 32 L. 183/2010), anche con ricorso d'urgenza.

`node_modules` e `tts` sono link alla cartella della parte 1 (non versionati); in un
ambiente nuovo `npm install` e, se serve Kokoro, `./setup_tts.sh`.
