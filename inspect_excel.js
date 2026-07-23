import xlsx from 'xlsx';

const filename = '몬스멕타_전국 소동물병원_260715.xlsx';
const workbook = xlsx.readFile(filename);

console.log('=== Sheet Names ===');
console.log(workbook.SheetNames);

for (const sheetName of workbook.SheetNames) {
  console.log(`\n=== Sheet: ${sheetName} ===`);
  const sheet = workbook.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  console.log(`Total rows (including header): ${data.length}`);
  if (data.length > 0) {
    console.log('Header:', data[0]);
    console.log('Sample Row 1:', data[1]);
    if (data.length > 2) console.log('Sample Row 2:', data[2]);
  }
}
