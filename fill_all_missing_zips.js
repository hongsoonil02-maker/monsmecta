import xlsx from 'xlsx';
import fs from 'fs';

async function lookupNaver(address) {
  // Clean address for search (remove detailed building/floor/room info like 101동 106호 or 2층 or () details if needed, but search with full first)
  const query = address + ' 우편번호';
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;
  
  try {
    const res = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'ko-KR,ko;q=0.9'
      }
    });
    if (res.status === 429) {
      await new Promise(r => setTimeout(r, 2000));
      return lookupNaver(address);
    }
    const text = await res.text();
    
    // 1. Check findby.co.kr/details/xxxxx or zooso.app or jusome matches
    const findby = [];
    const fbRegex = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
    let m;
    while ((m = fbRegex.exec(text)) !== null) {
      findby.push(m[1]);
    }
    
    // 2. Check title/mark postal codes around 우편번호
    const bodyZips = [];
    const bodyRegex = /우편번호[^0-9]{0,10}([0-6]\d{4})/g;
    while ((m = bodyRegex.exec(text)) !== null) {
      bodyZips.push(m[1]);
    }
    
    // If no exact match, try fallback query with just road name + number (e.g., strip () and sub-details)
    const uniqueFindby = Array.from(new Set(findby));
    const uniqueBody = Array.from(new Set(bodyZips));
    
    let chosen = uniqueFindby[0] || uniqueBody[0] || null;
    
    if (!chosen) {
      // try simplified address (e.g. up to road name number)
      const roadMatch = address.match(/^([가-힣\s]+(?:로|길)\s*\d+(?:-\d+)?)/);
      if (roadMatch && roadMatch[1] && roadMatch[1].trim() !== address.trim()) {
        const fallbackUrl = `https://search.naver.com/search.naver?query=${encodeURIComponent(roadMatch[1].trim() + ' 우편번호')}`;
        const fRes = await fetch(fallbackUrl, {
          headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
          }
        });
        const fText = await fRes.text();
        let fm;
        while ((fm = fbRegex.exec(fText)) !== null) {
          if (!chosen) chosen = fm[1];
        }
        while ((fm = bodyRegex.exec(fText)) !== null) {
          if (!chosen) chosen = fm[1];
        }
      }
    }
    
    return {
      address,
      chosen,
      findby: uniqueFindby,
      bodyZips: uniqueBody
    };
  } catch(e) {
    return { address, chosen: null, error: e.message };
  }
}

async function runAll() {
  const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
  const results = {};
  let totalMissing = 0;
  let resolvedCount = 0;
  
  for (const sheetName of wb.SheetNames) {
    const sheet = wb.Sheets[sheetName];
    const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
    const headers = data[0] || [];
    const zipIdx = headers.findIndex(h => String(h).includes('우편') || String(h).includes('우편번호'));
    const addrIdx = headers.findIndex(h => String(h).includes('주소'));
    const nameIdx = headers.findIndex(h => String(h).includes('병원') || String(h).includes('상호'));
    
    console.log(`Processing ${sheetName} (ZipIdx=${zipIdx}, AddrIdx=${addrIdx})...`);
    
    const missingItems = [];
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const zip = row[zipIdx];
      const addr = row[addrIdx];
      if ((zip === undefined || zip === null || String(zip).trim() === '') && addr) {
        missingItems.push({ sheetName, rowIndex: i, name: row[nameIdx], address: String(addr).trim() });
      }
    }
    
    totalMissing += missingItems.length;
    console.log(`Found ${missingItems.length} missing postal codes in ${sheetName}. Looking up with concurrency 5...`);
    
    // process in batches of 5
    for (let i = 0; i < missingItems.length; i += 5) {
      const batch = missingItems.slice(i, i + 5);
      const batchResults = await Promise.all(batch.map(async item => {
        const res = await lookupNaver(item.address);
        return { ...item, ...res };
      }));
      
      for (const r of batchResults) {
        if (r.chosen) {
          resolvedCount++;
        }
        results[`${r.sheetName}_${r.rowIndex}`] = r;
      }
      process.stdout.write(`\rProgress: ${Math.min(i + 5, missingItems.length)} / ${missingItems.length} resolved in this sheet...`);
      await new Promise(r => setTimeout(r, 150));
    }
    console.log('\nDone sheet:', sheetName);
  }
  
  console.log(`\n=== FINAL STATS ===`);
  console.log(`Total missing: ${totalMissing}`);
  console.log(`Resolved: ${resolvedCount} (${(resolvedCount / totalMissing * 100).toFixed(1)}%)`);
  
  fs.writeFileSync('lookup_results.json', JSON.stringify(results, null, 2), 'utf-8');
  console.log('Saved all lookup results to lookup_results.json');
}

runAll();
