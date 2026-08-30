const fs = require('fs');
const { execSync } = require('child_process');

const logPath = 'C:\\Users\\master\\agrolib\\obsidian_log.md';
const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
const logEntry = `\n- **[${now}] [monsmecta_landing]**: 원내 A4 알림판(notice_a4_winner_poster.html) 디자인을 보호자 감성·공감형으로 개선. 상단 공감 후킹 배지(하트비트 애니메이션), 증상 아이콘 카드 5종(구토/설사/복통/식욕부진/기력저하), 가격 박스 상단 신뢰 배지(수의사 임상 처방·전 축종) 및 소프트 글로우 추가. A4 규격(800×1131px) 오버플로 없이 렌더링 검증 완료.\n`;

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
