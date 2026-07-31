const xlsx = require('xlsx');

function readExcel() {
    const filePath = 'C:\\\\Users\\\\master\\\\monsmecta-landing\\\\몬스멕타(Monsmecta) 배합비(mo) .xlsx';
    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const data = xlsx.utils.sheet_to_json(sheet, { header: 1 });
    console.log(JSON.stringify(data, null, 2));
}

readExcel();
