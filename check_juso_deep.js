async function checkJusoJsDeep() {
  const url = 'https://www.juso.go.kr/assets/index-fc618106.js';
  const res = await fetch(url);
  const text = await res.text();
  
  // Find strings containing '/' and ending with something or API calls
  const matches = text.match(/["']\/[a-zA-Z0-9_\-\.\/]+["']/g) || [];
  const unique = Array.from(new Set(matches));
  console.log('All path-like strings in index.js:', unique.filter(p => !p.includes('.css') && !p.includes('.png') && !p.includes('.svg')));
}

checkJusoJsDeep();
