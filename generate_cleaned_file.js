import xlsx from 'xlsx';
import fs from 'fs';

const lookupResults = JSON.parse(fs.readFileSync('clean_lookup_results.json', 'utf-8'));

// Add the single Naju manual resolution if not present
lookupResults['전국_소동물병원_DM발송_주소록_4251'] = {
  chosenZip: '58257',
  address: '전남광주통합특별시 나주시 과원동 121-1'
};

const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
const newWb = xlsx.utils.book_new();

console.log('=== STARTING EXCEL PROCESSING & DEDUPLICATION ===');

let totalFilled = 0;
let totalRemovedDupes = 0;

for (const sheetName of wb.SheetNames) {
  const sheet = wb.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  const headers = data[0] || [];
  const nameIdx = headers.findIndex(h => String(h).includes('병원') || String(h).includes('상호'));
  const zipIdx = headers.findIndex(h => String(h).includes('우편'));
  const addrIdx = headers.findIndex(h => String(h).includes('주소'));
  
  console.log(`\nSheet: [${sheetName}] (Original data rows: ${data.length - 1})`);
  
  let sheetFilled = 0;
  let sheetRemoved = 0;
  
  // First pass: fill missing postal codes and clean '전남광주통합특별시' if needed
  const processedRows = [data[0]]; // keep header
  const seenExact = new Set();
  const seenNormal = new Set();
  
  // Collect all normal (non-JeonnamGwangju) normalized keys first to detect exact copies
  for (let i = 1; i < data.length; i++) {
    const row = data[i] || [];
    const addr = String(row[addrIdx] || '').trim();
    const name = String(row[nameIdx] || '').trim();
    if (!addr && !name) continue;
    
    if (!addr.includes('전남광주통합특별시')) {
      const cleanAddr = addr.replace(/^(서울특별시|부산광역시|대구광역시|인천광역시|광주광역시|대전광역시|울산광역시|세종특별자치시|경기도|강원특별자치도|충청북도|충청남도|전라북도|전북특별자치도|전라남도|경상북도|경상남도|제주특별자치도)\s+/, '').replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
      const cleanName = name.replace(/\s+/g, '').toLowerCase();
      seenNormal.add(`${cleanName}|${cleanAddr}`);
    }
  }
  
  for (let i = 1; i < data.length; i++) {
    const row = [...(data[i] || [])];
    const name = String(row[nameIdx] || '').trim();
    let addr = String(row[addrIdx] || '').trim();
    let zip = row[zipIdx];
    
    if (!name && !addr) continue; // skip empty rows
    
    // Check if zip is missing or empty
    if (zip === undefined || zip === null || String(zip).trim() === '') {
      const lookupKey = `${sheetName}_${i}`;
      const lookupInfo = lookupResults[lookupKey];
      if (lookupInfo && lookupInfo.chosenZip) {
        zip = lookupInfo.chosenZip;
        row[zipIdx] = zip;
        sheetFilled++;
        totalFilled++;
      }
    }
    
    // Ensure postal code is stored as a 5-character string (pad leading zeros if dropped as numbers, e.g. Seoul 4-digit zips)
    if (row[zipIdx] !== undefined && row[zipIdx] !== null && String(row[zipIdx]).trim() !== '') {
      let sZip = String(row[zipIdx]).trim();
      if (sZip.length > 0 && sZip.length < 5) {
        sZip = sZip.padStart(5, '0');
      }
      row[zipIdx] = sZip;
    }
    
    // Check for '전남광주통합특별시' copy
    if (addr.includes('전남광주통합특별시')) {
      const cleanAddr = addr.replace(/^전남광주통합특별시\s+/, '').replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
      const cleanName = name.replace(/\s+/g, '').toLowerCase();
      const key = `${cleanName}|${cleanAddr}`;
      
      if (seenNormal.has(key)) {
        // exact duplicate copy of an existing 전라남도/광주광역시 row -> remove
        sheetRemoved++;
        totalRemovedDupes++;
        continue;
      } else {
        // unique row only in 전남광주통합특별시 -> correct province to 전라남도 or 광주광역시
        if (addr.includes('나주시') || addr.includes('강진군') || addr.includes('고흥군') || addr.includes('담양군') || addr.includes('함평군')) {
          row[addrIdx] = addr.replace('전남광주통합특별시', '전라남도');
        } else if (addr.includes('북구') || addr.includes('서구') || addr.includes('동구') || addr.includes('남구') || addr.includes('광산구')) {
          row[addrIdx] = addr.replace('전남광주통합특별시', '광주광역시');
        }
        addr = row[addrIdx];
      }
    }
    
    // Exact duplicate check
    const normName = name.replace(/\s+/g, '').toLowerCase();
    const normAddr = addr.replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
    const exactKey = `${normName}|${normAddr}`;
    
    if (seenExact.has(exactKey)) {
      sheetRemoved++;
      totalRemovedDupes++;
      continue;
    }
    seenExact.add(exactKey);
    
    processedRows.push(row);
  }
  
  console.log(`  -> Postal codes filled: +${sheetFilled}`);
  console.log(`  -> Duplicate rows removed: -${sheetRemoved}`);
  console.log(`  -> Final cleaned rows: ${processedRows.length - 1}`);
  
  const newSheet = xlsx.utils.aoa_to_sheet(processedRows);
  xlsx.utils.book_append_sheet(newWb, newSheet, sheetName);
}

const outputFile = '몬스멕타_전국 소동물병원_260715_정리완료.xlsx';
xlsx.writeFile(newWb, outputFile);

console.log(`\n=== SUMMARY ===`);
console.log(`Total missing postal codes filled: ${totalFilled}`);
console.log(`Total duplicate rows removed: ${totalRemovedDupes}`);
console.log(`Cleaned Excel saved to: ${outputFile}`);
