const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const labels = [
    {
        key: 'hepamax',
        html: 'monsmecta_hepamax_30ml_94x45.html',
        pdfName: '몬스멕타_헤파맥스_30ml_라벨_인쇄용(94x45mm)',
        pngName: '몬스멕타_헤파맥스_30ml_라벨_고해상도(94x45mm).png'
    },
    {
        key: 'renal',
        html: 'monsmecta_renal_30ml_94x45.html',
        pdfName: '몬스멕타_레날디톡스_30ml_라벨_인쇄용(94x45mm)',
        pngName: '몬스멕타_레날디톡스_30ml_라벨_고해상도(94x45mm).png'
    },
    {
        key: 'original',
        html: 'monsmecta_original_30ml_94x45.html',
        pdfName: '몬스멕타_오리지널_30ml_라벨_인쇄용(94x45mm)',
        pngName: '몬스멕타_오리지널_30ml_라벨_고해상도(94x45mm).png'
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
        
        await page.setViewport({
            width: 1110,
            height: 531,
            deviceScaleFactor: 2
        });

        const htmlUrl = 'file://' + path.join(labelDir, item.html).replace(/\\/g, '/');
        console.log('Loading:', htmlUrl);
        await page.goto(htmlUrl, { waitUntil: 'networkidle0' });

        // Save PDF with fallback if locked
        let savedPdfPath = '';
        const targets = [
            path.join(labelDir, `${item.pdfName}.pdf`),
            path.join(labelDir, `${item.pdfName}_최종.pdf`),
            path.join(labelDir, `${item.pdfName}_v2.pdf`),
            path.join(labelDir, `${item.pdfName}_v3.pdf`)
        ];

        for (const targetPath of targets) {
            try {
                await page.pdf({
                    path: targetPath,
                    width: '94mm',
                    height: '45mm',
                    printBackground: true,
                    margin: { top: 0, right: 0, bottom: 0, left: 0 },
                    pageRanges: '1'
                });
                savedPdfPath = targetPath;
                console.log('Successfully saved PDF:', targetPath);
                break;
            } catch (err) {
                console.log(`Could not write to ${path.basename(targetPath)} (${err.message}), trying next name...`);
            }
        }

        // Try copying to the main name if it wasn't the first target
        if (savedPdfPath && savedPdfPath !== targets[0]) {
            try {
                fs.copyFileSync(savedPdfPath, targets[0]);
                console.log('Mirrored to main target:', targets[0]);
            } catch (e) {
                // Ignore lock
            }
        }

        // Generate PNG
        const element = await page.$('.label-sheet');
        if (element) {
            const pngPath = path.join(labelDir, item.pngName);
            await element.screenshot({
                path: pngPath,
                type: 'png'
            });
            console.log('Saved PNG:', pngPath);
        }

        await page.close();
    }

    await browser.close();
    console.log('Render script completed successfully!');
})();
