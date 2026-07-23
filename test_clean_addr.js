function cleanAddress(addr) {
  // Remove parentheses like (신천동) or (안양동,신강빌딩 지상1층)
  let cleaned = addr.replace(/\([^)]*\)/g, '').trim();
  // Remove floor/room/building details like 1층동 102호 or 1층 or 101동 106호
  // Usually the road address is like: [시/도] [시/군/구] [읍/면/동] [도로명] [본번-부번]
  // Let's grab up to the first number sequence (plus optional hyphens/numbers immediately after)
  // e.g. "경기도 시흥시 삼미시장1길 19, 1층" -> "경기도 시흥시 삼미시장1길 19"
  const roadMatch = cleaned.match(/^([가-힣\s]+(?:로|길|대로|거리)\s*\d+(?:-\d+)?)/);
  if (roadMatch && roadMatch[1]) {
    return roadMatch[1].trim();
  }
  return cleaned.split(',')[0].trim();
}

async function lookupZooso(cleanAddr) {
  const url = `https://zooso.app/search?q=${encodeURIComponent(cleanAddr)}`;
  try {
    const res = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0' }
    });
    const text = await res.text();
    const regex = /\/zipcode\/([0-6]\d{4})/g;
    const zips = [];
    let m;
    while ((m = regex.exec(text)) !== null) {
      zips.push(m[1]);
    }
    return Array.from(new Set(zips));
  } catch(e) {
    return [];
  }
}

async function testClean() {
  const samples = [
    '경기도 시흥시 삼미시장1길 19 (신천동)',
    '경기도 안산시 상록구 예술광장1로 94, 1층동 102호 (성포동,정인프라자)',
    '경기도 안산시 상록구 오목로 78 (본오동,1층)',
    '경기도 안성시 일죽면 금일로 428',
    '경기도 안양시 동안구 흥안대로 492 (관양동,1층)',
    '경기도 안양시 만안구 안양로 150 (안양동,신강빌딩 지상1층)',
    '경기도 안양시 만안구 안양로 258 (안양동)',
    '경기도 오산시 성호대로 108 (원동)',
    '경기도 용인시 수지구 광교중앙로 302, 1층 101호 (상현동, 광교지구 블루스퀘어)',
    '경기도 용인시 수지구 만현로 110 (상현동)'
  ];
  
  for (const addr of samples) {
    const cleaned = cleanAddress(addr);
    const zips = await lookupZooso(cleaned);
    console.log(`Original: "${addr}" -> Cleaned: "${cleaned}" -> Zooso zips: ${JSON.stringify(zips)}`);
    await new Promise(r => setTimeout(r, 300));
  }
}

testClean();
