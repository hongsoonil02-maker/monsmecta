import puppeteer from 'puppeteer';

async function testLookup(address) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  // Set user agent
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
  
  console.log('Testing juso.go.kr for:', address);
  
  // Intercept XHR / API requests to see where juso gets results
  page.on('response', async (response) => {
    const url = response.url();
    if (url.includes('do') || url.includes('api') || url.includes('search') || url.includes('List')) {
      const type = response.headers()['content-type'] || '';
      if (type.includes('json') || type.includes('text')) {
        try {
          const text = await response.text();
          if (text.includes('zipNo') || text.includes('우편번호') || /\b\d{5}\b/.test(text)) {
            console.log(`[Response URL]: ${url}`);
            console.log(`[Response snippet]:`, text.slice(0, 500));
          }
        } catch (e) {}
      }
    }
  });

  await page.goto(`https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword=${encodeURIComponent(address)}`, { waitUntil: 'networkidle2' });
  
  // Extract text from page content after loading
  const content = await page.content();
  const zips = content.match(/\b[0-6]\d{4}\b/g) || [];
  console.log('Page body zips found:', Array.from(new Set(zips)));
  
  await browser.close();
}

testLookup('강원특별자치도 강릉시 강릉대로 337-5');
