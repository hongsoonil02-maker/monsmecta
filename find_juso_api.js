async function findEndpoint() {
  const jsRes = await fetch('https://www.juso.go.kr/assets/index-fc618106.js');
  const jsText = await jsRes.text();
  
  // Find all URLs or endpoints mentioned in the JS bundle
  const endpoints = jsText.match(/["'][^"']*\.do[^"']*["']/g) || [];
  const apiPaths = jsText.match(/["']\/[^"']*["']/g) || [];
  
  console.log('*.do matches:', Array.from(new Set(endpoints)).slice(0, 30));
  console.log('API paths with search or addr:', Array.from(new Set(apiPaths)).filter(p => p.includes('search') || p.includes('addr') || p.includes('juso')).slice(0, 30));
}

findEndpoint();
