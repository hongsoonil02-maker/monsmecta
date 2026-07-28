const fs = require('fs');
const path = require('path');

const files = [
    'monsmecta_blue_label_en.html',
    'monsmecta_green_label_en.html',
    'monsmecta_orange_label_en.html',
    'monsmecta_amber_label_en.html',
    'monsmecta_teal_label_en.html'
];

for (const file of files) {
    const p = path.join(__dirname, 'public', 'assets', file);
    if (!fs.existsSync(p)) continue;
    
    let content = fs.readFileSync(p, 'utf-8');
    
    // 1. Center the top badge by wrapping it in a flex center div and removing ml-10
    content = content.replace(
        /<div>\s*<div\s*class="inline-block text-center ml-10 /g,
        '<div class="flex justify-center w-full">\n                        <div\n                            class="inline-block text-center '
    );

    // 2. Center the text block (subtitle, h1, h2) and change H2 to FOR BIRDS
    content = content.replace(
        /<div class="ml-10">\s*<p class="text-sm font-semibold ([^"]+) mb-2 tracking-wide">([^<]+)<\/p>\s*<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 ml-4">MONSMECTA<\/h1>\s*<h2 class="text-2xl font-bold montserrat ([^"]+) tracking-\[0\.2em\] mb-10 ml-4">([^<]+)<\/h2>\s*<\/div>/g,
        '<div class="w-full text-center flex flex-col items-center">\n                            <p class="text-sm font-semibold $1 mb-2 tracking-wide text-center">$2</p>\n                            <h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 text-center">MONSMECTA</h1>\n                            <h2 class="text-2xl font-bold montserrat $3 tracking-[0.2em] mb-10 text-center">FOR BIRDS</h2>\n                        </div>'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Centered English labels and updated H2 to FOR BIRDS');
