async function testRegionSearch() {
  const query = '강릉대로 337-5';
  const url = `https://postcode.map.kakao.com/search?region_name=${encodeURIComponent(query)}&cq=${encodeURIComponent(query)}&mode=transmit&zn=Y`;
  const res = await fetch(url);
  const text = await res.text();
  
  console.log('Length:', text.length);
  const zips = text.match(/\b\d{5}\b/g) || [];
  console.log('5-digit numbers found:', Array.from(new Set(zips)));
  
  // Look for any address items or results in the returned HTML
  if (text.includes('25492')) {
    console.log('FOUND 25492 in response!');
  } else {
    // Print lines containing post or addr or zip inside the body
    const lines = text.split('\n').filter(l => l.includes('25') || l.includes('우편번호') || l.includes('result'));
    console.log('Matching lines snippet:', lines.slice(0, 10));
  }
}

testRegionSearch();
