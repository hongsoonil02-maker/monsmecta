import os
import re
import glob

# The directory where the labels are stored
directory = r"c:\Users\master\monsmecta-landing\public\assets"

# The 10 specific label files
target_files = [
    "monsmecta_amber_label.html",
    "monsmecta_amber_label_en.html",
    "monsmecta_blue_label.html",
    "monsmecta_blue_label_en.html",
    "monsmecta_green_label.html",
    "monsmecta_green_label_en.html",
    "monsmecta_orange_label.html",
    "monsmecta_orange_label_en.html",
    "monsmecta_teal_label.html",
    "monsmecta_teal_label_en.html",
]

def update_label(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the gap and layout
    content = content.replace(
        '<div class="relative z-10 flex flex-row gap-12">',
        '<div class="relative z-10 flex flex-row gap-10 justify-between">'
    )

    # 2. Update left column width
    content = content.replace(
        '<div class="w-[44%] flex flex-col justify-between">',
        '<div class="w-[46%] flex flex-col justify-between pr-4">'
    )

    # 3. Update right column width and insert divider
    divider = '''
                <!-- Vertical Divider (Label Fold Line) -->
                <div class="border-l-[1.5px] border-dashed border-white/30 my-4 shrink-0"></div>

                <!-- Right Column (Specs & Details) -->
                <div class="w-[50%] flex flex-col justify-between pl-2">
'''
    content = content.replace(
        '                <!-- Right Column (Specs & Details) -->\n                <div class="w-[56%] flex flex-col justify-between">',
        divider.strip('\n')
    )
    
    # Also handle cases where there's no comment exactly matching
    if 'w-[56%]' in content:
        content = content.replace(
            '<div class="w-[56%] flex flex-col justify-between">',
            '<!-- Vertical Divider --><div class="border-l-[1.5px] border-dashed border-white/30 my-4 shrink-0"></div>\n                <div class="w-[50%] flex flex-col justify-between pl-2">'
        )

    # 4. Update the right column background to dark translucent
    content = content.replace(
        'class="bg-white text-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl h-full flex flex-col justify-between"',
        'class="bg-black/20 text-white/90 border border-white/20 rounded-2xl p-6 sm:p-8 shadow-inner h-full flex flex-col justify-between"'
    )

    # 5. Generic color replacements for the right column text/borders
    content = content.replace('text-slate-900', 'text-white')
    content = content.replace('text-slate-800', 'text-white/90')
    content = content.replace('text-slate-700', 'text-white/80')
    content = content.replace('text-slate-600', 'text-white/70')
    content = content.replace('border-slate-200', 'border-white/20')
    content = content.replace('bg-slate-100', 'bg-black/30')
    
    # The title text for effects was something like text-[#92400e], we can change any hex color in the effect title to a generic nice color like yellow-400
    content = re.sub(r'text-\[#[a-fA-F0-9]+\]', 'text-yellow-400', content)
    
    # 6. Some labels use text-lime-600 or similar for the warning box. Let's just make it universally visible in dark mode.
    content = content.replace('text-lime-600', 'text-yellow-400')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {os.path.basename(filepath)}")

for filename in target_files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        update_label(filepath)
    else:
        print(f"File not found: {filename}")

print("All targeted labels updated successfully!")
