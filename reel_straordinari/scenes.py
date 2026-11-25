# -*- coding: utf-8 -*-
"""
Copione del reel "Fai 50 ore, te ne pagano 40" (serie: cose sul lavoro che il tuo
capo spera che tu non scopra mai; piano editoriale n. 1, straordinari non pagati).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

BEATS = [
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    {"id": "b02", "visual": "contract",
     "say":  "Andrea ha un contratto da quaranta ore a settimana.",
     "text": "ANDREA HA UN CONTRATTO DA [g]40 ORE[/g] A SETTIMANA"},
    {"id": "b03", "visual": "late",
     "say":  "Ma ogni giorno lavora dieci ore. Fanno cinquanta a settimana.",
     "text": "MA OGNI GIORNO LAVORA 10 ORE. FANNO [r]50 A SETTIMANA[/r]"},
    {"id": "b04", "visual": "payslip",
     "say":  "In busta paga, però, gli straordinari non ci sono mai.",
     "text": "IN BUSTA PAGA GLI STRAORDINARI [r]NON CI SONO MAI[/r]"},
    {"id": "b05", "visual": "boss",
     "say":  "«Qui siamo una famiglia: si resta finché serve.»",
     "text": "«QUI SIAMO UNA FAMIGLIA: [r]SI RESTA FINCHÉ SERVE[/r]»"},
    {"id": "b06", "visual": "boss",
     "say":  "«E poi gli straordinari non te li ho mai chiesti.»",
     "text": "«E POI GLI STRAORDINARI [r]NON TE LI HO MAI CHIESTI[/r]»"},
    {"id": "b07", "visual": "wrong",
     "say":  "Peccato che non funzioni così.",
     "text": "PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},

    {"id": "b08", "visual": "law",
     "say":  "Per legge l'orario normale è di quaranta ore a settimana, o meno se lo prevede il tuo contratto collettivo.",
     "text": "ORARIO NORMALE: [g]40 ORE[/g] A SETTIMANA, O MENO SE LO PREVEDE IL CCNL"},
    {"id": "b09", "visual": "law",
     "say":  "Le ore in più sono straordinario, e vanno pagate con la maggiorazione del contratto collettivo.",
     "text": "LE ORE IN PIÙ SONO STRAORDINARIO: [g]PAGATE CON LA MAGGIORAZIONE[/g]"},
    {"id": "b10", "visual": "knows",
     "say":  "E se il capo sa che resti, e lo accetta, non può dire che non te l'ha chiesto.",
     "text": "SE IL CAPO SA CHE RESTI E LO ACCETTA, [r]NON PUÒ DIRE CHE NON L'HA CHIESTO[/r]"},
    {"id": "b11", "visual": "calc",
     "say":  "Dieci ore in più a settimana, per un anno: sono più di quattrocento ore.",
     "text": "10 ORE IN PIÙ A SETTIMANA, PER UN ANNO: [g]OLTRE 400 ORE[/g]"},
    {"id": "b12", "visual": "proofs",
     "say":  "Il punto è provarle: badge, mail, chat, accessi al computer, colleghi.",
     "text": "SERVONO PROVE: [g]BADGE[/g], [g]MAIL[/g], [g]CHAT[/g], [g]COLLEGHI[/g]"},
    {"id": "b13", "visual": "time",
     "say":  "E per recuperarle hai tempo: in genere cinque anni, che di solito partono dalla fine del rapporto.",
     "text": "PER RECUPERARLE, IN GENERE, [g]5 ANNI[/g] DALLA FINE DEL RAPPORTO"},

    {"id": "b14", "visual": "ask",
     "say":  "Così Andrea mette in fila le prove, e chiede le differenze.",
     "text": "ANDREA METTE IN FILA LE PROVE E [g]CHIEDE LE DIFFERENZE[/g]"},
    {"id": "b15", "visual": "cede",
     "say":  "Il capo ci ripensa. «Va bene, sistemiamo.»",
     "text": "IL CAPO CI RIPENSA. «VA BENE, [g]SISTEMIAMO[/g]»"},

    {"id": "b16", "visual": "cta",
     "say":  "Lavori più ore di quelle che ti pagano?",
     "text": "LAVORI [r]PIÙ ORE[/r] DI QUELLE CHE TI PAGANO?"},
    {"id": "b17", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
