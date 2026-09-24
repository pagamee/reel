# -*- coding: utf-8 -*-
"""
Copione del reel "Mansioni superiori" (serie: cose sul lavoro che il tuo capo
spera che tu non scopra mai, parte 3).

Ogni battuta ("beat") ha:
  id      identificativo
  visual  disegno da mostrare; battute consecutive con lo stesso visual
          restano sulla stessa illustrazione (niente stacco)
  say     testo letto dalla voce (numeri in lettere, così il TTS non sbaglia)
  text    testo a schermo, scritto "a macchina" mentre la voce parla.
          Marcatori colore: [g]verde[/g]  [r]rosso[/r]  [i]indaco Pagamee[/i]
"""

SERIES_PART = "PARTE 3"

BEATS = [
    # --- aggancio -----------------------------------------------------------
    {"id": "b01", "visual": "hook",
     "say":  "Cose sul lavoro che il tuo capo spera che tu non scopra mai.",
     "text": "COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},

    # --- la storia ----------------------------------------------------------
    {"id": "b02", "visual": "duties",
     "say":  "Da sette mesi Andrea fa il lavoro del suo responsabile.",
     "text": "DA [r]7 MESI[/r] ANDREA FA IL LAVORO DEL SUO RESPONSABILE"},
    {"id": "b03", "visual": "duties",
     "say":  "Organizza i turni, gestisce il team, forma i nuovi arrivati.",
     "text": "ORGANIZZA I [g]TURNI[/g], GESTISCE IL [g]TEAM[/g], FORMA I [g]NUOVI[/g] ARRIVATI"},
    {"id": "b04", "visual": "payslip",
     "say":  "Ma in busta paga il livello è sempre lo stesso. E lo stipendio pure.",
     "text": "MA IN BUSTA PAGA IL LIVELLO È [r]SEMPRE LO STESSO[/r]. E LO STIPENDIO PURE"},
    {"id": "b05", "visual": "ask",
     "say":  "Così chiede al capo il livello più alto, e le differenze arretrate.",
     "text": "COSÌ CHIEDE AL CAPO IL [g]LIVELLO PIÙ ALTO[/g] E LE DIFFERENZE ARRETRATE"},
    {"id": "b06", "visual": "grow",
     "say":  "«Ma dai, ti sto facendo crescere! È esperienza, mica una promozione.»",
     "text": "«TI STO FACENDO CRESCERE! È [r]ESPERIENZA[/r], MICA UNA PROMOZIONE»"},
    {"id": "b07", "visual": "temp",
     "say":  "«E poi è una cosa temporanea.»",
     "text": "«E POI È UNA COSA [r]TEMPORANEA[/r]»"},

    # --- cosa dice la legge -------------------------------------------------
    {"id": "b08", "visual": "law",
     "say":  "Temporanea da sette mesi? Vediamo cosa dice la legge.",
     "text": "TEMPORANEA DA 7 MESI? [g]VEDIAMO COSA DICE LA LEGGE[/g]"},
    {"id": "b09", "visual": "law",
     "say":  "Per il Codice Civile, se fai mansioni di livello superiore, ti spetta la paga di quel livello.",
     "text": "SE FAI MANSIONI DI [g]LIVELLO SUPERIORE[/g], TI SPETTA LA PAGA DI QUEL LIVELLO"},
    {"id": "b10", "visual": "stairs",
     "say":  "E ti spetta dal primo giorno, per tutto il periodo.",
     "text": "E TI SPETTA [g]DAL PRIMO GIORNO[/g], PER TUTTO IL PERIODO"},
    {"id": "b11", "visual": "six",
     "say":  "Non solo: dopo il periodo fissato dal tuo contratto collettivo, o in mancanza dopo sei mesi continuativi,",
     "text": "DOPO IL PERIODO DEL TUO CCNL, O IN MANCANZA [g]6 MESI CONTINUATIVI[/g],"},
    {"id": "b12", "visual": "six",
     "say":  "il livello superiore diventa definitivo.",
     "text": "IL LIVELLO SUPERIORE [g]DIVENTA DEFINITIVO[/g]"},

    # --- le eccezioni -------------------------------------------------------
    {"id": "b13", "visual": "except",
     "say":  "Attenzione, però: se stai sostituendo un collega assente, che ha diritto a tornare al suo posto,",
     "text": "ATTENZIONE: SE [r]SOSTITUISCI UN COLLEGA ASSENTE[/r] CHE HA DIRITTO A TORNARE,"},
    {"id": "b14", "visual": "except",
     "say":  "la paga in più ti spetta, ma il livello non diventa definitivo.",
     "text": "LA PAGA IN PIÙ SÌ, [r]IL LIVELLO DEFINITIVO NO[/r]"},
    {"id": "b15", "visual": "prevalent",
     "say":  "E le mansioni superiori devono essere prevalenti: non basta farle ogni tanto.",
     "text": "E DEVONO ESSERE [g]PREVALENTI[/g]: NON BASTA FARLE OGNI TANTO"},

    # --- finale della storia ------------------------------------------------
    {"id": "b16", "visual": "daily",
     "say":  "Andrea non sostituisce nessuno. E fa il responsabile ogni giorno, da sette mesi.",
     "text": "ANDREA NON SOSTITUISCE NESSUNO. E LO FA [g]OGNI GIORNO DA 7 MESI[/g]"},
    {"id": "b17", "visual": "threat",
     "say":  "Quindi: o livello e arretrati, o giudice del lavoro.",
     "text": "QUINDI: O [g]LIVELLO E ARRETRATI[/g], O [r]GIUDICE DEL LAVORO[/r]"},
    {"id": "b18", "visual": "cede",
     "say":  "Il capo ci ripensa. «Va bene, facciamo il contratto nuovo.»",
     "text": "IL CAPO CI RIPENSA. «VA BENE, [g]FACCIAMO IL CONTRATTO NUOVO[/g]»"},
    {"id": "b19", "visual": "proofs",
     "say":  "Il consiglio: conserva mail, ordini di servizio e turni. Sono le tue prove.",
     "text": "CONSERVA [g]MAIL[/g], [g]ORDINI DI SERVIZIO[/g] E [g]TURNI[/g]: SONO LE TUE PROVE"},

    # --- chiusura -----------------------------------------------------------
    {"id": "b20", "visual": "cta",
     "say":  "Fai il lavoro di un livello superiore, con la paga di prima?",
     "text": "FAI IL LAVORO DI UN [r]LIVELLO SUPERIORE[/r] CON LA PAGA DI PRIMA?"},
    {"id": "b21", "visual": "cta",
     "say":  "Scrivici: verifichiamo il tuo caso, e non anticipi un euro.",
     "text": "[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
