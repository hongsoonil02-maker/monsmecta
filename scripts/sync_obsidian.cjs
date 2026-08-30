const fs = require('fs');
const { execSync } = require('child_process');

const logPath = 'C:\\Users\\master\\agrolib\\obsidian_log.md';
const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
const logEntry = `\n- **[${now}] [monsmecta_landing]**: A4 알림판 product-showcase 섹션(실사 사진+핵심 성분+효능) 세로 밀도 약 20% 축소 — 사진 max-height 320px, 성분/효능 폰트·패딩·간격 일괄 압축으로 페이지 넘침 방지 및 답답함 해소. A4 규격(scrollHeight 1123px = clientHeight, 오버플로 0) 검증 통과.\n`;

try {
  fs.appendFileSync(logPath, logEntry, 'utf8');
  console.log('Appended log to obsidian_log.md successfully.');
} catch (err) {
  console.error('Failed to append log:', err.message);
}

try {
  const addRes = execSync('git -C "C:\\Users\\master\\agrolib" add .', { encoding: 'utf8' });
  console.log('git add:', addRes);
  const commitRes = execSync('git -C "C:\\Users\\master\\agrolib" commit -m "auto-sync: dev log update"', { encoding: 'utf8' });
  console.log('git commit:', commitRes);
  const pushRes = execSync('git -C "C:\\Users\\master\\agrolib" push', { encoding: 'utf8' });
  console.log('git push:', pushRes);
  console.log('agrolib auto-sync completed successfully.');
} catch (err) {
  console.log('Git output / notice:', err.stdout || err.message);
}
