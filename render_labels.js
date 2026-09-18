import puppeteer from 'puppeteer';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const labels = [
    {
        key: 'hepamax',
        html: 'monsmecta_hepamax_30ml_94x45.html',
        pdf: '몬스멕타_헤파맥스_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_헤파맥스_30ml_라벨_고해상도(94x45mm).png',
        png_en: 'monsmecta_hepamax_30ml_label_hd.png'
    },
    {
        key: 'renal',
        html: 'monsmecta_renal_30ml_94x45.html',
        pdf: '몬스멕타_레날디톡스_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_레날디톡스_30ml_라벨_고해상도(94x45mm).png',
        png_en: 'monsmecta_renal_30ml_label_hd.png'
    },
    {
        key: 'original',
        html: 'monsmecta_original_30ml_94x45.html',
        pdf: '몬스멕타_오리지널_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_오리지널_30ml_라벨_고해상도(94x45mm).png',
        png_en: 'monsmecta_original_30ml_label_hd.png'
    }
];

(async () => {
    console.log('Launching browser for print-ready PDF & Image render...');
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const labelDir = path.resolve(__dirname, 'public/assets/labels');

    for (const item of labels) {
        const page = await browser.newPage();
        
        // 94mm x 45mm rendered at high DPI (deviceScaleFactor: 3.5 -> ~330 DPI)
        await page.setViewport({
            width: 1110,
            height: 531,
            deviceScaleFactor: 3.5
        });

        const htmlUrl = 'file://' + path.join(labelDir, item.html).replace(/\\/g, '/');
        console.log(`Loading: ${htmlUrl}`);
        await page.goto(htmlUrl, { waitUntil: 'networkidle0' });

        // Generate Print-Ready PDF
        const pdfPath = path.join(labelDir, item.pdf);
        await page.pdf({
            path: pdfPath,
            width: '94mm',
            height: '45mm',
            printBackground: true,
            margin: { top: 0, right: 0, bottom: 0, left: 0 },
            pageRanges: '1'
        });
        console.log(`Saved PDF: ${pdfPath}`);

        // Generate Ultra-High-Resolution PNG
        const element = await page.$('.label-sheet');
        if (element) {
            const pngBuffer = await element.screenshot({
                type: 'png'
            });
            const pngPath = path.join(labelDir, item.png);
            fs.writeFileSync(pngPath, pngBuffer);
            console.log(`Saved PNG: ${pngPath}`);

            if (item.png_en) {
                const pngEnPath = path.join(labelDir, item.png_en);
                fs.writeFileSync(pngEnPath, pngBuffer);
                console.log(`Saved PNG (Safe ASCII): ${pngEnPath}`);
            }
        }

        await page.close();
    }

    await browser.close();
    console.log('All labels successfully generated in PDF and PNG!');
})();
