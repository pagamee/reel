SLUG="reel_malattia"; TITLE="In malattia e ti tolgono soldi dalla busta"
BEATS=[ {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"sick","say":"Andrea si ammala, e resta a casa dieci giorni, con il certificato del medico.","text":"ANDREA SI AMMALA: [r]10 GIORNI A CASA[/r], CON IL CERTIFICATO"},
 {"id":"b03","visual":"payslip","say":"In busta paga, quei giorni sono quasi tutti spariti.","text":"IN BUSTA PAGA, QUEI GIORNI SONO [r]QUASI TUTTI SPARITI[/r]"},
 {"id":"b04","visual":"boss","say":"«Se non lavori, non ti pago. Semplice.»","text":"«SE NON LAVORI, [r]NON TI PAGO[/r]. SEMPLICE»"},
 {"id":"b05","visual":"wrong","say":"Peccato che non funzioni così.","text":"PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},
 {"id":"b06","visual":"law","say":"In malattia, per la maggior parte dei dipendenti, spetta un'indennità dell'INPS.","text":"IN MALATTIA, DI SOLITO, SPETTA [g]UN'INDENNITÀ INPS[/g]"},
 {"id":"b07","visual":"law","say":"E spesso il contratto collettivo obbliga il datore a integrarla, anche fino all'intera paga.","text":"E SPESSO IL CCNL OBBLIGA IL DATORE A [g]INTEGRARLA[/g], ANCHE FINO AL 100%"},
 {"id":"b08","visual":"first","say":"Anche i primi tre giorni, in molti contratti, sono a carico del datore.","text":"ANCHE I [g]PRIMI 3 GIORNI[/g], IN MOLTI CCNL, SONO A CARICO DEL DATORE"},
 {"id":"b09","visual":"advance","say":"Di solito è proprio il datore ad anticipare tutto in busta paga.","text":"DI SOLITO È IL DATORE AD [g]ANTICIPARE TUTTO IN BUSTA[/g]"},
 {"id":"b10","visual":"check","say":"Se i conti non tornano, le differenze si recuperano. Controlla il tuo contratto collettivo.","text":"SE I CONTI NON TORNANO, [g]LE DIFFERENZE SI RECUPERANO[/g]"},
 {"id":"b11","visual":"cede","say":"Il capo ci ripensa. «Va bene, sistemo la busta.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]SISTEMO LA BUSTA[/g]»"},
 {"id":"b12","visual":"cta","say":"Ti hanno tolto soldi per la malattia?","text":"TI HANNO TOLTO SOLDI [r]PER LA MALATTIA[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(thermometer(0,0,20),"translate(170,-480) scale(1.6)"));
ART.sick=b=>
  bed(300,1440,560,false)+guy({x:780,y:1790,s:0.62,look:-0.3,face:'sad',brows:'worried',sweat:true,l:[-30,200],r:[30,200]})+
  A(G(paper(0,0,260,300,txt(107,70,"CERTIFICATO",30,INDIGO)+lines(26,120,170,3,40)+txt(107,260,"10 GG",56,RED)),"translate(120,700) rotate(-5 130 150)"),{from:b[0]+":CERTIFICATO",inn:"pop"})+
  G(thermometer(0,0,30),"translate(560,980) scale(1.8)");
ART.payslip=b=>
  payslipDoc(110,660,560,720,[["Giorni malattia","10"],["Pagato","0 €",RED]],-3)+
  A(`<ellipse cx="520" cy="1010" rx="170" ry="64" fill="none" stroke="${RED}" stroke-width="9" transform="rotate(-5 520 1010)"/>`,{from:b[0]+":SPARITI",inn:"draw"})+
  guy({x:870,y:1790,s:0.6,look:-0.3,face:'o',brows:'worried',l:[-30,200],r:[30,200]});
ART.boss=sceneBoss({face:'smirk',brows:'angry',lh:'point',stamp:"NON TI PAGO",at:b=>b[0]+":PAGO"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"INPS E CCNL",art:"MALATTIA",line:"indennità|+ integrazione",p1:"INDENNITÀ INPS",c1:b=>b[0]+":INPS",p2:"+ INTEGRAZIONE DEL DATORE",c2:b=>b[1]+":INTEGRARLA"});
ART.first=b=>{
  const marks=[b[0]+"+0.3",b[0]+"+0.6",b[0]+"+0.9"];
  return monthsGrid(260,660,560,3,3,marks,{title:"GIORNI 1-2-3",col:GREEN})+
    A(pill(540,1300,640,"DATORE (SPESSO)",GREEN),{from:b[0]+":DATORE",inn:"stamp"})+
    guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
};
ART.advance=b=>
  payslipDoc(110,660,560,720,[["Malattia INPS","+ €",GREEN],["Integrazione","+ €",GREEN]],-3)+
  A(stamp(780,1340,"IN BUSTA",-8,GREEN),{from:b[0]+":BUSTA",inn:"stamp"})+
  guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.check=b=>
  calculator(130,700,300,-6)+
  A(txt(720,900,"DIFFERENZE",76,GREEN),{from:b[0]+":DIFFERENZE",inn:"stamp"})+
  A(coin(620,1060,48)+coin(730,1030,40)+coin(830,1070,44),{from:b[0]+":RECUPERANO",inn:"drop"})+
  guy({x:420,y:1790,s:0.62,look:0.4,face:'smirk',brows:'sly',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.cede=sceneCede("SISTEMO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["IN MALATTIA","E [r]TI TOLGONO SOLDI[/r]?","[g]NON FUNZIONA COSÌ[/g]."]
COVER_ART='    coverPair(G(thermometer(0,0,20),"translate(170,-480) scale(1.6)"))'
