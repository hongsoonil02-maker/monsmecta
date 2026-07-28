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
    let content = fs.readFileSync(p, 'utf-8');
    
    // Add text-center to the inline-block container
    content = content.replace(/class="inline-block ([^"]+ rounded-full px-4 py-1\.5 mb-6)"/, 'class="inline-block text-center $1"');
    
    fs.writeFileSync(p, content);
}
console.log('Text centered in all labels');
