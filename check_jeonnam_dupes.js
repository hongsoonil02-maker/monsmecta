import xlsx from 'xlsx';

const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
for (const sheetName of wb.SheetNames) {
  const sheet = wb.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  const headers = data[0] || [];
  const nameIdx = headers.findIndex(h => String(h).includes('병원') || String(h).includes('상호'));
  const addrIdx = headers.findIndex(h => String(h).includes('주소'));
  
  const jeonnamGwangjuRows = [];
  const normalRows = {};
  
  for (let i = 1; i < data.length; i++) {
    const name = String(data[i][nameIdx] || '').trim();
    const addr = String(data[i][addrIdx] || '').trim();
    if (addr.includes('전남광주통합특별시')) {
      jeonnamGwangjuRows.push({ row: i + 1, name, addr });
    } else {
      // normalize name and address without province prefix
      const cleanAddr = addr.replace(/^(서울특별시|부산광역시|대구광역시|인천광역시|광주광역시|대전광역시|울산광역시|세종특별자치시|경기도|강원특별자치도|충청북도|충청남도|전라북도|전북특별자치도|전라남도|경상북도|경상남도|제주특별자치도)\s+/, '').replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
      const cleanName = name.replace(/\s+/g, '').toLowerCase();
      const key = `${cleanName}|${cleanAddr}`;
      normalRows[key] = { row: i + 1, name, addr };
    }
  }
  
  let dupeMatchCount = 0;
  console.log(`\nSheet: ${sheetName} -> Total '전남광주통합특별시' rows: ${jeonnamGwangjuRows.length}`);
  for (const jg of jeonnamGwangjuRows) {
    const cleanAddr = jg.addr.replace(/^전남광주통합특별시\s+/, '').replace(/\s+/g, '').replace(/\([^)]*\)/g, '').toLowerCase();
    const cleanName = jg.name.replace(/\s+/g, '').toLowerCase();
    const key = `${cleanName}|${cleanAddr}`;
    if (normalRows[key]) {
      dupeMatchCount++;
      if (dupeMatchCount <= 10) {
        console.log(`  DUPE MATCH: Row ${jg.row} [${jg.name}] (${jg.addr}) == Row ${normalRows[key].row} [${normalRows[key].name}] (${normalRows[key].addr})`);
      }
    }
  }
  console.log(`Total '전남광주통합특별시' rows in ${sheetName} that are exact copies of existing 전라남도/광주광역시 rows: ${dupeMatchCount} / ${jeonnamGwangjuRows.length}`);
}
