SLUG="reel_parttime_imposto"; TITLE="«Da lunedì passi a part-time»"
BEATS=[
 {"id":"b01","visual":"hook","say":"Cose sul lavoro che il tuo capo spera che tu non scopra mai.","text":"COSE SUL LAVORO CHE IL TUO CAPO SPERA CHE TU [r]NON SCOPRA MAI[/r]"},
 {"id":"b02","visual":"full","say":"Andrea lavora a tempo pieno da tre anni.","text":"ANDREA LAVORA [g]A TEMPO PIENO[/g] DA 3 ANNI"},
 {"id":"b03","visual":"boss","say":"Un giorno il capo gli dice: «Da lunedì passi a part-time. Venti ore.»","text":"«DA LUNEDÌ PASSI A [r]PART-TIME[/r]. 20 ORE»"},
 {"id":"b04","visual":"boss","say":"«E se non firmi, sei fuori.»","text":"«E SE NON FIRMI, [r]SEI FUORI[/r]»"},
 {"id":"b05","visual":"wrong","say":"Peccato che non funzioni così.","text":"PECCATO CHE [g]NON FUNZIONI COSÌ[/g]"},
 {"id":"b06","visual":"law","say":"Per legge, il passaggio da tempo pieno a part-time richiede il tuo accordo, per iscritto.","text":"DA TEMPO PIENO A PART-TIME SERVE [g]IL TUO ACCORDO, PER ISCRITTO[/g]"},
 {"id":"b07","visual":"law","say":"E il tuo rifiuto non è un motivo valido per licenziarti.","text":"E IL TUO RIFIUTO [g]NON È UN MOTIVO VALIDO[/g] PER LICENZIARTI"},
 {"id":"b08","visual":"half","say":"Meno ore vuol dire meno stipendio, meno contributi, e un TFR più basso.","text":"MENO ORE: [r]MENO STIPENDIO[/r], [r]MENO CONTRIBUTI[/r], [r]TFR PIÙ BASSO[/r]"},
 {"id":"b09","visual":"sign","say":"Quindi, se firmi, deve essere una tua scelta. Non la paura.","text":"SE FIRMI, DEVE ESSERE [g]UNA TUA SCELTA[/g]. NON LA PAURA"},
 {"id":"b10","visual":"ask","say":"Andrea non firma, e chiede la proposta per iscritto, con le motivazioni.","text":"ANDREA NON FIRMA E CHIEDE LA PROPOSTA [g]PER ISCRITTO[/g]"},
 {"id":"b11","visual":"cede","say":"Il capo ci ripensa. «Va bene, resti a tempo pieno.»","text":"IL CAPO CI RIPENSA. «VA BENE, [g]RESTI A TEMPO PIENO[/g]»"},
 {"id":"b12","visual":"cta","say":"Ti vogliono passare a part-time contro la tua volontà?","text":"TI VOGLIONO PASSARE A PART-TIME [r]CONTRO LA TUA VOLONTÀ[/r]?"},
 {"id":"b13","visual":"cta","say":"Scrivici: verifichiamo il tuo caso, e non anticipi un euro.","text":"[i]SCRIVICI[/i]: VERIFICHIAMO IL TUO CASO E [g]NON ANTICIPI UN EURO[/g]"},
]
ART=r'''
ART.hook=sceneHook(G(clock(0,0,70,9,0),"translate(170,-470)"));
ART.full=b=>
  contractDoc(330,660,420,560,-3,{big:"40 ORE",bigCol:GREEN,sub:"tempo pieno"})+
  guy({x:200,y:1790,s:0.62,look:0.4,face:'smile',brows:'up',l:[-30,200],r:[120,-160],bendR:30,rh:'point'});
ART.boss=sceneBoss({face:'smirk',brows:'angry',lh:'point',stamp:"20 ORE",at:b=>b[0]+":PART-TIME",
  behind:contractDoc(-500,-720,240,320,-6,{big:"20 ORE",bigCol:RED,sub:"part-time"}),
  extra:b=>A(stamp(560,1460,"SEI FUORI",-6),{from:b[1]+":FUORI",inn:"stamp"})});
ART.wrong=sceneWrong;
ART.law=sceneLaw({title:"D.LGS. 81/2015",art:"ART. 8",line:"accordo|scritto",p1:"SERVE IL TUO ACCORDO SCRITTO",c1:b=>b[0]+":ACCORDO",p2:"RIFIUTO ≠ LICENZIAMENTO",c2:b=>b[1]+":MOTIVO"});
ART.half=b=>
  A(pill(540,760,700,"− STIPENDIO",RED),{from:b[0]+":STIPENDIO",inn:"stamp"})+
  A(pill(540,900,700,"− CONTRIBUTI",RED),{from:b[0]+":CONTRIBUTI",inn:"stamp"})+
  A(pill(540,1040,700,"− TFR",RED),{from:b[0]+":TFR",inn:"stamp"})+
  guy({x:540,y:1800,s:0.55,look:0,face:'sad',brows:'worried',l:[-30,200],r:[30,200]});
ART.sign=b=>
  contractDoc(110,660,380,500,-4,{big:"20 ORE",bigCol:RED,sub:"part-time"})+
  A(pill(760,900,420,"SCELTA",GREEN),{from:b[0]+":SCELTA",inn:"stamp"})+
  A(G(pill(0,0,420,"PAURA",RED)+ln(-200,0,200,0,10,INK),"translate(760,1040)"),{from:b[0]+":PAURA",inn:"stamp"})+
  guy({x:780,y:1800,s:0.55,look:-0.3,face:'smirk',brows:'sly',l:[-30,200],r:[30,200]});
ART.ask=b=>
  guy({x:400,y:1780,s:0.92,look:0.5,face:'smirk',brows:'sly',l:[-30,230],r:[150,-40],bendR:30,rh:'dot',behind:slip(120,-760,230,"PROPOSTA?","per iscritto",-4)})+
  A(mailIcon(720,900,220,"MOTIVI",6),{from:b[0]+":ISCRITTO",inn:"slide"});
ART.cede=sceneCede("PIENO");
ART.cta=sceneCTA;
'''
COVER_TITLE=["«DA LUNEDÌ","PASSI A [r]PART-TIME[/r]»?","[g]SERVE IL TUO SÌ[/g]."]
COVER_ART='    coverPair(G(clock(0,0,70,9,0),"translate(170,-470)"))'
