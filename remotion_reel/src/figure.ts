// Builder SVG estratti VERBATIM da reel_pipeline/reel_template.html.
// Generano markup stick-figure identico al pipeline originale (framework-agnostici).
/* eslint-disable */
export const W = 1080, H = 1920;
const INK = "#141414";
let UID = 0;
export function person(o: any): string {
  o=Object.assign({cx:540,sc:1,hair:'short',glasses:false,tie:null,
    shirt:'white',face:'neutral',larm:[-118,215],rarm:[118,215],
    lhand:'fist',rhand:'fist',hold:null,sweat:false,name:'fig'},o);

  const HR=80, headCy=-560, neckTop=-478,
        shTop=-455, shHW=76,          // spalle
        sleeveY=-388, sleeveHW=104,   // fondo manica
        hemY=-262, hemHW=92,          // orlo maglietta  (torso 193, gambe 262)
        feetY=0;
  const uid = ++UID;
  const S=[];
  const line=(x1,y1,x2,y2,w=9)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${INK}" stroke-width="${w}" stroke-linecap="round"/>`;
  const circ=(x,y,r,fill="none",w=9,extra="")=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" stroke="${INK}" stroke-width="${w}" ${extra}/>`;
  const path=(d,fill="none",w=9)=>`<path d="${d}" fill="${fill}" stroke="${INK}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`;

  /* ombra a terra */
  S.push(`<ellipse cx="0" cy="16" rx="140" ry="24" fill="#000" opacity="0.08"/>`);

  /* gambe: partono dall'orlo della maglietta */
  S.push(line(-30,hemY-4,-62,feetY));
  S.push(line( 30,hemY-4, 62,feetY));
  S.push(line(-62,feetY,-96,feetY+2));   // piedi
  S.push(line( 62,feetY, 96,feetY+2));

  /* ---- maglietta / busto ---- */
  const shirtD =
    `M ${-shHW} ${shTop}`+
    ` L ${-sleeveHW} ${sleeveY}`+          // spalla -> fondo manica sx
    ` L ${-sleeveHW+30} ${sleeveY+22}`+    // risvolto manica
    ` L ${-hemHW} ${hemY}`+                // fianco sx
    ` L ${hemHW} ${hemY}`+                 // orlo
    ` L ${sleeveHW-30} ${sleeveY+22}`+
    ` L ${sleeveHW} ${sleeveY}`+
    ` L ${shHW} ${shTop}`+
    ` Q 0 ${shTop+44} ${-shHW} ${shTop} Z`; // scollo

  const shirtFill = o.shirt==='blazer' ? "#dde5f0" : (o.shirt==='check' ? "#fdecea" : "#ffffff");
  S.push(`<clipPath id="shirt${uid}"><path d="${shirtD}"/></clipPath>`);
  S.push(path(shirtD, shirtFill));

  if(o.shirt==='check'){
    const g=[];
    for(let gx=-100;gx<=100;gx+=34) g.push(`<line x1="${gx}" y1="${shTop-10}" x2="${gx}" y2="${hemY+4}" stroke="#e5342b" stroke-width="4" opacity="0.45"/>`);
    for(let gy=shTop+6;gy<hemY;gy+=38)  g.push(`<line x1="-110" y1="${gy}" x2="110" y2="${gy}" stroke="#e5342b" stroke-width="4" opacity="0.45"/>`);
    S.push(`<g clip-path="url(#shirt${uid})">${g.join("")}</g>`);
  }
  if(o.shirt==='blazer'){
    // revers + camicia bianca a V
    S.push(`<g clip-path="url(#shirt${uid})">
      <path d="M ${-shHW+6} ${shTop+6} L -8 ${shTop+62} L 0 ${hemY} L ${-hemHW+18} ${hemY} Z" fill="#c3d0e2" stroke="none"/>
      <path d="M ${shHW-6} ${shTop+6} L 8 ${shTop+62} L 0 ${hemY} L ${hemHW-18} ${hemY} Z" fill="#c3d0e2" stroke="none"/>
      <path d="M -30 ${shTop+2} L 0 ${shTop+74} L 30 ${shTop+2}" fill="#ffffff" stroke="none"/>
    </g>`);
    S.push(path(`M -30 ${shTop+2} L 0 ${shTop+74} L 30 ${shTop+2}`,"none",6));
    S.push(path(`M ${-shHW+10} ${shTop+14} L -6 ${shTop+70}`,"none",7));
    S.push(path(`M ${shHW-10} ${shTop+14} L 6 ${shTop+70}`,"none",7));
  }
  S.push(path(shirtD,"none",9));          // contorno maglietta sopra i riempimenti

  /* cravatta (corta, finisce a metà busto) */
  if(o.tie){
    const tieEnd = hemY-34;
    S.push(`<path d="M 0 ${shTop+30} L -17 ${shTop+62} L 0 ${tieEnd} L 17 ${shTop+62} Z" fill="${o.tie}" stroke="${INK}" stroke-width="4"/>`);
    S.push(`<path d="M -13 ${shTop+18} L 0 ${shTop+38} L 13 ${shTop+18}" fill="${o.tie}" stroke="${INK}" stroke-width="5" stroke-linejoin="round"/>`);
  }

  /* ---- braccia ---- */
  /* origine: fondo manica; mano: [x, y sotto la spalla] con riferimento sy */
  const sy = shTop+18;
  const armFrom = (sx,sy0,hx,hy,side)=>{
    // leggera curva "a mano libera": il gomito si piega verso il basso/esterno
    const mx=(sx+hx)/2 + side*10, my=(sy0+hy)/2 + 16;
    return `<path d="M ${sx} ${sy0} Q ${mx} ${my} ${hx} ${hy}" fill="none" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`;
  };
  const laX=o.larm[0], laY=sy+o.larm[1];
  const raX=o.rarm[0], raY=sy+o.rarm[1];
  S.push(armFrom(-sleeveHW+20, sleeveY+14, laX, laY, -1));
  S.push(armFrom( sleeveHW-20, sleeveY+14, raX, raY,  1));

  /* mani: pugnetto tondo, oppure dito puntato, oppure palmo aperto */
  const hand=(x,y,kind,side)=>{
    if(kind==='point'){
      return circ(x,y,14,"#fff",7)+line(x+side*12,y-4,x+side*46,y-14,8);
    }
    if(kind==='open'){   // palmo aperto: cerchio + 3 ditini
      let d=circ(x,y,15,"#fff",7);
      d+=line(x-10,y-14,x-12,y-34,7)+line(x+2,y-17,x+2,y-39,7)+line(x+13,y-13,x+18,y-33,7);
      return d;
    }
    return circ(x,y,14,"#fff",7);
  };

  /* prop in mano destra */
  if(o.hold==='phone'){
    S.push(`<g transform="translate(${raX-34},${raY-92})"><rect x="0" y="0" width="74" height="126" rx="13" fill="#fff" stroke="${INK}" stroke-width="6"/><rect x="11" y="15" width="52" height="82" rx="4" fill="#dbe7ff"/><line x1="17" y1="32" x2="49" y2="32" stroke="#2b5fb3" stroke-width="5"/><line x1="17" y1="49" x2="56" y2="49" stroke="#9bb6e8" stroke-width="5"/><line x1="17" y1="64" x2="43" y2="64" stroke="#9bb6e8" stroke-width="5"/><circle cx="37" cy="110" r="6" fill="none" stroke="${INK}" stroke-width="4"/></g>`);
  } else if(o.hold==='paper'){
    S.push(`<g transform="translate(${raX-4},${raY-110})"><rect x="0" y="0" width="100" height="134" rx="6" fill="#fff" stroke="${INK}" stroke-width="5"/><line x1="15" y1="26" x2="85" y2="26" stroke="#2b5fb3" stroke-width="6"/><line x1="15" y1="50" x2="85" y2="50" stroke="#c7c7c7" stroke-width="5"/><line x1="15" y1="70" x2="70" y2="70" stroke="#c7c7c7" stroke-width="5"/><line x1="15" y1="90" x2="85" y2="90" stroke="#c7c7c7" stroke-width="5"/><line x1="15" y1="112" x2="60" y2="112" stroke="#e5342b" stroke-width="6"/></g>`);
  } else if(o.hold==='cash'){
    S.push(`<g transform="translate(${raX-46},${raY-60})">
      <rect x="6" y="10" width="112" height="62" rx="6" fill="#eaf7ee" stroke="${INK}" stroke-width="5" transform="rotate(-7 62 41)"/>
      <rect x="0" y="0" width="112" height="62" rx="6" fill="#eaf7ee" stroke="${INK}" stroke-width="5"/>
      <circle cx="56" cy="31" r="17" fill="none" stroke="#1a9e4b" stroke-width="5"/>
      <text x="56" y="45" font-family="Comic Neue, DejaVu Sans" font-weight="700" font-size="34" fill="#1a9e4b" text-anchor="middle">&#8364;</text></g>`);
  }

  S.push(hand(laX,laY,o.lhand,-1));
  if(!o.hold) S.push(hand(raX,raY,o.rhand,1));
  else S.push(circ(raX,raY,14,"#fff",7));

  /* collo + testa */
  S.push(line(0,neckTop,0,shTop+6,9));
  S.push(circ(0,headCy,HR,"#fff",9,`data-head="1"`));

  /* capelli */
  if(o.hair==='grey'||o.hair==='short'){
    const col = o.hair==='grey' ? "#9aa0a6" : INK;
    S.push(`<path d="M ${-HR+6} ${headCy-22} Q 0 ${headCy-HR-26} ${HR-6} ${headCy-22}" fill="none" stroke="${col}" stroke-width="15" stroke-linecap="round"/>`);
    if(o.hair==='grey'){
      // stempiatura + basette
      S.push(`<path d="M ${-HR+16} ${headCy-38} q 22 -20 44 -10" fill="none" stroke="${col}" stroke-width="10" stroke-linecap="round"/>`);
      S.push(`<path d="M ${-HR+6} ${headCy-20} q -7 18 -1 30" fill="none" stroke="${col}" stroke-width="9" stroke-linecap="round"/>`);
      S.push(`<path d="M ${HR-6} ${headCy-20} q 7 18 1 30" fill="none" stroke="${col}" stroke-width="9" stroke-linecap="round"/>`);
    }
  } else if(o.hair==='bob'){
    // caschetto: due bande laterali fino alla mascella + frangia
    const jaw=headCy+72, HAIR="#3b2b22";
    S.push(`<path d="
      M ${-HR-12} ${jaw}
      L ${-HR-12} ${headCy-6}
      Q ${-HR-12} ${headCy-HR-24} 0 ${headCy-HR-20}
      Q ${HR+12} ${headCy-HR-24} ${HR+12} ${headCy-6}
      L ${HR+12} ${jaw}
      L ${HR-18} ${jaw}
      L ${HR-18} ${headCy-16}
      Q ${HR-34} ${headCy-58} 0 ${headCy-62}
      Q ${-HR+34} ${headCy-58} ${-HR+18} ${headCy-16}
      L ${-HR+18} ${jaw} Z" fill="${HAIR}" stroke="${INK}" stroke-width="6" stroke-linejoin="round"/>`);
  }

  /* viso */
  const ey=headCy-6, ex=30, my=headCy+42;
  if(o.face==='angry'){
    S.push(line(-ex-17,ey-26,-ex+13,ey-14,9));
    S.push(line( ex-13,ey-14, ex+17,ey-26,9));
  }
  S.push(`<circle cx="${-ex}" cy="${ey}" r="7" fill="${INK}"/>`);
  S.push(`<circle cx="${ex}" cy="${ey}" r="7" fill="${INK}"/>`);
  if(o.glasses){
    S.push(circ(-ex,ey,25,"none",6));
    S.push(circ( ex,ey,25,"none",6));
    S.push(line(-ex+25,ey,ex-25,ey,6));
  }
  if(o.face==='talk')        S.push(`<ellipse cx="0" cy="${my}" rx="23" ry="19" fill="#c0392b" stroke="${INK}" stroke-width="6"/>`);
  else if(o.face==='worried')S.push(path(`M -27 ${my+9} Q 0 ${my-15} 27 ${my+9}`,"none",7));
  else if(o.face==='angry')  S.push(path(`M -27 ${my+7} Q 0 ${my-11} 27 ${my+7}`,"none",7));
  else if(o.face==='smile'||o.face==='calm') S.push(path(`M -31 ${my-7} Q 0 ${my+29} 31 ${my-7}`,"none",7));
  else if(o.face==='flat')   S.push(line(-24,my+4,24,my+4,7));
  else                       S.push(path(`M -22 ${my} Q 0 ${my+13} 22 ${my}`,"none",7));

  if(o.face!=='angry'){
    const by=ey-30, lift=(o.face==='worried')?-11:0, drop=(o.face==='worried')?9:0;
    S.push(line(-ex-17,by+drop,-ex+14,by+lift,8));
    S.push(line( ex-14,by+lift, ex+17,by+drop,8));
  }
  if(o.sweat){
    S.push(`<path d="M ${HR+16} ${headCy-40} q 15 21 0 35 q -15 -14 0 -35 Z" fill="#7ec8f0" stroke="${INK}" stroke-width="3"/>`);
    S.push(`<path d="M ${HR+34} ${headCy+18} q 11 15 0 25 q -11 -10 0 -25 Z" fill="#7ec8f0" stroke="${INK}" stroke-width="3"/>`);
  }

  return `<g transform="translate(${o.cx},0) scale(${o.sc})" data-fig="${o.name}">${S.join("")}</g>`;
}

export function stageFig(inner: string, baseY: number): string {
  return `<svg class="fig" viewBox="0 0 ${W} ${H}"><g transform="translate(0,${baseY})">${inner}</g></svg>`;
}

export const POSE: Record<string, any> = {
  down:      {larm:[-122,212], rarm:[122,212]},
  shrug:     {larm:[-178,-16], rarm:[178,-16], lhand:'open', rhand:'open'},
  handsUp:   {larm:[-152,-152], rarm:[152,-152], lhand:'open', rhand:'open'},
  surrender: {larm:[-158,-126], rarm:[158,-126], lhand:'open', rhand:'open'},
};
