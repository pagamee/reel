import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_prescrizione"; TITLE="Quanto tempo hai per chiedere i soldi?"
BEATS=[H,
 {"id":"b02","visual":"old","say":"Andrea ha lasciato il lavoro tre anni fa. Gli devono ancora straordinari e TFR.","text":"ANDREA HA LASCIATO IL LAVORO [g]3 ANNI FA[/g]. GLI DEVONO STRAORDINARI E TFR"},
 {"id":"b03","visual":"boss","say":"Il vecchio capo gli scrive: «Ormai è passato troppo tempo. È tutto prescritto.»","text":"«ORMAI È PASSATO TROPPO TEMPO. [r]È TUTTO PRESCRITTO[/r]»"},
 W("b04"),
 {"id":"b05","visual":"law","say":"Per stipendi, straordinari, differenze e TFR, il termine è in genere di cinque anni.","text":"STIPENDI, STRAORDINARI, DIFFERENZE E TFR: IN GENERE [g]5 ANNI[/g]"},
 {"id":"b06","visual":"law","say":"E secondo la Cassazione, di regola i cinque anni partono dalla fine del rapporto.","text":"SECONDO LA CASSAZIONE, DI REGOLA PARTONO [g]DALLA FINE DEL RAPPORTO[/g]"},
 {"id":"b07","visual":"timeline","say":"Quindi Andrea, a tre anni dalla fine, è ancora in tempo.","text":"QUINDI, A 3 ANNI DALLA FINE, [g]È ANCORA IN TEMPO[/g]"},
 {"id":"b08","visual":"letter","say":"E c'è un modo per fermare il tempo: una lettera di messa in mora.","text":"E PER FERMARE IL TEMPO BASTA [g]UNA LETTERA DI MESSA IN MORA[/g]"},
 {"id":"b09","visual":"letter","say":"Interrompe la prescrizione, e il conto riparte da zero.","text":"INTERROMPE LA PRESCRIZIONE: [g]IL CONTO RIPARTE DA ZERO[/g]"},
 {"id":"b10","visual":"warn","say":"Attenzione però: per impugnare un licenziamento i tempi sono molto più brevi, sessanta giorni.","text":"ATTENZIONE: PER IMPUGNARE UN LICENZIAMENTO [r]SOLO 60 GIORNI[/r]"},
 {"id":"b11","visual":"cede","say":"Il vecchio capo ci ripensa. «Va bene, parliamone.»","text":"IL VECCHIO CAPO CI RIPENSA. «VA BENE, [g]PARLIAMONE[/g]»"},
]+CTA("b12","b13","Pensi che sia troppo tardi per i tuoi soldi?","PENSI CHE SIA [r]TROPPO TARDI[/r] PER I TUOI SOLDI?")
ART=r'''
ART.hook=sceneHook(G(hourglass(0,0,160),"translate(170,-450)"));
ART.old=b=>
  G(paper(0,0,300,300,`<rect x="0" y="0" width="254" height="70" fill="${INDIGO_SOFT}"/>`+txt(127,52,"FINE RAPPORTO",30,INDIGO)+txt(127,200,"2023",90,INK)),"translate(110,680) rotate(-5 150 150)")+
  A(pill(720,800,460,"STRAORDINARI",RED),{from:b[0]+":STRAORDINARI",inn:"stamp"})+
  A(pill(720,940,460,"TFR",RED),{from:b[0]+":TFR",inn:"stamp"})+
  guy({x:560,y:1790,s:0.7,look:0,face:'flat',brows:'worried',l:[-30,230],r:[30,230]});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"PRESCRITTO",at:b=>b[0]+":PRESCRITTO",extra:b=>G(hourglass(0,0,220),"translate(220,1200)")});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CODICE CIVILE",art:"ART. 2948",line:"5 anni",p1:"IN GENERE 5 ANNI",c1:b=>b[0]+":5",p2:"DALLA FINE DEL RAPPORTO",c2:b=>b[1]+":FINE"});
ART.timeline=b=>{
  let g=ln(140,1000,940,1000,10,INK);
  for(let i=0;i<=5;i++){const x=140+i*160; g+=ln(x,980,x,1020,8)+txt(x,1080,i+"",48,INK);}
  g+=A(rct(140,960,480,80,14,GREEN_SOFT,5,GREEN),{from:b[0]+"+0.2",inn:"slide"})+A(txt(380,940,"3 ANNI",56,GREEN),{from:b[0]+":3",inn:"pop"});
  g+=txt(140,900,"FINE",40,"#52525b")+A(stamp(700,780,"IN TEMPO",-6,GREEN),{from:b[0]+":TEMPO",inn:"stamp"});
  return g+guy({x:540,y:1800,s:0.5,look:0,face:'grin',brows:'up',l:[-30,200],r:[30,200]});
};
ART.letter=b=>
  A(letter(110,680,320,"MESSA IN MORA",-6),{from:b[0]+":LETTERA",inn:"stamp"})+
  hourglass(780,1000,300)+
  A(stamp(780,1300,"STOP",-8,GREEN),{from:b[1]+":INTERROMPE",inn:"stamp"})+
  A(txt(780,780,"↺ DA ZERO",60,GREEN),{from:b[1]+":ZERO",inn:"pop"})+
  guy({x:300,y:1800,s:0.5,look:0.3,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.warn=b=>
  A(G(paper(0,0,320,320,txt(137,110,"LICENZIAMENTO",34,"#52525b")+txt(137,210,"60",110,RED)+txt(137,280,"GIORNI",44,RED)),"translate(600,700) rotate(5 160 160)"),{from:b[0]+":60",inn:"stamp"})+
  alarmClock(300,980,140)+A(ringLines(300,980,140),{from:b[0]+":ATTENZIONE",loop:"shake:4:0.3"})+
  guy({x:780,y:1800,s:0.5,look:-0.3,face:'o',brows:'up',l:[-160,-100],bendL:30,lh:'point',r:[30,200]});
ART.cede=sceneCede("PARLIAMONE");
ART.cta=sceneCTA;
'''
COVER_TITLE=["TI DEVONO SOLDI","DA [r]ANNI[/r]?","[g]FORSE SEI ANCORA IN TEMPO[/g]."]
COVER_ART='    coverPair(G(hourglass(0,0,160),"translate(170,-450)"))'
