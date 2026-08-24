#!/usr/bin/env node
/**
 * 인코딩 무결성 검사기 (배포 게이트)
 *
 * 배경: 2026-08 커밋 a493cce에서 Windows 기본 코드페이지(cp949)로 HTML을
 * 읽고/쓰는 ad-hoc 편집 때문에 dashboard ko/ja/zh/es/fr의 한글이
 * U+FFFD/'?'로 유실되어 배포된 적이 있다.
 *
 * 이 검사는 public/ 하위 HTML과 src/locales 하위 JSON에서
 *   1) U+FFFD (치환 문자)
 *   2) 3개 이상 연속된 '?'
 * 를 발견하면 실패(exit 1)시켜 손상된 파일이 배포되는 것을 차단한다.
 *
 * 주의: 이 저장소의 파일을 편집할 때는 항상 UTF-8을 명시할 것.
 *  - Python: open(path, encoding="utf-8")
 *  - Node: fs.readFileSync(path, "utf8")
 *  - PowerShell 5.1: Get-Content/Set-Content -Encoding UTF8 (기본값은 ANSI)
 */
const fs = require('fs');
const path = require('path');

const ROOTS = ['public', 'src/locales'];
const EXTS = new Set(['.html', '.json']);
const MAX_REPORT = 30;

function* walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* walk(full);
    else if (EXTS.has(path.extname(entry.name).toLowerCase())) yield full;
  }
}

const problems = [];
for (const root of ROOTS) {
  const rootPath = path.join(__dirname, '..', root);
  if (!fs.existsSync(rootPath)) continue;
  for (const file of walk(rootPath)) {
    const rel = path.relative(path.join(__dirname, '..'), file);
    const text = fs.readFileSync(file, 'utf8');
    const lines = text.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].includes('\uFFFD')) {
        problems.push(`${rel}:${i + 1}: U+FFFD 치환 문자 발견 (인코딩 손상)`);
      }
      if (/\?{3,}/.test(lines[i])) {
        problems.push(`${rel}:${i + 1}: '???' 연속 물음표 (인코딩 손상 의심)`);
      }
    }
  }
}

if (problems.length > 0) {
  console.error('\n[check-encoding] 인코딩 손상 발견 — 배포를 중단합니다.\n');
  problems.slice(0, MAX_REPORT).forEach((p) => console.error('  ' + p));
  if (problems.length > MAX_REPORT) {
    console.error(`  ... 외 ${problems.length - MAX_REPORT}건`);
  }
  console.error(
    `\n총 ${problems.length}건. 최근 편집에서 UTF-8이 아닌 인코딩으로 파일을 읽거나 쓰지 않았는지 확인하세요.` +
      '\n손상된 파일은 git 이력에서 손상 이전 버전으로 복구해야 합니다 (U+FFFD는 되돌릴 수 없음).\n'
  );
  process.exit(1);
}

console.log('[check-encoding] HTML/JSON 인코딩 무결성 OK');
