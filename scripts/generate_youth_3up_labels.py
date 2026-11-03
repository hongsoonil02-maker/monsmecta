# -*- coding: utf-8 -*-
"""
몬스멕타 유스 에디션 30ml 3구(3-up) A4 실측 인쇄용 PDF 생성기
- 01_monsmecta_original_youth.html
- 02_monsmecta_hepamax_youth.html
- 03_monsmecta_renal_youth.html

1장 A4 용지에 101mm x 42mm (좌7 + 중7 + 우3mm) 라벨 3개를 코너 재단선 및 50mm 실측 눈금자와 함께 배치.
"""
import os
import sys
import shutil
import pathlib
from playwright.sync_api import sync_playwright
import pymupdf

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LABELS_DIR = os.path.join(BASE_DIR, "public", "assets", "labels")
DESKTOP_DIR = r"C:\Users\master\Desktop\몬스멕타_인쇄소전달용_85x40mm"
PREVIEW_DIR = os.path.join(BASE_DIR, "scratch", "youth_3up_test")

os.makedirs(LABELS_DIR, exist_ok=True)
os.makedirs(DESKTOP_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)

TARGETS = [
    {
        "id": "01",
        "file": "01_monsmecta_original_youth.html",
        "title": "몬스멕타 오리지널",
        "color": "#0b3b2c",
        "pdf_en": "01_monsmecta_original_youth_30ml_3up.pdf",
        "pdf_ko": "01_몬스멕타_유스_30ml_3구_A4실측.pdf"
    },
    {
        "id": "02",
        "file": "02_monsmecta_hepamax_youth.html",
        "title": "몬스멕타 헤파맥스",
        "color": "#431206",
        "pdf_en": "02_monsmecta_hepamax_youth_30ml_3up.pdf",
        "pdf_ko": "02_몬스멕타_헤파맥스_유스_30ml_3구_A4실측.pdf"
    },
    {
        "id": "03",
        "file": "03_monsmecta_renal_youth.html",
        "title": "몬스멕타 레날디톡스",
        "color": "#0b203d",
        "pdf_en": "03_monsmecta_renal_youth_30ml_3up.pdf",
        "pdf_ko": "03_몬스멕타_레날디톡스_유스_30ml_3구_A4실측.pdf"
    }
]

def safe_copy(src, dst):
    try:
        shutil.copyfile(src, dst)
        return dst
    except Exception as e:
        alt = dst.replace(".pdf", "_new.pdf")
        shutil.copyfile(src, alt)
        return alt

def generate():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # 1. 개별 3구 PDF 생성 (01, 02, 03)
        for t in TARGETS:
            page = browser.new_page(viewport={"width": 1280, "height": 1400})
            html_uri = pathlib.Path(os.path.join(LABELS_DIR, t["file"])).resolve().as_uri()
            page.goto(f"{html_uri}?size=30")
            page.wait_for_timeout(400)
            
            page.evaluate(f"""() => {{
                if (typeof setSize === 'function') setSize('30');
                if (typeof setPaper === 'function') setPaper('a4');
                
                const titleEl = document.querySelector('.a4-header-guide h2');
                if (titleEl) {{
                    titleEl.textContent = '[30ml 실물 테스트용] {t['title']} 유스 3구 실측 라벨 (좌측 7mm + 중간 7mm + 우측 3mm 접착 = 총 101×42mm × 3개)';
                }}
                
                const originalCropBox = document.querySelector('.crop-marks-box');
                if (!originalCropBox) return;
                
                const container = document.createElement('div');
                container.className = 'multi-label-print-container';
                container.style.display = 'flex';
                container.style.flexDirection = 'column';
                container.style.alignItems = 'center';
                container.style.gap = '8mm';
                container.style.marginTop = '2mm';
                container.style.width = '100%';
                
                for (let i = 1; i <= 3; i++) {{
                    const itemWrap = document.createElement('div');
                    itemWrap.style.display = 'flex';
                    itemWrap.style.flexDirection = 'column';
                    itemWrap.style.alignItems = 'center';
                    
                    const tag = document.createElement('div');
                    tag.style.textAlign = 'center';
                    tag.style.fontSize = '7.5pt';
                    tag.style.fontWeight = '700';
                    tag.style.color = '#64748b';
                    tag.style.marginBottom = '1.5mm';
                    tag.textContent = '▼ 테스트 라벨 #' + i + ' ({t['title']} 유스 / 좌 7 + 중 7 + 우 3 = 총 101×42mm)';
                    
                    const clone = originalCropBox.cloneNode(true);
                    clone.style.margin = '0 auto';
                    
                    itemWrap.appendChild(tag);
                    itemWrap.appendChild(clone);
                    container.appendChild(itemWrap);
                }}
                
                originalCropBox.parentNode.replaceChild(container, originalCropBox);
                
                const header = document.querySelector('.a4-header-guide');
                if (header) {{
                    header.style.marginBottom = '3mm';
                }}
                const cutInst = document.querySelector('.a4-cut-instructions');
                if (cutInst) {{
                    cutInst.style.marginTop = '4mm';
                    cutInst.style.fontSize = '7.5pt';
                }}
            }}""")
            page.wait_for_timeout(300)
            page.emulate_media(media="print")
            page.wait_for_timeout(200)
            
            target_en = os.path.join(LABELS_DIR, t["pdf_en"])
            page.pdf(
                path=target_en,
                format="A4",
                print_background=True,
                margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
            )
            
            # 복사 및 검증
            target_ko = os.path.join(LABELS_DIR, t["pdf_ko"])
            safe_copy(target_en, target_ko)
            safe_copy(target_en, os.path.join(DESKTOP_DIR, t["pdf_en"]))
            safe_copy(target_en, os.path.join(DESKTOP_DIR, t["pdf_ko"]))
            
            doc = pymupdf.open(target_en)
            print(f"[{t['title']}] PDF 생성 완료: {t['pdf_en']} (페이지 수: {len(doc)})")
            pix = doc[0].get_pixmap(dpi=150)
            pix.save(os.path.join(PREVIEW_DIR, f"{t['id']}_preview_page.png"))
            doc.close()
            page.close()
        
        # 2. 3종 통합본(콤보) 3구 PDF 생성 (오리지널 + 헤파맥스 + 레날디톡스 각 1개씩 총 3구)
        print("\n=== 3종 통합 콤보 3구 A4 PDF 생성 중 ===")
        cb_list = []
        for t in TARGETS:
            p_sub = browser.new_page()
            html_uri = pathlib.Path(os.path.join(LABELS_DIR, t["file"])).resolve().as_uri()
            p_sub.goto(f"{html_uri}?size=30")
            p_sub.wait_for_timeout(350)
            p_sub.evaluate("() => { if (typeof setSize === 'function') setSize('30'); if (typeof setPaper === 'function') setPaper('a4'); }")
            p_sub.wait_for_timeout(200)
            cb_list.append(p_sub.evaluate("() => document.querySelector('.crop-marks-box').outerHTML"))
            p_sub.close()
            
        combo_page = browser.new_page(viewport={"width": 1280, "height": 1400})
        combo_uri = pathlib.Path(os.path.join(LABELS_DIR, TARGETS[0]["file"])).resolve().as_uri()
        combo_page.goto(f"{combo_uri}?size=30")
        combo_page.wait_for_timeout(350)
        
        combo_page.evaluate("""(data) => {
            if (typeof setSize === 'function') setSize('30');
            if (typeof setPaper === 'function') setPaper('a4');
            
            const titleEl = document.querySelector('.a4-header-guide h2');
            if (titleEl) {
                titleEl.textContent = '[30ml 유스 에디션] 몬스멕타 3종 통합 실측 라벨 (좌7+중7+우3mm / 101×42mm)';
            }
            const originalCropBox = document.querySelector('.crop-marks-box');
            if (!originalCropBox) return;
            
            const container = document.createElement('div');
            container.className = 'multi-label-print-container';
            container.style.display = 'flex';
            container.style.flexDirection = 'column';
            container.style.alignItems = 'center';
            container.style.gap = '8mm';
            container.style.marginTop = '2mm';
            container.style.width = '100%';
            
            const itemsMeta = [
                { title: '▼ 1. 몬스멕타™ 오리지널 유스 (에메랄드) - 좌측 7mm + 중간 7mm + 우측 3mm 접착 (총 101×42mm)', color: '#0b3b2c' },
                { title: '▼ 2. 몬스멕타™ 헤파맥스 유스 (앰버골드) - 좌측 7mm + 중간 7mm + 우측 3mm 접착 (총 101×42mm)', color: '#451a03' },
                { title: '▼ 3. 몬스멕타™ 레날디톡스 유스 (인디고바이올렛) - 좌측 7mm + 중간 7mm + 우측 3mm 접착 (총 101×42mm)', color: '#1e1b4b' }
            ];
            
            for (let i = 0; i < 3; i++) {
                const tag = document.createElement('div');
                tag.style.textAlign = 'center';
                tag.style.fontSize = '7.5pt';
                tag.style.fontWeight = '800';
                tag.style.color = itemsMeta[i].color;
                tag.style.marginBottom = '1.5mm';
                tag.textContent = itemsMeta[i].title;
                
                const wrap = document.createElement('div');
                wrap.style.display = 'flex';
                wrap.style.flexDirection = 'column';
                wrap.style.alignItems = 'center';
                wrap.appendChild(tag);
                
                const div = document.createElement('div');
                div.innerHTML = data.items[i];
                wrap.appendChild(div.firstElementChild);
                container.appendChild(wrap);
            }
            
            originalCropBox.parentNode.replaceChild(container, originalCropBox);
            
            const header = document.querySelector('.a4-header-guide');
            if (header) {
                header.style.marginBottom = '3mm';
            }
            const cutInst = document.querySelector('.a4-cut-instructions');
            if (cutInst) {
                cutInst.style.marginTop = '4mm';
                cutInst.style.fontSize = '7.5pt';
            }
        }""", {"items": cb_list})
        
        combo_page.wait_for_timeout(300)
        combo_page.emulate_media(media="print")
        combo_page.wait_for_timeout(200)
        
        combo_pdf_en = "00_monsmecta_youth_30ml_3up_combo.pdf"
        combo_pdf_ko = "00_몬스멕타_유스_30ml_3종통합_3구_A4실측.pdf"
        combo_path_en = os.path.join(LABELS_DIR, combo_pdf_en)
        combo_path_ko = os.path.join(LABELS_DIR, combo_pdf_ko)
        
        combo_page.pdf(
            path=combo_path_en,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        safe_copy(combo_path_en, combo_path_ko)
        safe_copy(combo_path_en, os.path.join(DESKTOP_DIR, combo_pdf_en))
        safe_copy(combo_path_en, os.path.join(DESKTOP_DIR, combo_pdf_ko))
        
        doc = pymupdf.open(combo_path_en)
        print(f"[3종 통합] PDF 생성 완료: {combo_pdf_en} (페이지 수: {len(doc)})")
        pix = doc[0].get_pixmap(dpi=150)
        pix.save(os.path.join(PREVIEW_DIR, "00_combo_preview_page.png"))
        doc.close()
        combo_page.close()
        
        browser.close()

if __name__ == "__main__":
    generate()

