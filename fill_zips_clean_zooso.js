import xlsx from 'xlsx';
import fs from 'fs';

function cleanAddress(addr) {
  let cleaned = addr.replace(/\([^)]*\)/g, '').trim();
  // match up to road name + number (e.g., 밤골5길 19 or 강릉대로 337-5)
  const roadMatch = cleaned.match(/^([가-힣\s]+(?:로|길|대로|거리)\s*\d+(?:-\d+)?)/);
  if (roadMatch && roadMatch[1]) {
    return roadMatch[1].trim();
  }
  return cleaned.split(',')[0].trim();
}

async function lookupZooso(query) {
  const url = `https://zooso.app/search?q=${encodeURIComponent(query)}`;
  try {
    const res = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
    });
    if (res.status !== 200) return [];
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

async function lookupNaver(query) {
  const url = `https://search.naver.com/search.naver?query=${encodeURIComponent(query + ' 우편번호')}`;
  try {
    const res = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
    });
    if (res.status !== 200) return [];
    const text = await res.text();
    const fbRegex = /findby\.co\.kr\/details\/([0-6]\d{4})/g;
    const findby = [];
    let m;
    while ((m = fbRegex.exec(text)) !== null) {
      findby.push(m[1]);
    }
    const bodyRegex = /우편번호[^0-9]{0,10}([0-6]\d{4})/g;
    const bodyZips = [];
    while ((m = bodyRegex.exec(text)) !== null) {
      bodyZips.push(m[1]);
    }
    const all = [...findby, ...bodyZips];
    return Array.from(new Set(all));
  } catch(e) {
    return [];
  }
}

async function runAll() {
  const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
  const results = {};
  let totalMissing = 0;
  let resolvedCount = 0;
  const unresolvedList = [];
  
  for (const sheetName of wb.SheetNames) {
    const sheet = wb.Sheets[sheetName];
    const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
    const headers = data[0] || [];
    const zipIdx = headers.findIndex(h => String(h).includes('우편') || String(h).includes('우편번호'));
    const addrIdx = headers.findIndex(h => String(h).includes('주소'));
    const nameIdx = headers.findIndex(h => String(h).includes('병원') || String(h).includes('상호'));
    
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
    console.log(`Sheet ${sheetName}: ${missingItems.length} missing postal codes. Looking up...`);
    
    // Process in batches of 5 with zooso first
    for (let i = 0; i < missingItems.length; i += 5) {
      const batch = missingItems.slice(i, i + 5);
      const batchResults = await Promise.all(batch.map(async item => {
        const cleaned = cleanAddress(item.address);
        let zips = await lookupZooso(cleaned);
        if (zips.length === 0 && cleaned !== item.address) {
          zips = await lookupZooso(item.address);
        }
        if (zips.length === 0) {
          // fallback to naver
          zips = await lookupNaver(cleaned);
        }
        return {
          ...item,
          cleanedAddress: cleaned,
          chosenZip: zips[0] || null,
          allZips: zips
        };
      }));
      
      for (const r of batchResults) {
        results[`${r.sheetName}_${r.rowIndex}`] = r;
        if (r.chosenZip) {
          resolvedCount++;
        } else {
          unresolvedList.push(r);
        }
      }
      process.stdout.write(`\rProgress: ${Math.min(i + 5, missingItems.length)} / ${missingItems.length}... (${resolvedCount} resolved total)`);
      await new Promise(r => setTimeout(r, 100));
    }
    console.log('\nFinished sheet:', sheetName);
  }
  
  console.log(`\n=== FINAL RESULTS ===`);
  console.log(`Total missing: ${totalMissing}`);
  console.log(`Resolved: ${resolvedCount} / ${totalMissing} (${(resolvedCount / totalMissing * 100).toFixed(1)}%)`);
  console.log(`Unresolved count: ${unresolvedList.length}`);
  if (unresolvedList.length > 0) {
    console.log('Sample unresolved addresses:\n', JSON.stringify(unresolvedList.slice(0, 15), null, 2));
  }
  
  fs.writeFileSync('clean_lookup_results.json', JSON.stringify(results, null, 2), 'utf-8');
  console.log('Saved to clean_lookup_results.json');
}

runAll();
