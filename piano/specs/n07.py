SLUG="reel_giusta_causa"; TITLE="Dimissioni per giusta causa: cosa sono"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"unpaid","say":"Andrea non prende lo stipendio da tre mesi. Vuole andarsene.","text":"ANDREA [r]NON PRENDE LO STIPENDIO[/r] DA 3 MESI. VUOLE ANDARSENE"},
 {"id":"b03","visual":"boss","say":"«Vuoi andartene? Allora dai il preavviso. E niente disoccupazione.»","text":"«VUOI ANDARTENE? DAI IL PREAVVISO. [r]E NIENTE DISOCCUPAZIONE[/r]»"},
 {"id":"b04","visual":"wrong","say":"Peccato che esistano le dimissioni per giusta causa.","text":"PECCATO CHE ESISTANO LE [g]DIMISSIONI PER GIUSTA CAUSA[/g]"},
 {"id":"b05","visual":"law","say":"Se il datore è gravemente inadempiente, puoi andartene subito, senza preavviso.","text":"SE IL DATORE È GRAVEMENTE INADEMPIENTE, [g]TE NE VAI SUBITO[/g], SENZA PREAVVISO"},
 {"id":"b06","visual":"law","say":"Esempi tipici: stipendi non pagati, molestie, demansionamento.","text":"ESEMPI: [r]STIPENDI NON PAGATI[/r], [r]MOLESTIE[/r], [r]DEMANSIONAMENTO[/r]"},
 {"id":"b07","visual":"money","say":"E in quel caso il preavviso lo paga il datore a te: è l'indennità di mancato preavviso.","text":"E IL PREAVVISO [g]LO PAGA IL DATORE A TE[/g]: INDENNITÀ DI MANCATO PREAVVISO"},
 {"id":"b08","visual":"money","say":"In più, con la giusta causa spetta la NASpI.","text":"IN PIÙ, CON LA GIUSTA CAUSA [g]SPETTA LA NASPI[/g]"},
 {"id":"b09","visual":"online","say":"Le dimissioni si fanno online, e la giusta causa va indicata nella procedura.","text":"DIMISSIONI ONLINE: LA GIUSTA CAUSA [g]VA INDICATA NELLA PROCEDURA[/g]"},
 {"id":"b10","visual":"proofs","say":"Il consiglio: prima metti per iscritto le contestazioni, e conserva le prove.","text":"PRIMA [g]CONTESTA PER ISCRITTO[/g] E CONSERVA LE PROVE"},
 {"id":"b11","visual":"end","say":"Così Andrea se ne va. E il capo, ora, gli deve stipendi, TFR e preavviso.","text":"ANDREA SE NE VA. IL CAPO GLI DEVE [g]STIPENDI, TFR E PREAVVISO[/g]"},
 {"id":"b12","visual":"cta","say":"Vuoi andartene perché non ti pagano?","text":"VUOI ANDARTENE [r]PERCHÉ NON TI PAGANO[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(cardboardBox(0,0,200),"translate(90,-480)"));
ART.unpaid=b=>{
  const marks=[b[0]+"+0.4",b[0]+"+0.7",b[0]+"+1.0"];
  return monthsGrid(260,660,560,3,3,marks,{title:"STIPENDIO",col:RED})+
    guy({x:540,y:1790,s:0.7,look:0,face:'sad',brows:'worried',sweat:true,l:[-30,230],r:[30,230]});
};
ART.boss=sceneBoss({face:'smirk',brows:'angry',lh:'point',stamp:"NIENTE NASPI",at:b=>b[0]+":DISOCCUPAZIONE"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CODICE CIVILE",art:"ART. 2119",line:"giusta|causa",p1:"SUBITO, SENZA PREAVVISO",c1:b=>b[0]+":SUBITO",p2:"STIPENDI · MOLESTIE · DEMANSIONAMENTO",c2:b=>b[1]+":STIPENDI",col2:RED});
ART.money=b=>
  A(slip(110,680,340,"PREAVVISO","PAGATO A TE",-5),{from:b[0]+":DATORE",inn:"pop"})+
  A(shield(620,680,320,"NASPI",""),{from:b[1]+":NASPI",inn:"pop"})+
  guy({x:540,y:1800,s:0.55,look:0,face:'grin',brows:'up',l:[-150,-60],bendL:30,lh:'open',r:[150,-60],bendR:30,rh:'open'});
ART.online=b=>
  monitor(540,1250,520,false)+desk(240,1250,600)+
  A(G(paper(0,0,360,200,txt(157,80,"DIMISSIONI",44,INK)+txt(157,150,"✓ GIUSTA CAUSA",40,GREEN)),"translate(360,860)"),{from:b[0]+":INDICATA",inn:"pop"})+
  guy({x:180,y:1790,s:0.6,look:0.5,face:'smirk',brows:'sly',l:[-30,200],r:[150,-60],bendR:30,rh:'point'});
ART.proofs=b=>
  guy({x:400,y:1780,s:0.92,look:0.5,face:'smirk',brows:'sly',l:[-30,230],r:[150,-40],bendR:30,rh:'dot',behind:folder(90,-720,260,"PROVE",-4)})+
  A(letter(690,700,260,"CONTESTAZIONE",6),{from:b[0]+":CONTESTA",inn:"slide"});
ART.end=b=>
  guy({x:330,y:1770,s:0.95,look:0.5,face:'grin',brows:'up',l:[118,118],bendL:30,r:[-118,118],bendR:30,front:cardboardBox(-170,-470,340)})+
  A(pill(720,780,500,"STIPENDI",GREEN),{from:b[0]+":STIPENDI",inn:"stamp"})+
  A(pill(720,910,500,"TFR",GREEN),{from:b[0]+":TFR",inn:"stamp"})+
  A(pill(720,1040,500,"PREAVVISO",GREEN),{from:b[0]+":PREAVVISO",inn:"stamp"});
ART.cta=sceneCTA;
'''
COVER_TITLE=["NON TI PAGANO","E [r]VUOI ANDARTENE[/r]?","[g]GIUSTA CAUSA[/g]."]
COVER_ART='    coverPair(G(cardboardBox(0,0,200),"translate(90,-480)"))'
