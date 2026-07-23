import xlsx from 'xlsx';
import fs from 'fs';

const filename = '몬스멕타_전국 소동물병원_260715.xlsx';
const workbook = xlsx.readFile(filename);

let allMissing = [];
let allRowsSummary = [];

for (const sheetName of workbook.SheetNames) {
  const sheet = workbook.Sheets[sheetName];
  const rows = xlsx.utils.sheet_to_json(sheet, { header: 1, defval: '' });
  const dataRows = rows.slice(1);
  
  let missingCount = 0;
  let exactDupCount = 0;
  let nameAddrDupCount = 0;
  let nameAddressMap = new Map();
  let rowStrMap = new Map();
  
  for (let i = 0; i < dataRows.length; i++) {
    const rowNum = i + 2;
    const row = dataRows[i];
    const name = String(row[0] || '').trim();
    const zip = String(row[1] || '').trim();
    const addr = String(row[2] || '').trim();
    
    if (!zip || zip === '-' || zip === '0' || zip === '00000') {
      missingCount++;
      allMissing.push({ sheetName, rowNum, name, zip, addr });
    }
    
    const key = `${name}||${addr}`;
    if (nameAddressMap.has(key)) {
      nameAddrDupCount++;
    } else {
      nameAddressMap.set(key, rowNum);
    }
    
    const rowStr = JSON.stringify([name, zip, addr]);
    if (rowStrMap.has(rowStr)) {
      exactDupCount++;
    } else {
      rowStrMap.set(rowStr, rowNum);
    }
  }
  
  console.log(`Sheet "${sheetName}":`);
  console.log(`  Total data rows: ${dataRows.length}`);
  console.log(`  Missing zip codes: ${missingCount}`);
  console.log(`  Name+Address duplicates within sheet: ${nameAddrDupCount}`);
  console.log(`  Exact row duplicates within sheet: ${exactDupCount}`);
}

console.log(`\nTotal missing zip codes across workbook: ${allMissing.length}`);
fs.writeFileSync('missing_zips.json', JSON.stringify(allMissing, null, 2));
