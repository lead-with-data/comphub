import re
import os

filepath = r"c:\Users\MUHAMMAD AHMAD\Downloads\calsome\index.html"

# Define the exact 15 calculators the user requested with standard links and tags
calculators = [
    {
        "title": "AWW Calculator",
        "desc": "Calculate exact Average Weekly Wage factoring in overtime, bonuses, and concurrent employment.",
        "link": "aww-calculator/index.html",
        "tag": "Core Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": ""
    },
    {
        "title": "Weekly Benefit Calculator",
        "desc": "Determine exact weekly statutory maximums based on state jurisdiction and earnings.",
        "link": "weekly-benefit-calculator/index.html",
        "tag": "Core Model",
        "icon": '<rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line>',
        "color": ""
    },
    {
        "title": "Lost Wages Calculator",
        "desc": "Calculate exact retroactive wage replacement owed for periods of Temporary Total or Partial Disability.",
        "link": "lost-wages-calculator/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Filing Deadline Checker",
        "desc": "Calculate the absolute final date to file a formal claim before the Statute of Limitations expires.",
        "link": "filing-deadline-checker/index.html",
        "tag": "Core Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": ""
    },
    {
        "title": "State Benefit Cap Lookup",
        "desc": "Lookup the exact statutory weekly benefit cap for your state and year of injury.",
        "link": "state-benefit-cap-lookup/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Waiting Period Calculator",
        "desc": "Determine when your first check is legally due and if you qualify to be paid for the initial waiting days.",
        "link": "waiting-period-calculator/index.html",
        "tag": "Tier 2 Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Coverage Requirement Checker",
        "desc": "Simple logic tree to determine if an employer is legally required to carry workers' comp insurance.",
        "link": "coverage-requirement-checker/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Attorney Fee Calculator",
        "desc": "Estimate maximum statutory attorney fee caps based on your final settlement or award amount.",
        "link": "attorney-fee-calculator/index.html",
        "tag": "Tier 3 Model",
        "icon": '<line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Impairment Rating Payout",
        "desc": "Determine the precise statutory payout value of an unscheduled permanent impairment rating (WPI).",
        "link": "impairment-rating-payout/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Body Part Scheduled Award",
        "desc": "Calculate specific state-mandated payouts for partial or total loss of use of scheduled body parts.",
        "link": "body-part-scheduled-award/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Death Benefits Calculator",
        "desc": "Estimate the statutory survivor benefits and maximum burial allowances payable to dependents.",
        "link": "death-benefits-calculator/index.html",
        "tag": "Tier 2 Model",
        "icon": '<circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "Employer Penalty Estimator",
        "desc": "Estimate statutory maximum fines and penalties for uninsured or dangerously non-compliant employers.",
        "link": "employer-penalty-estimator/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    },
    {
        "title": "Settlement Range Guide",
        "desc": "Forecast potential resolution ranges using medical multipliers, historical wage data, and disability algorithms.",
        "link": "settlement-range-guide/index.html",
        "tag": "Core Model",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>',
        "color": ""
    },
    {
        "title": "Vocational Rehab Guide",
        "desc": "Discover what retraining benefits or job displacement vouchers your state mandates.",
        "link": "vocational-rehab-guide/index.html",
        "tag": "Tier 2 Model",
        "icon": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>',
        "color": "background: rgba(138, 43, 226, 0.08); color: #8A2BE2; border-color: rgba(138, 43, 226, 0.2);"
    },
    {
        "title": "SS Offset Calculator",
        "desc": "Understand the complex federal formula for how Social Security Disability (SSDI) reduces your comp checks.",
        "link": "ss-offset-calculator/index.html",
        "tag": "Tier 3 Model",
        "icon": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="7.5 4.21 12 6.81 16.5 4.21"></polyline><polyline points="7.5 19.79 7.5 14.6 3 12"></polyline><polyline points="21 12 16.5 14.6 16.5 19.79"></polyline><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>',
        "color": "background: rgba(0, 191, 255, 0.08); color: #0077FF; border-color: rgba(0, 191, 255, 0.2);"
    }
]

grid_html = '<div class="calc-grid">\n'
for i, c in enumerate(calculators):
    style_str = f' style="{c["color"]}"' if c["color"] else ''
    btn_text = 'Run Calculation' if 'Guide' not in c['title'] and 'Checker' not in c['title'] else 'View Guide'
    if 'Checker' in c['title']: btn_text = 'Check Status'
    if 'Lookup' in c['title']: btn_text = 'Lookup Values'
    if 'Offset' in c['title']: btn_text = 'View Formula'
    
    grid_html += f'''            <!-- Calculator {i+1} -->
            <a href="{c['link']}" style="text-decoration: none;">
                <article class="card calc-card reveal">
                    <div class="calc-card-header">
                        <div class="calc-icon">
                            <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24">{c['icon']}</svg>
                        </div>
                        <span class="tag-t1"{style_str}>{c['tag']}</span>
                    </div>
                    <h3>{c['title']}</h3>
                    <p>{c['desc']}</p>
                    <div class="card-link">
                        {btn_text}
                        <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </div>
                </article>
            </a>\n\n'''

grid_html += '        </div>'

full_html = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workers' Compensation Hub | Premium Legal Calculators</title>
    <meta name="description"
        content="Free, state-specific workers' compensation calculators. Estimate settlement values, weekly benefits, and permanent disability ratings instantly.">
    <link rel="stylesheet" href="global.css">

    <style>
        /* Modern Luxury Header */
        .site-header {{
            padding: 32px 0;
            position: absolute;
            top: 0;
            width: 100%;
            z-index: 100;
        }}

        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .logo {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 12px;
            letter-spacing: -0.02em;
        }}

        .logo svg {{
            width: 32px;
            height: 32px;
            color: var(--brand-primary);
            fill: rgba(255, 90, 0, 0.1);
        }}

        .trust-badge {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8rem;
            color: var(--brand-secondary);
            font-weight: 600;
            padding: 10px 20px;
            border-radius: var(--radius-pill);
            border: 1px solid rgba(74, 93, 35, 0.2);
            background: rgba(74, 93, 35, 0.05);
            backdrop-filter: blur(10px);
        }}

        /* Hero */
        .hero {{
            padding: 200px 0 120px;
            text-align: center;
            position: relative;
        }}

        .hero h1 {{
            font-size: clamp(3.5rem, 7vw, 5rem);
            margin-bottom: 24px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}

        .hero p {{
            font-size: 1.25rem;
            max-width: 550px;
            margin: 0 auto 56px;
            line-height: 1.7;
            color: var(--text-secondary);
        }}

        .hero-actions {{
            display: flex;
            justify-content: center;
            gap: 20px;
        }}

        /* Calculator Grid */
        .calculator-section {{
            padding: 80px 0 140px;
            position: relative;
        }}

        .calc-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 32px;
        }}

        /* Luxury Card Layout */
        .calc-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 32px;
        }}

        .calc-icon {{
            width: 60px;
            height: 60px;
            border-radius: 18px;
            background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
            border: 1px solid rgba(0, 0, 0, 0.06);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.04), inset 0 2px 4px rgba(255,255,255,1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--brand-primary);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease, border-color 0.4s ease;
        }}

        .calc-card:hover .calc-icon {{
            transform: scale(1.08) rotate(-3deg);
            background: linear-gradient(135deg, #ffffff 0%, #fff0e5 100%);
            border-color: rgba(255, 90, 0, 0.2);
            color: var(--brand-hover);
        }}

        .tag-t1 {{
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            padding: 8px 16px;
            border-radius: var(--radius-pill);
            background: rgba(255, 90, 0, 0.08);
            color: var(--brand-primary);
            border: 1px solid rgba(255, 90, 0, 0.15);
        }}

        .calc-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 16px;
            font-weight: 700;
        }}

        .calc-card p {{
            font-size: 1.05rem;
            margin-bottom: 40px;
            color: var(--text-secondary);
            min-height: 54px;
            line-height: 1.6;
        }}

        .card-link {{
            display: inline-flex;
            align-items: center;
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            gap: 8px;
            padding-top: 24px;
            border-top: 1px solid var(--border-subtle);
            width: 100%;
        }}

        .calc-card:hover .card-link {{
            color: var(--brand-primary);
            gap: 12px;
        }}

        /* Footer */
        .site-footer {{
            border-top: 1px solid var(--border-subtle);
            color: var(--text-tertiary);
            padding: 80px 0;
            text-align: center;
        }}

        .site-footer .disclaimer {{
            max-width: 700px;
            margin: 0 auto 32px;
            font-size: 0.85rem;
            color: var(--text-tertiary);
            line-height: 1.8;
        }}

        @media (max-width: 768px) {{
            .hero {{
                padding: 160px 0 100px;
            }}

            .hero-actions {{
                flex-direction: column;
                padding: 0 24px;
            }}

            .btn {{
                width: 100%;
            }}
        }}
    </style>
    <meta property="og:title" content="Workers' Compensation Hub | Premium Legal Calculators">
    <meta property="og:description"
        content="Free, state-specific workers' compensation calculators. Estimate settlement values, weekly benefits, and permanent disability ratings instantly.">
    <meta property="og:type" content="website">
</head>

<body>

    <!-- Header -->
    <header class="site-header">
        <div class="container header-content">
            <div class="logo">
                <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                </svg>
                CompHub
            </div>
            <div class="trust-badge">
                <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24"
                    style="width:16px; height:16px;">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                </svg>
                Secure Environment
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-glow"></div>
        <div class="container reveal active">
            <h1>Legal Valuation,<br>
                <div class="rotating-text">
                    <div class="rotating-words">
                        <span>Simplified.</span>
                        <span>Quantified.</span>
                        <span>Accelerated.</span>
                        <span>Simplified.</span>
                    </div>
                </div>
            </h1>
            <p>Vibrant, highly-accurate calculation models for extreme precision in workers' compensation analysis. Built for clarity and confidence.</p>

            <div class="hero-actions">
                <a href="#tools" class="btn btn-primary">
                    Explore Models
                    <svg class="icon" role="img" aria-label="Vector Icon" viewBox="0 0 24 24">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </a>
            </div>

            <div class="stats-banner">
                <div class="stat-item">
                    <span class="stat-num">15</span>
                    <span class="stat-label">Precision Models</span>
                </div>
                <div class="stat-item">
                    <span class="stat-num">50</span>
                    <span class="stat-label">State Datasets</span>
                </div>
                <div class="stat-item">
                    <span class="stat-num">0s</span>
                    <span class="stat-label">Calculation Time</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Calculators Section -->
    <main class="container calculator-section" id="tools">
{grid_html}
    </main>

    <footer class="site-footer">
        <div class="container">
            <p class="disclaimer">
                The models provided on this platform are for informational and structural estimation purposes only. All workers' compensation claims are subject to nuanced jurisdiction-specific legal interpretations, precise medical evidence, and judicial discretion. This tool assumes standard statutory frameworks and is not a substitute for qualified legal counsel. Use of this application does not create an attorney-client relationship. By utilizing these tools, you agree that CompHub is not liable for any direct, indirect, incidental, or consequential damages arising out of your decisions.
            </p>

            <div class="footer-bottom">
                &copy; 2024 CompHub Premium Analytics. All rights reserved.
            </div>
        </div>
    </footer>

    <!-- Scroll Reveal Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const reveals = document.querySelectorAll('.reveal');
            
            const revealOptions = {{
                threshold: 0.1,
                rootMargin: "0px 0px -50px 0px"
            }};

            const revealOnScroll = new IntersectionObserver(function(entries, observer) {{
                entries.forEach(entry => {{
                    if (!entry.isIntersecting) {{
                        return;
                    }} else {{
                        entry.target.classList.add('active');
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, revealOptions);

            reveals.forEach(reveal => {{
                revealOnScroll.observe(reveal);
            }});
        }});
    </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Index successfully recreated!")
