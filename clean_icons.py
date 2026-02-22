import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith("index.html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # Remove <span class="calc-num"...>...</span> tag.
            # Handles multi-line tags gracefully.
            content = re.sub(r'<span class="calc-num"[^>]*>.*?</span>\s*', '', content, flags=re.DOTALL | re.IGNORECASE)

            # Remove the <svg that contains the '<' icon specifically for the "Back to Dashboard" in the new calculators
            # Search for <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none"><path d="M15 19l-7-7 7-7"/></svg>
            content = re.sub(r'<svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none">\s*<path d="M15 19l-7-7 7-7"\s*/?>\s*</svg>\s*', '', content, flags=re.DOTALL)
            
            # Same but with no self-closing slash (just in case HTML formatter did that)
            content = re.sub(r'<svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none"><path d="M15 19l-7-7 7-7"/></svg>\s*', '', content, flags=re.DOTALL)
            
            # If the file had "Back to Dashboard", it might also have "Return to Models" in old models which has an icon
            # Let me check if they also want the `<` icon removed from old calculators.
            # "and < icon appearing on new calculators pages"
            # It explicitly says "on new calculators pages".
            
            if original_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {path}")

print("Cleanup script finished.")
