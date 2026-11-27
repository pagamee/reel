import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_busta_non_pagata"; TITLE="Busta paga consegnata, soldi mai arrivati"
BEATS=[H,
 {"id":"b02","visual":"slip","say":"Ogni mese Andrea riceve la busta paga. Tutto in regola, sulla carta.","text":"OGNI MESE ANDREA RICEVE LA BUSTA PAGA. [g]TUTTO IN REGOLA[/g], SULLA CARTA"},
 {"id":"b03","visual":"bank","say":"Ma sul conto, da due mesi, non arriva niente.","text":"MA SUL CONTO, DA 2 MESI, [r]NON ARRIVA NIENTE[/r]"},
 {"id":"b04","visual":"boss","say":"«La busta paga te l'ho data, l'hai pure firmata. Quindi sei pagato.»","text":"«LA BUSTA L'HAI FIRMATA. [r]QUINDI SEI PAGATO[/r]»"},
 W("b05"),
 {"id":"b06","visual":"law","say":"Firmare la busta paga per ricevuta, di regola, non vuol dire che ti hanno pagato.","text":"FIRMARE LA BUSTA PER RICEVUTA, DI REGOLA, [g]NON VUOL DIRE ESSERE PAGATO[/g]"},
 {"id":"b07","visual":"law","say":"Il pagamento lo deve dimostrare il datore. Per esempio con un bonifico.","text":"IL PAGAMENTO [g]LO DEVE DIMOSTRARE IL DATORE[/g]: PER ESEMPIO CON UN BONIFICO"},
 {"id":"b08","visual":"proof","say":"Anzi: quella busta paga è una prova del tuo credito.","text":"ANZI: QUELLA BUSTA PAGA È [g]UNA PROVA DEL TUO CREDITO[/g]"},
 {"id":"b09","visual":"decree","say":"Con le buste paga si può chiedere al giudice un decreto ingiuntivo, in tempi brevi.","text":"CON LE BUSTE PAGA, [g]DECRETO INGIUNTIVO[/g] IN TEMPI BREVI"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, faccio il bonifico.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]FACCIO IL BONIFICO[/g]»"},
]+CTA("b11","b12","Hai la busta paga, ma non i soldi?","HAI LA BUSTA PAGA, [r]MA NON I SOLDI[/r]?")
ART=r'''
ART.hook=sceneHook(G(paper(0,0,170,220,`<rect x="0" y="0" width="124" height="40" fill="${INDIGO_SOFT}"/>`+lines(20,80,110,3,40)),"translate(70,-640) rotate(-8 85 110)"));
ART.slip=b=>
  payslipDoc(110,660,560,720,[["Netto","1.450 €"],["Firma","✓",GREEN]],-3)+
  A(stamp(780,1300,"IN REGOLA",-8,GREEN),{from:b[0]+":REGOLA",inn:"stamp"})+
  guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.bank=b=>
  phone(380,640,320,rct(12,40,296,70,0,INDIGO_SOFT,0)+txt(160,88,"CONTO",32,INDIGO)+txt(160,260,"+ 0 €",80,RED)+lines(40,340,240,3,50),-3)+
  A(stamp(540,1300,"2 MESI",-8),{from:b[0]+":2",inn:"stamp"})+
  guy({x:880,y:1800,s:0.5,look:-0.3,face:'sad',brows:'worried',sweat:true,l:[-30,200],r:[30,200]});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'point',stamp:"SEI PAGATO",at:b=>b[0]+":PAGATO",
  behind:payslipDoc(-520,-740,240,300,[["","✓"]],-6)});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"BUSTA PAGA",art:"FIRMA",line:"per|ricevuta",p1:"RICEVUTA ≠ PAGAMENTO",c1:b=>b[0]+":RICEVUTA",p2:"LO PROVA IL DATORE",c2:b=>b[1]+":DIMOSTRARE"});
ART.proof=b=>
  payslipDoc(110,660,560,720,[["Netto","1.450 €",GREEN]],-3)+
  A(stamp(760,1300,"PROVA",-8,GREEN),{from:b[0]+":PROVA",inn:"stamp"})+
  guy({x:880,y:1800,s:0.45,look:-0.3,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.decree=b=>
  A(decreeDoc(620,680,330,440,5),{from:b[0]+":DECRETO",inn:"pop"})+
  payslipDoc(110,700,380,480,[["Netto","1.450 €"]],-6)+
  guy({x:540,y:1790,s:0.55,look:0,face:'smirk',brows:'sly',l:[-150,-60],bendL:30,lh:'open',r:[150,-60],bendR:30,rh:'open'});
ART.cede=sceneCede("BONIFICO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["HAI LA BUSTA PAGA","MA [r]NON I SOLDI[/r]?","[g]È UNA PROVA[/g]."]
COVER_ART='    coverPair(G(paper(0,0,170,220,`<rect x="0" y="0" width="124" height="40" fill="${INDIGO_SOFT}"/>`+lines(20,80,110,3,40)),"translate(110,-640) rotate(-8 85 110)"))'
