import xlsx from 'xlsx';

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
    
    const findby = [];
    const fbRegex = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
    let m;
    while ((m = fbRegex.exec(text)) !== null) {
      findby.push(m[1]);
    }
    
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
  } catch(e) {
    return { address, error: e.message };
  }
}

async function runTest20() {
  const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
  const sheet = wb.Sheets['전국_소동물병원_DM발송_주소록'];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  
  const missing = [];
  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const zip = row[3];
    if (zip === undefined || zip === null || String(zip).trim() === '') {
      missing.push({ row: i + 1, name: row[0], address: row[2] });
    }
  }
  
  console.log(`Total missing in sheet 1: ${missing.length}`);
  console.log('Testing first 20 missing addresses on Naver...\n');
  
  for (let i = 0; i < Math.min(20, missing.length); i++) {
    const item = missing[i];
    const res = await lookupNaver(item.address);
    console.log(`Row ${item.row} [${item.name}]: "${item.address}" -> findby: ${JSON.stringify(res.findby)} | bodyZips: ${JSON.stringify(res.bodyZips)}`);
    await new Promise(r => setTimeout(r, 200)); // slight delay
  }
}

runTest20();
