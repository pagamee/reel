# -*- coding: utf-8 -*-
"""
Copione del reel "TFR e fuori busta" (serie: cose sul lavoro che il tuo capo
spera che tu non scopra mai, parte 4).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 4"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "fired",
     "say":  "Andrea viene licenziato, e l'azienda gli liquida il TFR.",
     "text": "ANDREA VIENE [r]LICENZIATO[/r], E L'AZIENDA GLI LIQUIDA IL TFR"},
    {"id": "b03", "visual": "inbusta",
     "say":  "Ma lo calcola solo sulla parte in busta paga.",
     "text": "MA LO CALCOLA [r]SOLO SULLA PARTE IN BUSTA[/r]"},
    {"id": "b04", "visual": "cash",
     "say":  "Per tre anni, Andrea ha preso ottocento euro al mese in contanti. Fuori busta.",
     "text": "PER 3 ANNI HA PRESO [r]800 € AL MESE IN CONTANTI[/r]. FUORI BUSTA"},
    {"id": "b05", "visual": "deny",
     "say":  "«Quali contanti? Io ho sempre pagato tutto in busta.»",
     "text": "«QUALI CONTANTI? IO HO SEMPRE PAGATO [r]TUTTO IN BUSTA[/r]»"},
    {"id": "b06", "visual": "chats",
     "say":  "Peccato che Andrea abbia i suoi messaggi, mese per mese.",
     "text": "PECCATO CHE ANDREA ABBIA [g]I SUOI MESSAGGI[/g], MESE PER MESE"},
    {"id": "b07", "visual": "guilt",
     "say":  "«E comunque quei soldi li hai presi pure tu. Ti metti nei guai da solo.»",
     "text": "«QUEI SOLDI LI HAI PRESI PURE TU. [r]TI METTI NEI GUAI DA SOLO[/r]»"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b08", "visual": "law",
     "say":  "Davvero? Vediamo cosa dice la legge.",
     "text": "DAVVERO? [g]VEDIAMO COSA DICE LA LEGGE[/g]"},
    {"id": "b09", "visual": "law",
     "say":  "Per il Codice Civile, il TFR si calcola su tutto quello che ricevi per il tuo lavoro, in modo non occasionale.",
     "text": "IL TFR SI CALCOLA SU [g]TUTTO QUELLO CHE RICEVI[/g] PER IL TUO LAVORO"},
    {"id": "b10", "visual": "law",
     "say":  "Anche sulla parte pagata in nero.",
     "text": "[g]ANCHE SULLA PARTE PAGATA IN NERO[/g]"},
    {"id": "b11", "visual": "calc",
     "say":  "Ottocento euro al mese per tre anni: sono circa duemila euro di TFR in più.",
     "text": "800 € AL MESE PER 3 ANNI: [g]CIRCA 2.000 € DI TFR IN PIÙ[/g]"},
    {"id": "b12", "visual": "inps",
     "say":  "E i contributi? Doveva versarli l'azienda, su tutta la paga.",
     "text": "E I CONTRIBUTI? [g]DOVEVA VERSARLI L'AZIENDA[/g], SU TUTTA LA PAGA"},
    {"id": "b13", "visual": "inps",
     "say":  "E le sanzioni per quelli non versati sono a carico suo.",
     "text": "E LE SANZIONI PER QUELLI NON VERSATI SONO [r]A CARICO SUO[/r]"},
    {"id": "b14", "visual": "report",
     "say":  "In più, il nero si può segnalare all'Ispettorato del lavoro e all'INPS.",
     "text": "IL NERO SI PUÒ SEGNALARE ALL'[g]ISPETTORATO DEL LAVORO[/g] E ALL'[g]INPS[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b15", "visual": "threat",
     "say":  "Andrea è chiaro: o TFR ricalcolato su tutto, o segnalazione.",
     "text": "O [g]TFR RICALCOLATO SU TUTTO[/g], O [r]SEGNALAZIONE[/r]"},
    {"id": "b16", "visual": "cede",
     "say":  "«Dai, dai, un attimo… ne parliamo.»",
     "text": "«DAI, DAI, UN ATTIMO… [g]NE PARLIAMO[/g]»"},
    {"id": "b17", "visual": "proofs",
     "say":  "Il consiglio: conserva ogni prova. Messaggi, prelievi, bonifici, colleghi che possono testimoniare.",
     "text": "CONSERVA OGNI PROVA: [g]MESSAGGI[/g], [g]PRELIEVI[/g], [g]BONIFICI[/g], [g]TESTIMONI[/g]"},
    {"id": "b18", "visual": "time",
     "say":  "E non aspettare troppo: per il TFR hai cinque anni dalla fine del rapporto.",
     "text": "E NON ASPETTARE: PER IL TFR HAI [r]5 ANNI[/r] DALLA FINE DEL RAPPORTO"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b19", "visual": "cta",
     "say":  "Ti pagavano in parte fuori busta?",
     "text": "TI PAGAVANO IN PARTE [r]FUORI BUSTA[/r]?"},
    {"id": "b20", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
