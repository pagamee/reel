/* ---------- scene ricorrenti del piano ---------- */
const HEART=(x,y,s=1)=>`<path d="M 0 30 C -60 -30 -130 20 0 120 C 130 20 60 -30 0 30 Z" fill="#fca5a5" stroke="${INK}" stroke-width="7" transform="translate(${x},${y}) scale(${s})"/>`;
const sceneWrong=b=>
  guy({x:420,y:1780,s:1.0,look:0.4,face:'smirk',brows:'sly',eyes:'sly',l:[-26,168],bendL:78,r:[40,-236],bendR:30,rh:'up'})+
  boss({x:880,y:1790,s:0.6,look:-0.5,face:'o',brows:'worried',l:[-30,200],r:[30,200]})+
  A(qmark(880,1060,110),{from:b[0]+"+0.4",loop:"bob:10:1.2"})+
  A(sparkle(620,880,60,GREEN,3,-60,80),{from:b[0]+"+0.3",loop:"blink:0.9"});
const sceneCede=(word)=>b=>
  guy({x:290,y:1770,s:0.92,look:0.6,face:'smirk',brows:'sly',eyes:'sly',l:[-30,230],r:[30,230]})+
  boss({x:810,y:1770,s:0.92,look:-0.5,face:'wavy',brows:'worried',sweat:true,l:[-170,-40],bendL:26,lh:'open',r:[160,-40],bendR:26,rh:'open'})+
  A(sparkle(560,860,60,GREEN,3,-70,80),{from:b[0]+":"+word,loop:"blink:0.9"});
const sceneCTA=b=>
  guy({x:330,y:1560,s:0.84,look:0.4,face:'grin',brows:'up',l:[-30,230],r:[210,-120],bendR:30,rh:'dot'})+
  phone(540,640,250,
    rct(12,40,226,70,0,INDIGO_SOFT,0)+txt(125,88,"Pagamee",30,INDIGO)+
    chatBubble(24,140,190,80,"#f4f4f5")+
    A(chatBubble(40,240,190,80,INDIGO_SOFT),{from:b[1]+":SCRIVICI"})+
    A(chatBubble(24,340,170,80,"#f4f4f5"),{from:b[1]+":VERIFICHIAMO"}),-4)+
  thumbOver(556,994,-30,30,0.84)+
  A(sparkle(830,640,60,INDIGO,3,-60,80),{from:b[1]+":SCRIVICI",loop:"blink:0.9"})+
  A(G(pagameeMark(-190,0,120)+sans(-100,38,"Pagamee",112,INK,"start"),"translate(540,1720)"),{from:b[0]+"+0.4",inn:"rise"});
/* libro della legge con due pillole che entrano sulle parole */
const sceneLaw=(o)=>b=>
  book(170,640,740,420,{title:o.title,art:o.art,line:o.line})+
  (o.p1?A(pill(540,1150,820,o.p1,GREEN),{from:o.c1(b),inn:"stamp"}):"")+
  (o.p2?A(pill(540,1290,820,o.p2,o.col2||GREEN),{from:o.c2(b),inn:"stamp"}):"")+
  guy({x:900,y:1800,s:0.45,look:-0.3,face:'smile',brows:'up',l:[-30,200],r:[30,200]});
const sceneHook=(prop)=>b=>
  guy({x:470,y:1760,s:1.12,look:0.35,face:'smirk',brows:'sly',eyes:'sly',l:[-26,168],bendL:78,r:[56,70],bendR:40,rh:'dot',behind:prop})+
  A(sparkle(840,1000,70,GREEN,3,-45,80),{from:b[0]+"+0.5",loop:"blink:0.9"});
const sceneBoss=(o)=>b=>
  boss({x:600,y:1780,s:1.0,look:-0.2,face:o.face||'smirk',brows:o.brows||'sly',eyes:o.eyes||'dot',l:[-200,-60],bendL:30,lh:o.lh||'point',r:o.r||[30,230],bendR:30,rh:o.rh||'dot',behind:o.behind||''})+
  (o.stamp?A(stamp(560,780,o.stamp,-6),{from:o.at(b),inn:"stamp"}):"")+(o.extra?o.extra(b):"");
const coverPair=(prop)=>
  boss({x:870,y:1790,s:0.62,look:-0.5,face:'sad',brows:'worried',sweat:true,l:[-30,230],r:[30,230]})+
  guy({x:400,y:1770,s:1.0,look:0.3,face:'grin',brows:'up',l:[-150,-70],bendL:30,lh:'thumb',r:[56,70],bendR:40,rh:'dot',front:prop})+
  sparkle(180,860,60,GREEN,3,-130,80);
