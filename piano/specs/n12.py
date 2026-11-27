import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_tfr_fallimento"; TITLE="L'azienda fallisce: il TFR è perso?"
BEATS=[H,
 {"id":"b02","visual":"closed","say":"L'azienda di Andrea fallisce. Lui resta senza lavoro, senza TFR e con tre stipendi arretrati.","text":"L'AZIENDA FALLISCE: [r]NIENTE TFR[/r] E [r]3 STIPENDI ARRETRATI[/r]"},
 {"id":"b03","visual":"boss","say":"«Mi dispiace. Non ci sono più soldi per nessuno.»","text":"«MI DISPIACE. [r]NON CI SONO PIÙ SOLDI[/r] PER NESSUNO»"},
 {"id":"b04","visual":"wrong","say":"Peccato che esista il Fondo di garanzia dell'INPS.","text":"PECCATO CHE ESISTA IL [g]FONDO DI GARANZIA INPS[/g]"},
 {"id":"b05","visual":"fund","say":"Se il datore è insolvente, il TFR lo paga il Fondo di garanzia.","text":"SE IL DATORE È INSOLVENTE, [g]IL TFR LO PAGA IL FONDO[/g]"},
 {"id":"b06","visual":"fund","say":"E copre anche le ultime tre mensilità, entro certi limiti.","text":"E COPRE ANCHE [g]LE ULTIME 3 MENSILITÀ[/g], ENTRO CERTI LIMITI"},
 {"id":"b07","visual":"steps","say":"Prima, però, i crediti vanno fatti valere nella procedura: oggi si chiama liquidazione giudiziale.","text":"PRIMA, I CREDITI VANNO NELLA [g]LIQUIDAZIONE GIUDIZIALE[/g]"},
 {"id":"b08","visual":"steps","say":"Poi si fa domanda all'INPS. Ci sono passaggi e tempi precisi da rispettare.","text":"POI [g]DOMANDA ALL'INPS[/g]: CON PASSAGGI E TEMPI PRECISI"},
 {"id":"b09","visual":"paid","say":"Così Andrea mette in fila i documenti, e recupera TFR e stipendi.","text":"ANDREA METTE IN FILA I DOCUMENTI E [g]RECUPERA TFR E STIPENDI[/g]"},
]+CTA("b10","b11","La tua azienda è fallita e ti deve dei soldi?","LA TUA AZIENDA È FALLITA E [r]TI DEVE DEI SOLDI[/r]?")
ART=r'''
ART.hook=sceneHook(G(bigUmbrella(0,0,100,["FONDO"]),"translate(150,-560)"));
ART.closed=b=>
  G(bankBuilding(0,0,320,"")+txt(0,140,"AZIENDA",48,INK),"translate(300,1000)")+
  A(stamp(300,860,"FALLITA",-10),{from:b[0]+":FALLISCE",inn:"stamp"})+
  A(pill(780,800,400,"TFR: 0 €",RED),{from:b[0]+":TFR",inn:"stamp"})+
  A(pill(780,940,400,"3 STIPENDI",RED),{from:b[0]+":STIPENDI",inn:"stamp"})+
  guy({x:780,y:1800,s:0.55,look:-0.3,face:'sad',brows:'worried',l:[-30,200],r:[30,200]});
ART.boss=sceneBoss({face:'sad',brows:'worried',lh:'open',stamp:"NIENTE SOLDI",at:b=>b[0]+":SOLDI"});
ART.wrong=sceneWrong;
ART.fund=b=>
  bigUmbrella(540,980,300,["FONDO DI","GARANZIA","INPS"])+drops([200,320,760,880],700)+
  guy({x:900,y:1800,s:0.45,look:-0.3,face:'grin',brows:'up',l:[-30,200],r:[30,200]})+
  A(pill(470,1330,560,"TFR",GREEN),{from:b[0]+":TFR",inn:"stamp"})+
  A(pill(470,1460,560,"ULTIME 3 MENSILITÀ",GREEN),{from:b[1]+":MENSILITÀ",inn:"stamp"});
ART.steps=b=>
  A(G(paper(0,0,300,400,txt(127,80,"TRIBUNALE",34,"#52525b")+fitTxt(127,170,"STATO",230,60,INK)+fitTxt(127,240,"PASSIVO",230,60,INK)+lines(30,290,200,2,40)),"translate(110,680) rotate(-5 150 200)"),{from:b[0]+":LIQUIDAZIONE",inn:"pop"})+
  A(pth("M 440 900 L 600 900 M 570 870 L 600 900 L 570 930","none",10,GREEN),{from:b[1],inn:"fade"})+
  A(G(bankBuilding(0,0,260,"")+txt(0,120,"INPS",50,INDIGO),"translate(800,980)"),{from:b[1]+":INPS",inn:"pop"})+
  guy({x:540,y:1800,s:0.5,look:0,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.paid=b=>
  guy({x:400,y:1780,s:0.92,look:0.5,face:'grin',brows:'up',l:[-30,230],r:[150,-40],bendR:30,rh:'dot',behind:folder(90,-720,260,"DOCUMENTI",-4)})+
  A(coin(720,1000,60,"TFR")+coin(850,950,50)+coin(800,1100,46),{from:b[0]+":RECUPERA",inn:"drop"});
ART.cta=sceneCTA;
'''
COVER_TITLE=["AZIENDA FALLITA?","IL [g]TFR[/g] E GLI STIPENDI","[r]NON SONO PERSI[/r]."]
COVER_ART='    coverPair(G(bigUmbrella(0,0,100,["FONDO"]),"translate(150,-560)"))'
