import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

(async () => {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();
    
    await page.setViewport({ width: 794, height: 1123, deviceScaleFactor: 2 });
    
    const filePath = 'file:///' + path.resolve(__dirname, 'public/assets/monsmecta_wave1-1_dm_letter_a4.html').replace(/\\/g, '/');
    await page.goto(filePath, { waitUntil: 'networkidle0' });
    
    const pdfPath = path.resolve(__dirname, 'public/assets/MONSMECTA_DM_Letter_A4_Refined.pdf');
    await page.pdf({
        path: pdfPath,
        format: 'A4',
        printBackground: true,
        margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
    });

    console.log('PDF generated successfully at:', pdfPath);
    await browser.close();
})();
