const fs = require('fs');
const path = require('path');

const files = [
    'monsmecta_green_label.html',
    'monsmecta_green_label_en.html'
];

for (const file of files) {
    const p = path.join(__dirname, 'public', 'assets', file);
    if (!fs.existsSync(p)) continue;
    
    let content = fs.readFileSync(p, 'utf-8');
    
    // Replace hex colors to match the landing page brand color (#00513b, #004230)
    content = content.replace(/#14532d/g, '#00513b');
    content = content.replace(/#166534/g, '#004230');
    
    // Replace specific Tailwind green classes with brand-specific darker greens
    content = content.replace(/bg-green-900\/50/g, 'bg-[#00281d]/60');
    content = content.replace(/bg-green-900\/40/g, 'bg-[#00281d]/40');
    
    // Replace the rest of Tailwind 'green' with 'emerald' which is a more bluish-green
    // matching the brand vibe better than the default yellowish-green.
    content = content.replace(/-green-/g, '-emerald-');
    
    fs.writeFileSync(p, content);
}
console.log('Updated green labels to match landing page brand color');
