# -*- coding: utf-8 -*-
"""Piano editoriale: 60 reel su 13 temi, alternati, uno al giorno alle 20:30 dal 26/11/2026."""
import datetime as dt
T = {
 "Straordinari non pagati": [
  ("Fai 50 ore, te ne pagano 40", "Le ore oltre l'orario vanno pagate come straordinario, con la maggiorazione del CCNL", "ORE"),
  ("«Il superminimo copre tutto»", "Un forfait è valido solo se copre davvero le ore che fai; la differenza va pagata", "FORFAIT"),
  ("«Sei impiegato, gli straordinari non ti spettano»", "Spettano a quasi tutti: le eccezioni (dirigenti, alcune figure direttive) sono poche", "IMPIEGATO"),
  ("Come provi gli straordinari", "Badge, chat, mail, accessi ai sistemi, colleghi testimoni", "PROVE"),
  ("«Nessuno ti ha chiesto di restare»", "Se il datore sa e accetta il lavoro in più, di regola va pagato", "RESTARE"),
  ("Lavori la domenica e a Natale, pagato uguale", "Festivi e giorno di riposo hanno maggiorazioni o riposi compensativi dal CCNL", "FESTIVI"),
 ],
 "Tredicesima e quattordicesima": [
  ("La tredicesima non è un regalo di Natale", "È retribuzione prevista dai CCNL: spetta, e a dicembre", "TREDICESIMA"),
  ("La quattordicesima: chi ce l'ha davvero", "Solo alcuni CCNL la prevedono (es. commercio, turismo): controlla il tuo", "QUATTORDICESIMA"),
  ("Te ne vai a giugno? La tredicesima matura lo stesso", "Ratei mese per mese: a fine rapporto ti spetta la parte maturata", "RATEI"),
  ("«La tredicesima te la do a febbraio»", "Il ritardo non è una scelta del capo: si recupera con gli interessi", "RITARDO"),
 ],
 "Ferie non godute": [
  ("Lasci il lavoro con 20 giorni di ferie", "A fine rapporto le ferie non godute vanno pagate", "FERIE"),
  ("«Non le hai fatte, le perdi»", "Non le perdi in automatico: il datore deve metterti davvero in condizione di farle", "PERSE"),
  ("«Te le pago e non le fai»", "Le 4 settimane minime non si monetizzano finché il rapporto è in corso", "MONETIZZARE"),
  ("ROL ed ex festività: soldi dimenticati", "Permessi non goduti: di solito pagati in busta o a fine rapporto, secondo CCNL", "ROL"),
  ("Ti ammali in ferie?", "La malattia certificata può sospendere le ferie", "MALATO"),
 ],
 "Buste paga in ritardo": [
  ("Lo stipendio arriva sempre il 20", "I termini li fissa il CCNL: il ritardo dà diritto a interessi e rivalutazione", "STIPENDIO"),
  ("Busta paga consegnata, soldi mai arrivati", "La busta paga è già una prova del credito", "BUSTA"),
  ("Decreto ingiuntivo: lo stipendio in poche settimane", "Con le buste paga si chiede al giudice un'ingiunzione di pagamento", "DECRETO"),
  ("«Ti pago in contanti»", "Dal 2018 lo stipendio va pagato con strumenti tracciabili", "CONTANTI"),
  ("Due mesi senza stipendio?", "Può essere giusta causa di dimissioni, con NASpI", "MESI"),
 ],
 "Livello sbagliato nel CCNL": [
  ("Assunto al 5° livello, ma fai un lavoro da 3°", "Conta quello che fai davvero: si recuperano le differenze", "LIVELLO"),
  ("Apprendista da anni, ma nessuno ti forma", "Senza formazione l'apprendistato può essere contestato", "APPRENDISTA"),
  ("Il CCNL «sbagliato» con minimi più bassi", "Certi contratti pagano meno del dovuto: si può chiedere la differenza", "CCNL"),
  ("Tirocinio o lavoro vero?", "Se lavori come un dipendente, il tirocinio può nascondere un rapporto di lavoro", "STAGE"),
  ("Come capire se il tuo livello è giusto", "Confronta mansioni e declaratorie del tuo CCNL", "INQUADRAMENTO"),
 ],
 "Part-time finti": [
  ("«Da lunedì passi a part-time»", "Il passaggio a part-time richiede il tuo accordo scritto; il rifiuto non giustifica il licenziamento", "PARTTIME"),
  ("Le ore supplementari hanno una maggiorazione", "Oltre l'orario part-time: limiti e maggiorazioni dal CCNL", "SUPPLEMENTARI"),
  ("«Domani vieni 4 ore in più»", "Collocazione dell'orario scritta nel contratto; cambi solo con clausole elastiche", "ORARIO"),
  ("Ti segnano meno ore di quelle che fai", "Fogli presenze, chat e testimoni contano", "PRESENZE"),
 ],
 "Dimissioni per giusta causa": [
  ("Dimissioni per giusta causa: cosa sono", "Quando il datore è gravemente inadempiente puoi andartene subito", "GIUSTACAUSA"),
  ("Te ne vai senza preavviso, e te lo pagano", "Con giusta causa spetta a te l'indennità di mancato preavviso", "PREAVVISO"),
  ("Dimissioni online: il dettaglio che cambia tutto", "Nella procedura telematica va indicata la giusta causa", "ONLINE"),
  ("L'errore che ti fa perdere la NASpI", "Dimissioni «normali» invece che per giusta causa", "ERRORE"),
  ("Stipendi non pagati: resisti o te ne vai?", "Il mancato pagamento è tipica giusta causa", "RESISTI"),
 ],
 "NASpI": [
  ("Licenziato per colpa tua? La NASpI spetta lo stesso", "Spetta anche dopo licenziamento disciplinare", "NASPI"),
  ("Ti dimetti: niente NASpI. Tranne quando…", "Giusta causa e alcuni casi di risoluzione consensuale", "DIMISSIONI"),
  ("68 giorni: la scadenza da non perdere", "La domanda va fatta entro 68 giorni dalla fine del rapporto", "68"),
  ("La NASpI tutta insieme per aprire un'attività", "Anticipazione in un'unica soluzione, a certe condizioni", "ANTICIPO"),
  ("Contratto a termine scaduto: NASpI?", "Sì, se hai i requisiti contributivi", "SCADENZA"),
 ],
 "Malattia trattenuta": [
  ("In malattia e ti tolgono soldi dalla busta", "Indennità INPS più integrazione del datore, secondo CCNL", "MALATTIA"),
  ("I primi 3 giorni di malattia chi li paga?", "Il periodo di carenza: spesso a carico del datore, dipende dal CCNL", "CARENZA"),
  ("Licenziato mentre sei in malattia", "Prima del comporto il licenziamento per malattia non è possibile", "COMPORTO"),
  ("Visita fiscale: le fasce orarie", "Dipendenti privati: 10-12 e 17-19", "VISITA"),
 ],
 "Reperibilità non pagata": [
  ("«Tieni il telefono acceso nel weekend»", "La reperibilità va pagata con l'indennità prevista dal CCNL", "REPERIBILITA"),
  ("Ti chiamano di notte e intervieni", "L'intervento è lavoro: si paga come tale", "INTERVENTO"),
  ("Reperibile «di fatto», senza contratto", "Se devi essere sempre disponibile, quella è reperibilità", "TELEFONO"),
  ("Reperibilità e riposo", "Dopo l'intervento valgono le regole sul riposo", "RIPOSO"),
 ],
 "Trasferte": [
  ("In trasferta e paghi tu le spese?", "Rimborsi e indennità di trasferta secondo CCNL", "TRASFERTA"),
  ("Il viaggio è orario di lavoro?", "Dipende dai casi: per alcuni lavoratori sì", "VIAGGIO"),
  ("Usi la tua auto per lavoro", "Rimborso chilometrico se lo prevede accordo o CCNL", "AUTO"),
  ("Trasfertista o in trasferta?", "Due regimi diversi, con indennità diverse", "TRASFERTISTA"),
 ],
 "TFR e fallimento": [
  ("L'azienda fallisce: il TFR è perso?", "Lo paga il Fondo di garanzia INPS", "FALLIMENTO"),
  ("Ultimi 3 stipendi non pagati prima del fallimento", "Il Fondo di garanzia copre anche le ultime 3 mensilità, entro dei limiti", "FONDO"),
  ("Insinuazione al passivo: cos'è", "Il passaggio per far valere i tuoi crediti nel fallimento", "PASSIVO"),
  ("TFR nel fondo pensione mai versato", "Si può recuperare: esistono tutele anche qui", "PENSIONE"),
  ("Azienda chiusa e sparita, ma non fallita", "Il Fondo di garanzia può intervenire anche in questi casi, a certe condizioni", "CHIUSA"),
 ],
 "Prescrizione dei crediti": [
  ("Quanto tempo hai per chiedere i soldi?", "In genere 5 anni per stipendi e differenze", "TEMPO"),
  ("Mentre lavori, il tempo non corre", "Secondo la Cassazione, per stipendi e differenze la prescrizione parte dalla fine del rapporto", "PRESCRIZIONE"),
  ("Licenziato: hai 60 giorni", "L'impugnazione del licenziamento ha termini stretti", "60GIORNI"),
  ("Una lettera che ferma il tempo", "La messa in mora interrompe la prescrizione", "LETTERA"),
 ],
}
# alternanza: un tema dopo l'altro, a giro
order, idx = [], {k: 0 for k in T}
while len(order) < sum(len(v) for v in T.values()):
    for k in T:
        if idx[k] < len(T[k]):
            order.append((k, *T[k][idx[k]])); idx[k] += 1
start = dt.date(2026, 11, 26)
G = ["lun","mar","mer","gio","ven","sab","dom"]
rows = ["| # | Data (20:30) | Tema | Titolo / gancio | Punto legale (da verificare) | Commenta |", "|---|---|---|---|---|---|"]
for i, (tema, tit, punto, kw) in enumerate(order):
    d = start + dt.timedelta(days=i)
    rows.append(f"| {i+1} | {G[d.weekday()]} {d.strftime('%d/%m/%Y')} | {tema} | {tit} | {punto} | {kw} |")
open("piano_editoriale.md", "w").write(
 "# Piano editoriale: 60 reel, uno al giorno alle 20:30\n\n"
 "Solo temi sul recupero di soldi dal lavoro. Temi alternati per non ripetersi. "
 "Ogni punto legale è semplificato e va fatto controllare a un legale prima della produzione.\n\n"
 + "\n".join(rows) + "\n")
print(len(order), "contenuti")
