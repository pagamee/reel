import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { spawn, execFileSync } from 'node:child_process';

/* Uso:
 *   node render.mjs check          controlli di layout su tutte le scene
 *   node render.mjs preview        un PNG per battuta (testo completo) + provino in preview/sheet.png
 *   node render.mjs full [fps]     video finale in out/reel.mp4
 *   node render.mjs still <t>      un fotogramma all'istante t (secondi) in out/still.png
 */
const mode = process.argv[2] || 'preview';
const tl   = JSON.parse(fs.readFileSync('timeline.json', 'utf8'));
const fileUrl = 'file://' + path.join(process.cwd(), 'reel.html');

const browser = await chromium.launch({
  executablePath: process.env.CHROME_BIN || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--force-color-profile=srgb', '--font-render-hinting=none'],
});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', e => errors.push(e.message));
await page.goto(fileUrl);
await page.waitForFunction(() => window.__READY__ === true, { timeout: 15000 });
await page.evaluate(async () => { await document.fonts.ready; });
await page.evaluate(() => window.renderFrame(0));
if (errors.length) { console.error('Errori JS:\n  ' + errors.join('\n  ')); process.exit(1); }

if (mode === 'check') {
  const report = await page.evaluate(() => {
    const out = [];
    for (const sg of window.segments()) {
      const errs = [];
      window.settle(sg.id);
      const root = document.getElementById(sg.id);
      const art = root.querySelector('.cam').getBoundingClientRect();
      let capBottom = 0;
      for (const b of sg.beats) {
        window.showCaption(sg.id, b);
        const el = document.getElementById('cap-' + b);
        const r = el.getBoundingClientRect();
        const lh = parseFloat(getComputedStyle(el).lineHeight);
        const lines = Math.round(r.height / lh);
        capBottom = Math.max(capBottom, r.bottom);
        if (lines > 4) errs.push(`${b}: didascalia su ${lines} righe (max 4)`);
        if (r.bottom > 590) errs.push(`${b}: didascalia troppo lunga, finisce a y=${Math.round(r.bottom)}`);
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (fs < 56) errs.push(`${b}: font ridotto a ${fs}px, testo troppo lungo`);
      }
      const tag = root.querySelector('#tag-parte');
      if (tag) capBottom = Math.max(capBottom, tag.getBoundingClientRect().bottom);
      if (art.left < 8 || art.right > 1072) errs.push(`disegno fuori dai bordi laterali [${Math.round(art.left)} → ${Math.round(art.right)}]`);
      if (art.bottom > 1905) errs.push(`disegno oltre il fondo (y=${Math.round(art.bottom)})`);
      if (art.top < capBottom + 12) errs.push(`disegno sotto il testo: parte a y=${Math.round(art.top)}, il testo finisce a ${Math.round(capBottom)}`);
      out.push({ id: sg.id, errs, art: [Math.round(art.left), Math.round(art.top), Math.round(art.right), Math.round(art.bottom)] });
    }
    return out;
  });
  let bad = 0;
  for (const s of report) {
    if (s.errs.length) bad++;
    console.log(`${s.errs.length ? ' FAIL ' : '  OK  '} ${s.id.padEnd(24)} disegno ${s.art.join(',')}`);
    s.errs.forEach(e => console.log('         - ' + e));
  }
  console.log(bad ? `\n${bad} scene da sistemare.` : `\nTutte le ${report.length} scene passano i controlli.`);
  await browser.close();
  process.exit(bad ? 1 : 0);
}

if (mode === 'preview') {
  fs.mkdirSync('preview', { recursive: true });
  for (const f of fs.readdirSync('preview')) fs.unlinkSync(path.join('preview', f));
  let i = 0;
  for (const b of tl.beats) {
    await page.evaluate(t => window.renderFrame(t), b.end - 0.04);
    await page.screenshot({ path: `preview/${String(i).padStart(2, '0')}_${b.id}_${b.visual}.png` });
    i++;
  }
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-pattern_type', 'glob', '-i', 'preview/[0-9]*.png',
    '-vf', 'scale=270:-1,pad=iw+6:ih+6:3:3:color=0x888888,tile=7x4', '-frames:v', '1', 'preview/sheet.png']);
  console.log('preview: ' + i + ' fotogrammi + preview/sheet.png');
} else if (mode === 'cover') {
  fs.mkdirSync('out', { recursive: true });
  const info = await page.evaluate(() => window.renderCover());
  await page.screenshot({ path: 'out/cover.png' });
  // come appare nella griglia del profilo (3:4) e nel feed (4:5)
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', 'out/cover.png', '-vf', 'crop=1080:1440:0:240', 'out/cover_griglia_3x4.png']);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', 'out/cover.png', '-vf', 'crop=1080:1350:0:285', 'out/cover_feed_4x5.png']);
  console.log('out/cover.png (+ ritagli 3:4 e 4:5)', JSON.stringify(info));
} else if (mode === 'still') {
  fs.mkdirSync('out', { recursive: true });
  await page.evaluate(t => window.renderFrame(t), parseFloat(process.argv[3] || '1'));
  await page.screenshot({ path: 'out/still.png' });
  console.log('out/still.png');
} else if (mode === 'full') {
  const fps = parseInt(process.argv[3] || '30', 10);
  fs.mkdirSync('out', { recursive: true });
  const n = Math.ceil(tl.total * fps);
  const ff = spawn('ffmpeg', [
    '-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(fps), '-i', 'pipe:0',
    '-i', 'audio/final.wav',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-pix_fmt', 'yuv420p', '-r', String(fps),
    '-c:a', 'aac', '-b:a', '192k', '-ac', '2', '-ar', '44100',
    '-movflags', '+faststart', '-shortest', 'out/reel.mp4',
  ], { stdio: ['pipe', 'inherit', 'inherit'] });
  const write = buf => new Promise((res, rej) => {
    if (ff.stdin.write(buf)) return res();
    ff.stdin.once('drain', res); ff.stdin.once('error', rej);
  });
  for (let f = 0; f < n; f++) {
    await page.evaluate(t => window.renderFrame(t), f / fps);
    await write(await page.screenshot({ type: 'png' }));
    if (f % 300 === 0) console.log(`frame ${f}/${n}  (${(f / fps).toFixed(1)}s)`);
  }
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r));
  if (code !== 0) { await browser.close(); throw new Error('ffmpeg uscito con codice ' + code); }
  console.log(`video pronto: out/reel.mp4  (${n} fotogrammi @ ${fps} fps)`);
}
if (errors.length) { console.error('Errori JS:\n  ' + errors.join('\n  ')); process.exitCode = 1; }
await browser.close();
