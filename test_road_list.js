import puppeteer from 'puppeteer';

async function testRoad() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  console.log('Navigating to ahuRoadNameDataList...');
  await page.goto('https://www.juso.go.kr/ahu/ahuRoadNameDataList', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  
  const forms = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('input, select, button')).map(i => ({
      tag: i.tagName,
      id: i.id,
      name: i.name,
      placeholder: i.placeholder,
      text: i.innerText ? i.innerText.trim() : i.value
    }));
  });
  console.log('Elements on ahuRoadNameDataList:\n', JSON.stringify(forms, null, 2));
  
  await browser.close();
}

testRoad();
