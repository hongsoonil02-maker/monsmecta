async function testSearch(keyword) {
  const url = `https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword=${encodeURIComponent(keyword)}`;
  const res = await fetch(url);
  const text = await res.text();
  
  // Extract zip codes or road addresses from the returned HTML
  // Usually juso.go.kr returns results in specific HTML tags or maybe we can call the ajax endpoint directly
  // Let's check for 5-digit postal codes in the text or look for class names
  const zips = text.match(/\b\d{5}\b/g) || [];
  console.log('Keyword:', keyword);
  console.log('Found 5-digit numbers:', Array.from(new Set(zips)).slice(0, 10));
  
  // Let's inspect snippet around "zipNo" or "우편번호" in the HTML response
  const idx = text.indexOf('우편번호');
  if (idx !== -1) {
    console.log('Context around 우편번호:', text.slice(idx - 100, idx + 200).replace(/\s+/g, ' '));
  } else {
    // Check if there's an ajax call made by AddressMainSearch.do
    const ajaxMatch = text.match(/url\s*:\s*["']([^"']+)["']/g);
    console.log('Ajax matches:', ajaxMatch);
  }
}

testSearch('서울특별시 강남구 테헤란로 152');
