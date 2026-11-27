import sys,os; sys.path.insert(0,os.path.dirname(__file__)); from _h import H,W,CTA
SLUG="reel_trasferte"; TITLE="In trasferta e paghi tu le spese?"
BEATS=[H,
 {"id":"b02","visual":"travel","say":"Andrea va spesso in trasferta per lavoro: treno, albergo, pranzi.","text":"ANDREA VA SPESSO IN [g]TRASFERTA[/g]: TRENO, ALBERGO, PRANZI"},
 {"id":"b03","visual":"receipts","say":"Paga tutto di tasca sua. E i rimborsi non arrivano mai.","text":"PAGA TUTTO DI TASCA SUA. E [r]I RIMBORSI NON ARRIVANO MAI[/r]"},
 {"id":"b04","visual":"boss","say":"«Le spese? Fanno parte del lavoro. Arrangiati.»","text":"«LE SPESE? FANNO PARTE DEL LAVORO. [r]ARRANGIATI[/r]»"},
 W("b05"),
 {"id":"b06","visual":"law","say":"Le spese che sostieni per conto dell'azienda vanno rimborsate.","text":"LE SPESE PER CONTO DELL'AZIENDA [g]VANNO RIMBORSATE[/g]"},
 {"id":"b07","visual":"law","say":"E molti contratti collettivi prevedono anche un'indennità di trasferta, in più dello stipendio.","text":"E MOLTI CCNL PREVEDONO [g]UN'INDENNITÀ DI TRASFERTA[/g], IN PIÙ"},
 {"id":"b08","visual":"car","say":"Se usi la tua auto, spesso spetta anche il rimborso chilometrico.","text":"SE USI LA TUA AUTO, SPESSO SPETTA [g]IL RIMBORSO CHILOMETRICO[/g]"},
 {"id":"b09","visual":"keep","say":"Il consiglio: conserva biglietti, scontrini e ricevute. Sono la prova di quanto ti devono.","text":"CONSERVA [g]BIGLIETTI[/g], [g]SCONTRINI[/g] E [g]RICEVUTE[/g]: SONO LA PROVA"},
 {"id":"b10","visual":"cede","say":"Il capo ci ripensa. «Va bene, ti rimborso tutto.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]TI RIMBORSO TUTTO[/g]»"},
]+CTA("b11","b12","Paghi tu le spese delle trasferte?","PAGHI TU [r]LE SPESE DELLE TRASFERTE[/r]?")
ART=r'''
ART.hook=sceneHook(G(suitcase(0,0,0.6),"translate(170,-430)"));
ART.travel=b=>
  guy({x:470,y:1760,s:1.0,look:0.35,face:'smile',brows:'up',l:[-26,168],bendL:78,r:[110,200],bendR:20,rh:'dot'})+suitcase(676,1530,0.9)+
  A(slip(80,680,240,"TRENO","€ 89",-6),{from:b[0]+":TRENO",inn:"pop"})+
  A(slip(400,660,240,"ALBERGO","€ 120",3),{from:b[0]+":ALBERGO",inn:"pop"})+
  A(slip(720,690,240,"PRANZI","€ 35",-3),{from:b[0]+":PRANZI",inn:"pop"});
ART.receipts=b=>
  envelope(120,700,260,-6,false)+slip(420,660,220,"SCONTRINO","€ 35",-8)+slip(660,700,220,"HOTEL","€ 120",6)+
  A(stamp(540,1180,"NON RIMBORSATO",-6),{from:b[0]+":RIMBORSI",inn:"stamp"})+
  guy({x:540,y:1800,s:0.5,look:0,face:'sad',brows:'worried',l:[-30,200],r:[30,200]});
ART.boss=sceneBoss({face:'smirk',brows:'sly',eyes:'sly',lh:'open',stamp:"ARRANGIATI",at:b=>b[0]+":ARRANGIATI"});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"CCNL",art:"TRASFERTA",line:"rimborsi|+ indennità",p1:"SPESE RIMBORSATE",c1:b=>b[0]+":RIMBORSATE",p2:"+ INDENNITÀ DI TRASFERTA",c2:b=>b[1]+":INDENNITÀ"});
ART.car=b=>
  G(`<path d="M -220 0 L -180 -90 L 160 -90 L 220 0 Z" fill="#bfdbfe" stroke="${INK}" stroke-width="8" stroke-linejoin="round"/>`+rct(-280,0,560,110,30,"#93c5fd",8)+cir(-170,110,46,INK,0)+cir(170,110,46,INK,0)+cir(-170,110,18,"#a1a1aa",0)+cir(170,110,18,"#a1a1aa",0),"translate(540,1000)")+
  A(txt(540,800,"€ / KM",80,GREEN),{from:b[0]+":CHILOMETRICO",inn:"stamp"})+
  guy({x:880,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
ART.keep=b=>
  guy({x:400,y:1780,s:0.92,look:0.5,face:'smirk',brows:'sly',l:[-30,230],r:[150,-40],bendR:30,rh:'dot',behind:folder(90,-720,260,"RICEVUTE",-4)})+
  A(slip(660,660,200,"BIGLIETTO","€ 89",-5),{from:b[0]+":BIGLIETTI",inn:"pop"})+
  A(slip(820,860,180,"SCONTRINO","€ 35",6),{from:b[0]+":SCONTRINI",inn:"pop"});
ART.cede=sceneCede("RIMBORSO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["IN TRASFERTA","[r]PAGHI TU LE SPESE[/r]?","[g]VANNO RIMBORSATE[/g]."]
COVER_ART='    coverPair(G(suitcase(0,0,0.6),"translate(170,-430)"))'
