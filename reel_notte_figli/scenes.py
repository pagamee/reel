# -*- coding: utf-8 -*-
"""
Copione del reel "Turni di notte con un figlio piccolo" (serie: cose sul lavoro
che il tuo capo spera che tu non scopra mai, parte 8).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 8"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "family",
     "say":  "Andrea ha un figlio di due anni. E la sera, la buonanotte gliela dà lui.",
     "text": "ANDREA HA UN [g]FIGLIO DI 2 ANNI[/g]. E LA SERA, LA BUONANOTTE GLIELA DÀ LUI"},
    {"id": "b03", "visual": "shifts",
     "say":  "Un giorno il capo lo mette in turno di notte. Fisso.",
     "text": "UN GIORNO IL CAPO LO METTE [r]IN TURNO DI NOTTE[/r]. FISSO"},
    {"id": "b04", "visual": "boss",
     "say":  "«L'azienda deve coprire le notti. Se lavori qui, ti adegui.»",
     "text": "«L'AZIENDA DEVE COPRIRE LE NOTTI. [r]SE LAVORI QUI, TI ADEGUI[/r]»"},
    {"id": "b05", "visual": "wrong",
     "say":  "Peccato che, per alcuni, la notte non sia un obbligo.",
     "text": "PECCATO CHE, PER ALCUNI, [g]LA NOTTE NON SIA UN OBBLIGO[/g]"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b06", "visual": "law",
     "say":  "Non è obbligata al lavoro notturno la madre di un figlio sotto i tre anni.",
     "text": "NON È OBBLIGATA AL LAVORO NOTTURNO LA [g]MADRE DI UN FIGLIO SOTTO I 3 ANNI[/g]"},
    {"id": "b07", "visual": "law",
     "say":  "O, in alternativa, il padre che vive con loro.",
     "text": "O, IN ALTERNATIVA, [g]IL PADRE CONVIVENTE[/g]"},
    {"id": "b08", "visual": "others",
     "say":  "E nemmeno il genitore unico affidatario di un figlio convivente sotto i dodici anni.",
     "text": "NEMMENO IL [g]GENITORE UNICO AFFIDATARIO[/g] DI UN FIGLIO CONVIVENTE SOTTO I 12 ANNI"},
    {"id": "b09", "visual": "others",
     "say":  "O chi ha a carico una persona con disabilità.",
     "text": "O CHI HA A CARICO [g]UNA PERSONA CON DISABILITÀ[/g]"},
    {"id": "b10", "visual": "mom",
     "say":  "E dalla gravidanza fino a un anno del bambino, per la mamma la notte è vietata.",
     "text": "DALLA GRAVIDANZA A 1 ANNO DEL BAMBINO, PER LA MAMMA [r]LA NOTTE È VIETATA[/r]"},
    {"id": "b11", "visual": "shield",
     "say":  "Non è un favore: è una tutela prevista dalla legge.",
     "text": "NON È UN FAVORE: [g]È UNA TUTELA DI LEGGE[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b12", "visual": "docs",
     "say":  "Andrea presenta i documenti, e chiede l'esonero per iscritto.",
     "text": "ANDREA PRESENTA I DOCUMENTI E CHIEDE [g]L'ESONERO PER ISCRITTO[/g]"},
    {"id": "b13", "visual": "report",
     "say":  "E se gli imponessero la notte lo stesso? Può segnalarlo all'Ispettorato del lavoro.",
     "text": "E SE GLI IMPONESSERO LA NOTTE LO STESSO? [r]SEGNALAZIONE ALL'ISPETTORATO[/r]"},
    {"id": "b14", "visual": "cede",
     "say":  "Il capo ci ripensa. «Va bene, niente notti.»",
     "text": "IL CAPO CI RIPENSA. «VA BENE, [g]NIENTE NOTTI[/g]»"},
    {"id": "b15", "visual": "goodnight",
     "say":  "E stasera, la buonanotte la dà ancora Andrea.",
     "text": "E STASERA, LA BUONANOTTE [g]LA DÀ ANCORA ANDREA[/g]"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b16", "visual": "cta",
     "say":  "Ti impongono la notte, anche se hai un figlio piccolo?",
     "text": "TI IMPONGONO LA NOTTE, [r]ANCHE SE HAI UN FIGLIO PICCOLO[/r]?"},
    {"id": "b17", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
