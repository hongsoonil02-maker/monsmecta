import fs from 'fs';

const data = JSON.parse(fs.readFileSync('lookup_results.json', 'utf-8'));
const keys = Object.keys(data);
console.log('Total entries:', keys.length);

let chosenCount = 0;
let nullCount = 0;
let errorCount = 0;
const nullSamples = [];

for (const k of keys) {
  const item = data[k];
  if (item.error) errorCount++;
  if (item.chosen) {
    chosenCount++;
  } else {
    nullCount++;
    if (nullSamples.length < 15) {
      nullSamples.push(item);
    }
  }
}

console.log(`Chosen: ${chosenCount}, Null: ${nullCount}, Error: ${errorCount}`);
console.log('Sample Null entries:\n', JSON.stringify(nullSamples, null, 2));
