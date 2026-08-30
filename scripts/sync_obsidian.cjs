const fs = require('fs');
const { execSync } = require('child_process');

const logPath = 'C:\\Users\\master\\agrolib\\obsidian_log.md';
const now = new Date().toISOString().replace('T', ' ').substring(0, 19);
const logEntry = `\n- **[${now}] [monsmecta_landing]**: 10종 라인업 세션 배경 밝은 슬레이트 라이트 테마(bg-slate-50) 및 화이트 카드로 리뉴얼, 다큐멘터리/오디오/편지/결제박스/푸터 세션 배경 전역 통일 동기화(slate-900/950), 모바일 모달 및 인포그래픽 2줄 타이틀 첫글자 세로 정렬(flex items-start) 교정, (100ml) 문구 삭제 및 파보겔 벤치마크 기반 모바일 여백/호흡감 개선 완료.\n`;

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
