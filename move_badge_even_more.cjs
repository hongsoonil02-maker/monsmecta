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
    
    // Change ml-8 to ml-10 for the badge
    content = content.replace(
        /class="inline-block text-center ml-8([^"]+ rounded-full px-4 py-1\.5 mb-6)"/,
        'class="inline-block text-center ml-10$1"'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Badge shifted 2 more spaces right (ml-10) in all labels');
