# -*- coding: utf-8 -*-
"""
몬스멕타 유스 에디션 라벨 10종(02~11) 일괄 생성기
- 베이스: 01_monsmecta_original_youth.html (유스 템플릿)
- 콘텐츠: 각 제품의 모던판(NN_..._modern.html)에서 제품별 블록을 추출해 이식
- 컬러: 유스 밝은 테마를 유지하며 제품 고유색(deep/accent/pop)으로 치환
"""
import io
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(BASE_DIR, "01_monsmecta_original_youth.html")

DEEP_BASE = "#0b3b2c"
ACCENT_BASE = "#0e9f6e"
POP_BASE = "#d9f548"
DEEP_RGBA_BASE = "rgba(12,59,44"   # 유스 템플릿의 그림자 rgba 접두사

PRODUCTS = [
    # (번호, 파일키, 한글명, deep, accent, pop)
    ("02", "hepamax",     "헤파맥스",       "#431206", "#ea4c10", "#fed7aa"),
    ("03", "renal",       "레날 디톡스",     "#0b203d", "#2563eb", "#bfdbfe"),
    ("04", "cancercare",  "캔서케어",       "#3b0764", "#9333ea", "#e9d5ff"),
    ("05", "coldzero",    "콜드제로",       "#083344", "#0891b2", "#a5f3fc"),
    ("06", "skincare",    "스킨케어",       "#500724", "#db2777", "#fbcfe8"),
    ("07", "heartcare",   "하트케어",       "#450a0a", "#dc2626", "#fecaca"),
    ("08", "jointcare",   "조인트케어",     "#1a2e05", "#65a30d", "#d9f99d"),
    ("09", "powerase",    "파워에이스",     "#431407", "#ea580c", "#fed7aa"),
    ("10", "probiotics",  "프로바이오틱스", "#052e16", "#16a34a", "#bbf7d0"),
    ("11", "vitaplus",    "비타플러스",     "#422006", "#ca8a04", "#fef08a"),
]


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def extract_div_inner(html, marker):
    """marker로 시작하는 div의 내부 HTML을 균형 카운팅으로 추출."""
    start = html.find(marker)
    if start < 0:
        raise ValueError("marker not found: " + marker)
    open_end = html.find(">", start) + 1
    depth = 1
    pos = open_end
    token = re.compile(r"<div\b|</div>")
    while True:
        m = token.search(html, pos)
        if not m:
            raise ValueError("unbalanced div for: " + marker)
        if m.group(0) == "<div":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return html[open_end:m.start()]
        pos = m.end()


def replace_div_inner(html, marker, new_inner):
    """marker로 시작하는 div의 내부 HTML을 교체."""
    start = html.find(marker)
    if start < 0:
        raise ValueError("marker not found for replace: " + marker)
    open_end = html.find(">", start) + 1
    depth = 1
    pos = open_end
    token = re.compile(r"<div\b|</div>")
    while True:
        m = token.search(html, pos)
        if not m:
            raise ValueError("unbalanced div for replace: " + marker)
        if m.group(0) == "<div":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return html[:open_end] + new_inner + html[m.start():]
        pos = m.end()


def grab(pattern, html, name):
    m = re.search(pattern, html, re.S)
    if not m:
        raise ValueError("pattern not found: " + name)
    return m.group(1)


def main():
    template = io.open(TEMPLATE, encoding="utf-8").read()

    for num, key, kname, deep, accent, pop in PRODUCTS:
        modern_path = os.path.join(BASE_DIR, "%s_monsmecta_%s_modern.html" % (num, key))
        modern = io.open(modern_path, encoding="utf-8").read()

        # --- 콘텐츠 추출 ---
        tagline = grab(r'<span class="tag">([^<]+)</span>', modern, "tagline")
        sub_name = grab(r'<div class="brand-sub-name">([^<]+)</div>', modern, "sub_name")
        sub_en = grab(r'<span class="brand-sub-en en">(.*?)</span>', modern, "sub_en").strip()
        fx100 = extract_div_inner(modern, '<div class="fx-card fx-card-100">')
        fx30 = extract_div_inner(modern, '<div class="fx-card fx-card-30" style="display:none;">')
        ing_ti = grab(r'<span class="ti">([^<]+)</span>', modern, "ing_ti")
        ing100 = extract_div_inner(modern, '<div class="ing-body-100">')
        ing30 = extract_div_inner(modern, '<div class="ing-body-30" style="display:none;">')
        lg_head = extract_div_inner(modern, '<div class="lg-head">')
        lg_body = extract_div_inner(modern, '<div class="lg-body">')
        dose = extract_div_inner(modern, '<div class="dose">')
        warn = extract_div_inner(modern, '<div class="warn">')
        meta = extract_div_inner(modern, '<div class="meta">')

        out = template

        # --- 컬러 치환 (16진수 + 그림자 rgba) ---
        dr, dg, db = hex_to_rgb(deep)
        ar, ag, ab = hex_to_rgb(accent)
        pr, pg, pb = hex_to_rgb(pop)
        out = out.replace(DEEP_RGBA_BASE, "rgba(%d,%d,%d" % (dr, dg, db))
        out = out.replace("rgba(14,159,110", "rgba(%d,%d,%d" % (ar, ag, ab))
        out = out.replace("rgba(217,245,72", "rgba(%d,%d,%d" % (pr, pg, pb))
        out = out.replace(DEEP_BASE, deep)
        out = out.replace(ACCENT_BASE, accent)
        out = out.replace(POP_BASE.lower(), pop)
        out = out.replace(POP_BASE.upper(), pop)
        # SVG data-URI 내 인코딩된 컬러 (%23d9f548 등)
        out = out.replace("%23" + POP_BASE[1:], "%23" + pop[1:])
        out = out.replace("%23" + ACCENT_BASE[1:], "%23" + accent[1:])
        out = out.replace("%23" + DEEP_BASE[1:], "%23" + deep[1:])

        # --- 타이틀/툴바/가이드 문구 ---
        out = out.replace(
            "<title>몬스멕타 Label (유스 에디션 TEST · 100ml / 30ml)</title>",
            "<title>몬스멕타 %s Label (유스 에디션 TEST · 100ml / 30ml)</title>" % kname)
        out = out.replace("몬스멕타 유스 에디션", "몬스멕타 %s 유스 에디션" % kname)

        # --- 히어로: 태그라인 + 2단 타이틀 ---
        out = out.replace('<span class="tag">연변 시 장 기능 개선 및 정장 작용에 뛰어난</span>',
                          '<span class="tag">%s</span>' % tagline, 1)
        new_ttl = (
            '\n                <div class="brand-sub-main">몬스멕타<sup class="tm">™</sup></div>\n'
            '                <div class="brand-sub-name">%s</div>\n'
            '                <span class="title-under title-under-sub"></span>\n'
            '                <span class="brand-sub-en en">%s</span>\n              ' % (sub_name, sub_en))
        out = replace_div_inner(out, '<div class="ttl-wrap">', new_ttl)

        # --- 핵심 효능 카드 ---
        out = replace_div_inner(out, '<div class="fx-card fx-card-100">', fx100)
        out = replace_div_inner(out, '<div class="fx-card fx-card-30" style="display:none;">', fx30)

        # --- 성분 카드 ---
        out = out.replace('<span class="ti">성분(5가지 복합체)</span>',
                          '<span class="ti">%s</span>' % ing_ti, 1)
        out = replace_div_inner(out, '<div class="ing-body-100">', ing100)
        out = replace_div_inner(out, '<div class="ing-body-30" style="display:none;">', ing30)

        # --- 법정 고시란 ---
        out = replace_div_inner(out, '<div class="lg-head">', lg_head)
        out = replace_div_inner(out, '<div class="lg-body">', lg_body)
        out = replace_div_inner(out, '<div class="dose">', dose)
        out = replace_div_inner(out, '<div class="warn">', warn)
        out = replace_div_inner(out, '<div class="meta">', meta)

        out_path = os.path.join(BASE_DIR, "%s_monsmecta_%s_youth.html" % (num, key))
        io.open(out_path, "w", encoding="utf-8", newline="\n").write(out)
        print("generated: %s (%s %s)" % (os.path.basename(out_path), kname, accent))


if __name__ == "__main__":
    main()
