@echo off
chcp 65001 > nul
echo ========================================================
echo   MONSMECTA 마케팅 컨텐츠 생성 및 자동 배포 공장 가동
echo ========================================================
echo.
echo [1/2] 55일령 발작 푸들 임상 기반 숏폼/커뮤니티 원고 생성 중...
node scripts/marketing/content_generator.cjs
echo.
echo [2/2] 멀티채널 마케팅 마스터 엔진 가동 (100배거 파이프라인)...
python scripts/marketing/monsmecta_marketing_master.py
echo.
echo ========================================================
echo   완료! scripts/marketing/output/ 폴더를 확인하세요.
echo ========================================================
pause
