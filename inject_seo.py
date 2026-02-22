import os
import re
import json

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"
brand = "CompHub Premium"
base_url = "https://lead-with-data.github.io/comphub"

def get_calc_info(folder_name):
    name = folder_name.replace('-', ' ').title()
    if folder_name == '':
        return {
            'title': f'Workers Comp & Financial Calculators | Free Tools | {brand}',
            'desc': 'Free online financial calculators for workers compensation, personal injury, and general financial planning. Get instant estimates trusted by thousands.',
            'name': 'CompHub Calculators'
        }
    
    return {
        'title': f'{name} | Free Online Estimate | {brand}',
        'desc': f'Calculate your {name.lower()} instantly. Free online {name.lower()} provides accurate estimates based on standard industry formulas. No signup required.',
        'name': name
    }

def generate_schema(folder_name, info, is_home=False):
    url = f"{base_url}/{folder_name}/" if folder_name else f"{base_url}/"
    url = url.replace('\\', '/')
    
    # Global Organization & Website Schema
    org_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": brand,
        "url": base_url,
        "description": "Premium online calculators for workers compensation, personal injury, and structured settlements."
    }
    
    website_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": brand,
        "url": base_url
    }
    
    schemas = [org_schema, website_schema]
    
    if not is_home:
        # SoftwareApplication Schema for Calculators
        app_schema = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": info['name'],
            "applicationCategory": "FinanceApplication",
            "operatingSystem": "Web Browser",
            "offers": {
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "USD"
            },
            "description": info['desc']
        }
        
        # Breadcrumb Schema
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": base_url
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": info['name'],
                    "item": url
                }
            ]
        }
        
        schemas.extend([app_schema, breadcrumb_schema])
        
    return '\n'.join([f'<script type="application/ld+json">\n{json.dumps(s, indent=2)}\n</script>' for s in schemas])

count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "index.html":
            path = os.path.join(root, file)
            folder = os.path.relpath(root, base_dir)
            if folder == '.':
                folder = ''
            
            info = get_calc_info(folder)
            schema_block = generate_schema(folder, info, is_home=(folder==''))
            url = f"{base_url}/{folder}/" if folder else f"{base_url}/"
            url = url.replace('\\', '/')
            url = url.replace('//', '/').replace('https:/', 'https://')
            if url.endswith('/') and folder != '':
               url = url[:-1]
               
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Replace canonical tag
            canonical_tag = f'<link rel="canonical" href="{url}" />'
            if 'rel="canonical"' in content:
                content = re.sub(r'<link[^>]*rel="canonical"[^>]*>', canonical_tag, content, flags=re.IGNORECASE)
                
            # Remove old JSON-LD
            content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
            
            # Inject new Schema back
            content = content.replace('</head>', f'{schema_block}\n</head>')
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Successfully re-injected SEO metadata for GitHub Pages URL into {count} pages.")
