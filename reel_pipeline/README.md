# Reel Pagamee — stile doodle (1080×1920)

Pipeline offline che produce un reel verticale in stile *stick figure*
(linee nere su fondo bianco) con scritte a schermo e voce narrante italiana.

Output: `out/reel.mp4` — 1080×1920, H.264 yuv420p, 30 fps, AAC stereo 44.1 kHz.

## Come si rigenera

```bash
npm install
./build.sh                 # voce offline (espeak-ng + mbrola it4)
./build.sh eleven          # voce ElevenLabs (serve ELEVENLABS_API_KEY in ambiente)
```

Musica di sottofondo (facoltativa, viene abbassata automaticamente sotto la voce):

```bash
python3 mix_audio.py --music /percorso/traccia.mp3 --music-db -26
node render.mjs full 30
```

## I pezzi

| file | cosa fa |
|---|---|
| `scenes.py` | copione: 10 scene, con la battuta del voice-over |
| `gen_audio.py` | genera un audio per battuta e scrive `timeline.json` (start/end/durata) |
| `mix_audio.py` | voce + whoosh ai cambi scena (+ musica opzionale) → `audio/final.wav` |
| `reel_template.html` | disegno delle scene: figure SVG, testi, fumetti, animazioni |
| `build_html.py` | inietta `timeline.json` nel template → `reel.html` |
| `render.mjs` | `check` (controlli layout), `preview` (1 PNG per scena), `full` (video) |

La durata di ogni scena **viene dall'audio**: si cambia il copione in `scenes.py`,
si rigenera, e il video si riadatta da solo.

## Controlli automatici

`node render.mjs check` ferma la build se una scena ha problemi:

- testo o fumetto fuori dall'area di sicurezza;
- testo sovrapposto alla testa di un personaggio;
- personaggi che si accavallano;
- a-capo non voluti (ogni riga è dichiarata a mano e non deve spezzarsi);
- codina del fumetto troppo lontana da chi parla, o sopra la sua testa.

`node render.mjs preview` salva un fotogramma per scena in `preview/` per il
controllo a occhio.

## Note di stile

- Fondo `#ffffff`, tratto `#141414` spesso 9 px, estremità arrotondate.
- Accenti solo sulle parole chiave: rosso `#e5342b`, verde `#1a9e4b`, blu `#2b5fb3`;
  cravatta del datore viola `#5b2a86`.
- Font: **Humor Sans** (stile xkcd); **Comic Neue** per il simbolo `€`, perché
  in Humor Sans quel glifo è corrotto (classe `.eur`).
- Personaggi: lavoratore (camicia a scacchi rossa), datore (camicia bianca +
  cravatta + occhiali + capelli grigi), avvocata (blazer + caschetto).
- Se una riga non entra in larghezza, `fitAll()` rimpicciolisce il blocco invece
  di mandarla a capo.

## Cambiare copione per un reel nuovo

1. Riscrivi le battute in `scenes.py`.
2. Adegua testi/pose in `buildScenes()` dentro `reel_template.html`.
3. `./build.sh` — i controlli dicono subito se qualcosa non torna.
