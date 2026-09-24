// Desktop + mobile QA screenshots, plus the 1200x630 share card render (research/og.html -> assets/img/og.jpg).
const puppeteer = require('C:/Users/George/Zonkel-Media/node_modules/puppeteer-core');
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'research', 'shots');
fs.mkdirSync(OUT, { recursive: true });
const url = 'file:///' + path.join(ROOT, 'index.html').replace(/\\/g, '/');
const ogUrl = 'file:///' + path.join(ROOT, 'research', 'og.html').replace(/\\/g, '/');
const onlyOg = process.argv.includes('--og');

(async () => {
  const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });
  if (!onlyOg) {
    for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }]]) {
      const page = await browser.newPage();
      await page.setViewport(vp);
      page.on('pageerror', e => console.log(name, 'PAGE ERROR:', e.message));
      await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
      console.log(name, 'marquee cards:', await page.evaluate(() => document.querySelectorAll('#marq .rc').length));
      await page.evaluate(() => document.querySelectorAll('.rv').forEach(e => e.classList.add('in')));
      await new Promise(r => setTimeout(r, 1200));
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      const sw = await page.evaluate(() => Math.max(...[...document.querySelectorAll('body *')].map(e => e.getBoundingClientRect().right)));
      console.log(name, 'height', h, 'maxRight', Math.round(sw), 'viewport', vp.width, sw > vp.width + 1 ? '  <-- SIDE SCROLL' : '');
      // hero CTA position vs fold
      const cta = await page.evaluate(() => { const b = document.querySelector('.hero__cta'); const r = b.getBoundingClientRect(); return { top: Math.round(r.top), bottom: Math.round(r.bottom), vh: innerHeight }; });
      console.log(name, 'hero CTA', JSON.stringify(cta));
      await page.screenshot({ path: path.join(OUT, name + '-fold.png') });
      let y = 0, i = 0;
      while (y < h && i < 14) {
        await page.evaluate(yy => window.scrollTo(0, yy), y);
        await new Promise(r => setTimeout(r, 350));
        await page.screenshot({ path: path.join(OUT, `${name}-${String(i).padStart(2, '0')}.png`) });
        y += vp.height; i++;
      }
      const wide = await page.evaluate(() => [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1).slice(0, 8).map(e => e.tagName + '.' + [...e.classList].join('.')));
      if (wide.length) console.log(name, 'overflow:', wide);
      await page.close();
    }
  }
  // share card
  const og = await browser.newPage();
  await og.setViewport({ width: 1200, height: 630, deviceScaleFactor: 2 });
  await og.goto(ogUrl, { waitUntil: 'networkidle0', timeout: 60000 });
  await og.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 800));
  await og.screenshot({ path: path.join(ROOT, 'research', 'og-2x.png') });
  await og.close();
  await browser.close();
  console.log('done');
})();
