import puppeteer from 'puppeteer';

async function findSearch() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  console.log('Navigating to juso.go.kr main page...');
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  
  // Inspect forms and inputs on the home page
  const forms = await page.evaluate(() => {
    const inputs = Array.from(document.querySelectorAll('input')).map(i => ({
      id: i.id,
      name: i.name,
      placeholder: i.placeholder,
      type: i.type
    }));
    const formList = Array.from(document.querySelectorAll('form')).map(f => ({
      id: f.id,
      action: f.action,
      method: f.method
    }));
    return { inputs, formList };
  });
  
  console.log('Forms & Inputs on juso.go.kr:\n', JSON.stringify(forms, null, 2));
  await browser.close();
}

findSearch();
