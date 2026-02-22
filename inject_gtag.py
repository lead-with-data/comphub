import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

gtag_snippet = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-SFFGR1TJ9H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-SFFGR1TJ9H');
</script>
"""

count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith("index.html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Check if gtag already exists
            if 'G-SFFGR1TJ9H' not in content:
                # Inject right after <head>
                # Using regex to match <head> ignoring case and attributes
                content = re.sub(r'(<head[^>]*>)', r'\1' + gtag_snippet, content, count=1, flags=re.IGNORECASE)
                
            if original_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Successfully injected Google Tag into {count} pages.")
