const fs = require('fs');
const path = require('path');

const files = [
    'monsmecta_blue_label.html',
    'monsmecta_green_label.html',
    'monsmecta_orange_label.html',
    'monsmecta_amber_label.html',
    'monsmecta_teal_label.html'
];

for (const file of files) {
    const p = path.join(__dirname, 'public', 'assets', file);
    if (!fs.existsSync(p)) continue;
    
    let content = fs.readFileSync(p, 'utf-8');
    
    // 1. Center the top badge by wrapping it in a flex center div and removing ml-10
    // This uses the exact safe replacement we used for the English fix
    content = content.replace(
        /<div>\s*<div\s*class="inline-block text-center ml-10 bg-([^"]+) border border-([^"]+) rounded-full px-4 py-1\.5 mb-6">\s*<span class="([^"]+)">Veterinary Exclusive Gut Health<br>Premier Solution<\/span>\s*<\/div>/g,
        '<div>\n                        <div class="w-full flex justify-center">\n                            <div class="inline-block text-center bg-$1 border border-$2 rounded-full px-4 py-1.5 mb-6">\n                                <span class="$3">Veterinary Exclusive Gut Health<br>Premier Solution</span>\n                            </div>\n                        </div>'
    );

    // 2. Center the text block (subtitle, h1, h2) for KR labels
    content = content.replace(
        /<div class="ml-10">\s*<p class="text-sm font-semibold ([^"]+) mb-2 tracking-wide">([^<]+)<\/p>\s*<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 ml-4">몬스멕타<\/h1>\s*<h2 class="text-2xl font-bold montserrat ([^"]+) tracking-\[0\.2em\] mb-10 ml-4">MONSMECTA<\/h2>\s*<\/div>/g,
        '<div class="w-full text-center flex flex-col items-center">\n                            <p class="text-sm font-semibold $1 mb-2 tracking-wide text-center">$2</p>\n                            <h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">몬스멕타</h1>\n                            <h2 class="text-2xl font-bold montserrat $3 tracking-[0.2em] mb-10 text-center">MONSMECTA</h2>\n                        </div>'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Centered Korean labels');
