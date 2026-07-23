import xlsx from 'xlsx';

const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');

for (const sheetName of wb.SheetNames) {
  const sheet = wb.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  const headers = data[0] || [];
  const nameIdx = headers.findIndex(h => String(h).includes('병원') || String(h).includes('상호'));
  const zipIdx = headers.findIndex(h => String(h).includes('우편'));
  const addrIdx = headers.findIndex(h => String(h).includes('주소'));
  
  console.log(`\n========================================`);
  console.log(`DUPLICATE ANALYSIS FOR: ${sheetName} (Total data rows: ${data.length - 1})`);
  console.log(`========================================`);
  
  // Map by normalized name + normalized address
  const byExact = {};
  const byName = {};
  const byAddr = {};
  
  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    if (!row || row.length === 0) continue;
    
    const rawName = String(row[nameIdx] || '').trim();
    const rawZip = String(row[zipIdx] || '').trim();
    const rawAddr = String(row[addrIdx] || '').trim();
    
    if (!rawName && !rawAddr) continue;
    
    // normalized keys
    const normName = rawName.replace(/\s+/g, '').toLowerCase();
    // remove spaces and () for address comparison
    const normAddr = rawAddr.replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
    
    const exactKey = `${normName}|${normAddr}`;
    
    if (!byExact[exactKey]) byExact[exactKey] = [];
    byExact[exactKey].push({ rowNum: i + 1, name: rawName, zip: rawZip, addr: rawAddr });
    
    if (normName && normName !== '동물병원' && normName !== '종합동물병원') {
      if (!byName[normName]) byName[normName] = [];
      byName[normName].push({ rowNum: i + 1, name: rawName, zip: rawZip, addr: rawAddr });
    }
    
    if (normAddr && normAddr.length > 5) {
      if (!byAddr[normAddr]) byAddr[normAddr] = [];
      byAddr[normAddr].push({ rowNum: i + 1, name: rawName, zip: rawZip, addr: rawAddr });
    }
  }
  
  // 1. Exact duplicates (same normalized name + normalized address)
  const exactDupes = Object.values(byExact).filter(group => group.length > 1);
  console.log(`\n[1] Exact Duplicates (Same Name & Same Address): ${exactDupes.length} groups (${exactDupes.reduce((acc, g) => acc + g.length - 1, 0)} redundant rows)`);
  if (exactDupes.length > 0) {
    console.log('Sample Exact Duplicate groups:');
    exactDupes.slice(0, 10).forEach((group, idx) => {
      console.log(`  Group ${idx + 1}:`);
      group.forEach(item => console.log(`    Row ${item.rowNum} | [${item.name}] | Zip: ${item.zip} | Addr: ${item.addr}`));
    });
  }
  
  // 2. Same address, different hospital name
  const addrDupes = Object.values(byAddr).filter(group => group.length > 1 && new Set(group.map(i => i.name.replace(/\s+/g, '').toLowerCase())).size > 1);
  console.log(`\n[2] Same Address (Cleaned) with Different/Modified Name: ${addrDupes.length} groups`);
  if (addrDupes.length > 0) {
    console.log('Sample Same-Address groups:');
    addrDupes.slice(0, 10).forEach((group, idx) => {
      console.log(`  Group ${idx + 1}:`);
      group.forEach(item => console.log(`    Row ${item.rowNum} | [${item.name}] | Zip: ${item.zip} | Addr: ${item.addr}`));
    });
  }
  
  // 3. Same hospital name, different address
  const nameDupes = Object.values(byName).filter(group => group.length > 1 && new Set(group.map(i => i.addr.replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase())).size > 1);
  console.log(`\n[3] Same Hospital Name with Different Address: ${nameDupes.length} groups`);
  if (nameDupes.length > 0) {
    console.log('Sample Same-Name groups:');
    nameDupes.slice(0, 10).forEach((group, idx) => {
      console.log(`  Group ${idx + 1}:`);
      group.forEach(item => console.log(`    Row ${item.rowNum} | [${item.name}] | Zip: ${item.zip} | Addr: ${item.addr}`));
    });
  }
}
