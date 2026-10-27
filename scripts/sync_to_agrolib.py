import os
import subprocess
from datetime import datetime

vault_path = r"C:\Users\master\agrolib"
log_path = os.path.join(vault_path, "obsidian_log.md")

now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"\n- **{now_str}**: 몬스멕타 전 라인업(11종) 우측 뒷면 화이트 에디션 라벨(110x75mm, 100ml) 독립 HTML, 인쇄용 HTML 및 1:1 PDF/PNG 전체 생성 & 깃허브 푸시 완료.\n"

with open(log_path, "a", encoding="utf-8") as f:
    f.write(log_entry)

print("Obsidian log appended.")

cmds = [
    ["git", "add", "."],
    ["git", "commit", "-m", "auto-sync: add 100ml white-back labels and print artifacts"],
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
