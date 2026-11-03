import subprocess
import datetime
import os

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"""
### [{now_str}] 몬스멕타 30ml 라벨 5대 세부 레이아웃 보정 (핵심효능·성분박스·글씨크기·용법용량·주의사항)
- 좌측 핵심효능 배지 및 내부 텍스트 상하 정중앙 배치, 5가지 복합체 성분 박스 상·하단 여백 확장.
- 우측 사료의 종류와 명칭 글씨 크기를 등록성분량(1.08mm)과 동일하게 맞추고, 용법용량 박스 수직 중앙 정렬 및 주의사항 박스 내 줄간격/상하 여백 균일화 완료.
"""

vault_path = r"C:\Users\master\agrolib"
log_path = os.path.join(vault_path, "obsidian_log.md")

try:
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("Obsidian log entry appended successfully.")
except Exception as e:
    print(f"Error appending log: {e}")

try:
    subprocess.run(["git", "add", "."], cwd=vault_path, check=True)
    subprocess.run(["git", "commit", "-m", "auto-sync: dev log update (fix seller name and label bottom crop)"], cwd=vault_path, check=True)
    subprocess.run(["git", "push"], cwd=vault_path, check=True)
    print("Agrolib git sync completed successfully.")
except Exception as e:
    print(f"Git sync error or already clean: {e}")
