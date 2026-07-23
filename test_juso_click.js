import puppeteer from 'puppeteer';

async function testClick() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('#mainHeaderSearch');
  
  const query = '강원특별자치도 강릉시 강릉대로 337-5';
  console.log('Typing:', query);
  await page.type('#mainHeaderSearch', query);
  
  console.log('Clicking .searchButton...');
  await Promise.all([
    page.click('.searchButton'),
    page.waitForNavigation({ waitUntil: 'domcontentloaded', timeout: 5000 }).catch(() => {})
  ]);
  
  await new Promise(r => setTimeout(r, 2000));
  console.log('Current URL after click:', page.url());
  
  const text = await page.evaluate(() => document.body.innerText);
  console.log('Page text snippet:\n', text.slice(0, 1000));
  
  const zips = text.match(/\b[0-6]\d{4}\b/g) || [];
  console.log('All 5-digit Zips found on page:', Array.from(new Set(zips)));
  
  await browser.close();
}

testClick();
