import os
import glob

base_dir = r"c:\Users\sooni\monsmecta-landing\public\assets"
files = glob.glob(os.path.join(base_dir, "*.html"))

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove CDN
    content = content.replace('<script src="https://cdn.tailwindcss.com"></script>', '')
    
    # Check if iframe.css is already linked
    if 'href="iframe.css"' not in content:
        # Insert <link> right after <title>
        content = content.replace('</title>', '</title>\n    <link rel="stylesheet" href="iframe.css">')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("CDN removed and iframe.css linked.")
