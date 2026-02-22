import re
import os

filepath = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Define the 9 new general calculators
new_calcs = [
    {
        "title": "Mortgage Calculator",
        "desc": "Calculate your monthly mortgage payment including principal and interest with amortization.",
        "link": "mortgage-calculator/index.html",
        "tag": "Real Estate",
        "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline>'
    },
    {
        "title": "Income Tax Calculator",
        "desc": "Estimate your Federal Income Tax liability based on the latest progressive tax brackets.",
        "link": "income-tax-calculator/index.html",
        "tag": "Finance",
        "icon": '<line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>'
    },
    {
        "title": "Student Loan Calculator",
        "desc": "Calculate your monthly student loan payments and total accrued interest over the life of the loan.",
        "link": "student-loan-calculator/index.html",
        "tag": "Education",
        "icon": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>'
    },
    {
        "title": "Annuity Payout",
        "desc": "Calculate the fixed monthly payout you will receive from a lump sum annuity investment.",
        "link": "annuity-payout-calculator/index.html",
        "tag": "Retirement",
        "icon": '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>'
    },
    {
        "title": "GPA Calculator",
        "desc": "Calculate your Grade Point Average (GPA) based on course credits and letter grades.",
        "link": "gpa-calculator/index.html",
        "tag": "Education",
        "icon": '<path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path>'
    },
    {
        "title": "BMI Calculator",
        "desc": "Calculate your Body Mass Index to determine your general weight category.",
        "link": "bmi-calculator/index.html",
        "tag": "Health",
        "icon": '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line>'
    },
    {
        "title": "Calorie/TDEE Calculator",
        "desc": "Calculate your Total Daily Energy Expenditure and target macronutrients for bulking or cutting.",
        "link": "tdee-calculator/index.html",
        "tag": "Health",
        "icon": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>'
    },
    {
        "title": "Retirement Calculator",
        "desc": "Estimate your future portfolio balance based on current savings and future contributions.",
        "link": "retirement-calculator/index.html",
        "tag": "Finance",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>'
    },
    {
        "title": "Compound Interest",
        "desc": "Calculate how your principal investment exponentially grows over time with compound interest.",
        "link": "compound-interest-calculator/index.html",
        "tag": "Finance",
        "icon": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline>'
    }
]

# Generate the new HTML blocks for these cards
new_html_blocks = "\n"
for i, c in enumerate(new_calcs):
    new_html_blocks += f'''
            <!-- Calculator {15 + i + 1} -->
            <a href="{c['link']}" style="text-decoration: none;">
                <article class="card calc-card reveal">
                    <div class="calc-card-header">
                        <div class="calc-icon">
                            <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24">{c['icon']}</svg>
                        </div>
                    </div>
                    <h3>{c['title']}</h3>
                    <p>{c['desc']}</p>
                    <div class="card-link">
                        Run Calculation
                        <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </div>
                </article>
            </a>\n'''

# Inject them just before the closing </div> of the .calc-grid
target_string = '        </div>\n    </main>'
replacement = new_html_blocks + '        </div>\n    </main>'

if target_string in html:
    html = html.replace(target_string, replacement)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully injected 9 new calculators into the grid.")
else:
    print("Error: Could not find the closing div of the grid. Please check the structure.")
