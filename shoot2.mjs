import { chromium } from 'playwright';
import fs from 'fs';
const out = process.argv[2]; const which = process.argv[3] || 'stills';
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
page.on('pageerror', e => console.log('err:', e.message));
await page.goto('http://localhost:8765/index.html');
await page.waitForFunction(() => window.ready === true, null, { timeout: 60000 });
const V = JSON.parse(fs.readFileSync(new URL('./views.json', import.meta.url)));
async function shot(v, file, dt = .15) {
  await page.evaluate(v => { setUI(v.ui !== false); setMode(v.mode || 'proposal'); setStep(v.s || 0); showPins(!v.nopins); setCam(v.p, v.t); if (v.nocard) hideCard(); draw(v.dt || .15); }, { ...v, dt });
  await page.screenshot({ path: file });
}
if (which === 'stills') {
  for (const [name, v] of Object.entries(V.stills)) { await shot(v, `${out}/${name}.png`); console.log('shot', name); }
}
if (which === 'clip') {
  const lerp = (a, b, t) => a.map((x, i) => x + (b[i] - x) * t);
  const ease = t => t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  let k = 0; const f = () => `${out}/frames/f${String(k++).padStart(3, '0')}.png`;
  for (const seg of V.clip) {
    if (seg.hold) { for (let i = 0; i < seg.hold; i++) await shot(seg, f(), .35); continue; }
    const a = V.stills[seg.from], b = V.stills[seg.to];
    for (let i = 0; i < seg.n; i++) { const t = ease(i / seg.n);
      await shot({ p: lerp(a.p, b.p, t), t: lerp(a.t, b.t, t), mode: seg.mode, s: i < seg.n / 2 ? a.s : b.s }, f(), .35); }
  }
  console.log('frames', k);
}
await browser.close();
