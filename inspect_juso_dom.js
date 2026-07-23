import puppeteer from 'puppeteer';

async function inspectJuso() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  const query = '강릉대로 337-5';
  console.log('Navigating to juso.go.kr...');
  await page.goto(`https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword=${encodeURIComponent(query)}`, { waitUntil: 'domcontentloaded' });
  
  // Wait a couple seconds for any client-side script or table rendering
  await new Promise(r => setTimeout(r, 3000));
  
  // Get all text and links/elements inside the main content area
  const info = await page.evaluate(() => {
    // Look for search result containers
    const results = document.querySelectorAll('.ol_list, .list, .search_list, table, .sub_table, #list, .result, .addr_list');
    let containerTexts = [];
    results.forEach(r => containerTexts.push(r.className + ' -> ' + r.innerText.slice(0, 300)));
    
    return {
      title: document.title,
      bodySnippet: document.body.innerText.slice(0, 1000),
      containers: containerTexts,
      allZips: document.body.innerText.match(/\b[0-6]\d{4}\b/g) || []
    };
  });
  
  console.log('Info:', JSON.stringify(info, null, 2));
  await browser.close();
}

inspectJuso();
