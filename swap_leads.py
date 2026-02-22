import os

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

replacement = '''<div class="calc-details-box" style="text-align: left; background: var(--bg-surface); border: 1px dashed var(--border-subtle); padding: 24px; border-radius: var(--radius); margin-bottom: 24px;">
                <h4 style="margin-bottom: 12px; font-size: 1.1rem; color: var(--text-primary);">Calculation Details</h4>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 0;">This calculation provides an estimate based on standard models. The actual value may fluctuate based on jurisdictional rules, specific claim details, or recent legislative changes. Please use this result as reference guidance rather than a guaranteed outcome.</p>
            </div>'''

count = 0
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith("index.html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            start_marker = '<div class="cta-box"'
            new_content = ""
            current_pos = 0
            
            while True:
                start_idx = content.find(start_marker, current_pos)
                if start_idx == -1:
                    new_content += content[current_pos:]
                    break
                
                new_content += content[current_pos:start_idx]
                
                # find the closing div by counting
                div_count = 0
                i = start_idx
                end_idx = start_idx
                while i < len(content):
                    if content.startswith('<div', i):
                        div_count += 1
                        i += 4
                    elif content.startswith('</div>', i):
                        div_count -= 1
                        i += 6
                        if div_count == 0:
                            end_idx = i
                            break
                    else:
                        i += 1
                
                new_content += replacement
                current_pos = end_idx
                count += 1
                
            if original_content != new_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print(f"Successfully replaced {count} attorney lead boxes with calculation details.")
