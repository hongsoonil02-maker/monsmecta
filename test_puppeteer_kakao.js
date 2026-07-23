import puppeteer from 'puppeteer';

async function testKakao(address) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://postcode.map.kakao.com/search', { waitUntil: 'networkidle2' });
  
  // Type address into region_name
  await page.type('#region_name', address);
  
  // Click search button or submit form
  await Promise.all([
    page.click('.btn_search'),
    page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 5000 }).catch(() => {})
  ]);
  
  // Wait a moment for dynamic rendering
  await new Promise(r => setTimeout(r, 1000));
  
  // Extract text or inspect structure of results
  const text = await page.evaluate(() => document.body.innerText);
  console.log('Result text:\n', text.slice(0, 1000));
  
  // Check for 5-digit numbers
  const zips = text.match(/\b[0-6]\d{4}\b/g) || [];
  console.log('Zips found:', Array.from(new Set(zips)));
  
  await browser.close();
}

testKakao('강원특별자치도 강릉시 강릉대로 337-5');
