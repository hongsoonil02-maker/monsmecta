import os
import re

def unify_colors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for Tailwind classes
    # Headers and dark backgrounds
    content = content.replace('bg-slate-900', 'bg-[#00513b]')
    content = content.replace('bg-slate-800', 'bg-[#003d2b]')
    content = content.replace('hover:bg-slate-800', 'hover:bg-[#003d2b]')
    content = content.replace('border-slate-800', 'border-[#003d2b]')
    
    # Specific gradients
    content = content.replace('from-slate-900', 'from-[#00513b]')
    content = content.replace('via-slate-950', 'via-[#004230]')
    content = content.replace('to-indigo-950', 'to-[#00281d]')
    content = content.replace('from-blue-900', 'from-[#00513b]')
    content = content.replace('to-indigo-900', 'to-[#003d2b]')
    
    # Indigo to Emerald
    content = content.replace('text-indigo-900', 'text-emerald-900')
    content = content.replace('text-indigo-600', 'text-emerald-600')
    content = content.replace('text-indigo-400', 'text-emerald-400')
    content = content.replace('bg-indigo-600', 'bg-emerald-600')
    content = content.replace('bg-indigo-50', 'bg-emerald-50')
    content = content.replace('border-indigo-100', 'border-emerald-100')
    content = content.replace('border-indigo-200', 'border-emerald-200')
    
    # Blue to Teal/Emerald
    content = content.replace('text-blue-900', 'text-teal-900')
    content = content.replace('text-blue-800', 'text-teal-800')
    content = content.replace('text-blue-300', 'text-emerald-300')
    content = content.replace('text-blue-200', 'text-emerald-200')
    content = content.replace('text-blue-100', 'text-emerald-100')
    content = content.replace('bg-blue-600', 'bg-teal-600')
    content = content.replace('bg-blue-50', 'bg-teal-50')
    content = content.replace('border-blue-300', 'border-teal-300')
    content = content.replace('from-blue-100', 'from-teal-100')
    content = content.replace('to-blue-50', 'to-teal-50')
    content = re.sub(r'linear-gradient\(to top,\s*#bfdbfe,\s*#eff6ff\)', 'linear-gradient(to top, #99f6e4, #f0fdfa)', content) # blue-200 to blue-50 -> teal-200 to teal-50
    content = content.replace('border-color: #93c5fd', 'border-color: #5eead4') # blue-300 to teal-300
    content = re.sub(r'rgba\(59,\s*130,\s*246,\s*0.4\)', 'rgba(20, 184, 166, 0.4)', content) # blue 500 to teal 500
    content = re.sub(r'rgba\(59,\s*130,\s*246,\s*0.1\)', 'rgba(20, 184, 166, 0.1)', content)
    content = content.replace('border-top: 3px solid #3b82f6', 'border-top: 3px solid #14b8a6') # blue 500 to teal 500
    content = content.replace('border-top: 4px dashed #3b82f6', 'border-top: 4px dashed #14b8a6')

    # Chart.js color replacements (Blue -> Emerald/Teal)
    # rgba(59, 130, 246, X) -> rgba(16, 185, 129, X) (Emerald 500)
    content = re.sub(r'rgba\(59,\s*130,\s*246,\s*(0\.\d+)\)', r'rgba(16, 185, 129, \1)', content)
    # rgba(37, 99, 235, X) -> rgba(5, 150, 105, X) (Emerald 600)
    content = re.sub(r'rgba\(37,\s*99,\s*235,\s*(0\.\d+|1)\)', r'rgba(5, 150, 105, \1)', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\Users\sooni\monsmecta-landing\public\assets"
files = ["james_infographic.html", "monsmecta_dashboard.html", "monsmecta_scenario.html"]

for file in files:
    process_path = os.path.join(base_dir, file)
    unify_colors(process_path)

print("Colors unified successfully.")
