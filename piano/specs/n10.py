import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_reperibilita"; TITLE="«Tieni il telefono acceso nel weekend»"
BEATS=[H,
 {"id":"b02","visual":"boss","say":"Venerdì sera il capo dice ad Andrea: «Nel weekend tieni il telefono acceso. Se succede qualcosa, intervieni.»","text":"«NEL WEEKEND [r]TIENI IL TELEFONO ACCESO[/r]. SE SUCCEDE QUALCOSA, INTERVIENI»"},
 {"id":"b03","visual":"weekend","say":"Andrea passa il weekend attaccato al telefono. In busta paga, niente.","text":"ANDREA PASSA IL WEEKEND [r]ATTACCATO AL TELEFONO[/r]. IN BUSTA, NIENTE"},
 W("b04"),
 {"id":"b05","visual":"law","say":"Quella si chiama reperibilità. E molti contratti collettivi prevedono un'indennità apposta.","text":"SI CHIAMA [g]REPERIBILITÀ[/g]: MOLTI CCNL PREVEDONO [g]UN'INDENNITÀ[/g]"},
 {"id":"b06","visual":"call","say":"E se ti chiamano e intervieni, quello è lavoro vero: va pagato, con le maggiorazioni.","text":"SE TI CHIAMANO E INTERVIENI, È [g]LAVORO VERO[/g]: PAGATO, CON LE MAGGIORAZIONI"},
 {"id":"b07","visual":"strict","say":"E se i vincoli sono molto stretti, i giudici europei l'hanno considerata orario di lavoro.","text":"VINCOLI MOLTO STRETTI? PER I GIUDICI UE PUÒ ESSERE [g]ORARIO DI LAVORO[/g]"},
 {"id":"b08","visual":"proofs","say":"Il consiglio: conserva i messaggi, le chiamate e gli orari degli interventi.","text":"CONSERVA [g]MESSAGGI[/g], [g]CHIAMATE[/g] E [g]ORARI DEGLI INTERVENTI[/g]"},
 {"id":"b09","visual":"cede","say":"Il capo ci ripensa. «Va bene, te la pago.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TE LA PAGO[/g]»"},
]+CTA("b10","b11","Ti chiedono di essere reperibile gratis?","TI CHIEDONO DI ESSERE [r]REPERIBILE GRATIS[/r]?")
ART=r'''
ART.hook=sceneHook(phone(80,-640,120,"",-10));
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'point',stamp:"SEMPRE ACCESO",at:b=>b[0]+":ACCESO",extra:b=>G(phone(0,0,150,"",-8),"translate(150,1100)")});
ART.weekend=b=>
  G(paper(0,0,300,280,`<rect x="0" y="0" width="254" height="70" fill="${RED_SOFT}"/>`+txt(127,52,"SAB · DOM",40,RED)+txt(127,190,"24 h",90,INK)),"translate(110,680) rotate(-5 150 140)")+
  guy({x:600,y:1780,s:0.84,look:0.2,face:'flat',brows:'worried',eyes:'tired',l:[-30,230],r:[150,-20],bendR:40,rh:'dot',behind:phone(180,-640,110,"",10)})+
  A(ringLines(810,1060,70),{from:b[0]+":TELEFONO",loop:"shake:4:0.3"})+
  A(stamp(560,1440,"0 €",-8),{from:b[0]+":NIENTE",inn:"stamp"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CCNL",art:"REPERIBILITÀ",line:"indennità",p1:"REPERIBILITÀ",c1:b=>b[0]+":REPERIBILITÀ",p2:"INDENNITÀ APPOSITA",c2:b=>b[0]+":INDENNITÀ"});
ART.call=b=>
  windowNight(620,640,360,320)+clock(270,860,110,3,10,{label:"03:10",labelCol:RED})+
  guy({x:470,y:1780,s:0.84,look:0.4,face:'flat',brows:'up',eyes:'tired',l:[-30,230],r:[150,-60],bendR:30,rh:'dot',behind:phone(170,-690,100,"",8)})+
  A(stamp(760,1260,"LAVORO",-8,GREEN),{from:b[0]+":LAVORO",inn:"stamp"});
ART.strict=b=>
  book(170,640,740,420,{title:"CORTE GIUSTIZIA UE",art:"2018",line:"vincoli|stretti"})+
  A(pill(540,1200,820,"PUÒ ESSERE ORARIO DI LAVORO",GREEN),{from:b[0]+":ORARIO",inn:"stamp"})+
  guy({x:900,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.proofs=b=>
  guy({x:540,y:1780,s:0.8,look:0.3,face:'smirk',brows:'sly',eyes:'dot',l:[-30,230],r:[170,-120],bendR:30,rh:'dot',behind:magnifier(322,-792,80,82)})+
  A(phone(90,660,170,chatTxt(14,80,142,"Intervieni ora")+chatTxt(14,160,142,"OK"),-6),{from:b[0]+":MESSAGGI",inn:"pop"})+
  A(G(phone(0,0,150,txt(75,140,"☎ 3",40,INK),4),"translate(420,640)"),{from:b[0]+":CHIAMATE",inn:"pop"})+
  A(slip(760,700,240,"INTERVENTI","03:10-05:00",5),{from:b[0]+":ORARI",inn:"pop"});
ART.cede=sceneCede("PAGO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["REPERIBILE","[r]NEL WEEKEND[/r]?","[g]VA PAGATA[/g]."]
COVER_ART='    coverPair(phone(80,-640,120,"",-10))'
