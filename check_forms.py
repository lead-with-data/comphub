import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

forms = 0
divs = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "index.html" and os.path.relpath(root, base_dir) != '.':
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if '<form' in content:
                    forms += 1
                elif 'calculator-form' in content:
                    divs += 1
                else:
                    print(f"Unknown structure in {path}")
                    
print(f"Calculators using <form>: {forms}")
print(f"Calculators using <div>: {divs}")
