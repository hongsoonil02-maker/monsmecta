import os
import subprocess
from datetime import datetime

vault_path = r"C:\Users\master\agrolib"
log_path = os.path.join(vault_path, "obsidian_log.md")

now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"\n- **{now_str}**: 몬스멕타 전 라인업 용기 100ml 교체(30ml 펌프 작동 불가 문제 개선) 및 라벨 정밀 규격 110mm x 75mm (100ml 정품 규격) 전역 리뉴얼 반영 완료.\n"

with open(log_path, "a", encoding="utf-8") as f:
    f.write(log_entry)

print("Obsidian log appended.")

cmds = [
    ["git", "add", "."],
    ["git", "commit", "-m", "auto-sync: update 100ml vessel and 110x75mm labels across monsmecta lineup"],
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
