import puppeteer from 'puppeteer';

async function inspectAllApi() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  page.on('request', req => {
    if (req.url().includes('/api/')) {
      console.log(`[REQ]: ${req.method()} ${req.url()} | BODY: ${req.postData()}`);
    }
  });
  
  page.on('response', async res => {
    if (res.url().includes('/api/')) {
      console.log(`[RES]: ${res.status()} ${res.url()}`);
      try {
        const text = await res.text();
        if (text.length > 5 && !text.includes('mergeUserCountLog')) {
          console.log(`[RES TEXT (${res.url()})]:\n`, text.slice(0, 1000));
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

inspectAllApi();
