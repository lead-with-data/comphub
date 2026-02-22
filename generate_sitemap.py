import os
import xml.etree.ElementTree as ET
from datetime import datetime

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"
base_url = "https://comphub.net"

urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "index.html":
            folder = os.path.relpath(root, base_dir)
            if folder == '.':
                folder = ''
            
            url = f"{base_url}/{folder}/" if folder else f"{base_url}/"
            url = url.replace('//', '/').replace('https:/', 'https://')
            if url.endswith('/') and folder != '':
               url = url[:-1]
               
            url_el = ET.SubElement(urlset, "url")
            
            loc = ET.SubElement(url_el, "loc")
            loc.text = url
            
            lastmod = ET.SubElement(url_el, "lastmod")
            lastmod.text = timestamp
            
            changefreq = ET.SubElement(url_el, "changefreq")
            priority = ET.SubElement(url_el, "priority")
            
            if folder == '':
                changefreq.text = "weekly"
                priority.text = "1.0"
            else:
                changefreq.text = "monthly"
                priority.text = "0.9"

tree = ET.ElementTree(urlset)
tree.write(os.path.join(base_dir, "sitemap.xml"), xml_declaration=True, encoding="UTF-8")
print("Successfully generated sitemap.xml with all calculators.")
