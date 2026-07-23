async function testSearchHTML() {
  const url = 'https://postcode.map.kakao.com/search?q=' + encodeURIComponent('강남대로 337');
  const res = await fetch(url);
  const text = await res.text();
  
  // Find all script tags or js files
  const scripts = text.match(/<script[^>]*src=["']([^"']+)["'][^>]*>/g) || [];
  console.log('Scripts:', scripts);
  
  // Find any inline script content
  const inlineScripts = text.match(/<script[^>]*>([\s\S]*?)<\/script>/g) || [];
  for (const s of inlineScripts) {
    if (s.includes('url') || s.includes('ajax') || s.includes('fetch') || s.includes('search')) {
      console.log('Inline script snippet:', s.slice(0, 1000));
    }
  }
}

testSearchHTML();
