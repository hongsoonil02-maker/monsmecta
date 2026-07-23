async function testFastApis() {
  const query = '속초시 밤골5길 19';
  
  // Test 1: zooso.app
  try {
    const zRes = await fetch(`https://zooso.app/search?q=${encodeURIComponent(query)}`, {
      headers: { 'User-Agent': 'Mozilla/5.0' }
    });
    console.log('zooso status:', zRes.status);
    const zText = await zRes.text();
    const zips = zText.match(/\b[0-6]\d{4}\b/g) || [];
    console.log('zooso zips:', Array.from(new Set(zips)));
  } catch(e) {
    console.log('zooso error:', e.message);
  }
  
  // Test 2: juso.go.kr addrLinkApi with dev key U01TX0FVVEgyMDI0MDExNzE1NTk1NTExNDQ0OTc= (public sample key or open api test)
  try {
    const jUrl = `https://business.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=5&keyword=${encodeURIComponent(query)}&confmKey=U01TX0FVVEgyMDI0MDExNzE1NTk1NTExNDQ0OTc=&resultType=json`;
    const jRes = await fetch(jUrl);
    console.log('juso status:', jRes.status);
    const jJson = await jRes.json();
    console.log('juso response:', JSON.stringify(jJson, null, 2));
  } catch(e) {
    console.log('juso error:', e.message);
  }
}

testFastApis();
