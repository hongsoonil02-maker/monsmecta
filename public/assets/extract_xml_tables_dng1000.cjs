const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, 'dng1000_pptx/ppt/slides/');

function extractTables(filePath) {
    const content = fs.readFileSync(filePath, 'utf-8');
    const tableRegex = /<a:tbl>(.*?)<\/a:tbl>/gs;
    let tableMatch;
    let foundAny = false;
    
    let out = `\n--- ${path.basename(filePath)} ---\n`;
    let tableCount = 0;
    
    while ((tableMatch = tableRegex.exec(content)) !== null) {
        foundAny = true;
        tableCount++;
        out += `\nTable ${tableCount}:\n`;
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
            out += rowData.join(' | ') + '\n';
        }
    }
    if (foundAny) console.log(out);
}

fs.readdirSync(dir).forEach(file => {
    if (file.endsWith('.xml')) {
        extractTables(path.join(dir, file));
    }
});
