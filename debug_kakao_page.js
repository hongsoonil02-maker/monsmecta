import puppeteer from 'puppeteer';

async function debugKakao() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://postcode.map.kakao.com/search', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  
  const html = await page.evaluate(() => document.documentElement.innerHTML);
  console.log('HTML length:', html.length);
  console.log('HTML snippet:\n', html.slice(0, 1500));
  
  await browser.close();
}

debugKakao();
