async function testSearch() {
  const url = 'https://postcode.map.kakao.com/search?q=' + encodeURIComponent('강남대로 337');
  const res = await fetch(url);
  const text = await res.text();
  console.log('Status:', res.status);
  console.log('Length:', text.length);
  // Look for postal codes or results in HTML or JSON
  const zips = text.match(/\b\d{5}\b/g) || [];
  console.log('5-digit codes found:', Array.from(new Set(zips)));
  
  // Also check if there's an api endpoint like /search/address or /api/search
  const apiMatches = text.match(/[\/a-zA-Z0-9_\-\.\?=&]+search[a-zA-Z0-9_\-\.\?=&]*/g) || [];
  console.log('Search strings in response:', Array.from(new Set(apiMatches)).slice(0, 10));
}

testSearch();
