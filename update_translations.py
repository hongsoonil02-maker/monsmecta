import os

base_path = r"c:\Users\master\monsmecta-landing\src\locales"
old_acc = "3333-26-3248376"
new_acc = "3333-37-2664149"

for lang in os.listdir(base_path):
    json_path = os.path.join(base_path, lang, "translation.json")
    if os.path.isfile(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the account number globally
        content = content.replace(old_acc, new_acc)
        
        # For 'en'
        content = content.replace('"deposit_holder_value": "Soonil Hong"', '"deposit_holder_value": "Soonil Hong (S&J Animal Hospital)"')
        content = content.replace('Account Holder: Soonil Hong', 'Account Holder: Soonil Hong (S&J Animal Hospital)')
        
        # For 'ja'
        content = content.replace('"deposit_holder_value": "ホンスニル"', '"deposit_holder_value": "ホンスニル (S&J動物病院)"')
        content = content.replace('預金者: ホンスニル', '預金者: ホンスニル (S&J動物病院)')

        # For 'zh' and others
        content = content.replace('洪淳一', '洪淳一(S&J动物医院)') 
        content = content.replace('Hong Soon-il', 'Hong Soon-il (S&J Animal Hospital)')
        
        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {lang}")
