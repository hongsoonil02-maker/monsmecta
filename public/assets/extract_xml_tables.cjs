const fs = require('fs');
const path = require('path');

function extractTables(filePath) {
    console.log(`\n--- ${path.basename(filePath)} ---`);
    const content = fs.readFileSync(filePath, 'utf-8');
    
    // Quick regex to find tables
    const tableRegex = /<a:tbl>(.*?)<\/a:tbl>/gs;
    let tableMatch;
    let tableCount = 0;
    
    while ((tableMatch = tableRegex.exec(content)) !== null) {
        tableCount++;
        console.log(`\nTable ${tableCount}:`);
        const tableContent = tableMatch[1];
        
        const rowRegex = /<a:tr[^>]*>(.*?)<\/a:tr>/gs;
        let rowMatch;
        while ((rowMatch = rowRegex.exec(tableContent)) !== null) {
            const rowContent = rowMatch[1];
            
            const cellRegex = /<a:tc[^>]*>(.*?)<\/a:tc>/gs;
            let cellMatch;
            const rowData = [];
            
            while ((cellMatch = cellRegex.exec(rowContent)) !== null) {
                const cellContent = cellMatch[1];
                
                const textRegex = /<a:t>(.*?)<\/a:t>/gs;
                let textMatch;
                const cellTexts = [];
                while ((textMatch = textRegex.exec(cellContent)) !== null) {
                    cellTexts.push(textMatch[1]);
                }
                rowData.push(cellTexts.join('').trim());
            }
            console.log(rowData.join(' | '));
        }
    }
}

extractTables(path.join(__dirname, 'liqi_pptx/ppt/slides/slide1.xml'));
extractTables(path.join(__dirname, 'liqi_pptx/ppt/slides/slide2.xml'));
