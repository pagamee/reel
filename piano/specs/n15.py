import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_quattordicesima"; TITLE="La quattordicesima: chi ce l'ha davvero"
BEATS=[H,
 {"id":"b02","visual":"july","say":"È luglio. La collega di Andrea, in un altro negozio, prende la quattordicesima.","text":"È LUGLIO. UNA COLLEGA, IN UN ALTRO NEGOZIO, PRENDE LA [g]QUATTORDICESIMA[/g]"},
 {"id":"b03","visual":"boss","say":"Andrea chiede la sua. «La quattordicesima? Da noi non esiste.»","text":"ANDREA CHIEDE LA SUA. «[r]DA NOI NON ESISTE[/r]»"},
 {"id":"b04","visual":"wrong","say":"Peccato che non lo decida il capo.","text":"PECCATO CHE [g]NON LO DECIDA IL CAPO[/g]"},
 {"id":"b05","visual":"law","say":"La quattordicesima non c'è per tutti: la prevedono alcuni contratti collettivi.","text":"LA QUATTORDICESIMA LA PREVEDONO [g]ALCUNI CCNL[/g]"},
 {"id":"b06","visual":"law","say":"Per esempio commercio, turismo e pubblici esercizi.","text":"PER ESEMPIO [g]COMMERCIO[/g], [g]TURISMO[/g], [g]PUBBLICI ESERCIZI[/g]"},
 {"id":"b07","visual":"due","say":"Se il tuo contratto la prevede, ti spetta. Di solito a luglio.","text":"SE IL TUO CCNL LA PREVEDE, [g]TI SPETTA[/g]. DI SOLITO A LUGLIO"},
 {"id":"b08","visual":"months","say":"E matura mese per mese: se te ne vai prima, ti spetta la parte maturata.","text":"MATURA MESE PER MESE: SE TE NE VAI PRIMA, [g]TI SPETTA LA PARTE MATURATA[/g]"},
 {"id":"b09","visual":"check","say":"Il consiglio: guarda in busta paga quale contratto collettivo ti applicano.","text":"GUARDA IN BUSTA PAGA [g]QUALE CCNL TI APPLICANO[/g]"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, te la pago con gli arretrati.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]CON GLI ARRETRATI[/g]»"},
]+CTA("b11","b12","Non ti hanno mai pagato la quattordicesima?","NON TI HANNO MAI PAGATO [r]LA QUATTORDICESIMA[/r]?")
ART=r'''
ART.hook=sceneHook(G(coin(0,0,70,"14"),"translate(120,-520)"));
ART.july=b=>
  G(paper(0,0,300,320,`<rect x="0" y="0" width="254" height="80" fill="${GREEN_SOFT}"/>`+txt(127,58,"LUGLIO",44,GREEN)+txt(127,230,"14",120,INK)),"translate(110,680) rotate(-5 150 160)")+
  guy({x:620,y:1780,s:0.84,look:0.3,face:'o',brows:'up',l:[-30,230],r:[30,230]})+
  A(G(coin(0,0,60,"14"),"translate(860,1000)"),{from:b[0]+":QUATTORDICESIMA",inn:"pop",loop:"bob:8:1"});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"NON ESISTE",at:b=>b[0]+":ESISTE"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CCNL",art:"14ª",line:"se prevista",p1:"SOLO ALCUNI CCNL",c1:b=>b[0]+":ALCUNI",p2:"COMMERCIO · TURISMO · PUBBL. ESERCIZI",c2:b=>b[1]+":COMMERCIO"});
ART.due=b=>
  shield(330,690,420,"14","")+
  A(pill(540,1300,640,"DI SOLITO A LUGLIO",GREEN),{from:b[0]+":LUGLIO",inn:"stamp"})+
  guy({x:880,y:1800,s:0.5,look:-0.3,face:'grin',brows:'up',l:[-160,-100],bendL:30,lh:'point',r:[30,200]});
ART.months=b=>{
  const marks=Array.from({length:12},(_,i)=>`${b[0]}+${(0.3+i*0.15).toFixed(2)}`);
  return monthsGrid(110,660,860,12,4,marks,{title:"1/12 AL MESE",col:GREEN})+
    A(pill(540,1300,640,"PARTE MATURATA",GREEN),{from:b[0]+":MATURATA",inn:"stamp"})+
    guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
};
ART.check=b=>
  guy({x:540,y:1780,s:0.8,look:0.3,face:'smirk',brows:'sly',eyes:'dot',l:[-30,230],r:[170,-120],bendR:30,rh:'dot',behind:magnifier(322,-792,80,82)})+
  payslipDoc(80,660,440,560,[["CCNL","Commercio",GREEN]],-4);
ART.cede=sceneCede("ARRETRATI");
ART.cta=sceneCTA;
'''
COVER_TITLE=["LA [g]QUATTORDICESIMA[/g]","«DA NOI [r]NON ESISTE[/r]»?","DIPENDE DAL TUO CCNL."]
COVER_ART='    coverPair(G(coin(0,0,70,"14"),"translate(120,-520)"))'
