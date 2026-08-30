const fs = require('fs');
const { execSync } = require('child_process');

const logPath = 'C:\\Users\\master\\agrolib\\obsidian_log.md';
const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
const logEntry = `\n- **[${now}] [monsmecta_landing]**: 모바일 히어로 섹션 메인 카피를 '임상수의사의 해답'과 'MONSMECTA'로 줄바꿈(개행 분리) 적용 및 10종 라인업 hero title 일괄 동기화 완료.\n`;

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
