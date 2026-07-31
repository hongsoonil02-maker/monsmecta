const xlsx = require('xlsx');

const data = [
  ['발급번호 : Ø1T2-CZX3-J0D0-8T2X-035B'],
  [],
  ['원재료명 또는 성분명 및 배합비율'],
  ['No.', '원재료명 또는 성분명', '배합비율(%)'],
  [1, '유산균혼합분말 [ 1.0 x 10^8 CFU/g ]', '10%'],
  [2, '└ Lactobacillus plantarum', '1.496%'],
  [3, '└ Lactobacillus paracasei', '1.496%'],
  [4, '└ Bifidobacterium longum', '1.496%'],
  [5, '└ Lactobacillus rhamnosus', '1.122%'],
  [6, '└ Bifidobacterium infantis', '0.934%'],
  [7, '└ Leuconostoc citreum', '0.93%'],
  [8, '└ Streptococcus thermophilus', '0.748%'],
  [9, '└ Lactobacillus casei', '0.468%'],
  [10, '└ Bifidobacterium breve', '0.186%'],
  [11, '└ Bifidobacterium lactis', '0.186%'],
  [12, '└ Bifidobacterium bifidum', '0.186%'],
  [13, '└ Lactobacillus acidophilus', '0.094%'],
  [14, '└ Lactobacillus reuteri', '0.094%'],
  [15, '└ Lactobacillus bulgaricus', '0.094%'],
  [16, '└ Lactobacillus fermentum', '0.094%'],
  [17, '└ Lactobacillus gasseri', '0.094%'],
  [18, '└ Lactobacillus salivarius', '0.094%'],
  [19, '└ Lactobacillus helveticus', '0.094%'],
  [20, '└ Lactococcus lactis subsp. lactis', '0.094%'],
  [21, '분말결정포도당', '20%']
];

const wb = xlsx.utils.book_new();
const ws = xlsx.utils.aoa_to_sheet(data);

// Adjust column widths
ws['!cols'] = [
  { wch: 8 },  // No.
  { wch: 45 }, // Name
  { wch: 15 }  // Ratio
];

xlsx.utils.book_append_sheet(wb, ws, '배합비율');
xlsx.writeFile(wb, 'c:\\\\Users\\\\master\\\\monsmecta-landing\\\\public\\\\assets\\\\probiotics_composition.xlsx');
console.log('Excel file created successfully!');
