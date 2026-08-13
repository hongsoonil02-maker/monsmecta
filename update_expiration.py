import os

repo = r"c:\Users\master\monsmecta_landing"
extensions = (".js", ".py", ".html")

for root, dirs, files in os.walk(repo):
    if "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(extensions):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "18개월" in content:
                    new_content = content.replace("18개월", "18개월")
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {path}")
            except Exception as e:
                print(f"Error on {path}: {e}")
