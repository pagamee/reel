import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_forfait"; TITLE="«Il forfait copre tutti gli straordinari»"
BEATS=[H,
 {"id":"b02","visual":"slip","say":"In busta paga Andrea ha una voce fissa: duecento euro di forfait straordinari.","text":"IN BUSTA HA UNA VOCE FISSA: [g]200 € DI FORFAIT STRAORDINARI[/g]"},
 {"id":"b03","visual":"hours","say":"Ma ogni mese fa trenta ore in più.","text":"MA OGNI MESE FA [r]30 ORE IN PIÙ[/r]"},
 {"id":"b04","visual":"boss","say":"«Il forfait copre tutto. Ore in più comprese.»","text":"«IL FORFAIT [r]COPRE TUTTO[/r]. ORE IN PIÙ COMPRESE»"},
 W("b05"),
 {"id":"b06","visual":"law","say":"Un forfait sugli straordinari si può fare. Ma deve essere adeguato alle ore che fai davvero.","text":"IL FORFAIT SI PUÒ FARE, MA [g]DEVE ESSERE ADEGUATO ALLE ORE VERE[/g]"},
 {"id":"b07","visual":"calc","say":"Trenta ore, con la maggiorazione, possono valere molto più di duecento euro.","text":"30 ORE CON LA MAGGIORAZIONE POSSONO VALERE [g]MOLTO PIÙ DI 200 €[/g]"},
 {"id":"b08","visual":"calc","say":"E se le ore vere valgono di più, la differenza ti spetta.","text":"SE LE ORE VERE VALGONO DI PIÙ, [g]LA DIFFERENZA TI SPETTA[/g]"},
 {"id":"b09","visual":"proofs","say":"Il consiglio: tieni traccia degli orari, con badge, mail e messaggi.","text":"TIENI TRACCIA DEGLI ORARI: [g]BADGE[/g], [g]MAIL[/g], [g]MESSAGGI[/g]"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, ti pago le differenze.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TI PAGO LE DIFFERENZE[/g]»"},
]+CTA("b11","b12","Hai un forfait che non copre le tue ore?","HAI UN FORFAIT [r]CHE NON COPRE LE TUE ORE[/r]?")
ART=r'''
ART.hook=sceneHook(badgeCard(60,-700,180,-10));
ART.slip=b=>
  payslipDoc(110,660,560,720,[["Paga base","1.400 €"],["Forfait straord.","200 €",GREEN]],-3)+
  A(`<ellipse cx="520" cy="1010" rx="170" ry="64" fill="none" stroke="${GREEN}" stroke-width="9" transform="rotate(-5 520 1010)"/>`,{from:b[0]+":FORFAIT",inn:"draw"})+
  guy({x:870,y:1790,s:0.6,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.hours=b=>
  windowNight(640,640,340,300)+clock(300,830,120,8,0,{label:"20:00",labelCol:RED,spin:b[0]})+
  desk(360,1420,560)+monitor(640,1420,280,true)+
  guy({x:470,y:1780,s:0.84,look:0.5,face:'flat',brows:'worried',eyes:'tired',l:[-30,230],r:[170,20],bendR:30,rh:'dot'})+
  A(stamp(760,1080,"+30 ORE",-8),{from:b[0]+":30",inn:"stamp"});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"COPRE TUTTO",at:b=>b[0]+":COPRE"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CASSAZIONE",art:"FORFAIT",line:"adeguato|alle ore",p1:"FORFAIT: SÌ",c1:b=>b[0]+":FORFAIT",p2:"MA ADEGUATO ALLE ORE VERE",c2:b=>b[0]+":ADEGUATO"});
ART.calc=b=>
  calculator(130,700,300,-6)+
  A(txt(720,800,"30 h + maggioraz.",54,INK),{from:b[0]+"+0.2",inn:"pop"})+
  A(txt(720,930,"> 200 €",96,GREEN),{from:b[0]+":200",inn:"stamp"})+
  A(pill(720,1100,420,"DIFFERENZA",GREEN),{from:b[1]+":DIFFERENZA",inn:"stamp"})+
  guy({x:420,y:1790,s:0.62,look:0.4,face:'grin',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'thumb'});
ART.proofs=b=>
  guy({x:540,y:1780,s:0.8,look:0.3,face:'smirk',brows:'sly',eyes:'dot',l:[-30,230],r:[170,-120],bendR:30,rh:'dot',behind:magnifier(322,-792,80,82)})+
  A(badgeCard(110,700,190,-8),{from:b[0]+":BADGE",inn:"pop"})+
  A(mailIcon(380,640,220,"21:03",4),{from:b[0]+":MAIL",inn:"pop"})+
  A(phone(790,640,170,chatTxt(14,80,142,"Resta stasera")+chatTxt(14,160,142,"OK"),6),{from:b[0]+":MESSAGGI",inn:"pop"});
ART.cede=sceneCede("DIFFERENZE");
ART.cta=sceneCTA;
'''
COVER_TITLE=["«IL FORFAIT","[r]COPRE TUTTO[/r]»?","[g]NON SEMPRE[/g]."]
COVER_ART='    coverPair(badgeCard(110,-640,170,-8))'
