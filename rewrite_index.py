import re
import os

filepath = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the exact 15 calculators the user requested
calculators = [
    {
        "title": "AWW Calculator",
        "desc": "Calculate exact Average Weekly Wage factoring in overtime, bonuses, and concurrent employment.",
        "link": "calculator-03/index.html",
        "tag": "Core Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": ""
    },
    {
        "title": "Weekly Benefit Calculator",
        "desc": "Determine exact weekly statutory maximums based on state jurisdiction and earnings.",
        "link": "calculator-01/index.html",
        "tag": "Core Model",
        "icon": '<rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line>',
        "color": ""
    },
    {
        "title": "Lost Wages Calculator",
        "desc": "Calculate exact retroactive wage replacement owed for periods of Temporary Total or Partial Disability.",
        "link": "calculator-07/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Filing Deadline Checker",
        "desc": "Calculate the absolute final date to file a formal claim before the Statute of Limitations expires.",
        "link": "calculator-05/index.html",
        "tag": "Core Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": ""
    },
    {
        "title": "State Benefit Cap Lookup",
        "desc": "Lookup the exact statutory weekly benefit cap for your state and year of injury.",
        "link": "calculator-08/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Waiting Period Calculator",
        "desc": "Determine when your first check is legally due and if you qualify to be paid for the initial waiting days.",
        "link": "calculator-09/index.html",
        "tag": "Tier 2 Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Coverage Requirement Checker",
        "desc": "Simple logic tree to determine if an employer is legally required to carry workers' comp insurance.",
        "link": "calculator-12/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Attorney Fee Calculator",
        "desc": "Estimate maximum statutory attorney fee caps based on your final settlement or award amount.",
        "link": "calculator-13/index.html",
        "tag": "Tier 3 Model",
        "icon": '<line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Impairment Rating Payout",
        "desc": "Determine the precise statutory payout value of an unscheduled permanent impairment rating (WPI).",
        "link": "calculator-04/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Body Part Scheduled Award",
        "desc": "Calculate specific state-mandated payouts for partial or total loss of use of scheduled body parts.",
        "link": "calculator-06/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Death Benefits Calculator",
        "desc": "Estimate the statutory survivor benefits and maximum burial allowances payable to dependents.",
        "link": "calculator-11/index.html",
        "tag": "Tier 2 Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Employer Penalty Estimator",
        "desc": "Estimate statutory maximum fines and penalties for uninsured or dangerously non-compliant employers.",
        "link": "calculator-14/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Settlement Range Guide",
        "desc": "Forecast potential resolution ranges using medical multipliers, historical wage data, and disability algorithms.",
        "link": "calculator-02/index.html",
        "tag": "Core Model",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": ""
    },
    {
        "title": "Vocational Rehab Guide",
        "desc": "Discover what retraining benefits or job displacement vouchers your state mandates.",
        "link": "calculator-10/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "SS Offset Calculator",
        "desc": "Understand the complex federal formula for how Social Security Disability (SSDI) reduces your comp checks.",
        "link": "calculator-15/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="7.5 4.21 12 6.81 16.5 4.21"></polyline><polyline points="7.5 19.79 7.5 14.6 3 12"></polyline><polyline points="21 12 16.5 14.6 16.5 19.79"></polyline><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    }
]

grid_html = '<div class="calculator-grid">\n'
for i, c in enumerate(calculators):
    style_str = f' style="{c["color"]}"' if c["color"] else ''
    btn_text = 'Run Calculation' if 'Guide' not in c['title'] and 'Checker' not in c['title'] else 'View Guide'
    if 'Checker' in c['title']: btn_text = 'Check Status'
    if 'Lookup' in c['title']: btn_text = 'Lookup Values'
    if 'Offset' in c['title']: btn_text = 'View Formula'
    
    grid_html += f'''            <!-- Calculator {i+1} -->
            <a href="{c['link']}" style="text-decoration: none;">
                <article class="card calc-card">
                    <div class="calc-card-header">
                        <div class="calc-icon">
                            <svg class="icon" viewBox="0 0 24 24">{c['icon']}</svg>
                        </div>
                        <span class="tag-t1"{style_str}>{c['tag']}</span>
                    </div>
                    <h3>{c['title']}</h3>
                    <p>{c['desc']}</p>
                    <div class="card-link">
                        {btn_text}
                        <svg class="icon" viewBox="0 0 24 24">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </div>
                </article>
            </a>\n\n'''

grid_html += '        </div>'

# Regex to find everything between <div class="calculator-grid"> and the closing </div> right before </main>
new_content = re.sub(r'<div class="calculator-grid">.*?</div>\s*</main>', grid_html + '\n    </main>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully rewrote index.html to show exactly 15 calculators.")
