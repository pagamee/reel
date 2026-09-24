# -*- coding: utf-8 -*-
"""
Copione del reel "Firma la liberatoria o non ti pago" (serie: cose sul lavoro che
il tuo capo spera che tu non scopra mai, parte 6).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 6"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "owed",
     "say":  "Andrea viene licenziato. Gli spettano l'ultimo stipendio, il TFR e le ferie non godute.",
     "text": "ANDREA VIENE LICENZIATO. GLI SPETTANO [g]STIPENDIO[/g], [g]TFR[/g] E [g]FERIE NON GODUTE[/g]"},
    {"id": "b03", "visual": "sheet",
     "say":  "Ma il capo gli mette davanti un foglio.",
     "text": "MA IL CAPO GLI METTE DAVANTI [r]UN FOGLIO[/r]"},
    {"id": "b04", "visual": "sheet",
     "say":  "«Firma qui: dichiari che non hai più nulla da pretendere.»",
     "text": "«FIRMA QUI: DICHIARI CHE [r]NON HAI PIÙ NULLA DA PRETENDERE[/r]»"},
    {"id": "b05", "visual": "blackmail",
     "say":  "«Se non firmi, non ti pago. I soldi sono miei: decido io.»",
     "text": "«SE NON FIRMI, [r]NON TI PAGO[/r]. I SOLDI SONO MIEI: DECIDO IO»"},
    {"id": "b06", "visual": "wrong",
     "say":  "Peccato che non funzioni così.",
     "text": "PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b07", "visual": "gift",
     "say":  "Stipendio, TFR e ferie non godute non sono un regalo: sono diritti tuoi.",
     "text": "STIPENDIO, TFR E FERIE [r]NON SONO UN REGALO[/r]: [g]SONO DIRITTI TUOI[/g]"},
    {"id": "b08", "visual": "gift",
     "say":  "E il pagamento di quello che ti spetta non si può legare a una rinuncia.",
     "text": "E IL PAGAMENTO [r]NON SI PUÒ LEGARE A UNA RINUNCIA[/r]"},
    {"id": "b09", "visual": "law",
     "say":  "Per il Codice Civile, le rinunce ai diritti del lavoratore si possono impugnare entro sei mesi.",
     "text": "LE RINUNCE AI TUOI DIRITTI SI POSSONO [g]IMPUGNARE ENTRO 6 MESI[/g]"},
    {"id": "b10", "visual": "law",
     "say":  "Fanno eccezione quelle firmate in sede protetta, come all'Ispettorato del lavoro o al sindacato.",
     "text": "ECCEZIONE: QUELLE FIRMATE IN [g]SEDE PROTETTA[/g], COME ISPETTORATO O SINDACATO"},
    {"id": "b11", "visual": "generic",
     "say":  "E una frase generica come «non ho più nulla da pretendere», di solito, non basta a farti perdere i tuoi diritti.",
     "text": "E UNA FRASE GENERICA, DI SOLITO, [g]NON BASTA A FARTI PERDERE I TUOI DIRITTI[/g]"},

    # --- finale della storia ------------------------------------------------
    {"id": "b12", "visual": "receipt",
     "say":  "Così Andrea firma, sì. Ma solo la ricevuta dei soldi che riceve.",
     "text": "ANDREA FIRMA, SÌ: MA [g]SOLO LA RICEVUTA[/g] DEI SOLDI CHE RICEVE"},
    {"id": "b13", "visual": "mora",
     "say":  "E se il capo non paga? Messa in mora, e poi decreto ingiuntivo. Con gli interessi.",
     "text": "E SE NON PAGA? [r]MESSA IN MORA[/r] E [r]DECRETO INGIUNTIVO[/r]. CON GLI INTERESSI"},
    {"id": "b14", "visual": "paid",
     "say":  "Il capo ci ripensa. E paga tutto, senza liberatoria.",
     "text": "IL CAPO CI RIPENSA. E [g]PAGA TUTTO[/g], SENZA LIBERATORIA"},
    {"id": "b15", "visual": "advice",
     "say":  "Il consiglio: non firmare rinunce sotto pressione, e tieni sempre una copia di quello che firmi.",
     "text": "[r]NON FIRMARE RINUNCE SOTTO PRESSIONE[/r] E [g]TIENI UNA COPIA[/g] DI TUTTO"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b16", "visual": "cta",
     "say":  "Ti chiedono una liberatoria per pagarti?",
     "text": "TI CHIEDONO [r]UNA LIBERATORIA[/r] PER PAGARTI?"},
    {"id": "b17", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
