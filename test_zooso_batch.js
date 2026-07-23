async function lookupZooso(address) {
  const url = `https://zooso.app/search?q=${encodeURIComponent(address)}`;
  try {
    const res = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9'
      }
    });
    if (res.status !== 200) {
      return { address, error: `Status ${res.status}` };
    }
    const text = await res.text();
    // match /zipcode/([0-6]\d{4})
    const regex = /\/zipcode\/([0-6]\d{4})/g;
    const zips = [];
    let m;
    while ((m = regex.exec(text)) !== null) {
      zips.push(m[1]);
    }
    return { address, zips: Array.from(new Set(zips)) };
  } catch(e) {
    return { address, error: e.message };
  }
}

async function test20() {
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
    const r = await lookupZooso(addr);
    console.log(r);
    await new Promise(res => setTimeout(res, 300));
  }
}

test20();
