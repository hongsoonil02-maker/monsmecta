async function testNaju() {
  const query = '전라남도 나주시 과원동 121-1';
  const url = `https://zooso.app/search?q=${encodeURIComponent(query)}`;
  const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  const text = await res.text();
  const regex = /\/zipcode\/([0-6]\d{4})/g;
  const zips = [];
  let m;
  while ((m = regex.exec(text)) !== null) {
    zips.push(m[1]);
  }
  console.log('Naju zips:', Array.from(new Set(zips)));
  
  if (zips.length === 0) {
    // try naver with just 나주시 과원동 121-1
    const nUrl = `https://search.naver.com/search.naver?query=${encodeURIComponent('나주시 과원동 121-1 우편번호')}`;
    const nRes = await fetch(nUrl, { headers: { 'User-Agent': 'Mozilla/5.0' } });
    const nText = await nRes.text();
    const fb = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
    while ((m = fb.exec(nText)) !== null) {
      zips.push(m[1]);
    }
    const bd = /우편번호[^0-9]{0,10}([0-6]\d{4})/g;
    while ((m = bd.exec(nText)) !== null) {
      zips.push(m[1]);
    }
    console.log('Naver fallback zips:', Array.from(new Set(zips)));
  }
}
testNaju();
