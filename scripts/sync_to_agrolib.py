import os
import subprocess
from datetime import datetime

vault_path = r"C:\Users\master\agrolib"
log_path = os.path.join(vault_path, "obsidian_log.md")

now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"\n- **{now_str}**: 몬스멕타 전 라인업(11종) 30ml 맞춤형 고가독성 신규 라벨(85x40mm) 포맷 일괄 생성 및 1:1 인쇄용 PDF, 고해상도 PNG 렌더링 완료 (고유 색상, 성분, 효능, 법정표시 완벽 반영).\n"

with open(log_path, "a", encoding="utf-8") as f:
    f.write(log_entry)

print("Obsidian log appended.")

cmds = [
    ["git", "add", "."],
    ["git", "commit", "-m", "auto-sync: dev log update (all 11 monsmecta 30ml labels)"],
    ["git", "push"]
]

for cmd in cmds:
    res = subprocess.run(cmd, cwd=vault_path, capture_output=True, text=True)
    print(f"Executed {' '.join(cmd)}: code {res.returncode}")
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())

print("Obsidian sync complete.")
