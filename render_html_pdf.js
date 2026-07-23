import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const htmlPath = path.resolve('public/assets/monsmecta_wave1-1_dm_letter_a4.html');
const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
let browserPath = fs.existsSync(edgePath) ? edgePath : (fs.existsSync(chromePath) ? chromePath : null);

console.log('Browser path:', browserPath);

if (browserPath) {
  const outPdf1 = path.resolve('public/assets/monsmecta_wave1-1_dm_letter_a4.pdf');
  const outPdf2 = path.resolve('public/assets/tournament_variant_16.pdf');
  
  const cmd1 = `"${browserPath}" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="${outPdf1}" "file:///${htmlPath.replace(/\\/g, '/')}"`;
  console.log('Running cmd1...');
  execSync(cmd1);

  const cmd2 = `"${browserPath}" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="${outPdf2}" "file:///${htmlPath.replace(/\\/g, '/')}"`;
  console.log('Running cmd2...');
  execSync(cmd2);

  console.log('PDF generated successfully via Headless Edge!');
} else {
  console.error('No Edge or Chrome found');
}
