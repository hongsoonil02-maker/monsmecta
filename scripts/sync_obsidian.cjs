const fs = require('fs');
const { execSync } = require('child_process');

const logPath = 'C:\\Users\\master\\agrolib\\obsidian_log.md';
const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
const logEntry = `\n- **[${now}] [monsmecta_landing]**: 다큐멘터리/자필차트/직캠플레이어/편지/오디오/결제박스/푸터 전역 짙은 검초록 배경 완전 제거 및 밝은 라이트 테마 전면 전환, 직캠 플레이어 및 비디오 아카이브 카드 밝은 화이트 테마 전환, 인포그래픽(SECTION 1~5) 한글+영문 줄맞춤 2줄 첫글자 세로 정렬(flex items-start) 완벽 교정 완료.\n`;

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
