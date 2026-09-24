// True side-scroll check: measures element rects, excluding the intentionally clipped marquee and hero media.
const puppeteer = require('C:/Users/George/Zonkel-Media/node_modules/puppeteer-core');
const path = require('path');
const url = 'file:///' + path.resolve(__dirname, '..', 'index.html').split(path.sep).join('/');
(async () => {
  const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });
  for (const [name, vp] of [['desktop', { width: 1440, height: 900 }], ['mobile', { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }], ['small', { width: 360, height: 740, deviceScaleFactor: 2, isMobile: true, hasTouch: true }]]) {
    const page = await browser.newPage(); await page.setViewport(vp);
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
    const r = await page.evaluate(() => {
      const cw = document.documentElement.clientWidth;
      const off = [...document.querySelectorAll('body *')].filter(e => !e.closest('.marq') && !e.closest('.hero__media') && !e.closest('.mnav') && e.getBoundingClientRect().right > cw + 1).slice(0, 10).map(e => e.tagName + '.' + [...e.classList].join('.') + ' r=' + Math.round(e.getBoundingClientRect().right));
      return { cw, sw: document.scrollingElement.scrollWidth, off };
    });
    console.log(name, JSON.stringify(r));
    await page.close();
  }
  await browser.close();
})();
