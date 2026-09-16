import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const mode = process.argv[2] || 'preview';     // 'preview' | 'check' | 'full'
const fps  = parseInt(process.argv[3] || '30', 10);
const cwd  = process.cwd();
const tl   = JSON.parse(fs.readFileSync('timeline.json','utf8'));
const fileUrl = 'file://' + path.join(cwd, 'reel.html');

const browser = await chromium.launch({
  executablePath: process.env.CHROME_BIN || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox','--force-color-profile=srgb','--font-render-hinting=none']
});
const page = await browser.newPage({ viewport:{width:1080,height:1920}, deviceScaleFactor:1 });
await page.goto(fileUrl);
await page.waitForFunction(() => window.__READY__ === true, { timeout: 15000 });
await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });

if (mode === 'check') {
  /* Controllo layout automatico: fuori schermo, sovrapposizioni, a-capo indesiderati. */
  const report = await page.evaluate((scenes) => {
    const SAFE = {x0:30, y0:30, x1:1050, y1:1884};
    const out = [];
    const inter = (a,b,pad=0) =>
      !(a.right-pad <= b.left || b.right <= a.left+pad ||
        a.bottom-pad <= b.top || b.bottom <= a.top+pad);

    for (const sc of scenes) {
      window.settle(sc.id);
      const root = document.getElementById('scene-'+sc.id);
      const errs = [], info = [];

      const heads = [...root.querySelectorAll('[data-head]')].map(h=>h.getBoundingClientRect());
      const figs  = [...root.querySelectorAll('[data-fig]')].map(g=>({
        name:g.getAttribute('data-fig'), r:g.getBoundingClientRect()}));
      const blocks = [...root.querySelectorAll('.txt, .bubble, .stack .row')];

      // unione dei rettangoli di testo = ingombro reale dell'inchiostro
      // (il box di .txt è largo quanto lo schermo: misurarlo darebbe falsi positivi)
      const inkBox = (el) => {
        let L=1e9,T=1e9,R=-1e9,B=-1e9;
        const mids=[];
        const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        let n;
        while ((n = walk.nextNode())) {
          if (!n.nodeValue.trim()) continue;
          const rg = document.createRange(); rg.selectNodeContents(n);
          for (const cr of rg.getClientRects()) {
            if (cr.width < 1) continue;
            L=Math.min(L,cr.left); T=Math.min(T,cr.top);
            R=Math.max(R,cr.right); B=Math.max(B,cr.bottom);
            mids.push((cr.top+cr.bottom)/2);
          }
        }
        if (R < L) { const r = el.getBoundingClientRect(); return {rect:r, lines:1}; }
        // Raggruppa i frammenti per riga. Font diversi sulla stessa riga (es. il
        // simbolo € preso da Comic Neue) hanno metriche diverse: senza tolleranza
        // verrebbero contati come righe separate.
        const lh = parseFloat(getComputedStyle(el).lineHeight) ||
                   parseFloat(getComputedStyle(el).fontSize)*1.2;
        const tol = lh*0.55;
        mids.sort((a,b)=>a-b);
        let lines=1;
        for (let i=1;i<mids.length;i++) if (mids[i]-mids[i-1] > tol) lines++;
        return {rect:{left:L,top:T,right:R,bottom:B,width:R-L,height:B-T}, lines};
      };

      for (const el of blocks) {
        const isBubble = el.classList.contains('bubble');
        const ink = inkBox(el);
        // per il fumetto conta il riquadro disegnato, non solo il testo
        const r = isBubble ? el.getBoundingClientRect() : ink.rect;
        const label = (el.textContent||'').trim().replace(/\s+/g,' ').slice(0,42);

        if (r.left < SAFE.x0 || r.right > SAFE.x1 || r.top < SAFE.y0 || r.bottom > SAFE.y1)
          errs.push(`FUORI SCHERMO  "${label}"  [${Math.round(r.left)},${Math.round(r.top)} → ${Math.round(r.right)},${Math.round(r.bottom)}]`);

        heads.forEach((h,i) => {
          if (inter(r,h,4)) errs.push(`TESTO SU TESTA #${i}  "${label}"`);
        });

        // conteggio righe reali vs righe volute (<br> + 1)
        const wanted = (el.innerHTML.match(/<br\s*\/?>/gi)||[]).length + 1;
        const got = ink.lines;
        if (got > wanted) errs.push(`A CAPO IMPREVISTO  "${label}"  righe ${got} invece di ${wanted}`);
        // testo che sborda dal fumetto
        if (isBubble) {
          const pad = 30;
          if (ink.rect.left < r.left+pad-6 || ink.rect.right > r.right-pad+6)
            errs.push(`TESTO FUORI DAL FUMETTO  "${label}"`);
        }
      }

      // personaggi che si accavallano
      for (let i=0;i<figs.length;i++) for (let j=i+1;j<figs.length;j++)
        if (inter(figs[i].r, figs[j].r, 0))
          errs.push(`PERSONAGGI SOVRAPPOSTI  ${figs[i].name} ↔ ${figs[j].name}`);

      // la codina del fumetto deve puntare alla testa di chi parla
      for (const b of root.querySelectorAll('[data-bubble]')) {
        const t = b.querySelector('[data-tail] path');
        const tr = t.getBoundingClientRect();
        const tip = {x:(tr.left+tr.right)/2, y:tr.bottom};
        let best = 1e9, which = -1;
        heads.forEach((h,i)=>{
          const cx=(h.left+h.right)/2, cy=(h.top+h.bottom)/2;
          const d = Math.hypot(tip.x-cx, tip.y-cy) - (h.width/2);
          if (d < best) { best = d; which = i; }
        });
        info.push(`codina → testa #${which}, distanza ${Math.round(best)}px`);
        if (best > 90) errs.push(`CODINA LONTANA dalla testa: ${Math.round(best)}px`);
        if (best < 0)   errs.push(`CODINA SOPRA la testa`);
      }

      out.push({id: sc.id, errs, info});
    }
    return out;
  }, tl.scenes);

  let bad = 0;
  for (const s of report) {
    const ok = s.errs.length === 0;
    if (!ok) bad++;
    console.log(`${ok ? '  OK  ' : ' FAIL '} ${s.id}` + (s.info.length ? `   (${s.info.join('; ')})` : ''));
    s.errs.forEach(e => console.log(`         - ${e}`));
  }
  console.log(bad ? `\n${bad} scene da sistemare.` : `\nTutte le ${report.length} scene passano i controlli di layout.`);
  await browser.close();
  process.exit(bad ? 1 : 0);
}

if (mode === 'preview') {
  const dir = 'preview'; fs.mkdirSync(dir,{recursive:true});
  let i=0;
  for (const s of tl.scenes) {
    const t = s.start + Math.min(1.2, s.dur*0.55);  // oltre l'animazione di entrata
    await page.evaluate((tt)=>window.renderFrame(tt), t);
    await page.waitForTimeout(30);
    await page.screenshot({ path: `${dir}/${String(i).padStart(2,'0')}_${s.id}.png` });
    i++;
  }
  console.log('preview done:', i, 'frames');
} else if (mode === 'full') {
  /* I fotogrammi vanno diretti in ffmpeg: niente migliaia di PNG su disco. */
  const { spawn } = await import('node:child_process');
  fs.mkdirSync('out', { recursive: true });
  const n = Math.ceil(tl.total * fps);
  const audio = 'audio/final.wav';
  const ff = spawn('ffmpeg', [
    '-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(fps), '-i', 'pipe:0',
    '-i', audio,
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '19',
    '-pix_fmt', 'yuv420p', '-r', String(fps),
    '-c:a', 'aac', '-b:a', '192k', '-ac', '2', '-ar', '44100',
    '-movflags', '+faststart', '-shortest',
    'out/reel.mp4'
  ], { stdio: ['pipe', 'inherit', 'inherit'] });

  const write = (buf) => new Promise((res, rej) => {
    if (ff.stdin.write(buf)) return res();
    ff.stdin.once('drain', res);
    ff.stdin.once('error', rej);
  });

  for (let f = 0; f < n; f++) {
    await page.evaluate((tt) => window.renderFrame(tt), f / fps);
    await write(await page.screenshot({ type: 'png' }));
    if (f % 150 === 0) console.log('frame', f, '/', n, '(' + (f / fps).toFixed(1) + 's)');
  }
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r));
  if (code !== 0) { await browser.close(); throw new Error('ffmpeg uscito con codice ' + code); }
  console.log('video pronto: out/reel.mp4  (' + n + ' fotogrammi @ ' + fps + ' fps)');
}
await browser.close();
