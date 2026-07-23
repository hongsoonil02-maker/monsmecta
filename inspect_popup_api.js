import puppeteer from 'puppeteer';

async function inspectPopupApi() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  page.on('request', req => {
    if (req.url().includes('selectPopupList')) {
      console.log(`[API REQ]: ${req.method()} ${req.url()}`);
      console.log(`[API REQ HEADERS]:`, req.headers());
      console.log(`[API REQ POST DATA]:`, req.postData());
    }
  });
  
  page.on('response', async res => {
    if (res.url().includes('selectPopupList')) {
      console.log(`[API RES STATUS]: ${res.status()}`);
      try {
        const json = await res.json();
        console.log(`[API RES JSON]:\n`, JSON.stringify(json, null, 2).slice(0, 2000));
      } catch(e) {
        const text = await res.text();
        console.log(`[API RES TEXT]:\n`, text.slice(0, 1000));
      }
    }
  });
  
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('#mainHeaderSearch');
  await page.type('#mainHeaderSearch', '강원특별자치도 강릉시 강릉대로 337-5');
  await page.click('.searchButton');
  
  await new Promise(r => setTimeout(r, 4000));
  await browser.close();
}

inspectPopupApi();
