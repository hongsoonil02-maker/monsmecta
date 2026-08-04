const xlsx = require('xlsx');

// 1. Load Sample Requests
const wb1 = xlsx.readFile('public/몬스멕타 주문내역.xlsx');
const sheet1 = wb1.Sheets['샘플신청'];
const data1 = xlsx.utils.sheet_to_json(sheet1);

// Deduplicate
const uniques = [];
const seen = new Set();
for (const row of data1) {
    const name = (row['동물병원명'] || '').trim().replace(/\s+/g, '');
    if (!name) continue;
    if (!seen.has(name)) {
        seen.add(name);
        row._cleanName = name;
        uniques.push(row);
    }
}

// 2. Load Address Book
const wb2 = xlsx.readFile('몬스멕타_전국 소동물병원_260715_정리완료.xlsx');
const sheet2 = wb2.Sheets[wb2.SheetNames[0]];
const data2 = xlsx.utils.sheet_to_json(sheet2);

// Function to calculate similarity between two strings
function similarity(s1, s2) {
    let matches = 0;
    const words = s1.split(/\s+/);
    for (const w of words) {
        if (w.length > 1 && s2.includes(w)) matches++;
    }
    return matches;
}

// 3. Match and Extract Postal Codes
const finalData = [];
for (const req of uniques) {
    const targetName = req._cleanName;
    const targetAddr = (req['샘플 배송 주소'] || '');
    
    // Find matches
    const matches = data2.filter(r => {
        const hName = (r['병원명/상호'] || '').trim().replace(/\s+/g, '');
        return hName === targetName;
    });

    let zipCode = '';
    let addrBookAddr = '';
    
    if (matches.length === 1) {
        zipCode = matches[0]['통합우편번호'];
        addrBookAddr = matches[0]['통합주소(100%번지수포함)'];
    } else if (matches.length > 1) {
        // Find best match by address similarity
        let bestMatch = matches[0];
        let bestScore = -1;
        for (const m of matches) {
            const score = similarity(targetAddr, m['통합주소(100%번지수포함)'] || '');
            if (score > bestScore) {
                bestScore = score;
                bestMatch = m;
            }
        }
        zipCode = bestMatch['통합우편번호'];
        addrBookAddr = bestMatch['통합주소(100%번지수포함)'];
    }

    finalData.push({
        '우편번호': zipCode || '',
        '주소': targetAddr.trim(),
        '참고주소(주소록)': addrBookAddr || '',
        '받는사람(병원명)': req['동물병원명'] ? req['동물병원명'].trim() : '',
        '받는사람(원장님)': req['원장님 성함'] ? req['원장님 성함'].trim() : '',
        '신청 구분': req['신청 구분'] ? req['신청 구분'].trim() : ''
    });
}

// 4. Create new workbook and save
const newWb = xlsx.utils.book_new();
const newWs = xlsx.utils.json_to_sheet(finalData);

// Adjust column widths for better printing
newWs['!cols'] = [
    { wch: 10 }, // 우편번호
    { wch: 40 }, // 주소
    { wch: 40 }, // 참고주소
    { wch: 20 }, // 병원명
    { wch: 15 }, // 원장님
    { wch: 20 }  // 신청 구분
];

xlsx.utils.book_append_sheet(newWb, newWs, '라벨인쇄용');
xlsx.writeFile(newWb, 'public/샘플신청_라벨인쇄용.xlsx');

console.log('Successfully generated public/샘플신청_라벨인쇄용.xlsx with', finalData.length, 'records.');
