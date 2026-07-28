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
    
    // Add ml-4 to the inline-block badge to shift it to the right
    content = content.replace(
        /class="inline-block text-center ([^"]+ rounded-full px-4 py-1\.5 mb-6)"/,
        'class="inline-block text-center ml-4 $1"'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Badge shifted right in all labels');
