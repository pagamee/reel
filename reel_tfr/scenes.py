# -*- coding: utf-8 -*-
"""
Copione del reel "Il TFR non si rateizza" (serie: cose sul lavoro che il tuo capo
spera che tu non scopra mai, parte 2).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 2"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "resign",
     "say":  "Andrea si è dimesso: ha trovato un lavoro migliore.",
     "text": "ANDREA SI È DIMESSO: HA TROVATO UN [g]LAVORO MIGLIORE[/g]"},
    {"id": "b03", "visual": "bossno",
     "say":  "Il capo la prende male. «Il TFR? Te lo scordi.»",
     "text": "IL CAPO LA PRENDE MALE. «IL TFR? [r]TE LO SCORDI[/r]»"},
    {"id": "b04", "visual": "rate",
     "say":  "«Te lo do a rate: trecento euro al mese. Se mi va.»",
     "text": "«TE LO DO [r]A RATE[/r]: 300 EURO AL MESE. SE MI VA»"},
    {"id": "b05", "visual": "causa",
     "say":  "«Non ti sta bene? Fammi causa: ci vediamo tra cinque anni.»",
     "text": "«NON TI STA BENE? [r]FAMMI CAUSA[/r]: CI VEDIAMO TRA 5 ANNI»"},
    {"id": "b06", "visual": "wrong",
     "say":  "Peccato che abbia torto su tutto.",
     "text": "PECCATO CHE ABBIA [g]TORTO SU TUTTO[/g]"},

    # --- cos'è il TFR -------------------------------------------------------
    {"id": "b07", "visual": "gift",
     "say":  "Il TFR non è un regalo, e nemmeno un premio fedeltà.",
     "text": "IL TFR [r]NON È UN REGALO[/r], E NEMMENO UN PREMIO FEDELTÀ"},
    {"id": "b08", "visual": "savings",
     "say":  "È stipendio che hai già guadagnato: l'azienda lo ha solo messo da parte, mese dopo mese.",
     "text": "È [g]STIPENDIO GIÀ GUADAGNATO[/g]: L'AZIENDA LO HA SOLO MESSO DA PARTE"},
    {"id": "b09", "visual": "law",
     "say":  "E per il Codice Civile spetta sempre, quando il rapporto finisce.",
     "text": "PER IL CODICE CIVILE [g]SPETTA SEMPRE[/g], QUANDO IL RAPPORTO FINISCE"},
    {"id": "b10", "visual": "law",
     "say":  "Anche se sei tu a dimetterti.",
     "text": "[g]ANCHE SE SEI TU A DIMETTERTI[/g]"},

    # --- tempi e rate -------------------------------------------------------
    {"id": "b11", "visual": "payday",
     "say":  "Quando? Di solito con l'ultima busta paga, o nei tempi del tuo contratto collettivo.",
     "text": "QUANDO? DI SOLITO CON L'[g]ULTIMA BUSTA PAGA[/g] O NEI TEMPI DEL TUO CCNL"},
    {"id": "b12", "visual": "norate",
     "say":  "E le rate? Senza il tuo accordo, non può importele.",
     "text": "E LE RATE? [r]SENZA IL TUO ACCORDO[/r] NON PUÒ IMPORTELE"},

    # --- se non paga --------------------------------------------------------
    {"id": "b13", "visual": "decree",
     "say":  "Se non paga, si chiede al giudice un decreto ingiuntivo.",
     "text": "SE NON PAGA, SI CHIEDE AL GIUDICE UN [g]DECRETO INGIUNTIVO[/g]"},
    {"id": "b14", "visual": "decree",
     "say":  "Con la busta paga come prova, i tempi sono brevi. Altro che cinque anni.",
     "text": "CON LA BUSTA PAGA COME PROVA I TEMPI SONO BREVI. [r]ALTRO CHE 5 ANNI[/r]"},
    {"id": "b15", "visual": "bank",
     "say":  "E se il decreto è esecutivo, si può pignorare il conto dell'azienda.",
     "text": "E SE È ESECUTIVO, SI PUÒ [r]PIGNORARE IL CONTO[/r] DELL'AZIENDA"},
    {"id": "b16", "visual": "costs",
     "say":  "Con interessi e, di solito, spese legali a carico suo.",
     "text": "CON [g]INTERESSI[/g] E, DI SOLITO, [g]SPESE LEGALI[/g] A CARICO SUO"},
    {"id": "b17", "visual": "fondo",
     "say":  "E se l'azienda fallisce? Il TFR lo paga il Fondo di garanzia dell'INPS.",
     "text": "E SE L'AZIENDA FALLISCE? PAGA IL [g]FONDO DI GARANZIA INPS[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b18", "visual": "explain",
     "say":  "Andrea glielo spiega, con calma.",
     "text": "ANDREA GLIELO SPIEGA, [g]CON CALMA[/g]"},
    {"id": "b19", "visual": "paid",
     "say":  "E il TFR arriva con l'ultima busta paga. Tutto, e senza rate.",
     "text": "E IL TFR ARRIVA CON L'ULTIMA BUSTA PAGA. [g]TUTTO, E SENZA RATE[/g]"},
    {"id": "b20", "visual": "moral",
     "say":  "Il TFR è tuo. E nessuno può usarlo come ricatto.",
     "text": "IL TFR È [g]TUO[/g]. E NESSUNO PUÒ USARLO [r]COME RICATTO[/r]"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b21", "visual": "cta",
     "say":  "Ti stanno facendo aspettare il TFR?",
     "text": "TI STANNO FACENDO [r]ASPETTARE IL TFR[/r]?"},
    {"id": "b22", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
