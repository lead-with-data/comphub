import re

index_path = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"
css_path = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\global.css"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Strip the old hero and grid
hero_grid_regex = re.compile(r'<!-- Hero Section -->.*?</main>', re.DOTALL)

# Let's rebuild a data-driven, interactive grid
calculators = [
    {
        "title": "AWW Calculator",
        "inputs": "Hourly, Overtime, Bonuses",
        "link": "aww-calculator/index.html",
        "tag": "Wage Core",
        "demo_val": "$1,240.50"
    },
    {
        "title": "Weekly Benefit Rate",
        "inputs": "State, AWW",
        "link": "weekly-benefit-calculator/index.html",
        "tag": "Indemnity",
        "demo_val": "$827.00/wk"
    },
    {
        "title": "Lost Wages (Back-Pay)",
        "inputs": "Dates, RTW Wages",
        "link": "lost-wages-calculator/index.html",
        "tag": "Indemnity",
        "demo_val": "$4,135.00"
    },
    {
        "title": "Statute of Limitations",
        "inputs": "State, Injury Date",
        "link": "filing-deadline-checker/index.html",
        "tag": "Legal",
        "demo_val": "342 Days Left"
    },
    {
        "title": "State Cap Lookup",
        "inputs": "State, Year",
        "link": "state-benefit-cap-lookup/index.html",
        "tag": "Reference",
        "demo_val": "Max: $1,619"
    },
    {
        "title": "Waiting Period",
        "inputs": "State, Days Off",
        "link": "waiting-period-calculator/index.html",
        "tag": "Indemnity",
        "demo_val": "Retroactive Paid"
    },
    {
        "title": "Coverage Checker",
        "inputs": "State, Industry, Employees",
        "link": "coverage-requirement-checker/index.html",
        "tag": "Employer",
        "demo_val": "Required"
    },
    {
        "title": "Attorney Fee Cap",
        "inputs": "State, Settlement $",
        "link": "attorney-fee-calculator/index.html",
        "tag": "Legal",
        "demo_val": "15% ($3,000)"
    },
    {
        "title": "Impairment Payout",
        "inputs": "State, WPI %, Rate",
        "link": "impairment-rating-payout/index.html",
        "tag": "Settlement",
        "demo_val": "$12,450.00"
    },
    {
        "title": "Scheduled Award",
        "inputs": "State, Body Part, Loss %",
        "link": "body-part-scheduled-award/index.html",
        "tag": "Settlement",
        "demo_val": "Arm (15%): $18k"
    },
    {
        "title": "Death Benefits",
        "inputs": "State, Dependents, AWW",
        "link": "death-benefits-calculator/index.html",
        "tag": "Indemnity",
        "demo_val": "$250k Cap"
    },
    {
        "title": "Employer Penalty",
        "inputs": "State, Employees, Days",
        "link": "employer-penalty-estimator/index.html",
        "tag": "Employer",
        "demo_val": "$10,000 Fine"
    },
    {
        "title": "Settlement Range",
        "inputs": "Med/Mo, PPD, Future Wages",
        "link": "settlement-range-guide/index.html",
        "tag": "Settlement",
        "demo_val": "$45k - $80k"
    },
    {
        "title": "Voc Rehab Guide",
        "inputs": "State, RTW Status",
        "link": "vocational-rehab-guide/index.html",
        "tag": "Reference",
        "demo_val": "$6,000 Voucher"
    },
    {
        "title": "SSDI Offset",
        "inputs": "ACE, SSDI $, Comp $",
        "link": "ss-offset-calculator/index.html",
        "tag": "Legal",
        "demo_val": "-$240/mo"
    }
]

new_ui = '''
    <!-- Clean, Non-Buzzword Hero -->
    <section class="compact-hero">
        <div class="container">
            <h1 class="system-title">Workers' Compensation Engine</h1>
            <p class="system-desc">15 deterministic legal calculators. No fluff, just accurate statutory math across 50 jurisdictions.</p>
        </div>
    </section>

    <!-- Interactive Interactive Grid -->
    <main class="container system-grid-container" id="tools">
        <div class="data-grid">
'''

for calc in calculators:
    new_ui += f'''
            <a href="{calc['link']}" class="interactive-widget">
                <div class="widget-header">
                    <span class="widget-tag">{calc['tag']}</span>
                    <div class="widget-status"></div>
                </div>
                <div class="widget-body">
                    <h3>{calc['title']}</h3>
                    <div class="mock-input-row">
                        <span class="mock-label">Inputs:</span>
                        <span class="mock-val">{calc['inputs']}</span>
                    </div>
                </div>
                <div class="widget-footer">
                    <div class="demo-output">
                        <span class="output-label">Demo Output</span>
                        <span class="output-val">{calc['demo_val']}</span>
                    </div>
                    <div class="run-btn">Launch <svg viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="M12 5l7 7-7 7"></path></svg></div>
                </div>
            </a>
'''

new_ui += '''
        </div>
    </main>
'''

updated_html = hero_grid_regex.sub(new_ui, html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(updated_html)

# CSS Update: Remove mist, rotating text, luxury cards, replace with crisp tech dashboard style
css_code = """
/* global.css */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg-canvas: #f4f4f5;
    --bg-surface: #ffffff;
    --text-primary: #09090b;
    --text-secondary: #71717a;
    --border-subtle: #e4e4e7;
    --brand-primary: #2563eb;
    --brand-hover: #1d4ed8;
    --accent: #10b981;
    --font-main: 'Inter', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    --radius: 8px;
    --shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: var(--font-main);
    background-color: var(--bg-canvas);
    color: var(--text-primary);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
}

a { text-decoration: none; color: inherit; }

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
}

/* Header */
.site-header {
    background: var(--bg-surface);
    border-bottom: 1px solid var(--border-subtle);
    padding: 16px 0;
}
.header-content {
    display: flex; justify-content: space-between; align-items: center;
}
.logo { font-weight: 700; font-size: 1.25rem; letter-spacing: -0.02em; display: flex; align-items: center; gap: 8px;}
.logo svg { width: 20px; height: 20px; color: var(--brand-primary); }

.trust-badge {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-secondary);
    background: var(--bg-canvas);
    padding: 4px 12px;
    border-radius: 4px;
    border: 1px solid var(--border-subtle);
}

/* Compact Hero */
.compact-hero {
    padding: 60px 0 40px;
}
.system-title {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 8px;
}
.system-desc {
    color: var(--text-secondary);
    font-size: 1.1rem;
    max-width: 600px;
}

/* Data Grid / Bento */
.system-grid-container {
    padding-bottom: 80px;
}
.data-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 16px;
}

/* Interactive Widget */
.interactive-widget {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius);
    padding: 20px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    transition: all 0.2s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.interactive-widget:hover {
    border-color: var(--brand-primary);
    box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    transform: translateY(-2px);
}

.widget-header {
    display: flex; justify-content: space-between; margin-bottom: 16px;
}
.widget-tag {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    background: #f1f5f9;
    color: #475569;
    padding: 4px 8px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}
.widget-status {
    width: 6px; height: 6px; border-radius: 50%; background: var(--border-subtle);
    transition: background 0.3s ease;
}
.interactive-widget:hover .widget-status {
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent);
}

.widget-body h3 {
    font-size: 1.1rem; font-weight: 600; margin-bottom: 12px;
}

.mock-input-row {
    display: flex; align-items: baseline; gap: 8px; font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 24px;
}
.mock-label { font-weight: 500; }
.mock-val { font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-primary); background: var(--bg-canvas); padding: 2px 6px; border-radius: 4px; border: 1px dashed var(--border-subtle); }

.widget-footer {
    margin-top: auto;
    display: flex; justify-content: space-between; align-items: flex-end;
    border-top: 1px solid var(--bg-canvas);
    padding-top: 16px;
}

.demo-output { display: flex; flex-direction: column; }
.output-label { font-size: 0.7rem; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 4px; }
.output-val { font-family: var(--font-mono); font-size: 1.1rem; font-weight: 700; color: var(--brand-primary); opacity: 0.5; transition: opacity 0.3s, transform 0.3s; transform: translateX(-5px); }

.interactive-widget:hover .output-val {
    opacity: 1;
    transform: translateX(0);
}

.run-btn {
    font-size: 0.85rem; font-weight: 600; color: var(--text-secondary); display: flex; align-items: center; gap: 4px; transition: color 0.2s;
}
.run-btn svg { width: 14px; height: 14px; stroke: currentColor; stroke-width: 2; fill: none; }
.interactive-widget:hover .run-btn { color: var(--brand-primary); }

.site-footer {
    text-align: center; padding: 40px; font-size: 0.85rem; color: var(--text-secondary); border-top: 1px solid var(--border-subtle);
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_code)

print("Redesign applied.")
