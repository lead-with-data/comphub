import os
import re

index_path = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add reveal class to all calc-cards
content = content.replace('class="card calc-card"', 'class="card calc-card reveal"')

# Inject Intersection Observer script before closing body tag
observer_script = """
    <!-- Scroll Reveal Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const reveals = document.querySelectorAll('.reveal');
            
            const revealOptions = {
                threshold: 0.1,
                rootMargin: "0px 0px -50px 0px"
            };

            const revealOnScroll = new IntersectionObserver(function(entries, observer) {
                entries.forEach(entry => {
                    if (!entry.isIntersecting) {
                        return;
                    } else {
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }
                });
            }, revealOptions);

            reveals.forEach(reveal => {
                revealOnScroll.observe(reveal);
            });
        });
    </script>
</body>
"""

if "Scroll Reveal Script" not in content:
    content = content.replace('</body>', observer_script)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected Reveal classes and JS observer successfully.")
