SLUG="reel_livello"; TITLE="Assunto al 5° livello, ma fai un lavoro da 3°"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"hired","say":"Andrea è stato assunto al quinto livello, come semplice addetto.","text":"ANDREA È STATO ASSUNTO AL [r]5° LIVELLO[/r], COME SEMPLICE ADDETTO"},
 {"id":"b03","visual":"tasks","say":"Ma dal primo giorno gestisce ordini, fornitori e magazzino. Un lavoro da terzo livello.","text":"MA GESTISCE [g]ORDINI[/g], [g]FORNITORI[/g] E [g]MAGAZZINO[/g]: UN LAVORO DA 3°"},
 {"id":"b04","visual":"boss","say":"«Il livello l'ho deciso io quando ti ho assunto. È quello.»","text":"«IL LIVELLO [r]L'HO DECISO IO[/r] QUANDO TI HO ASSUNTO»"},
 {"id":"b05","visual":"wrong","say":"Peccato che non conti l'etichetta sul contratto.","text":"PECCATO CHE [g]NON CONTI L'ETICHETTA[/g] SUL CONTRATTO"},
 {"id":"b06","visual":"law","say":"Conta quello che fai davvero, ogni giorno.","text":"CONTA [g]QUELLO CHE FAI DAVVERO[/g], OGNI GIORNO"},
 {"id":"b07","visual":"law","say":"Il tuo contratto collettivo descrive le mansioni di ogni livello: si chiamano declaratorie.","text":"IL TUO CCNL DESCRIVE OGNI LIVELLO: SI CHIAMANO [g]DECLARATORIE[/g]"},
 {"id":"b08","visual":"stairs","say":"Se le tue mansioni sono di un livello più alto, ti spetta la paga di quel livello.","text":"MANSIONI DA LIVELLO PIÙ ALTO? [g]TI SPETTA LA PAGA DI QUEL LIVELLO[/g]"},
 {"id":"b09","visual":"back","say":"E puoi recuperare le differenze arretrate, in genere fino a cinque anni.","text":"E RECUPERI LE [g]DIFFERENZE ARRETRATE[/g], IN GENERE FINO A 5 ANNI"},
 {"id":"b10","visual":"compare","say":"Il consiglio: confronta le tue mansioni con le declaratorie del tuo contratto. È scritto tutto lì.","text":"CONFRONTA LE TUE MANSIONI CON LE [g]DECLARATORIE DEL CCNL[/g]"},
 {"id":"b11","visual":"cede","say":"Il capo ci ripensa. «Va bene, ti inquadro al terzo.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TI INQUADRO AL 3°[/g]»"},
 {"id":"b12","visual":"cta","say":"Fai un lavoro più qualificato del tuo livello?","text":"FAI UN LAVORO [r]PIÙ QUALIFICATO DEL TUO LIVELLO[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(clipboard(96,-560,200,10));
ART.hired=b=>
  contractDoc(330,660,420,560,-3,{big:"5° LIV.",bigCol:RED,sub:"addetto"})+
  guy({x:200,y:1790,s:0.62,look:0.4,face:'smile',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.tasks=b=>
  guy({x:280,y:1770,s:0.9,look:0.5,face:'smile',brows:'up',l:[-30,230],r:[150,120],bendR:30,rh:'dot',behind:clipboard(150,-560,150,8)})+
  A(slip(420,660,250,"ORDINI","✓",-4),{from:b[0]+":ORDINI",inn:"pop"})+
  A(G(team(0,0,1.0)+txt(0,-100,"FORNITORI",44,GREEN),"translate(820,820)"),{from:b[0]+":FORNITORI",inn:"pop"})+
  A(G(cardboardBox(0,0,240)+txt(120,200,"MAGAZZINO",40,GREEN),"translate(640,1150)"),{from:b[0]+":MAGAZZINO",inn:"pop"});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',stamp:"DECIDO IO",at:b=>b[0]+":DECISO"});
ART.wrong=sceneWrong;
ART.law=b=>
  book(170,640,740,420,{title:"CCNL",art:"LIVELLI",line:"declaratorie"})+
  A(pill(540,1150,820,"CONTA IL LAVORO REALE",GREEN),{from:b[0]+":DAVVERO",inn:"stamp"})+
  A(pill(540,1290,820,"DECLARATORIE",GREEN),{from:b[1]+":DECLARATORIE",inn:"stamp"})+
  guy({x:900,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.stairs=b=>
  stairs(360,1650,220,["5°","4°","3°"])+
  A(guy({x:910,y:1650-3*220*0.62,s:0.6,look:-0.2,face:'grin',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'thumb'}),{from:b[0]+":PAGA",inn:"rise"})+
  A(coin(560,1000,50)+coin(660,940,40)+coin(480,900,36),{from:b[0]+":PAGA",inn:"drop"});
ART.back=b=>{
  const marks=Array.from({length:12},(_,i)=>`${b[0]}+${(0.3+i*0.15).toFixed(2)}`);
  return monthsGrid(110,660,860,12,4,marks,{title:"DIFFERENZE",col:GREEN})+
    A(G(paper(0,0,280,220,txt(117,80,"IN GENERE",34,"#52525b")+fitTxt(117,170,"5 ANNI",200,64,GREEN)),"translate(640,1260) rotate(5 140 110)"),{from:b[0]+":5",inn:"stamp"})+
    guy({x:300,y:1800,s:0.45,look:0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
};
ART.compare=b=>
  guy({x:540,y:1780,s:0.8,look:0.3,face:'smirk',brows:'sly',eyes:'dot',l:[-30,230],r:[170,-120],bendR:30,rh:'dot',behind:magnifier(322,-792,80,82)})+
  clipboard(80,660,240,-6)+
  A(book(560,700,400,240,{title:"CCNL",art:"3° LIV.",line:"ordini|fornitori"}),{from:b[0]+":DECLARATORIE",inn:"pop"});
ART.cede=sceneCede("INQUADRO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["ASSUNTO AL [r]5°[/r],","FAI UN LAVORO DA [g]3°[/g]?","[g]TI SPETTA DI PIÙ[/g]."]
COVER_ART='    coverPair(clipboard(-110,-600,220,0))+stairs(640,1500,90,["5°","4°","3°"])'
