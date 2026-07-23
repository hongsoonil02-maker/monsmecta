import xlsx from 'xlsx';

const wb = xlsx.readFile('몬스멕타_전국 소동물병원_260715.xlsx');
for (const sheetName of wb.SheetNames) {
  const sheet = wb.Sheets[sheetName];
  const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
  console.log(`Sheet: ${sheetName}`);
  console.log('Headers (Row 1):', data[0]);
  console.log('Sample Row 2:', data[1]);
  console.log('Sample Row 3:', data[2]);
  
  // count how many rows have empty postal code column
  // let's find index of '우편번호'
  const headers = data[0] || [];
  const zipIdx = headers.findIndex(h => String(h).includes('우편') || String(h).includes('우편번호'));
  console.log(`Zip column index: ${zipIdx}`);
  if (zipIdx !== -1) {
    let missingCount = 0;
    for (let i = 1; i < data.length; i++) {
      const val = data[i][zipIdx];
      if (val === undefined || val === null || String(val).trim() === '') {
        missingCount++;
      }
    }
    console.log(`Missing count in ${sheetName}: ${missingCount} / ${data.length - 1}`);
  }
  console.log('-----------------------------------');
}
