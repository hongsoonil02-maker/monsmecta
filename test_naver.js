async function testNaver() {
  const query = '강릉대로 337-5 우편번호';
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;
  
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept-Language': 'ko-KR,ko;q=0.9'
    }
  });
  
  const text = await res.text();
  console.log('HTML Length:', text.length);
  
  // Look for 5-digit postal codes around '우편번호' or 'postcode'
  const lines = text.split('\n').filter(l => l.includes('우편번호') || l.includes('25492') || /\b[0-6]\d{4}\b/.test(l));
  console.log('Matching lines count:', lines.length);
  if (lines.length > 0) {
    console.log('Sample matching lines:\n', lines.slice(0, 10).join('\n'));
  }
}

testNaver();
