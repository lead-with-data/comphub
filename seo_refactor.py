import os
import shutil
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

slug_mapping = {
    "calculator-01": "weekly-benefit-calculator",
    "calculator-02": "settlement-range-guide",
    "calculator-03": "aww-calculator",
    "calculator-04": "impairment-rating-payout",
    "calculator-05": "filing-deadline-checker",
    "calculator-06": "body-part-scheduled-award",
    "calculator-07": "lost-wages-calculator",
    "calculator-08": "state-benefit-cap-lookup",
    "calculator-09": "waiting-period-calculator",
    "calculator-10": "vocational-rehab-guide",
    "calculator-11": "death-benefits-calculator",
    "calculator-12": "coverage-requirement-checker",
    "calculator-13": "attorney-fee-calculator",
    "calculator-14": "employer-penalty-estimator",
    "calculator-15": "ss-offset-calculator"
}

# 1. Rename Output Directories
for old_name, new_slug in slug_mapping.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_slug)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)

# 2. Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

for old_name, new_slug in slug_mapping.items():
    index_content = index_content.replace(f'href="{old_name}/index.html"', f'href="{new_slug}/index.html"')

# Add specific OG tags to master index
if '<meta property="og:title"' not in index_content:
    og = """<meta property="og:title" content="Workers' Compensation Hub | Premium Legal Calculators">
    <meta property="og:description" content="Free, state-specific workers' compensation calculators. Estimate settlement values, weekly benefits, and permanent disability ratings instantly.">
    <meta property="og:type" content="website">"""
    index_content = index_content.replace('</head>', og + '\n</head>')

# Ensure SVGs have aria tags for SEO
index_content = re.sub(r'<svg class="icon"(?!.*?role="img")', r'<svg class="icon" role="img" aria-label="Vector Icon"', index_content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# 3. Process each calculator's index.html
for new_slug in slug_mapping.values():
    calc_index_path = os.path.join(base_dir, new_slug, 'index.html')
    if os.path.exists(calc_index_path):
        with open(calc_index_path, 'r', encoding='utf-8') as f:
            calc_content = f.read()

        title_match = re.search(r'<title>(.*?)</title>', calc_content)
        p_match = re.search(r'<h1>.*?</h1>\s*<p>(.*?)</p>', calc_content, re.DOTALL)
        
        desc_text = "Workers' Compensation calculator and estimation tool."
        
        if title_match and p_match:
            desc_text = p_match.group(1).replace('\n', ' ').strip()
            if len(desc_text) > 155:
                desc_text = desc_text[:152] + '...'
                
            if '<meta name="description"' not in calc_content:
                meta_tag = f'<meta name="description" content="{desc_text}">\n    '
                calc_content = calc_content.replace('<title>', meta_tag + '<title>')

        if '<meta property="og:title"' not in calc_content:
            og_tags = f'''<meta property="og:title" content="{title_match.group(1) if title_match else ''}">
    <meta property="og:description" content="{desc_text}">
    <meta property="og:type" content="article">'''
            calc_content = calc_content.replace('</head>', og_tags + '\n</head>')

        calc_content = re.sub(r'<svg class="icon"(?!.*?role="img")', r'<svg class="icon" role="img" aria-label="Vector Icon"', calc_content)
        
        with open(calc_index_path, 'w', encoding='utf-8') as f:
            f.write(calc_content)

print("SEO Rename and Meta Tag Upgrade Complete.")
