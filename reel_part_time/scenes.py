# -*- coding: utf-8 -*-
"""
Copione del reel "Part-time sulla carta" (serie: cose che il tuo capo spera
che tu non scopra mai, parte 1).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
    {"id": "b02", "visual": "contract",
     "say":  "Sul contratto c'è scritto part-time.",
     "text": "SUL CONTRATTO C'È SCRITTO [g]PART-TIME[/g]"},
    {"id": "b03", "visual": "contract",
     "say":  "Ma tu, in realtà, lavori a tempo pieno.",
     "text": "MA TU, IN REALTÀ, LAVORI [r]A TEMPO PIENO[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b04", "visual": "desk",
     "say":  "Prendi Andrea: assunto per ventiquattro ore a settimana.",
     "text": "PRENDI ANDREA: ASSUNTO PER [g]24 ORE[/g] A SETTIMANA"},
    {"id": "b05", "visual": "desk",
     "say":  "Ma ogni giorno entra alle otto e mezza, ed esce alle cinque e mezza.",
     "text": "MA OGNI GIORNO ENTRA ALLE [r]8:30[/r] ED ESCE ALLE [r]17:30[/r]"},
    {"id": "b06", "visual": "payslip",
     "say":  "In busta paga, però, le ore sono sempre e solo ventiquattro.",
     "text": "IN BUSTA PAGA, PERÒ, LE ORE SONO SEMPRE E SOLO [r]24[/r]"},
    {"id": "b07", "visual": "envelope",
     "say":  "E le altre sedici? A volte arrivano in un'altra busta, in contanti.",
     "text": "E LE ALTRE 16? A VOLTE ARRIVANO IN UN'ALTRA BUSTA, [r]IN CONTANTI[/r]"},
    {"id": "b08", "visual": "empty",
     "say":  "A volte, nemmeno quella.",
     "text": "A VOLTE, [r]NEMMENO QUELLA[/r]"},

    # --- cosa si perde ------------------------------------------------------
    {"id": "b09", "visual": "lost",
     "say":  "Soldi che non contano per la pensione, il TFR, la tredicesima e le ferie.",
     "text": "SOLDI CHE NON CONTANO PER LA [r]PENSIONE[/r], IL [r]TFR[/r], LA [r]13ª[/r] E LE [r]FERIE[/r]"},
    {"id": "b10", "visual": "sick",
     "say":  "E se ti ammali o perdi il lavoro, l'INPS vede solo ventiquattro ore.",
     "text": "E SE TI AMMALI O PERDI IL LAVORO, L'INPS VEDE SOLO [r]24 ORE[/r]"},

    # --- la distinzione -----------------------------------------------------
    {"id": "b11", "visual": "think",
     "say":  "Attenzione, però: fare qualche ora in più non è vietato.",
     "text": "ATTENZIONE, PERÒ: FARE QUALCHE ORA IN PIÙ [g]NON È VIETATO[/g]"},
    {"id": "b12", "visual": "extra",
     "say":  "Si chiamano ore supplementari: vanno in busta paga, di solito con una maggiorazione.",
     "text": "SI CHIAMANO [g]ORE SUPPLEMENTARI[/g]: VANNO IN BUSTA PAGA, DI SOLITO CON UNA MAGGIORAZIONE"},
    {"id": "b13", "visual": "night",
     "say":  "Il problema è quando il part-time esiste solo sulla carta.",
     "text": "IL PROBLEMA È QUANDO IL PART-TIME ESISTE [r]SOLO SULLA CARTA[/r]"},
    {"id": "b14", "visual": "night",
     "say":  "E il tempo pieno, invece, è la regola.",
     "text": "E IL TEMPO PIENO, INVECE, [r]È LA REGOLA[/r]"},

    # --- cosa puoi fare -----------------------------------------------------
    {"id": "b15", "visual": "rights",
     "say":  "In quel caso puoi chiedere le differenze di stipendio.",
     "text": "IN QUEL CASO PUOI CHIEDERE LE [g]DIFFERENZE DI STIPENDIO[/g]"},
    {"id": "b16", "visual": "rights",
     "say":  "E che tutto venga ricalcolato sulle ore vere:",
     "text": "E CHE TUTTO VENGA RICALCOLATO [g]SULLE ORE VERE[/g]:"},
    {"id": "b17", "visual": "rights",
     "say":  "TFR, tredicesima, ferie. E i contributi per la pensione.",
     "text": "[g]TFR[/g], [g]13ª[/g], [g]FERIE[/g]. E I [g]CONTRIBUTI[/g] PER LA PENSIONE"},

    # --- i tempi ------------------------------------------------------------
    {"id": "b18", "visual": "deadline",
     "say":  "Per lo stipendio, di solito, hai cinque anni dalla fine del rapporto.",
     "text": "PER LO STIPENDIO, DI SOLITO, HAI [g]5 ANNI[/g] DALLA FINE DEL RAPPORTO"},
    {"id": "b19", "visual": "alarm",
     "say":  "Ma i contributi si prescrivono mentre lavori: meglio non aspettare.",
     "text": "MA I CONTRIBUTI SI PRESCRIVONO MENTRE LAVORI: [r]MEGLIO NON ASPETTARE[/r]"},

    # --- le prove -----------------------------------------------------------
    {"id": "b20", "visual": "proofs",
     "say":  "E ricorda: tutto si gioca sulle prove.",
     "text": "E RICORDA: TUTTO SI GIOCA [r]SULLE PROVE[/r]"},
    {"id": "b21", "visual": "proofs",
     "say":  "Timbrature, turni su WhatsApp, mail mandate alle sette di sera, colleghi pronti a testimoniare.",
     "text": "[g]TIMBRATURE[/g], [g]TURNI SU WHATSAPP[/g], [g]MAIL[/g] ALLE 19:00, [g]COLLEGHI[/g] PRONTI A TESTIMONIARE"},
    {"id": "b22", "visual": "notebook",
     "say":  "E da oggi, segnati ogni giorno a che ora entri e a che ora esci.",
     "text": "E DA OGGI, SEGNATI OGNI GIORNO [g]A CHE ORA ENTRI[/g] E [g]A CHE ORA ESCI[/g]"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b23", "visual": "sixteen",
     "say":  "Perché se il contratto dice ventiquattro ore, e tu ne fai quaranta,",
     "text": "PERCHÉ SE IL CONTRATTO DICE [g]24 ORE[/g] E TU NE FAI [r]40[/r],"},
    {"id": "b24", "visual": "sixteen",
     "say":  "quelle sedici ore non sono sparite. E nemmeno i tuoi diritti.",
     "text": "QUELLE 16 ORE [r]NON SONO SPARITE[/r]. E NEMMENO I TUOI DIRITTI"},
    {"id": "b25", "visual": "cta",
     "say":  "Ti riconosci? Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "TI RICONOSCI? [i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
