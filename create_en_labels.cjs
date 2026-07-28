const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, 'public', 'assets');
const amberKrPath = path.join(dir, 'monsmecta_amber_label.html');
const amberEnPath = path.join(dir, 'monsmecta_amber_label_en.html');

// 1. Rename amber to amber_en
fs.renameSync(amberKrPath, amberEnPath);

// 2. Replacements definition
const replacements = [
    ['연변 시 장 기능 개선 및 정장 작용에 뛰어난', 'Excellent for improving bowel function & intestinal health'],
    ['<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 ml-4">몬스멕타</h1>', '<h1 class="text-6xl font-black text-white tracking-tight leading-none mb-2 ml-4">MONSMECTA</h1>'],
    ['성분\\s*\\(5가지 복합체\\)', 'Ingredients (5 Complex Formula)'],
    ['1\\) 항균·항바이러스 작용', '1) Antibacterial & Antiviral Effects'],
    ['\\- 1\\-deoxynojirimycin \\(DNJ\\) 천연성분 함유', '- Contains natural 1-deoxynojirimycin (DNJ)'],
    ['특허균주 Bacillus subtilis MORI 균주', 'Patented Strain Bacillus subtilis MORI'],
    ['2\\) 장 기능 개선 및 정장 작용', '2) Improves Bowel Function & Intestinal Health'],
    ['\\- 포도당', '- Glucose'],
    ['3\\) 상피세포의 회복', '3) Epithelial Cell Recovery'],
    ['\\- 비타민 A', '- Vitamin A'],
    ['4\\) 전해질제', '4) Electrolytes'],
    ['5\\) 연변 및 설사 개선, 독소 제거', '5) Relieves Soft Stools & Diarrhea, Removes Toxins'],
    ['\\- 몬모릴로나이트', '- Montmorillonite'],
    ['\\(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에\\s*도움\\)', '(Helps remove fungal toxins, boost immunity, and improve intestinal environment)'],
    ['사료 성분등록번호', 'Feed Registration No.'],
    ['제XX9UY0145호', 'No. XX9UY0145'],
    ['사료의 종류 및 명칭 / 형태 / 용도', 'Type & Name / Form / Purpose'],
    ['보조사료 / 미생물제 / 바실러스 서브틸리스 \\| 액상 \\| 반려동물용', 'Supplementary Feed / Microbial Agent / Bacillus subtilis | Liquid | For Pets'],
    ['등록성분량', 'Registered Ingredients Content'],
    ['바실러스 서브틸리스 1\\.0 x 10\\^7 cfu/g 이상, 부형제\\(정제수\\)', 'Bacillus subtilis ≥ 1.0 x 10^7 cfu/g, Excipient (Purified Water)'],
    ['사용한 원료의 명칭', 'Raw Materials Used'],
    ['바실러스 서브틸리스, 비타민A, 아세트산나트륨, 프로피온산나트륨, 포도당, 정제수', 'Bacillus subtilis, Vitamin A, Sodium Acetate, Sodium Propionate, Glucose, Purified Water'],
    ['▶ 효과', '▶ Benefits'],
    ['장 관련 질병\\(파보, 로타, 코로나 등\\)에 대한 저항력 향상에 도움', 'Helps improve resistance to intestinal diseases (Parvo, Rota, Corona, etc.)'],
    ['면역 기능 및 건강 상태 유지에 도움', 'Helps maintain immune function and overall health'],
    ['장 기능 개선 및 정장 작용에 도움', 'Helps improve bowel function and intestinal health'],
    ['대상축종', 'Target Animals'],
    ['송아지 , 갓난 돼지, 새끼 염소, 새끼 양, 망아지, 강아지, 고양이, 모든 동물\\(조류,파충류,어류,등등\\)', 'Calves, Piglets, Kids (Goats), Lambs, Foals, Dogs, Cats, All Animals (Birds, Reptiles, Fish, etc.)'],
    ['용법 및 용량', 'Dosage & Administration'],
    ['1일 투당 2~4ml, 5~7일간 경구 급여', 'Orally administer 2~4ml per head daily for 5~7 days'],
    ['⚠️ 주의사항', '⚠️ Cautions'],
    ['직사광선을 피하여 건조하고 서늘한 곳에 보관하십시오\\.', 'Store in a cool, dry place away from direct sunlight.'],
    ['제품 특성 상 가라앉는 성분들이 있어서', 'Due to the nature of the product, there may be sedimentation. Please'],
    ['흔들어서 사용', 'shake well'],
    ['하십시오\\.', 'before use.'],
    ['제품에 대하여 문의하실 경우 제조원 또는 판매원으로 연락하여 주시기 바랍니다\\.', 'For inquiries about the product, please contact the manufacturer or distributor.'],
    ['포장단위', 'Packaging Unit'],
    ['제조일자', 'Mfg Date'],
    ['별도표기', 'Marked Separately'],
    ['유통기한', 'Expiration Date'],
    ['제조일로부터\\s*18개월', '18 months from manufacturing date'],
    ['판매원 : \\(주\\)한국아그로', 'Distributor : KOREA AGRO Co., Ltd.'],
    ['서울특별시 마포구 큰우물로 75, 1506호\\(도화동, 성지빌딩\\)', '#1506, Seongji Bldg, 75 Keunu-mul-ro, Mapo-gu, Seoul, Republic of Korea'],
    ['제조원 : 엠오바이오', 'Manufacturer : MO BIO'],
    ['경기도 화성시 팔탄면 석포로 74번길 10-25', '10-25, Seokpo-ro 74beon-gil, Paltan-myeon, Hwaseong-si, Gyeonggi-do, Republic of Korea'],
    ['플라스틱', 'PLASTIC']
];

// 3. Restore amber KR from EN
let amberContent = fs.readFileSync(amberEnPath, 'utf-8');
for (let [kr, en] of replacements) {
    let safeEn = en.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    let safeKr = kr.replace(/\\/g, ''); 
    if (kr === '성분\\s*\\(5가지 복합체\\)') safeKr = '성분 (5가지 복합체)';
    if (kr === '\\(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에\\s*도움\\)') safeKr = '(곰팡이 독소 제거, 면역 증강 및 장 환경 개선에 도움)';
    if (kr === '제조일로부터\\s*18개월') safeKr = '제조일로부터 18개월';
    
    amberContent = amberContent.replace(new RegExp(safeEn, 'g'), safeKr);
}

// Special case for amber H2 title
amberContent = amberContent.replace(
    /<h2 class="text-2xl font-bold montserrat text-amber-200\/80 tracking-\[0\.2em\] mb-10 ml-4">PROBIOTICS<\/h2>/g, 
    '<h2 class="text-2xl font-bold montserrat text-amber-200/80 tracking-[0.2em] mb-10 ml-4">MONSMECTA</h2>'
);
fs.writeFileSync(amberKrPath, amberContent);

// 4. Generate EN versions for other 4 labels
const others = [
    { base: 'monsmecta_blue_label.html', en: 'monsmecta_blue_label_en.html', color: 'blue' },
    { base: 'monsmecta_green_label.html', en: 'monsmecta_green_label_en.html', color: 'green' },
    { base: 'monsmecta_orange_label.html', en: 'monsmecta_orange_label_en.html', color: 'orange' },
    { base: 'monsmecta_teal_label.html', en: 'monsmecta_teal_label_en.html', color: 'teal' }
];

for (const item of others) {
    let content = fs.readFileSync(path.join(dir, item.base), 'utf-8');
    
    for (const [kr, en] of replacements) {
        content = content.replace(new RegExp(kr, 'g'), en);
    }
    
    // Special case for H2 title based on color
    const h2Regex = new RegExp(`<h2 class="text-2xl font-bold montserrat text-${item.color}-200/80 tracking-\\[0\\.2em\\] mb-10 ml-4">MONSMECTA<\\/h2>`, 'g');
    const h2Replacement = `<h2 class="text-2xl font-bold montserrat text-${item.color}-200/80 tracking-[0.2em] mb-10 ml-4">PROBIOTICS</h2>`;
    content = content.replace(h2Regex, h2Replacement);
    
    fs.writeFileSync(path.join(dir, item.en), content);
}

console.log('Successfully created both KR and EN files for all 5 labels.');
