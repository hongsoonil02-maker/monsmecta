async function testEpost(query) {
  try {
    const res = await fetch('https://www.epost.go.kr/search.RetrievePstcdInnerList.comm', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
      },
      body: `keyword=${encodeURIComponent(query)}`
    });
    const text = await res.text();
    console.log('Epost length:', text.length);
    const zips = text.match(/\b\d{5}\b/g) || [];
    console.log('Epost zips found:', Array.from(new Set(zips)));
  } catch (e) {
    console.error('Epost error:', e.message);
  }
}

async function testJusoApi(query) {
  // Public test keys often used or let's check open juso API
  const url = `https://business.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=5&keyword=${encodeURIComponent(query)}&confmKey=devU01TX0FVVEgyMDI2MDcyNTE1MDQxNTExNzk0MTU=&resultType=json`;
  try {
    const res = await fetch(url);
    const json = await res.json();
    console.log('Juso API response:', JSON.stringify(json, null, 2));
  } catch (e) {
    console.error('Juso API error:', e.message);
  }
}

testEpost('강남대로 337');
testJusoApi('강남대로 337');
