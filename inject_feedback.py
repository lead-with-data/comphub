import os
import re

base_dir = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome"

feedback_snippet = """
<!-- Feedback Widget -->
<script>
document.addEventListener('DOMContentLoaded', () => {
    const feedbackHTML = `
        <div class="feedback-widget" style="margin-top: 24px; text-align: center; border-top: 1px dashed var(--border-subtle); padding-top: 24px;">
            <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 12px;">Did this calculation help you?</p>
            <div style="display: flex; gap: 12px; justify-content: center;">
                <button onclick="sendFeedback('yes', this)" style="padding: 8px 16px; border: 1px solid var(--border-subtle); background: var(--bg-surface); border-radius: 20px; cursor: pointer; display: flex; align-items: center; gap: 6px; font-weight: 500; color: var(--text-primary); transition: all 0.2s;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg> Yes
                </button>
                <button onclick="sendFeedback('no', this)" style="padding: 8px 16px; border: 1px solid var(--border-subtle); background: var(--bg-surface); border-radius: 20px; cursor: pointer; display: flex; align-items: center; gap: 6px; font-weight: 500; color: var(--text-primary); transition: all 0.2s;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path></svg> No
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
    widget.innerHTML = '<p style="font-size: 0.95rem; color: var(--brand-primary); font-weight: 600;">Thank you for your feedback!</p>';
}
</script>
"""

count = 0

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "index.html":
            path = os.path.join(root, file)
            folder = os.path.relpath(root, base_dir)
            if folder == '.':
                continue # Skip the master index.html homepage, we only want this on specific calculators
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Check if gtag already exists
            if 'function sendFeedback(' not in content:
                content = content.replace('</body>', f'{feedback_snippet}\n</body>')
                
            if original_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                
print(f"Successfully injected GA4 Feedback Widget into {count} calculators.")
