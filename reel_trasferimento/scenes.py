# -*- coding: utf-8 -*-
"""
Copione del reel "Trasferimento da un giorno all'altro" (serie: cose sul lavoro
che il tuo capo spera che tu non scopra mai, parte 5).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 5"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "call",
     "say":  "Venerdì pomeriggio, il capo chiama Andrea nel suo ufficio.",
     "text": "VENERDÌ POMERIGGIO, IL CAPO CHIAMA ANDREA NEL SUO UFFICIO"},
    {"id": "b03", "visual": "napoli",
     "say":  "«Da lunedì lavori nella sede di Napoli.»",
     "text": "«DA LUNEDÌ LAVORI NELLA SEDE DI [r]NAPOLI[/r]»"},
    {"id": "b04", "visual": "life",
     "say":  "Andrea vive a Milano, con la famiglia e un mutuo da pagare.",
     "text": "ANDREA VIVE A [g]MILANO[/g], CON LA [g]FAMIGLIA[/g] E UN [g]MUTUO[/g] DA PAGARE"},
    {"id": "b05", "visual": "clause",
     "say":  "«Decisione aziendale. E il contratto prevede la mobilità: fidati.»",
     "text": "«DECISIONE AZIENDALE. IL CONTRATTO PREVEDE LA [r]MOBILITÀ[/r]: FIDATI»"},
    {"id": "b06", "visual": "blank",
     "say":  "Ma una clausola di mobilità non è un assegno in bianco.",
     "text": "MA LA CLAUSOLA DI MOBILITÀ [g]NON È UN ASSEGNO IN BIANCO[/g]"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b07", "visual": "law",
     "say":  "Per il Codice Civile, puoi essere trasferito in un'altra sede solo per comprovate ragioni tecniche, organizzative e produttive.",
     "text": "SOLO PER [g]COMPROVATE RAGIONI[/g] TECNICHE, ORGANIZZATIVE E PRODUTTIVE"},
    {"id": "b08", "visual": "law",
     "say":  "Ragioni vere, e dimostrabili. Non basta un «fidati».",
     "text": "RAGIONI VERE E [g]DIMOSTRABILI[/g]. NON BASTA UN [r]«FIDATI»[/r]"},
    {"id": "b09", "visual": "punish",
     "say":  "E il trasferimento non può essere una punizione mascherata.",
     "text": "E NON PUÒ ESSERE UNA [r]PUNIZIONE MASCHERATA[/r]"},
    {"id": "b10", "visual": "ccnl",
     "say":  "In più, molti contratti collettivi prevedono la forma scritta e un preavviso minimo.",
     "text": "MOLTI CCNL PREVEDONO LA [g]FORMA SCRITTA[/g] E UN [g]PREAVVISO MINIMO[/g]"},
    {"id": "b11", "visual": "care",
     "say":  "E se assisti un familiare con i permessi della legge centoquattro, serve il tuo consenso.",
     "text": "SE ASSISTI UN FAMILIARE CON I PERMESSI [g]104[/g], [g]SERVE IL TUO CONSENSO[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b12", "visual": "ask",
     "say":  "Andrea chiede le ragioni del trasferimento per iscritto.",
     "text": "ANDREA CHIEDE LE RAGIONI DEL TRASFERIMENTO [g]PER ISCRITTO[/g]"},
    {"id": "b13", "visual": "threat",
     "say":  "E se non ci sono, lo impugna. Anche d'urgenza, davanti al giudice del lavoro.",
     "text": "SE NON CI SONO, LO IMPUGNA. [r]ANCHE D'URGENZA[/r], DAVANTI AL GIUDICE"},
    {"id": "b14", "visual": "time",
     "say":  "Occhio ai tempi: il trasferimento va impugnato per iscritto entro sessanta giorni.",
     "text": "OCCHIO AI TEMPI: VA IMPUGNATO PER ISCRITTO [r]ENTRO 60 GIORNI[/r]"},
    {"id": "b15", "visual": "cede",
     "say":  "Il capo ci ripensa. «Aspetta, sento la direzione.»",
     "text": "IL CAPO CI RIPENSA. «ASPETTA, [g]SENTO LA DIREZIONE[/g]»"},
    {"id": "b16", "visual": "deal",
     "say":  "E alla fine si trova una soluzione che non stravolge la vita di Andrea.",
     "text": "E SI TROVA UNA SOLUZIONE CHE [g]NON STRAVOLGE LA SUA VITA[/g]"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b17", "visual": "cta",
     "say":  "Ti vogliono trasferire da un giorno all'altro?",
     "text": "TI VOGLIONO TRASFERIRE [r]DA UN GIORNO ALL'ALTRO[/r]?"},
    {"id": "b18", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
