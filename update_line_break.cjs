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
    
    // Replace the wrapping behavior with a specific <br> placement
    content = content.replace(
        /Veterinary Exclusive Gut\s*Health Premier Solution/g,
        'Veterinary Exclusive Gut Health<br>Premier Solution'
    );
    
    fs.writeFileSync(p, content);
}
console.log('Line break updated in all labels');
