# -*- coding: utf-8 -*-
"""
Copione del reel "Turno cambiato all'ultimo minuto" (serie: cose sul lavoro che
il tuo capo spera che tu non scopra mai, parte 7).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 7"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "night",
     "say":  "Sono le ventitré. Andrea è appena tornato a casa dal turno.",
     "text": "SONO LE [r]23[/r]. ANDREA È APPENA TORNATO A CASA DAL TURNO"},
    {"id": "b03", "visual": "msg",
     "say":  "Gli arriva un messaggio del capo.",
     "text": "GLI ARRIVA [r]UN MESSAGGIO DEL CAPO[/r]"},
    {"id": "b04", "visual": "msg",
     "say":  "«Domani non entri alle quattordici. Entri alle sei.»",
     "text": "«DOMANI NON ENTRI ALLE 14. [r]ENTRI ALLE 6[/r]»"},
    {"id": "b05", "visual": "boss",
     "say":  "«Ho un buco da coprire. I turni li decido io, e tu ti adegui.»",
     "text": "«HO UN BUCO DA COPRIRE. [r]I TURNI LI DECIDO IO[/r], E TU TI ADEGUI»"},
    {"id": "b06", "visual": "limit",
     "say":  "Ci si adegua, sì. Ma fino a un certo punto.",
     "text": "CI SI ADEGUA, SÌ. [g]MA FINO A UN CERTO PUNTO[/g]"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b07", "visual": "plan",
     "say":  "I turni vanno programmati, e le modifiche comunicate con un preavviso ragionevole.",
     "text": "TURNI [g]PROGRAMMATI[/g], E CAMBI CON UN [g]PREAVVISO RAGIONEVOLE[/g]"},
    {"id": "b08", "visual": "plan",
     "say":  "Spesso è il contratto collettivo a fissare il preavviso minimo.",
     "text": "SPESSO È IL [g]CCNL[/g] A FISSARE IL PREAVVISO MINIMO"},
    {"id": "b09", "visual": "rest",
     "say":  "E c'è un limite che vale per tutti: undici ore di riposo consecutive ogni ventiquattro.",
     "text": "E C'È UN LIMITE PER TUTTI: [g]11 ORE DI RIPOSO[/g] CONSECUTIVE OGNI 24"},
    {"id": "b10", "visual": "rest",
     "say":  "Andrea ha staccato alle ventidue: rientrando alle sei, ne farebbe solo otto.",
     "text": "HA STACCATO ALLE 22: RIENTRANDO ALLE 6, NE FAREBBE [r]SOLO 8[/r]"},
    {"id": "b11", "visual": "rest",
     "say":  "Salvo deroghe del contratto collettivo, così non si può.",
     "text": "SALVO DEROGHE DEL CCNL, [r]COSÌ NON SI PUÒ[/r]"},
    {"id": "b12", "visual": "flex",
     "say":  "«Ma nel contratto c'è la flessibilità!»",
     "text": "«MA NEL CONTRATTO C'È LA [r]FLESSIBILITÀ[/r]!»"},
    {"id": "b13", "visual": "flex",
     "say":  "La flessibilità non è un potere illimitato: va usata con correttezza e buona fede.",
     "text": "LA FLESSIBILITÀ [r]NON È ILLIMITATA[/r]: VA USATA CON [g]CORRETTEZZA E BUONA FEDE[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b14", "visual": "write",
     "say":  "Andrea risponde: «Me lo metta per iscritto, con il preavviso previsto dal contratto.»",
     "text": "ANDREA: «ME LO METTA [g]PER ISCRITTO[/g], CON IL PREAVVISO DEL CONTRATTO»"},
    {"id": "b15", "visual": "cede",
     "say":  "Il capo ci ripensa. «Va bene, sento l'ufficio del personale.»",
     "text": "IL CAPO CI RIPENSA. «VA BENE, [g]SENTO L'UFFICIO DEL PERSONALE[/g]»"},
    {"id": "b16", "visual": "advice",
     "say":  "Il consiglio: salva i messaggi, e controlla cosa dice il tuo contratto collettivo sui cambi turno.",
     "text": "[g]SALVA I MESSAGGI[/g] E CONTROLLA COSA DICE IL TUO [g]CCNL[/g] SUI CAMBI TURNO"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b17", "visual": "cta",
     "say":  "Ti cambiano i turni all'ultimo minuto?",
     "text": "TI CAMBIANO I TURNI [r]ALL'ULTIMO MINUTO[/r]?"},
    {"id": "b18", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
