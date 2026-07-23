async function cleanNaver(address) {
  const query = address + ' 우편번호';
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;
  
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept-Language': 'ko-KR,ko;q=0.9'
    }
  });
  const text = await res.text();
  
  // Find all findby.co.kr/details/xxxxx matches
  const findby = [];
  const fbRegex = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
  let m;
  while ((m = fbRegex.exec(text)) !== null) {
    findby.push(m[1]);
  }
  
  // Find all matches in bodyText where 우편번호 is followed or preceded by 5 digits
  // e.g. "우편번호 25492" or "25492" inside titles
  const bodyZips = [];
  const bodyRegex = /우편번호[^0-9]{0,10}([0-6]\d{4})/g;
  while ((m = bodyRegex.exec(text)) !== null) {
    bodyZips.push(m[1]);
  }
  
  return {
    address,
    findby: Array.from(new Set(findby)),
    bodyZips: Array.from(new Set(bodyZips))
  };
}

async function testClean() {
  const samples = [
    '강원특별자치도 강릉시 강릉대로 337-5',
    '강원특별자치도 속초시 밤골5길 19',
    '경기도 고양시 덕양구 권율대로 889',
    '경기도 성남시 분당구 동판교로 52',
    '서울특별시 강남구 강남대로 337',
    '전북특별자치도 전주시 완산구 효자동2가 1238-4'
  ];
  
  for (const addr of samples) {
    console.log(await cleanNaver(addr));
  }
}

testClean();
