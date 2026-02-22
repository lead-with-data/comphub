import re

index_path = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"
css_path = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\global.css"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Strip the tags
html = re.sub(r'\s*<span class="tag-t1"[^>]*>.*?</span>', '', html, flags=re.DOTALL)

# 2. Update .calc-icon and hover state in index.html to be more minimalistic
new_calc_icon_css = """
        /* Minimalist Icon */
        .calc-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: #FAFAFA;
            border: 1px solid rgba(0,0,0,0.06);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-primary);
            transition: all 0.3s ease;
        }

        .calc-card:hover .calc-icon {
            background: var(--text-primary);
            color: #FFFFFF;
            transform: scale(1.05);
            border-color: var(--text-primary);
        }
"""
html = re.sub(r'\.calc-icon\s*\{.*?\.calc-card:hover \.calc-icon\s*\{[^}]*\}', new_calc_icon_css.strip(), html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_card_css = """
/* Modern Minimalist Card */
.card {
    background: #FFFFFF;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 16px;
    padding: 36px 32px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
}

.card:hover {
    transform: translateY(-4px);
    border-color: rgba(0, 0, 0, 0.15);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.06);
}
"""
css = re.sub(r'/\* Luxury Minimalist Card \*/.*?\.card:hover\s*\{[^}]*\}', new_card_css.strip(), css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Minimalist redesign applied successfully!")
