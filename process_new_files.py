import os
import re

def process_file(src_path, dst_path, source_name):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add word-break if not exists
    if "word-break: keep-all" not in content:
        if "body {" in content:
            content = content.replace("body {", "* {\n            word-break: keep-all;\n            overflow-wrap: break-word;\n        }\n        body {", 1)

    # 2. Add ResizeObserver before </body>
    script = f"""
<script>
    const observer = new ResizeObserver(() => {{
        window.parent.postMessage({{
            type: 'resize-iframe',
            source: '{source_name}',
            height: document.documentElement.scrollHeight
        }}, '*');
    }});
    observer.observe(document.body);
    window.addEventListener('load', () => {{
        window.parent.postMessage({{
            type: 'resize-iframe',
            source: '{source_name}',
            height: document.documentElement.scrollHeight
        }}, '*');
    }});
</script>
</body>
"""
    if "resize-iframe" not in content:
        content = content.replace('</body>', script)
    else:
        # Replace the existing script to include the source parameter
        content = re.sub(r"type:\s*'resize-iframe',?", f"type: 'resize-iframe',\\n            source: '{source_name}',", content)

    # Specific edit for james_infographic.html
    if source_name == 'james':
        content = content.replace('7,500원 ~ 7,700원', '7,700원(부가세포함)')

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Update existing james_infographic
process_file(
    r"c:\Users\sooni\monsmecta-landing\public\assets\james_infographic.html",
    r"c:\Users\sooni\monsmecta-landing\public\assets\james_infographic.html",
    "james"
)

# 2. Add scenario
process_file(
    r"C:\Users\sooni\OneDrive - Agro Korea Co.,Ltd\몬스멕타 상담 시나리오 인포그래픽.html",
    r"c:\Users\sooni\monsmecta-landing\public\assets\monsmecta_scenario.html",
    "scenario"
)

# 3. Add dashboard
process_file(
    r"C:\Users\sooni\Downloads\code_artifact.html",
    r"c:\Users\sooni\monsmecta-landing\public\assets\monsmecta_dashboard.html",
    "dashboard"
)

print("Files processed successfully.")
