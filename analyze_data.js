import xlsx from 'xlsx';

const filename = '몬스멕타_전국 소동물병원_260715.xlsx';
const workbook = xlsx.readFile(filename);

for (const sheetName of workbook.SheetNames) {
  console.log(`\n========================================`);
  console.log(`Analyzing Sheet: ${sheetName}`);
  console.log(`========================================`);
  const sheet = workbook.Sheets[sheetName];
  const rows = xlsx.utils.sheet_to_json(sheet, { header: 1, defval: '' });
  
  const header = rows[0];
  console.log('Header:', header);
  
  const dataRows = rows.slice(1);
  console.log(`Total data rows: ${dataRows.length}`);
  
  let missingZip = [];
  let emptyAddress = [];
  let nameAddressMap = new Map();
  let exactDuplicates = [];
  let nameAddressDuplicates = [];
  
  for (let i = 0; i < dataRows.length; i++) {
    const rowNum = i + 2; // Excel row number
    const row = dataRows[i];
    const name = String(row[0] || '').trim();
    const zip = String(row[1] || '').trim();
    const addr = String(row[2] || '').trim();
    
    if (!zip || zip === '-' || zip === '0' || zip === '00000') {
      missingZip.push({ rowNum, name, zip, addr });
    }
    if (!addr) {
      emptyAddress.push({ rowNum, name, zip, addr });
    }
    
    const key = `${name}||${addr}`;
    if (nameAddressMap.has(key)) {
      nameAddressDuplicates.push({
        rowNum,
        name,
        zip,
        addr,
        firstSeenAt: nameAddressMap.get(key)
      });
    } else {
      nameAddressMap.set(key, { rowNum, name, zip, addr });
    }
  }
  
  console.log(`\n--- Missing Postal Codes (${missingZip.length}) ---`);
  missingZip.forEach(item => {
    console.log(`Row ${item.rowNum}: Name="${item.name}", Zip="${item.zip}", Address="${item.addr}"`);
  });
  
  console.log(`\n--- Empty Addresses (${emptyAddress.length}) ---`);
  emptyAddress.forEach(item => {
    console.log(`Row ${item.rowNum}: Name="${item.name}", Zip="${item.zip}", Address="${item.addr}"`);
  });
  
  console.log(`\n--- Duplicates by Name + Address (${nameAddressDuplicates.length}) ---`);
  nameAddressDuplicates.forEach(item => {
    console.log(`Row ${item.rowNum} duplicate of Row ${item.firstSeenAt.rowNum}: Name="${item.name}", Zip="${item.zip}", Address="${item.addr}"`);
  });
}
