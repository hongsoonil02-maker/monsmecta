import puppeteer from 'puppeteer';

async function testKarb() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  console.log('Navigating to ahuKarbSbdList...');
  await page.goto('https://www.juso.go.kr/ahu/ahuKarbSbdList', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  
  const forms = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('input')).map(i => ({ id: i.id, name: i.name, placeholder: i.placeholder, type: i.type }));
  });
  console.log('Inputs on ahuKarbSbdList:\n', forms);
  
  // Find a text input and type
  const textInput = forms.find(f => f.type === 'text');
  if (textInput && textInput.id) {
    console.log('Typing into:', textInput.id);
    await page.type('#' + textInput.id, '강릉대로 337-5');
    await page.keyboard.press('Enter');
    
    // Also try clicking search button
    const btn = await page.$('.searchButton, button[type="submit"], .btn_search');
    if (btn) await btn.click();
    
    await new Promise(r => setTimeout(r, 3000));
    const text = await page.evaluate(() => document.body.innerText);
    console.log('Page after search:\n', text.slice(0, 1500));
  }
  
  await browser.close();
}

testKarb();
