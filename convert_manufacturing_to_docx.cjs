const fs = require('fs');
const { marked } = require('marked');
const HTMLtoDOCX = require('html-to-docx');

async function convert() {
    try {
        const mdContent = fs.readFileSync('c:\\\\Users\\\\master\\\\.gemini\\\\antigravity-ide\\\\brain\\\\6bf2fb23-0dba-4767-9dff-3ed1b2745f36\\\\monsmecta_manufacturing_process.md', 'utf8');
        const html = marked.parse(mdContent);
        
        // Add basic styling for tables and fonts
        const htmlContent = `
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body { font-family: "Malgun Gothic", sans-serif; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid black; padding: 8px; }
                </style>
            </head>
            <body>
                ${html}
            </body>
            </html>
        `;
        
        const fileBuffer = await HTMLtoDOCX(htmlContent, null, {
            table: { row: { cantSplit: true } },
            footer: true,
            pageNumber: true,
        });

        const outputPath = 'c:\\\\Users\\\\master\\\\monsmecta-landing\\\\public\\\\assets\\\\monsmecta_manufacturing_process.docx';
        fs.writeFileSync(outputPath, fileBuffer);
        console.log('Successfully generated DOCX!');
    } catch (err) {
        console.error('Error during conversion:', err);
    }
}

convert();
