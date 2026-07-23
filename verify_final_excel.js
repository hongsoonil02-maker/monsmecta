import xlsx from 'xlsx';

const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715_정리완료.xlsx');

console.log('=== FINAL VERIFICATION OF CLEANED EXCEL ===');

for (const sheetName of wb.SheetNames) {
  const sheet = wb.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  const headers = data[0] || [];
  const zipIdx = headers.findIndex(h => String(h).includes('우편'));
  
  let missing = 0;
  let totalRows = data.length - 1;
  
  for (let i = 1; i < data.length; i++) {
    const val = data[i][zipIdx];
    if (val === undefined || val === null || String(val).trim() === '') {
      missing++;
      if (missing <= 5) {
        console.log(`  Still missing in ${sheetName} row ${i + 1}:`, data[i]);
      }
    }
  }
  
  console.log(`Sheet [${sheetName}]: Total Rows=${totalRows}, Missing Postal Codes=${missing}`);
}
