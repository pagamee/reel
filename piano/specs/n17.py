import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_apprendista"; TITLE="Apprendista da anni, ma nessuno ti forma"
BEATS=[H,
 {"id":"b02","visual":"contract","say":"Andrea è assunto come apprendista. Paga più bassa, perché deve imparare il mestiere.","text":"ASSUNTO COME [r]APPRENDISTA[/r]: PAGA PIÙ BASSA, PERCHÉ DEVE IMPARARE"},
 {"id":"b03","visual":"alone","say":"Ma nessuno gli insegna niente. Dal primo giorno lavora come gli altri.","text":"MA [r]NESSUNO GLI INSEGNA NIENTE[/r]: LAVORA COME GLI ALTRI"},
 {"id":"b04","visual":"boss","say":"«L'apprendistato è così: impari facendo.»","text":"«L'APPRENDISTATO È COSÌ: [r]IMPARI FACENDO[/r]»"},
 W("b05"),
 {"id":"b06","visual":"law","say":"L'apprendistato è un contratto di formazione: deve esserci un piano formativo, e un tutor.","text":"È UN CONTRATTO DI FORMAZIONE: SERVONO [g]PIANO FORMATIVO[/g] E [g]TUTOR[/g]"},
 {"id":"b07","visual":"law","say":"È proprio per la formazione che la paga può essere più bassa.","text":"È [g]PER LA FORMAZIONE[/g] CHE LA PAGA PUÒ ESSERE PIÙ BASSA"},
 {"id":"b08","visual":"convert","say":"Se la formazione manca del tutto, il contratto può essere trattato come un normale tempo indeterminato.","text":"SE LA FORMAZIONE MANCA DEL TUTTO, PUÒ DIVENTARE [g]UN NORMALE TEMPO INDETERMINATO[/g]"},
 {"id":"b09","visual":"diff","say":"E le differenze di paga si possono recuperare.","text":"E [g]LE DIFFERENZE DI PAGA[/g] SI POSSONO RECUPERARE"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, sistemiamo il contratto.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]SISTEMIAMO IL CONTRATTO[/g]»"},
]+CTA("b11","b12","Sei apprendista, ma nessuno ti forma?","SEI APPRENDISTA, MA [r]NESSUNO TI FORMA[/r]?")
ART=r'''
ART.hook=sceneHook(G(gradCap(0,0,0.9),"translate(160,-460)"));
ART.contract=b=>
  contractDoc(330,660,420,560,-3,{big:"APPRENDISTA",bigCol:RED,sub:"paga ridotta"})+
  guy({x:200,y:1790,s:0.62,look:0.4,face:'smile',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.alone=b=>
  desk(360,1420,560)+monitor(640,1420,280,true)+
  guy({x:470,y:1780,s:0.84,look:0.5,face:'flat',brows:'worried',l:[-30,230],r:[170,20],bendR:30,rh:'dot'})+
  A(G(gradCap(0,0,0.9)+xmark(0,0,80,RED),"translate(230,820)"),{from:b[0]+":NIENTE",inn:"stamp"});
ART.boss=sceneBoss({face:'grin',brows:'up',lh:'open',stamp:"IMPARI FACENDO",at:b=>b[0]+":FACENDO"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"D.LGS. 81/2015",art:"APPRENDISTATO",line:"piano|formativo",p1:"PIANO FORMATIVO + TUTOR",c1:b=>b[0]+":PIANO",p2:"PAGA RIDOTTA PER LA FORMAZIONE",c2:b=>b[1]+":FORMAZIONE"});
ART.convert=b=>
  contractDoc(110,660,340,460,-5,{big:"APPRENDISTA",bigCol:RED,sub:""})+
  A(pth("M 480 900 L 600 900 M 570 870 L 600 900 L 570 930","none",10,GREEN),{from:b[0]+":DIVENTARE",inn:"fade"})+
  A(contractDoc(630,660,340,460,4,{big:"INDETERM.",bigCol:GREEN,sub:"pieno"}),{from:b[0]+":INDETERMINATO",inn:"pop"})+
  guy({x:540,y:1800,s:0.5,look:0,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.diff=b=>
  stairs(360,1650,220,["APPR.","LIV.","LIV.+"])+
  A(coin(560,1000,50)+coin(660,940,40)+coin(480,900,36),{from:b[0]+":DIFFERENZE",inn:"drop"})+
  guy({x:910,y:1650-3*220*0.62,s:0.6,look:-0.2,face:'grin',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'thumb'});
ART.cede=sceneCede("SISTEMIAMO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["APPRENDISTA","MA [r]NESSUNO TI FORMA[/r]?","[g]TI SPETTA DI PIÙ[/g]."]
COVER_ART='    coverPair(G(gradCap(0,0,0.9),"translate(160,-460)"))'
