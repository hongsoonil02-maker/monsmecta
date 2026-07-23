import puppeteer from 'puppeteer';

async function testVueSearch() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('#mainHeaderSearch');
  
  const query = '강원특별자치도 강릉시 강릉대로 337-5';
  console.log('Setting value with Vue dispatchEvents for:', query);
  await page.evaluate((q) => {
    const input = document.querySelector('#mainHeaderSearch');
    input.value = q;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
  }, query);
  
  await new Promise(r => setTimeout(r, 500));
  
  console.log('Clicking .searchButton...');
  await page.click('.searchButton');
  
  // Wait for results container or navigation
  await new Promise(r => setTimeout(r, 3000));
  console.log('URL after click:', page.url());
  
  const info = await page.evaluate(() => {
    return {
      title: document.title,
      text: document.body.innerText.slice(0, 1500),
      zips: document.body.innerText.match(/\b[0-6]\d{4}\b/g) || []
    };
  });
  
  console.log('Info after search:', JSON.stringify(info, null, 2));
  await browser.close();
}

testVueSearch();
