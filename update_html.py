import os

src = r"C:\Users\sooni\OneDrive - Agro Korea Co.,Ltd\MONSMECTA 학술 마케팅 인포그래픽2.html"
dst = r"c:\Users\sooni\monsmecta-landing\public\assets\james_infographic.html"

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# Make modifications:
# 1. Add word-break
content = content.replace("        body {\n            font-family: 'Noto Sans KR', sans-serif;", "        * {\n            word-break: keep-all;\n            overflow-wrap: break-word;\n        }\n        body {\n            font-family: 'Noto Sans KR', sans-serif;")

# 2. Update logo path
content = content.replace('로고1_에스앤제이%20동물병원.jpg', 'sj_logo.png')
content = content.replace('onerror="handleLogoError(this)"', 'onerror="this.style.display=\'none\'"')

# 3. Add ResizeObserver before </body>
script = """
<script>
    const observer = new ResizeObserver(() => {
        window.parent.postMessage({
            type: 'resize-iframe',
            height: document.documentElement.scrollHeight
        }, '*');
    });
    observer.observe(document.body);
    window.addEventListener('load', () => {
        window.parent.postMessage({
            type: 'resize-iframe',
            height: document.documentElement.scrollHeight
        }, '*');
    });
</script>
</body>
"""
content = content.replace('</body>', script)

# 4. Remove handleLogoError script block
start_idx = content.find('<script>\n        // 실제 대표님의 고유 로고 이미지만')
end_idx = content.find('</script>', start_idx)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx+9:]

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)
