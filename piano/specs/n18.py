import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_supplementari"; TITLE="Le ore supplementari del part-time"
BEATS=[H,
 {"id":"b02","visual":"contract","say":"Andrea ha un part-time da venti ore a settimana.","text":"ANDREA HA UN [g]PART-TIME DA 20 ORE[/g] A SETTIMANA"},
 {"id":"b03","visual":"more","say":"Ma ogni settimana il capo gli chiede di restare. E le ore diventano trenta.","text":"MA OGNI SETTIMANA RESTA DI PIÙ: [r]LE ORE DIVENTANO 30[/r]"},
 {"id":"b04","visual":"boss","say":"«Le ore in più te le pago normali. O meglio: quando posso.»","text":"«LE ORE IN PIÙ TE LE PAGO NORMALI. [r]QUANDO POSSO[/r]»"},
 W("b05"),
 {"id":"b06","visual":"law","say":"Nel part-time, le ore oltre l'orario si chiamano supplementari. E vanno pagate tutte.","text":"NEL PART-TIME, LE ORE IN PIÙ SONO [g]SUPPLEMENTARI[/g]: VANNO PAGATE TUTTE"},
 {"id":"b07","visual":"law","say":"Se il contratto collettivo non dice nulla, la legge prevede una maggiorazione del quindici per cento.","text":"SE IL CCNL NON DICE NULLA, PER LEGGE [g]+15% DI MAGGIORAZIONE[/g]"},
 {"id":"b08","visual":"limit","say":"E fissa anche un limite: non più del venticinque per cento delle ore settimanali.","text":"E UN LIMITE: [r]MAX 25%[/r] DELLE ORE SETTIMANALI"},
 {"id":"b09","visual":"fake","say":"Se le ore in più diventano la regola, quel part-time può nascondere un tempo pieno. Con le differenze da recuperare.","text":"SE DIVENTANO LA REGOLA, PUÒ NASCONDERE [g]UN TEMPO PIENO[/g]: DIFFERENZE DA RECUPERARE"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, te le pago con la maggiorazione.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]CON LA MAGGIORAZIONE[/g]»"},
]+CTA("b11","b12","Sei part-time ma lavori molte più ore?","SEI PART-TIME MA [r]LAVORI MOLTE PIÙ ORE[/r]?")
ART=r'''
ART.hook=sceneHook(G(clock(0,0,70,2,0),"translate(170,-470)"));
ART.contract=b=>
  contractDoc(330,660,420,560,-3,{big:"20 ORE",bigCol:GREEN,sub:"part-time"})+
  guy({x:200,y:1790,s:0.62,look:0.4,face:'smile',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.more=b=>
  hoursBar(110,820,860,"20 ORE",20/40*12,GREEN,GREEN_SOFT,b[0])+
  hoursBar(110,960,860,"30 ORE",30/40*12,RED,RED_SOFT,b[0]+":30")+
  guy({x:540,y:1800,s:0.55,look:0,face:'flat',brows:'worried',eyes:'tired',l:[-30,200],r:[30,200]});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"QUANDO POSSO",at:b=>b[0]+":POSSO"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"D.LGS. 81/2015",art:"ART. 6",line:"lavoro|supplementare",p1:"SUPPLEMENTARI: PAGATE TUTTE",c1:b=>b[0]+":SUPPLEMENTARI",p2:"+15% SE IL CCNL TACE",c2:b=>b[1]+":15"});
ART.limit=b=>
  hoursBar(110,860,860,"20 ORE + 25% = 25",25/40*12,INDIGO,INDIGO_SOFT,b[0])+
  A(stamp(540,1120,"MAX 25%",-6),{from:b[0]+":25",inn:"stamp"})+
  guy({x:540,y:1800,s:0.55,look:0,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.fake=b=>
  contractDoc(110,660,340,460,-5,{big:"20 ORE",bigCol:RED,sub:"sulla carta"})+
  A(contractDoc(630,660,340,460,4,{big:"30+ ORE",bigCol:GREEN,sub:"nella realtà"}),{from:b[0]+":PIENO",inn:"pop"})+
  A(coin(540,1200,50)+coin(630,1170,40),{from:b[0]+":DIFFERENZE",inn:"drop"})+
  guy({x:540,y:1800,s:0.5,look:0,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.cede=sceneCede("MAGGIORAZIONE");
ART.cta=sceneCTA;
'''
COVER_TITLE=["PART-TIME DA [g]20 ORE[/g],","[r]NE FAI 30[/r]?","LE ORE IN PIÙ SI PAGANO."]
COVER_ART='    coverPair(G(clock(0,0,70,2,0),"translate(170,-470)"))'
