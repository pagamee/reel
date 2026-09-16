/* eslint-disable */
import React, { useLayoutEffect, useRef, useState } from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { SceneDef, El } from "./scenes";

const clamp = (v: number, a: number, b: number) => Math.max(a, Math.min(b, v));
const easeOutCubic = (x: number) => 1 - Math.pow(1 - x, 3);
const easeOutBack = (x: number) => {
  const c1 = 1.70158, c3 = c1 + 1;
  return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2);
};
const smoothIn = (lt: number, a: number, b: number) => clamp((lt - a) / (b - a), 0, 1);

function parseStyle(s: string): React.CSSProperties {
  const out: any = {};
  s.split(";").forEach((decl) => {
    const i = decl.indexOf(":");
    if (i < 0) return;
    const k = decl.slice(0, i).trim();
    const v = decl.slice(i + 1).trim();
    if (!k) return;
    const camel = k.replace(/-([a-z])/g, (_, c) => c.toUpperCase());
    out[camel] = v;
  });
  return out;
}

const linesHtml = (lines: string[]) => lines.map((l) => `<span class="ln">${l}</span>`).join("<br>");

// auto-restringimento identico a fitAll(): riduce il font finché le righe stanno in maxW
function fit(el: HTMLElement, maxW: number) {
  const lns = Array.from(el.querySelectorAll<HTMLElement>(".ln"));
  if (!lns.length) return;
  const widest = () => Math.max(...lns.map((n) => n.offsetWidth));
  let fs = parseFloat(getComputedStyle(el).fontSize);
  let guard = 0;
  while (widest() > maxW && fs > 20 && guard++ < 120) {
    fs -= 2;
    el.style.fontSize = fs + "px";
  }
}

// animazione d'entrata per-frame (pop / rise), come renderFrame() dell'originale
function animStyle(type: string, delay: number, lt: number): React.CSSProperties {
  const AD = type === "pop" ? 0.52 : 0.48;
  const p = clamp((lt - delay) / AD, 0, 1);
  if (type === "pop") {
    const e = easeOutBack(p);
    return {
      opacity: clamp(p * 1.8, 0, 1),
      transform: `translateY(${(1 - e) * 26}px) scale(${0.66 + 0.34 * e})`,
      transformOrigin: "center",
    };
  }
  if (type === "rise") {
    const e = easeOutCubic(p);
    return { opacity: p, transform: `translateY(${(1 - e) * 52}px)` };
  }
  return {};
}

const Bubble: React.FC<{ el: Extract<El, { kind: "bubble" }>; lt: number; fontsReady: boolean }> = ({ el, lt, fontsReady }) => {
  const ref = useRef<HTMLDivElement>(null);
  const [tail, setTail] = useState<{ box: React.CSSProperties; viewBox: string; d: string; patch: React.CSSProperties } | null>(null);
  const BORD = 6;

  useLayoutEffect(() => {
    const b = ref.current;
    if (!b) return;
    const inner = el.w - 2 * 38 - 2 * BORD;
    fit(b, inner);
    const [tipX, tipY] = el.tip;
    const left = b.offsetLeft, top = b.offsetTop;
    const wpx = b.offsetWidth - 2 * BORD;
    const ox = left + BORD;
    const baseY = top + b.offsetHeight - BORD;
    const hpx = Math.max(24, tipY - baseY + 12);
    const cx = clamp(tipX, ox + 86, ox + wpx - 86);
    const b1 = cx - 56 - ox, b2 = cx + 44 - ox;
    const tx = tipX - ox, ty = tipY - baseY;
    const d =
      `M ${b1} 0` +
      ` C ${b1 + (tx - b1) * 0.2} ${ty * 0.46}, ${tx - 26} ${ty * 0.78}, ${tx} ${ty}` +
      ` C ${tx + 10} ${ty * 0.7}, ${b2 + (tx - b2) * 0.42} ${ty * 0.4}, ${b2} 0 Z`;
    setTail({
      viewBox: `0 -10 ${wpx} ${hpx + 10}`,
      box: { left: 0, top: b.offsetHeight - 2 * BORD - 10, width: wpx, height: hpx + 10 },
      d,
      patch: { x: b1 + 7, y: -9, width: b2 - b1 - 14, height: 15 },
    });
  }, [fontsReady, el]);

  return (
    <div
      ref={ref}
      className="bubble"
      style={{ left: el.x, top: el.y, width: el.w, fontSize: el.fs, ...animStyle(el.anim, el.delay, lt) }}
    >
      <span dangerouslySetInnerHTML={{ __html: linesHtml(el.lines) }} />
      {tail && (
        <svg className="tailsvg" viewBox={tail.viewBox} style={{ position: "absolute", ...tail.box }}>
          <path d={tail.d} fill="#fff" stroke="#141414" strokeWidth={6} strokeLinejoin="round" />
          <rect {...(tail.patch as any)} fill="#fff" />
        </svg>
      )}
    </div>
  );
};

const TxtEl: React.FC<{ el: Extract<El, { kind: "txt" }>; lt: number; fontsReady: boolean }> = ({ el, lt, fontsReady }) => {
  const ref = useRef<HTMLDivElement>(null);
  useLayoutEffect(() => {
    if (ref.current) fit(ref.current, 950);
  }, [fontsReady, el]);
  return (
    <div
      ref={ref}
      className={el.cls}
      style={{ ...parseStyle(el.style), ...animStyle(el.anim, el.delay, lt) }}
      dangerouslySetInnerHTML={{ __html: linesHtml(el.lines) }}
    />
  );
};

const StackEl: React.FC<{ el: Extract<El, { kind: "stack" }>; lt: number; fontsReady: boolean }> = ({ el, lt, fontsReady }) => {
  const ref = useRef<HTMLDivElement>(null);
  useLayoutEffect(() => {
    if (!ref.current) return;
    ref.current.querySelectorAll<HTMLElement>(".row").forEach((row) => {
      const maxW = parseFloat(row.getAttribute("data-fit") || "950");
      fit(row, maxW);
    });
  }, [fontsReady, el]);
  return (
    <div
      ref={ref}
      className="stack"
      style={{ ...parseStyle(el.style), ...animStyle(el.anim, el.delay, lt) }}
      dangerouslySetInnerHTML={{ __html: el.rowsHtml }}
    />
  );
};

export const Scene: React.FC<{
  scene: SceneDef;
  startSec: number;
  durSec: number;
  totalSec: number;
  fontsReady: boolean;
}> = ({ scene, startSec, durSec, totalSec, fontsReady }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const lt = frame / fps; // tempo locale nella scena (la Sequence azzera il frame)
  const fin = smoothIn(lt, 0, 0.26);
  const fout = 1 - smoothIn(lt, durSec - 0.16, durSec);
  const sceneOpacity = fin * fout;
  const globalT = startSec + lt;
  const progPct = clamp((100 * globalT) / totalSec, 0, 100);

  return (
    <div className="scene" style={{ opacity: sceneOpacity }}>
      <div dangerouslySetInnerHTML={{ __html: scene.figure }} />
      {scene.els.map((el, i) => {
        if (el.kind === "txt") return <TxtEl key={i} el={el} lt={lt} fontsReady={fontsReady} />;
        if (el.kind === "bubble") return <Bubble key={i} el={el} lt={lt} fontsReady={fontsReady} />;
        return <StackEl key={i} el={el} lt={lt} fontsReady={fontsReady} />;
      })}
      <div className="prog" style={{ width: `${progPct}%` }} />
    </div>
  );
};
