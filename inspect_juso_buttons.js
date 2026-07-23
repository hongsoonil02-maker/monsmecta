import puppeteer from 'puppeteer';

async function inspectButtons() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  await page.goto('https://www.juso.go.kr', { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 2000));
  
  const buttons = await page.evaluate(() => {
    const headerInput = document.getElementById('mainHeaderSearch');
    const parent = headerInput ? headerInput.parentElement.parentElement : null;
    return {
      parentHTML: parent ? parent.innerHTML : null,
      allButtons: Array.from(document.querySelectorAll('button, a')).map(el => ({
        text: el.innerText.trim(),
        onclick: el.getAttribute('onclick'),
        href: el.getAttribute('href'),
        className: el.className,
        id: el.id
      })).filter(b => b.text.includes('검색') || (b.onclick && b.onclick.includes('search')) || (b.href && b.href.includes('search')))
    };
  });
  
  console.log('Buttons:', JSON.stringify(buttons, null, 2));
  await browser.close();
}

inspectButtons();
