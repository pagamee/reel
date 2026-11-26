SLUG="reel_stipendio_ritardo"; TITLE="Lo stipendio arriva sempre il 20"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"calendar","say":"Lo stipendio di Andrea dovrebbe arrivare il dieci del mese.","text":"LO STIPENDIO DOVREBBE ARRIVARE [g]IL 10 DEL MESE[/g]"},
 {"id":"b03","visual":"calendar","say":"Arriva il venti. Poi il trenta. Poi il mese dopo.","text":"ARRIVA IL 20. POI IL 30. [r]POI IL MESE DOPO[/r]"},
 {"id":"b04","visual":"boss","say":"«Abbi pazienza: i clienti mi pagano in ritardo.»","text":"«ABBI PAZIENZA: [r]I CLIENTI MI PAGANO IN RITARDO[/r]»"},
 {"id":"b05","visual":"wrong","say":"Peccato che non sia un problema tuo.","text":"PECCATO CHE [g]NON SIA UN PROBLEMA TUO[/g]"},
 {"id":"b06","visual":"law","say":"La data di pagamento la fissa il contratto: collettivo o individuale.","text":"LA DATA DI PAGAMENTO [g]LA FISSA IL CONTRATTO[/g]"},
 {"id":"b07","visual":"law","say":"E i ritardi dei clienti sono un rischio dell'azienda, non tuo.","text":"I RITARDI DEI CLIENTI SONO [r]UN RISCHIO DELL'AZIENDA[/r], NON TUO"},
 {"id":"b08","visual":"interest","say":"Sugli stipendi pagati in ritardo maturano interessi e rivalutazione.","text":"SUGLI STIPENDI IN RITARDO MATURANO [g]INTERESSI E RIVALUTAZIONE[/g]"},
 {"id":"b09","visual":"exit","say":"E se i ritardi sono gravi e ripetuti, possono giustificare le dimissioni per giusta causa. Con la NASpI.","text":"RITARDI GRAVI E RIPETUTI: POSSIBILI [g]DIMISSIONI PER GIUSTA CAUSA[/g], CON NASPI"},
 {"id":"b10","visual":"mora","say":"Prima, però, Andrea manda una messa in mora. E con le buste paga può chiedere un decreto ingiuntivo.","text":"PRIMA, [r]MESSA IN MORA[/r]. CON LE BUSTE PAGA, [r]DECRETO INGIUNTIVO[/r]"},
 {"id":"b11","visual":"cede","say":"Il capo ci ripensa. «Va bene, da questo mese puntuale.»","text":"IL CAPO CI RIPENSA. «VA BENE, DA QUESTO MESE [g]PUNTUALE[/g]»"},
 {"id":"b12","visual":"cta","say":"Lo stipendio ti arriva sempre in ritardo?","text":"LO STIPENDIO TI ARRIVA [r]SEMPRE IN RITARDO[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(alarmClock(0,0,70),"translate(150,-470)"));
ART.calendar=b=>{
  const day=(x,y,n,col,from)=>A(G(paper(0,0,220,240,`<rect x="0" y="0" width="174" height="60" fill="${col===RED?RED_SOFT:GREEN_SOFT}"/>`+txt(87,150,n,90,col)),`translate(${x},${y})`),{from,inn:"pop"});
  return day(100,680,"10",GREEN,b[0])+day(400,700,"20",RED,b[1]+":20")+day(700,680,"30",RED,b[1]+":30")+
    A(G(paper(0,0,260,240,`<rect x="0" y="0" width="214" height="60" fill="${RED_SOFT}"/>`+fitTxt(107,150,"MESE DOPO",190,48,RED)),"translate(410,1020)"),{from:b[1]+":MESE",inn:"stamp"})+
    guy({x:880,y:1800,s:0.5,look:-0.3,face:'sad',brows:'worried',l:[-30,200],r:[30,200]});
};
ART.boss=sceneBoss({face:'wavy',brows:'worried',lh:'open',stamp:"PAZIENZA",at:b=>b[0]+":PAZIENZA"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CONTRATTO",art:"PAGA",line:"entro il|giorno X",p1:"DATA FISSATA DAL CONTRATTO",c1:b=>b[0]+":CONTRATTO",p2:"RISCHIO DELL'AZIENDA",c2:b=>b[1]+":RISCHIO",col2:RED});
ART.interest=b=>
  calculator(130,700,300,-6)+
  A(txt(720,820,"+ INTERESSI",72,GREEN),{from:b[0]+":INTERESSI",inn:"pop"})+
  A(txt(720,940,"+ RIVALUTAZIONE",60,GREEN),{from:b[0]+":RIVALUTAZIONE",inn:"pop"})+
  A(coin(620,1100,48,"%")+coin(730,1070,40,"%")+coin(830,1110,44,"%"),{from:b[0]+":INTERESSI",inn:"drop"})+
  guy({x:420,y:1790,s:0.62,look:0.4,face:'smirk',brows:'sly',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.exit=b=>
  guy({x:330,y:1770,s:0.95,look:0.5,face:'smirk',brows:'sly',l:[118,118],bendL:30,r:[-118,118],bendR:30,front:cardboardBox(-170,-470,340)})+
  A(pill(700,800,560,"GIUSTA CAUSA",GREEN),{from:b[0]+":GIUSTA",inn:"stamp"})+
  A(pill(700,940,560,"+ NASPI",GREEN),{from:b[0]+":NASPI",inn:"stamp"});
ART.mora=b=>
  A(letter(70,680,300,"MESSA IN MORA",-6),{from:b[0]+":MORA",inn:"stamp"})+
  A(decreeDoc(620,680,330,440,5),{from:b[0]+":DECRETO",inn:"pop"})+
  guy({x:540,y:1790,s:0.55,look:0,face:'smirk',brows:'sly',l:[-150,-60],bendL:30,lh:'open',r:[150,-60],bendR:30,rh:'open'});
ART.cede=sceneCede("PUNTUALE");
ART.cta=sceneCTA;
'''
COVER_TITLE=["LO STIPENDIO","ARRIVA [r]SEMPRE IN RITARDO[/r]?","[g]NON È UN TUO PROBLEMA[/g]."]
COVER_ART='    coverPair(G(alarmClock(0,0,70),"translate(150,-470)"))'
