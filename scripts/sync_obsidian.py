import subprocess
import datetime
import os

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"""
### [{now_str}] 몬스멕타 전 라인업(11종) 30ml 라벨 화이트 뒷면(Type B) 및 선택 토글 뷰 생성 완료
- 몬스멕타 11종 전체 라인업(85x40mm)에 원본 올 다크(Type A)와 화이트 뒷면(Type B) 토글 및 비교 뷰 구축.
- 원본 제조사/판매원 정보(에스앤제이 동물병원 용인, 엠오바이오 화성) 100% 원본 유지 및 고해상도 인쇄용 PDF/PNG 산출물 생성 완료.
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
    subprocess.run(["git", "commit", "-m", "auto-sync: dev log update (all 11 monsmecta labels white-back toggle support)"], cwd=vault_path, check=True)
    subprocess.run(["git", "push"], cwd=vault_path, check=True)
    print("Agrolib git sync completed successfully.")
except Exception as e:
    print(f"Git sync error or already clean: {e}")
