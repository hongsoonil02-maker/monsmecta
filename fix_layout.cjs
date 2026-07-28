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
    
    // Fix the flex layout issue by correctly closing the inner flex container
    // and restoring the outer container to a simple div
    content = content.replace(
        /<div class="flex justify-center w-full">\s*<div\s*class="inline-block text-center bg-([^"]+) border border-([^"]+) rounded-full px-4 py-1\.5 mb-6">\s*<span class="([^"]+)">Veterinary Exclusive Gut Health<br>Premier Solution<\/span>\s*<\/div>/g,
        '<div>\n                        <div class="w-full flex justify-center">\n                            <div class="inline-block text-center bg-$1 border border-$2 rounded-full px-4 py-1.5 mb-6">\n                                <span class="$3">Veterinary Exclusive Gut Health<br>Premier Solution</span>\n                            </div>\n                        </div>'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Fixed flex layout issue on EN labels');
