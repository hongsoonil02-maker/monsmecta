import puppeteer from 'puppeteer';

async function testCatch() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Opening kakao search...');
  await page.goto('https://postcode.map.kakao.com/search', { timeout: 5000, waitUntil: 'domcontentloaded' }).catch(e => console.log('Goto caught:', e.message));
  
  // Check if input exists
  const inputExists = await page.$('#region_name');
  console.log('#region_name exists?', !!inputExists);
  
  if (inputExists) {
    await page.type('#region_name', '강릉대로 337-5');
    await page.click('.btn_search');
    
    await new Promise(r => setTimeout(r, 2000));
    const text = await page.evaluate(() => document.body.innerText);
    console.log('Result text:\n', text.slice(0, 1000));
    const zips = text.match(/\b[0-6]\d{4}\b/g) || [];
    console.log('Zips found:', Array.from(new Set(zips)));
  }
  
  await browser.close();
}

testCatch();
