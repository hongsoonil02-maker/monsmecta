async function lookupNaver(address) {
  const query = address + ' 우편번호';
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;
  
  try {
    const res = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9'
      }
    });
    const text = await res.text();
    
    // Check findby.co.kr or zooso.app or jusome.com links which have postal codes like details/25492 or 우편번호 25492
    // Also check text matches like /([0-6]\d{4})/
    const findbyMatches = text.match(/findby\.co\.kr\/details\/([0-6]\d{4})/g) || [];
    const extractedZips = findbyMatches.map(m => m.split('/details/')[1]);
    
    // Also look for regex pattern around 우편번호
    const zipRegex = /우편번호[^\d]*([0-6]\d{4})/g;
    let match;
    while ((match = zipRegex.exec(text)) !== null) {
      extractedZips.push(match[1]);
    }
    
    // Also check title / mark matches
    const all5Digits = Array.from(new Set(extractedZips));
    return { address, zips: all5Digits };
  } catch(e) {
    return { address, error: e.message };
  }
}

async function testBatch() {
  const samples = [
    '강원특별자치도 강릉시 강릉대로 337-5',
    '강원특별자치도 속초시 밤골5길 19',
    '경기도 고양시 덕양구 권율대로 889',
    '경기도 성남시 분당구 동판교로 52',
    '서울특별시 강남구 강남대로 337'
  ];
  
  for (const addr of samples) {
    const res = await lookupNaver(addr);
    console.log(res);
  }
}

testBatch();
