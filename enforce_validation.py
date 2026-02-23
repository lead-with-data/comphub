import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"
count = 0

for root, dirs, files in os.walk(base_dir):
    if "index.html" in files:
        path = os.path.join(root, "index.html")
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if '<div class="calculator-form">' in content and "calculateBtn.addEventListener('click', () => {" in content:
            
            # 1. Change <div class="calculator-form"> to <form id="calc-form" class="calculator-form">
            content = content.replace('<div class="calculator-form">', '<form id="calc-form" class="calculator-form">', 1)
            
            # 2. Change closing </div> to </form> right after the calculate button
            content = re.sub(r'(id="calculate-btn".*?</button>\s*)</div>', r'\1</form>', content, flags=re.DOTALL, count=1)
            
            # 3. Add type="submit" to the calculate button
            content = content.replace('<button id="calculate-btn"', '<button type="submit" id="calculate-btn"')
            
            # 4. Update the event listener to catch 'submit' instead of 'click' and prevent default
            old_listener = "calculateBtn.addEventListener('click', () => {"
            new_listener = "document.getElementById('calc-form').addEventListener('submit', (e) => {\n                e.preventDefault();"
            content = content.replace(old_listener, new_listener)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Enforced HTML5 Form Validation in: {os.path.basename(root)}")

print(f"Total files updated: {count}")
