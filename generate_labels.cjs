const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, 'public/assets/monsmecta_blue_label.html');
const content = fs.readFileSync(src, 'utf-8');

function replaceColors(theme, baseBg, baseBorder, secondaryBg) {
    let newContent = content;
    // Replace hex colors first
    newContent = newContent.replace(/bg-\[\#1e3a8a\]/g, `bg-[${baseBg}]`);
    newContent = newContent.replace(/border-\[\#1e40af\]/g, `border-[${baseBorder}]`);
    newContent = newContent.replace(/bg-\[\#1e40af\]/g, `bg-[${secondaryBg}]`);
    newContent = newContent.replace(/text-\[\#1e40af\]/g, `text-[${baseBorder}]`);

    // Replace Tailwind 'blue' with the theme color
    newContent = newContent.replace(/blue-/g, `${theme}-`);
    return newContent;
}

// 1. Green theme (녹색조)
let greenContent = replaceColors('green', '#14532d', '#166534', '#166534');
greenContent = greenContent.replace('Blue Label Design', 'Green Label Design');
fs.writeFileSync(path.join(__dirname, 'public/assets/monsmecta_green_label.html'), greenContent);

// 2. Orange/Vermillion theme (주홍색조)
let orangeContent = replaceColors('orange', '#7c2d12', '#9a3412', '#9a3412');
orangeContent = orangeContent.replace('Blue Label Design', 'Orange Label Design');
orangeContent = orangeContent.replace(/orange-400/g, 'yellow-300');
orangeContent = orangeContent.replace(/orange-600/g, 'yellow-500');
fs.writeFileSync(path.join(__dirname, 'public/assets/monsmecta_orange_label.html'), orangeContent);

// 3. Bird theme - Amber (조류)
let amberContent = replaceColors('amber', '#78350f', '#92400e', '#92400e');
amberContent = amberContent.replace('Blue Label Design', 'Bird Amber Label Design');
amberContent = amberContent.replace(/orange-400/g, 'lime-400');
amberContent = amberContent.replace(/orange-600/g, 'lime-600');
fs.writeFileSync(path.join(__dirname, 'public/assets/monsmecta_amber_label.html'), amberContent);

// 4. Bird theme 2 - Teal (조류 2)
let tealContent = replaceColors('teal', '#134e4a', '#115e59', '#115e59');
tealContent = tealContent.replace('Blue Label Design', 'Bird Teal Label Design');
fs.writeFileSync(path.join(__dirname, 'public/assets/monsmecta_teal_label.html'), tealContent);

console.log('Successfully generated 4 new color variations!');
