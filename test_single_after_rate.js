async function testSingle() {
  const query = '경기도 시흥시 삼미시장1길 19 우편번호';
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept-Language': 'ko-KR,ko;q=0.9'
    }
  });
  const text = await res.text();
  console.log('Status:', res.status, 'Length:', text.length);
  if (text.includes('captcha') || text.includes('비정상적인') || text.includes('로봇')) {
    console.log('CAPTCHA / Bot check triggered!');
  } else {
    const fbRegex = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
    let m;
    const findby = [];
    while ((m = fbRegex.exec(text)) !== null) {
      findby.push(m[1]);
    }
    console.log('findby:', Array.from(new Set(findby)));
    const bodyRegex = /우편번호[^0-9]{0,10}([0-6]\d{4})/g;
    const bodyZips = [];
    while ((m = bodyRegex.exec(text)) !== null) {
      bodyZips.push(m[1]);
    }
    console.log('bodyZips:', Array.from(new Set(bodyZips)));
    if (findby.length === 0 && bodyZips.length === 0) {
      console.log('Snippet of response:\n', text.slice(0, 1500));
    }
  }
}

testSingle();
