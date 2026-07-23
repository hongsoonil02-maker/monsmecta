import puppeteer from 'puppeteer';

async function testFast() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Navigating to Kakao search...');
  await page.goto('https://postcode.map.kakao.com/search', { waitUntil: 'domcontentloaded' });
  await page.waitForSelector('#region_name');
  
  const query = '강원특별자치도 강릉시 강릉대로 337-5';
  await page.type('#region_name', query);
  await page.click('.btn_search');
  
  // Wait for results
  await page.waitForSelector('.link_post', { timeout: 5000 }).catch(e => console.log('Timeout waiting for .link_post'));
  
  const text = await page.evaluate(() => document.body.innerText);
  console.log('Result text:\n', text.slice(0, 1000));
  
  await browser.close();
}

testFast();
