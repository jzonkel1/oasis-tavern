// node research/shot-one.cjs <html file> <out png> [width] [height]
const puppeteer = require('C:/Users/George/Zonkel-Media/node_modules/puppeteer-core');
const path = require('path');
const [,, file, out, w = '1440', h = '900'] = process.argv;
const url = 'file:///' + path.resolve(file).split(path.sep).join('/');
(async () => {
  const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: +w, height: +h });
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: out, fullPage: true });
  await browser.close();
  console.log('wrote', out);
})();
