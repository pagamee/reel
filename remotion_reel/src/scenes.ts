/* eslint-disable */
import { person, stageFig, POSE } from "./figure";

export type Anim = "rise" | "pop" | "none";

export type El =
  | { kind: "txt"; cls: string; style: string; lines: string[]; anim: Anim; delay: number }
  | { kind: "bubble"; x: number; y: number; w: number; tip: [number, number]; lines: string[]; fs: number; anim: Anim; delay: number }
  | { kind: "stack"; style: string; rowsHtml: string; anim: Anim; delay: number };

export type SceneDef = { id: string; figure: string; els: El[] };

const txt = (cls: string, style: string, lines: string[], o: { anim?: Anim; delay?: number } = {}): El =>
  ({ kind: "txt", cls, style, lines, anim: o.anim ?? "rise", delay: o.delay ?? 0 });

const bubble = (o: { x: number; y: number; w: number; tip: [number, number]; lines: string[]; fs?: number; anim?: Anim; delay?: number }): El =>
  ({ kind: "bubble", x: o.x, y: o.y, w: o.w, tip: o.tip, lines: o.lines, fs: o.fs ?? 50, anim: o.anim ?? "pop", delay: o.delay ?? 0 });

const stack = (style: string, rowsHtml: string, o: { anim?: Anim; delay?: number } = {}): El =>
  ({ kind: "stack", style, rowsHtml, anim: o.anim ?? "pop", delay: o.delay ?? 0.25 });

export const SCENES: SceneDef[] = [
  {
    id: "s1_hook",
    figure: stageFig(person(Object.assign({ cx: 540, sc: 1.04, hair: "short", shirt: "check", face: "worried", name: "worker" }, POSE.shrug)), 1520),
    els: [
      txt("txt headline", "top:132px", ["Ti hanno pagato", 'una parte <span class="red">IN NERO</span>?']),
      txt("txt", "top:398px;font-size:210px;line-height:1;color:#e5342b;font-weight:700", ["?"], { anim: "pop", delay: 0.3 }),
      txt("txt caption", "top:1608px", ["Ecco cosa rischia <b>davvero</b>", "il tuo datore di lavoro"], { delay: 0.45 }),
    ],
  },
  {
    id: "s2_setup",
    figure: stageFig(person({ cx: 540, sc: 1.08, hair: "short", shirt: "check", face: "flat", larm: [-168, 150], rarm: [168, 132], hold: "paper", name: "worker" }), 1575),
    els: [
      txt("txt headline small", "top:126px", ["TFR calcolato solo", 'sulla <span class="blue">busta paga</span>']),
      txt("txt", "top:382px;font-size:94px;font-weight:700;line-height:1.14", ['ma <span class="green">600<span class="eur">€</span>/mese</span> in contanti', '<span style="font-size:0.66em">per <b>2 anni</b>, fuori busta</span>'], { anim: "pop", delay: 0.3 }),
      txt("txt caption", "top:1666px", ["Il TFR va calcolato su <b>tutto</b>", "quello che hai davvero preso"], { delay: 0.6 }),
    ],
  },
  {
    id: "s3_confront",
    figure: stageFig(
      person({ cx: 318, sc: 0.88, hair: "short", shirt: "check", face: "talk", larm: [-124, 205], rarm: [186, 96], name: "worker" }) +
        person(Object.assign({ cx: 770, sc: 0.88, hair: "grey", glasses: true, tie: "#5b2a86", shirt: "white", face: "flat", name: "boss" }, POSE.down)),
      1650
    ),
    els: [
      txt("txt headline small", "top:112px", ["Marco affronta il capo"]),
      bubble({ x: 60, y: 650, w: 700, tip: [318, 1056], fs: 48, lines: ["«Il TFR l'hai calcolato", "solo sulla parte ufficiale.»"] }),
    ],
  },
  {
    id: "s4_deny",
    figure: stageFig(
      person(Object.assign({ cx: 288, sc: 0.88, hair: "short", shirt: "check", face: "flat", name: "worker" }, POSE.down)) +
        person(Object.assign({ cx: 770, sc: 0.88, hair: "grey", glasses: true, tie: "#5b2a86", shirt: "white", face: "worried", name: "boss" }, POSE.handsUp)),
      1650
    ),
    els: [
      txt("txt headline small", "top:112px", ['Il datore <span class="red">nega</span> tutto']),
      bubble({ x: 318, y: 640, w: 700, tip: [770, 1054], fs: 48, lines: ["«Non so di cosa parli,", "ho sempre pagato tutto!»"] }),
    ],
  },
  {
    id: "s5_proof",
    figure: stageFig(person({ cx: 540, sc: 1.08, hair: "short", shirt: "check", face: "calm", larm: [-160, 200], rarm: [164, 120], hold: "phone", name: "worker" }), 1545),
    els: [
      txt("txt", "top:150px;font-size:128px;line-height:1.06;font-weight:700", ['HO LE <span class="green">PROVE</span>'], { anim: "pop" }),
      txt("txt caption", "top:1592px;font-size:54px", ["messaggi · testimoni", "movimenti di cassa"], { delay: 0.35 }),
    ],
  },
  {
    id: "s6_threat",
    figure: stageFig(
      person({ cx: 308, sc: 0.92, hair: "short", shirt: "check", face: "angry", larm: [-124, 205], rarm: [196, 64], rhand: "point", name: "worker" }) +
        person({ cx: 818, sc: 0.76, hair: "grey", glasses: true, tie: "#5b2a86", shirt: "white", face: "worried", sweat: true, larm: [-150, 118], rarm: [150, 118], name: "boss" }),
      1690
    ),
    els: [
      txt("txt headline small", "top:104px", ["«Altrimenti mi rivolgo a…»"]),
      stack(
        "top:378px",
        `<div class="row" data-fit="950" style="font-size:86px"><span class="ln"><span class="red">ISPETTORATO</span></span></div>
         <div class="row" data-fit="950" style="font-size:86px"><span class="ln"><span class="red">DEL LAVORO</span></span></div>
         <div class="row" data-fit="950" style="font-size:68px;margin-top:26px"><span class="ln">+ <span class="blue">INPS</span></span></div>`
      ),
    ],
  },
  {
    id: "s7_risk",
    figure: stageFig(person({ cx: 540, sc: 0.92, hair: "grey", glasses: true, tie: "#5b2a86", shirt: "white", face: "worried", sweat: true, larm: [-176, -40], rarm: [176, -40], lhand: "open", rhand: "open", name: "boss" }), 1740),
    els: [
      txt("txt headline small", "top:110px", ['Il datore <span class="red">rischia grosso</span>']),
      stack(
        "top:356px",
        `<div class="row" data-fit="950" style="font-size:80px"><span class="ln"><span class="red">MAXI-SANZIONE</span></span></div>
         <div class="row" data-fit="950" style="font-size:52px;color:#555;margin-top:2px"><span class="ln">per lavoro nero</span></div>
         <div class="row" data-fit="950" style="font-size:62px;margin-top:30px"><span class="ln">contributi arretrati</span></div>
         <div class="row" data-fit="950" style="font-size:62px"><span class="ln">+ interessi</span></div>`
      ),
    ],
  },
  {
    id: "s8_cede",
    figure: stageFig(
      person({ cx: 288, sc: 0.88, hair: "short", shirt: "check", face: "calm", larm: [-124, 205], rarm: [124, 205], name: "worker" }) +
        person({ cx: 772, sc: 0.88, hair: "grey", glasses: true, tie: "#5b2a86", shirt: "white", face: "worried", larm: [-118, 206], rarm: [150, -104], rhand: "open", name: "boss" }),
      1660
    ),
    els: [
      txt("txt headline small", "top:112px", ['E <span class="green">cede</span> subito']),
      bubble({ x: 336, y: 662, w: 690, tip: [772, 1066], fs: 50, lines: ["«Aspetta…", "troviamo un accordo.»"] }),
    ],
  },
  {
    id: "s9_lesson",
    figure: stageFig(person({ cx: 540, sc: 1.08, hair: "bob", shirt: "blazer", face: "calm", larm: [-158, 176], rarm: [168, 142], name: "lawyer" }), 1610),
    els: [
      txt("txt headline small", "top:128px", ['Il <span class="red">nero</span> non conviene']),
      txt("txt", "top:330px;font-size:52px;line-height:1.28;color:#555", ["Non fa risparmiare:", "espone a rischi enormi"], { delay: 0.3 }),
      txt("txt", "top:1658px;font-size:58px;line-height:1.26", ["I tuoi diritti valgono.", "<b>Sempre.</b>"], { delay: 0.55 }),
    ],
  },
  {
    id: "s10_cta",
    figure: stageFig(person({ cx: 540, sc: 0.88, hair: "bob", shirt: "blazer", face: "smile", larm: [-150, 190], rarm: [178, -128], rhand: "open", name: "lawyer" }), 1620),
    els: [
      txt("txt", "top:298px;font-size:104px;line-height:1.12;font-weight:700", ["Hai un caso", "simile?"], { anim: "pop" }),
      txt("txt", "top:564px;font-size:60px;color:#333", ["Parlane con noi"], { delay: 0.35 }),
      txt("txt wordmark", "top:1672px;color:#e5342b", ["Pagamee"], { delay: 0.6 }),
    ],
  },
];
