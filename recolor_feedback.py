import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

new_feedback_snippet = """<!-- Feedback Widget -->
<script>
document.addEventListener('DOMContentLoaded', () => {
    const feedbackHTML = `
        <div class="feedback-widget" style="margin-top: 40px; background: rgba(0, 0, 0, 0.02); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 32px 24px; text-align: center; box-shadow: 0 4px 16px rgba(0,0,0,0.02); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: var(--text-tertiary);"></div>
            <h4 style="font-size: 1.35rem; color: var(--text-primary); margin-bottom: 8px; font-weight: 700;">Was this calculation helpful?</h4>
            <p style="font-size: 1.05rem; color: var(--text-secondary); margin-bottom: 24px; max-width: 500px; margin-left: auto; margin-right: auto;">Your feedback directly helps us improve these free tools for everyone.</p>
            <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                <button onclick="sendFeedback('yes', this)" style="padding: 14px 28px; border: 2px solid var(--brand-primary); background: var(--brand-primary); color: white; border-radius: 8px; cursor: pointer; display: flex; align-items: center; gap: 10px; font-weight: 600; font-size: 1.1rem; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 12px rgba(0, 112, 243, 0.25);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 16px rgba(0, 112, 243, 0.35)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 12px rgba(0, 112, 243, 0.25)';">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> Yes, it helped!
                </button>
                <button onclick="sendFeedback('no', this)" style="padding: 14px 28px; border: 2px solid var(--border-subtle); background: var(--bg-surface); color: var(--text-primary); border-radius: 8px; cursor: pointer; display: flex; align-items: center; gap: 10px; font-weight: 600; font-size: 1.1rem; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.05);" onmouseover="this.style.transform='translateY(-3px)'; this.style.borderColor='var(--text-tertiary)'; this.style.boxShadow='0 6px 12px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='var(--border-subtle)'; this.style.boxShadow='0 2px 6px rgba(0,0,0,0.05)';">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg> No, it didn't
                </button>
            </div>
        </div>
    `;

    // Attempt to inject into the results zone so it appears with the results
    let container = document.querySelector('.calculator-results') || document.querySelector('#result-box') || document.querySelector('.result-box') || document.querySelector('.calculator-container') || document.querySelector('.card');
    
    if (container) {
        container.insertAdjacentHTML('beforeend', feedbackHTML);
    }
});

function sendFeedback(choice, btn) {
    if (typeof gtag === 'function') {
        const calcName = document.title.split('|')[0].trim();
        gtag('event', 'calculator_feedback', {
            'calculator_name': calcName,
            'satisfaction': choice
        });
    }
    const widget = btn.closest('.feedback-widget');
    widget.innerHTML = `
        <div style="padding: 20px 0;">
            <svg style="color: #10B981; margin-bottom: 12px;" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            <h4 style="font-size: 1.25rem; color: var(--text-primary); margin-bottom: 8px;">Thanks for your feedback!</h4>
        </div>
    `;
}
</script>"""

count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "index.html":
            path = os.path.join(root, file)
            folder = os.path.relpath(root, base_dir)
            if folder == '.':
                continue # Skip the master index.html homepage
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Use regex to find and replace the old feedback snippet
            pattern = re.compile(r'<!-- Feedback Widget -->.*?</script>', re.DOTALL)
            
            if pattern.search(content):
                content = pattern.sub(new_feedback_snippet, content)
            
            if original_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Successfully overhauled GA4 Feedback Widget into {count} calculators to subtle grey & simplified thank you.")
