import puppeteer from 'puppeteer';

async function inspectNet() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  page.on('request', req => {
    const url = req.url();
    if (!url.endsWith('.png') && !url.endsWith('.jpg') && !url.endsWith('.css') && !url.endsWith('.js') && !url.endsWith('.woff2')) {
      console.log(`[REQ]: ${req.method()} ${url}`);
    }
  });
  
  page.on('response', async res => {
    const url = res.url();
    if (!url.endsWith('.png') && !url.endsWith('.jpg') && !url.endsWith('.css') && !url.endsWith('.js') && !url.endsWith('.woff2')) {
      console.log(`[RES]: ${res.status()} ${url}`);
      try {
        const text = await res.text();
        if (text.includes('25492') || text.includes('강릉대로')) {
          console.log(`[RES BODY MATCH in ${url}]:\n`, text.slice(0, 500));
        }
      } catch(e) {}
    }
  });
  
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('#mainHeaderSearch');
  
  await page.type('#mainHeaderSearch', '강원특별자치도 강릉시 강릉대로 337-5');
  await page.click('.searchButton');
  
  await new Promise(r => setTimeout(r, 4000));
  await browser.close();
}

inspectNet();
