const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const labels = [
    {
        key: 'hepamax',
        html: 'monsmecta_hepamax_30ml_94x45.html',
        pdf: '몬스멕타_헤파맥스_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_헤파맥스_30ml_라벨_고해상도(94x45mm).png'
    },
    {
        key: 'renal',
        html: 'monsmecta_renal_30ml_94x45.html',
        pdf: '몬스멕타_레날디톡스_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_레날디톡스_30ml_라벨_고해상도(94x45mm).png'
    },
    {
        key: 'original',
        html: 'monsmecta_original_30ml_94x45.html',
        pdf: '몬스멕타_오리지널_30ml_라벨_인쇄용(94x45mm).pdf',
        png: '몬스멕타_오리지널_30ml_라벨_고해상도(94x45mm).png'
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
        
        // 94mm x 45mm at 300 DPI is approx 1110 x 531 px
        await page.setViewport({
            width: 1110,
            height: 531,
            deviceScaleFactor: 2
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

        // Generate Ultra-High-Resolution PNG (300 DPI equivalent)
        const element = await page.$('.label-sheet');
        if (element) {
            const pngPath = path.join(labelDir, item.png);
            await element.screenshot({
                path: pngPath,
                type: 'png'
            });
            console.log(`Saved PNG: ${pngPath}`);
        }

        await page.close();
    }

    await browser.close();
    console.log('All labels successfully generated in PDF and PNG!');
})();
