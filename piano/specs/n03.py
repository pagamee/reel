SLUG="reel_ferie"; TITLE="Lasci il lavoro con 20 giorni di ferie"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"leave","say":"Andrea lascia il lavoro. Ha ancora venti giorni di ferie mai fatte.","text":"ANDREA LASCIA IL LAVORO. HA ANCORA [g]20 GIORNI DI FERIE[/g] MAI FATTE"},
 {"id":"b03","visual":"boss","say":"«Le ferie non le hai fatte? Peggio per te: le hai perse.»","text":"«NON LE HAI FATTE? PEGGIO PER TE: [r]LE HAI PERSE[/r]»"},
 {"id":"b04","visual":"wrong","say":"Peccato che non funzioni così.","text":"PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},
 {"id":"b05","visual":"law","say":"A fine rapporto, le ferie maturate e non godute vanno pagate.","text":"A FINE RAPPORTO, LE FERIE NON GODUTE [g]VANNO PAGATE[/g]"},
 {"id":"b06","visual":"law","say":"Si chiama indennità sostitutiva, e la trovi nell'ultima busta paga.","text":"SI CHIAMA [g]INDENNITÀ SOSTITUTIVA[/g]: NELL'ULTIMA BUSTA PAGA"},
 {"id":"b07","visual":"eu","say":"E per la Corte di giustizia europea, le ferie non si perdono in automatico.","text":"PER LA CORTE UE, LE FERIE [g]NON SI PERDONO IN AUTOMATICO[/g]"},
 {"id":"b08","visual":"eu","say":"Si perdono solo se il datore ti ha messo davvero in condizione di farle, e ti ha avvisato.","text":"SOLO SE IL DATORE TI HA [g]MESSO IN CONDIZIONE DI FARLE[/g] E TI HA AVVISATO"},
 {"id":"b09","visual":"calc","say":"Venti giorni di ferie possono valere quasi un mese di stipendio.","text":"20 GIORNI DI FERIE: [g]QUASI UN MESE DI STIPENDIO[/g]"},
 {"id":"b10","visual":"slip","say":"Il consiglio: controlla il saldo ferie sulla busta paga. È scritto lì.","text":"CONTROLLA IL [g]SALDO FERIE[/g] SULLA BUSTA PAGA: È SCRITTO LÌ"},
 {"id":"b11","visual":"cede","say":"Il capo ci ripensa. «Va bene, te le pago.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TE LE PAGO[/g]»"},
 {"id":"b12","visual":"cta","say":"Hai lasciato il lavoro con ferie non pagate?","text":"HAI LASCIATO IL LAVORO CON [r]FERIE NON PAGATE[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(bigUmbrella(0,0,110,[""]),"translate(150,-560)"));
ART.leave=b=>
  guy({x:330,y:1770,s:0.95,look:0.5,face:'smile',brows:'up',l:[118,118],bendL:30,r:[-118,118],bendR:30,front:cardboardBox(-170,-470,340)})+
  A(G(bigUmbrella(0,0,150,["20 GG"]),"translate(780,960)"),{from:b[0]+":20",inn:"pop"});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"PERSE",at:b=>b[0]+":PERSE",
  extra:b=>G(bigUmbrella(0,0,110,[""]),"translate(230,1150)")+xmark(230,1100,90,RED)});
ART.wrong=sceneWrong;
ART.law=b=>
  payslipDoc(110,660,560,720,[["Ferie residue","20 gg"],["Indennità ferie","+ €",GREEN]],-3)+
  A(`<ellipse cx="520" cy="1010" rx="170" ry="64" fill="none" stroke="${GREEN}" stroke-width="9" transform="rotate(-5 520 1010)"/>`,{from:b[1]+":INDENNITÀ",inn:"draw"})+
  A(stamp(800,1300,"PAGATE",-8,GREEN),{from:b[0]+":PAGATE",inn:"stamp"})+
  guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.eu=b=>
  book(170,640,740,420,{title:"CORTE GIUSTIZIA UE",art:"2018",line:"ferie|non perse"})+
  A(xmark(540,1200,80,RED)+txt(540,1340,"PERSE IN AUTOMATICO",48,RED),{from:b[0]+":AUTOMATICO",inn:"stamp"})+
  A(pill(540,1480,760,"SOLO SE TI HA AVVISATO",GREEN),{from:b[1]+":AVVISATO",inn:"stamp"});
ART.calc=b=>
  calculator(130,700,300,-6)+
  A(txt(720,800,"20 giorni",64,INK),{from:b[0]+"+0.2",inn:"pop"})+
  A(txt(720,960,"≈ 1 MESE",96,GREEN),{from:b[0]+":MESE",inn:"stamp"})+
  A(coin(620,1100,48)+coin(730,1070,40)+coin(830,1110,44),{from:b[0]+":MESE",inn:"drop"})+
  guy({x:420,y:1790,s:0.62,look:0.4,face:'grin',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'thumb'});
ART.slip=b=>
  guy({x:540,y:1780,s:0.8,look:0.3,face:'smirk',brows:'sly',eyes:'dot',l:[-30,230],r:[170,-120],bendR:30,rh:'dot',behind:magnifier(322,-792,80,82)})+
  A(payslipDoc(80,660,440,560,[["Saldo ferie","20 gg",GREEN]],-4),{from:b[0]+":SALDO",inn:"pop"});
ART.cede=sceneCede("PAGO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["LASCI IL LAVORO","CON [g]20 GIORNI DI FERIE[/g]?","[r]VANNO PAGATI[/r]."]
COVER_ART='    coverPair(G(bigUmbrella(0,0,110,[""]),"translate(150,-560)"))'
