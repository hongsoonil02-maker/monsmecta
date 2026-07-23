import xlsx from 'xlsx';

const filename = '몬스멕타_전국 소동물병원_260715.xlsx';
const workbook = xlsx.readFile(filename);

const sheet1Rows = xlsx.utils.sheet_to_json(workbook.Sheets['전국_소동물병원_DM발송_주소록'], { header: 1, defval: '' }).slice(1);
const sheet2Rows = xlsx.utils.sheet_to_json(workbook.Sheets['전국_출장진료동물병원송_DM발송_주소록'], { header: 1, defval: '' }).slice(1);

console.log('=== Checking Sheet 1 vs Sheet 2 Overlaps ===');
const sheet1Map = new Map();
sheet1Rows.forEach((r, idx) => {
  const name = String(r[0] || '').trim();
  const addr = String(r[2] || '').trim();
  sheet1Map.set(`${name}||${addr}`, { rowNum: idx + 2, name, addr, zip: r[1] });
});

let overlaps = 0;
sheet2Rows.forEach((r, idx) => {
  const name = String(r[0] || '').trim();
  const addr = String(r[2] || '').trim();
  const key = `${name}||${addr}`;
  if (sheet1Map.has(key)) {
    overlaps++;
    console.log(`Sheet 2 Row ${idx + 2} matches Sheet 1 Row ${sheet1Map.get(key).rowNum}: Name="${name}", Address="${addr}"`);
  }
});
console.log(`Total exact Name+Address overlaps between Sheet 1 and Sheet 2: ${overlaps}`);

// Also check partial matches by address alone across or within sheets
console.log('\n=== Checking Same Address with different names within Sheet 1 (Top 10) ===');
const addrMap = new Map();
sheet1Rows.forEach((r, idx) => {
  const name = String(r[0] || '').trim();
  const addr = String(r[2] || '').trim();
  if (!addr) return;
  if (!addrMap.has(addr)) addrMap.set(addr, []);
  addrMap.get(addr).push({ rowNum: idx + 2, name });
});

let sameAddrCount = 0;
for (const [addr, items] of addrMap.entries()) {
  if (items.length > 1) {
    sameAddrCount++;
    if (sameAddrCount <= 10) {
      console.log(`Address: "${addr}" -> Rows:`, items);
    }
  }
}
console.log(`Total unique addresses that have multiple rows in Sheet 1: ${sameAddrCount}`);
