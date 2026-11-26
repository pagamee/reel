SLUG="reel_tredicesima"; TITLE="La tredicesima non è un regalo di Natale"
H="Cose sul lavoro che il tuo capo spera che tu non scopra mai."
BEATS=[
 {"id":"b01","visual":"hook","say":H,"text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"december","say":"È dicembre, e Andrea aspetta la tredicesima.","text":"È DICEMBRE, E ANDREA ASPETTA LA [g]TREDICESIMA[/g]"},
 {"id":"b03","visual":"boss","say":"«Quest'anno niente tredicesima: è andata male.»","text":"«QUEST'ANNO [r]NIENTE TREDICESIMA[/r]: È ANDATA MALE»"},
 {"id":"b04","visual":"boss","say":"«E poi è un regalo di Natale, mica un obbligo.»","text":"«È UN [r]REGALO DI NATALE[/r], MICA UN OBBLIGO»"},
 {"id":"b05","visual":"wrong","say":"Peccato che non funzioni così.","text":"PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},
 {"id":"b06","visual":"gift","say":"La tredicesima è prevista dai contratti collettivi: è retribuzione, non un regalo.","text":"È PREVISTA DAI CCNL: [g]È RETRIBUZIONE[/g], [r]NON UN REGALO[/r]"},
 {"id":"b07","visual":"gift","say":"E non dipende da come è andato l'anno dell'azienda.","text":"E [g]NON DIPENDE DA COME È ANDATO L'ANNO[/g] DELL'AZIENDA"},
 {"id":"b08","visual":"months","say":"Matura mese per mese: un dodicesimo per ogni mese lavorato.","text":"MATURA MESE PER MESE: [g]1/12 PER OGNI MESE[/g] LAVORATO"},
 {"id":"b09","visual":"months","say":"Di solito si paga a dicembre, insieme allo stipendio.","text":"DI SOLITO SI PAGA [g]A DICEMBRE[/g], CON LO STIPENDIO"},
 {"id":"b10","visual":"leave","say":"E se cambi lavoro a metà anno, ti spetta la parte maturata.","text":"SE CAMBI LAVORO A METÀ ANNO, TI SPETTA [g]LA PARTE MATURATA[/g]"},
 {"id":"b11","visual":"mora","say":"Se non arriva? Messa in mora, e poi decreto ingiuntivo. Con gli interessi.","text":"SE NON ARRIVA? [r]MESSA IN MORA[/r] E [r]DECRETO INGIUNTIVO[/r]. CON GLI INTERESSI"},
 {"id":"b12","visual":"cede","say":"Il capo ci ripensa. «Va bene, te la pago con lo stipendio.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TE LA PAGO[/g] CON LO STIPENDIO»"},
 {"id":"b13","visual":"cta","say":"Ti hanno saltato la tredicesima?","text":"TI HANNO [r]SALTATO LA TREDICESIMA[/r]?"},
 {"id":"b14","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(giftBox(0,0,0.7),"translate(170,-430)"));
ART.december=b=>
  windowNight(620,640,360,320)+
  G(paper(0,0,300,320,`<rect x="0" y="0" width="254" height="80" fill="${RED_SOFT}"/>`+txt(127,58,"DICEMBRE",40,RED)+txt(127,230,"25",120,INK)),"translate(150,680) rotate(-5 150 160)")+
  guy({x:540,y:1790,s:0.8,look:0.2,face:'smile',brows:'up',l:[-30,230],r:[30,230]})+
  A(G(coin(0,0,50,"13"),"translate(840,1150)"),{from:b[0]+":TREDICESIMA",inn:"pop",loop:"bob:8:1"});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"NIENTE",at:b=>b[0]+":NIENTE",
  extra:b=>A(G(giftBox(0,0,0.7),"translate(230,1180)"),{from:b[1]+":REGALO",inn:"pop"})});
ART.wrong=sceneWrong;
ART.gift=b=>
  giftBox(280,900,0.9)+A(xmark(280,920,110,RED),{from:b[0]+":REGALO",inn:"stamp"})+
  A(shield(560,680,380,"13",""),{from:b[0]+":RETRIBUZIONE",inn:"pop"})+
  A(pill(540,1330,760,"ANCHE SE L'ANNO VA MALE",GREEN),{from:b[1]+":ANNO",inn:"stamp"})+
  guy({x:900,y:1800,s:0.45,look:-0.3,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.months=b=>{
  const marks=Array.from({length:12},(_,i)=>`${b[0]}+${(0.4+i*0.18).toFixed(2)}`);
  return monthsGrid(110,660,860,12,4,marks,{title:"1/12 AL MESE",col:GREEN})+
    A(G(coin(0,0,60,"13"),"translate(540,1350)"),{from:b[1]+":DICEMBRE",inn:"drop"})+
    guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
};
ART.leave=b=>
  guy({x:300,y:1780,s:0.9,look:0.5,face:'smile',brows:'up',l:[118,118],bendL:30,r:[-118,118],bendR:30,front:cardboardBox(-170,-470,340)})+
  A(G(paper(0,0,320,300,txt(137,90,"GEN–GIU",44,"#52525b")+txt(137,200,"6/12",90,GREEN)),"translate(620,720) rotate(5 160 150)"),{from:b[0]+":MATURATA",inn:"stamp"});
ART.mora=b=>
  A(letter(70,680,300,"MESSA IN MORA",-6),{from:b[0]+":MORA",inn:"stamp"})+
  A(decreeDoc(620,680,330,440,5),{from:b[0]+":DECRETO",inn:"pop"})+
  A(G(coin(0,0,46,"%")+coin(90,-30,40,"%")+coin(170,10,44,"%"),"translate(430,1180)"),{from:b[0]+":INTERESSI",inn:"drop"})+
  guy({x:540,y:1790,s:0.55,look:0,face:'smirk',brows:'sly',l:[-150,-60],bendL:30,lh:'open',r:[150,-60],bendR:30,rh:'open'});
ART.cede=sceneCede("PAGO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["LA [g]TREDICESIMA[/g]","NON È UN","[r]REGALO DI NATALE[/r]."]
COVER_ART='    coverPair(G(coin(0,0,70,"13"),"translate(120,-520)"))+G(giftBox(0,0,0.6),"translate(800,1000)")+xmark(800,1010,80,RED)'
