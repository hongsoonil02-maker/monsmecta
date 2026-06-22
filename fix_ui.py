import os
import re

def modify_app_jsx():
    path = r"c:\Users\sooni\monsmecta-landing\src\App.jsx"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix Footer colors
    content = content.replace('bg-slate-950 text-slate-400 py-16 border-t border-slate-900', 'bg-[#00281d] text-emerald-400/80 py-16 border-t border-[#003d2b]')
    content = content.replace('border-slate-800/50 text-sm font-semibold tracking-wider text-slate-600', 'border-[#003d2b]/50 text-sm font-semibold tracking-wider text-emerald-600/80')
    content = content.replace('text-slate-500 mt-4', 'text-emerald-500 mt-4')
    
    # 2. Fix the order form box background
    content = content.replace('bg-slate-900 p-8 md:p-10 rounded-2xl text-white shadow-2xl relative overflow-hidden', 'bg-[#003d2b] p-8 md:p-10 rounded-2xl text-white shadow-2xl relative overflow-hidden')

    # 3. Fix the infographic section spacing at the top
    # <section className="py-24 bg-white max-w-6xl mx-auto px-4"> -> py-16
    content = content.replace('<section className="py-24 bg-white max-w-6xl mx-auto px-4">', '<section className="py-12 bg-white max-w-6xl mx-auto px-4">')
    # <div className="text-center mb-16"> -> mb-10
    content = content.replace('<div className="text-center mb-16">', '<div className="text-center mb-8">')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def modify_iframe_scripts():
    base_dir = r"c:\Users\sooni\monsmecta-landing\public\assets"
    files = ["james_infographic.html", "monsmecta_dashboard.html", "monsmecta_scenario.html"]
    
    for file in files:
        path = os.path.join(base_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We need to change the height calculation from document.documentElement.scrollHeight
        # to a more accurate one that ignores the iframe's fixed height.
        # document.body.offsetHeight or document.querySelector('body > div').offsetHeight
        
        # Replace document.documentElement.scrollHeight
        # with: document.body.scrollHeight (Wait, body scrollHeight also inherits sometimes)
        # Let's use: document.body.offsetHeight + 50 (to account for margins)
        
        content = content.replace('document.documentElement.scrollHeight', 'document.body.offsetHeight + 50')
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    modify_app_jsx()
    modify_iframe_scripts()
    print("Modifications applied.")
