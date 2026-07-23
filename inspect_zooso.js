async function inspectZooso(query) {
  const url = `https://zooso.app/search?q=${encodeURIComponent(query)}`;
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Accept-Language': 'ko-KR,ko;q=0.9'
    }
  });
  console.log('zooso status for', query, ':', res.status);
  const text = await res.text();
  
  // Look for cards/list items containing the query
  // Print lines around '우편번호' or around 5 digit codes
  const lines = text.split('\n');
  const matches = lines.filter(l => l.includes('우편번호') || l.includes('zip') || /\b[0-6]\d{4}\b/.test(l));
  console.log(`Matched lines (${matches.length}):`);
  console.log(matches.slice(0, 15).join('\n'));
}

async function run() {
  await inspectZooso('강릉대로 337-5');
  await inspectZooso('속초시 밤골5길 19');
}

run();
