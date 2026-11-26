SLUG="reel_naspi"; TITLE="Licenziato per colpa tua? La NASpI spetta lo stesso"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"fired","say":"Andrea viene licenziato per un errore sul lavoro.","text":"ANDREA VIENE [r]LICENZIATO[/r] PER UN ERRORE SUL LAVORO"},
 {"id":"b03","visual":"boss","say":"«Licenziato per colpa tua: la disoccupazione te la scordi.»","text":"«LICENZIATO PER COLPA TUA: [r]LA DISOCCUPAZIONE TE LA SCORDI[/r]»"},
 {"id":"b04","visual":"wrong","say":"Peccato che non funzioni così.","text":"PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},
 {"id":"b05","visual":"law","say":"La NASpI spetta a chi perde il lavoro senza volerlo. E un licenziamento, anche disciplinare, è involontario.","text":"LA NASPI SPETTA A CHI PERDE IL LAVORO [g]SENZA VOLERLO[/g], ANCHE SE LICENZIATO"},
 {"id":"b06","visual":"law","say":"Quindi spetta anche se ti licenziano per giusta causa.","text":"QUINDI SPETTA [g]ANCHE CON LA GIUSTA CAUSA[/g]"},
 {"id":"b07","visual":"req","say":"Servono almeno tredici settimane di contributi negli ultimi quattro anni.","text":"SERVONO [g]13 SETTIMANE DI CONTRIBUTI[/g] NEGLI ULTIMI 4 ANNI"},
 {"id":"b08","visual":"deadline","say":"E la domanda va fatta all'INPS entro sessantotto giorni.","text":"LA DOMANDA ALL'INPS VA FATTA [r]ENTRO 68 GIORNI[/r]"},
 {"id":"b09","visual":"challenge","say":"Se poi il licenziamento è ingiusto, puoi anche impugnarlo: entro sessanta giorni.","text":"SE IL LICENZIAMENTO È INGIUSTO, SI IMPUGNA [r]ENTRO 60 GIORNI[/r]"},
 {"id":"b10","visual":"apply","say":"Così Andrea fa domanda, e la NASpI arriva.","text":"ANDREA FA DOMANDA, E [g]LA NASPI ARRIVA[/g]"},
 {"id":"b11","visual":"cta","say":"Ti hanno detto che non hai diritto alla NASpI?","text":"TI HANNO DETTO CHE [r]NON HAI DIRITTO ALLA NASPI[/r]?"},
 {"id":"b12","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(shield(0,0,160,"NASPI",""),"translate(70,-640)"));
ART.fired=b=>
  guy({x:330,y:1770,s:0.95,look:0.5,face:'sad',brows:'worried',l:[118,118],bendL:30,r:[-118,118],bendR:30,front:cardboardBox(-170,-470,340)})+
  boss({x:830,y:1770,s:0.9,look:-0.5,face:'flat',brows:'angry',l:[-190,-40],bendL:30,lh:'dot',r:[30,230],behind:letter(-400,-720,160,"LICENZ.",-8)});
ART.boss=sceneBoss({face:'smirk',brows:'angry',lh:'point',stamp:"SCORDATELA",at:b=>b[0]+":SCORDI"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"D.LGS. 22/2015",art:"NASPI",line:"perdita|involontaria",p1:"PERDITA INVOLONTARIA DEL LAVORO",c1:b=>b[0]+":VOLERLO",p2:"ANCHE CON LA GIUSTA CAUSA",c2:b=>b[1]+":GIUSTA"});
ART.req=b=>{
  let g=rct(110,700,860,420,16,PAPER,7)+`<rect x="114" y="704" width="852" height="82" rx="12" fill="${GREEN_SOFT}"/>`+txt(540,762,"13 SETTIMANE IN 4 ANNI",48,GREEN);
  for(let i=0;i<13;i++){const cx=170+(i%7)*124, cy=860+Math.floor(i/7)*130;
    g+=txt(cx,cy-30,"S"+(i+1),30,"#71717a")+A(check(cx,cy+20,26,GREEN),{from:`${b[0]}+${(0.3+i*0.12).toFixed(2)}`,inn:"stamp"});}
  return g+guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
};
ART.deadline=b=>
  hourglass(300,1080,340)+
  A(G(paper(0,0,320,320,txt(137,110,"ENTRO",44,"#52525b")+txt(137,200,"68",110,RED)+txt(137,270,"GIORNI",44,RED)),"translate(610,700) rotate(5 160 160)"),{from:b[0]+":68",inn:"stamp"})+
  guy({x:780,y:1790,s:0.6,look:-0.3,face:'flat',brows:'up',l:[-160,-100],bendL:30,lh:'point',r:[30,200]});
ART.challenge=b=>
  A(G(gavel(0,0,1.15,-35),"translate(820,880)"),{from:b[0]+":IMPUGNA",inn:"stamp"})+
  A(G(paper(0,0,280,260,txt(117,90,"ENTRO",40,"#52525b")+fitTxt(117,200,"60 GG",200,80,RED)),"translate(110,700) rotate(-5 140 130)"),{from:b[0]+":60",inn:"stamp"})+
  guy({x:540,y:1780,s:0.8,look:0,face:'smirk',brows:'sly',l:[-150,-60],bendL:30,lh:'open',r:[150,-60],bendR:30,rh:'open'});
ART.apply=b=>
  bankBuilding(700,1000,340,"")+txt(700,1140,"INPS",56,INDIGO)+
  guy({x:300,y:1790,s:0.8,look:0.4,face:'grin',brows:'up',l:[-30,230],r:[150,-80],bendR:30,rh:'dot'})+
  A(mailIcon(410,880,170,"NASPI",-6),{from:b[0]+":DOMANDA",inn:"slide"})+
  A(coin(560,1280,46)+coin(650,1250,40),{from:b[0]+":ARRIVA",inn:"drop"});
ART.cta=sceneCTA;
'''
COVER_TITLE=["LICENZIATO","[r]PER COLPA TUA[/r]?","[g]LA NASPI TI SPETTA[/g]."]
COVER_ART='    coverPair(G(shield(0,0,160,"NASPI",""),"translate(70,-640)"))'
