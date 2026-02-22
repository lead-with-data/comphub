# High-Fidelity Finance UI/UX Design System: Workers' Comp Hub

## 1. Core Principles
The landing page and all calculators must exude **trust, authority, and clarity**. Users are often stressed, dealing with physical injuries, and looking for reliable financial information.
*   **Accessibility First (WCAG 2.1 AA+):** High contrast ratios, legible typography, focus states for keyboard navigation, and clear ARIA labels.
*   **Cognitive Load Reduction:** Complex legal and financial topics broke down into simple, digestible steps. Lots of whitespace.
*   **Trust Signals:** Professional color palette, clear disclaimers, secure connection indicators ("Bank-level security" visual metaphors).
*   **Mobile Excellence:** Since many users will be browsing from mobile devices (often while at doctors' offices or home recovering), the UI must be flawlessly responsive with large touch targets.

## 2. Typography System
We use a premium, highly readable pairing that balances modern finance with authoritative legal tones.
*   **Headings (Authority):** `Outfit`, sans-serif. Used for H1-H3. It's geometric, modern, and clean. (Replacing Syne for a more corporate/financial feel).
*   **Body (Clarity):** `Inter`, sans-serif. The gold standard for modern interface legibility. (Replacing Literata for better screen rendering at small sizes).
*   **Data/Numbers (Precision):** `JetBrains Mono` or `DM Mono`. Used for all calculated results, dollar amounts, and tabular data to ensure numbers align perfectly.

## 3. Color Palette (High-Contrast & Trust-Focused)
A sophisticated palette moving away from stark black/white to deep, calming tones.
*   **Background (Canvas):** `#F8FAFC` (Slate 50) - A very subtle, cool off-white that feels clean but reduces eye strain.
*   **Surface (Cards/Modals):** `#FFFFFF` (White) - Pure white for content containers to create elevation.
*   **Primary Text:** `#0F172A` (Slate 900) - Near-black for maximum WCAG contrast.
*   **Secondary Text:** `#475569` (Slate 600) - For descriptions and less critical info.
*   **Primary Action (Trust/Finance):** `#2563EB` (Blue 600) - A strong, vibrant blue associated with trust and stability.
    *   *Hover:* `#1D4ED8` (Blue 700)
    *   *Focus Ring:* `rgba(37, 99, 235, 0.4)`
*   **Success/Money (Positive):** `#059669` (Emerald 600) - Used for settlement ranges and positive financial outcomes.
*   **Warning/Alert (Attention):** `#D97706` (Amber 600) - Used for deadlines or missing info.
*   **Error/Destructive:** `#DC2626` (Red 600).
*   **Borders/Dividers:** `#E2E8F0` (Slate 200).

## 4. UI Components & Interaction Design
### Buttons
*   **Primary:** Solid background (`#2563EB`), white text, bold font, slight shadow (`box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1)`). Hover state lifts button 1px.
*   **Secondary:** Outlined, text matches outline color.
*   **Border Radius:** `8px` - The sweet spot between friendly (rounded) and professional (sharp).

### Form Inputs (The core of the calculators)
*   Must have visible labels.
*   Background: `#FFFFFF`.
*   Border: `1.5px solid #CBD5E1`.
*   Focus State: **CRITICAL FOR ACCESSIBILITY**. Border turns `#2563EB` and gets an outer box-shadow ring.
*   Touch Targets: Minimum height of `48px` for all interactive elements.

### Cards (Calculator Modules)
*   Clean white background.
*   Subtle border (`1px solid #E2E8F0`).
*   Soft shadow for elevation (`box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05)`).
*   Hover effect: Slight upward transition (`transform: translateY(-2px)`) to indicate clickability.

## 5. Master Landing Page Layout (The "Hub")
1.  **Header/Navigation:** Clean logo mark. "Secure & Confidential" badge to build immediate trust.
2.  **Hero Section:** 
    *   Clear Value Proposition: "Discover What Your Workers' Comp Case is Really Worth."
    *   Subtext: "20+ free, state-specific calculators. No sign-up required."
    *   Call to Action: "Start with the Top Calculators" (Anchors to Tier 1).
3.  **Calculator Grid (The Core Toolset):**
    *   Organized by category (Tiers 1-4).
    *   Each calculator is represented by a "Card".
    *   Card includes: Icon, Title, Short Description, "Calculate Now" arrow.
    *   Visual hierarchy highlights the "Must-Use" tools (Weekly Benefit, Settlement Value).
4.  **Trust & Educational Section:**
    *   "Why use these tools?" (Accuracy, State-Specific, Free).
    *   Disclaimer banner (Not legal advice, estimations only).
5.  **Footer:** Standard links, privacy policy, terms.

## 6. CSS Architecture Strategy
*   We will create a specific `global.css` for the hub that contains all CSS variables (tokens) representing this design system.
*   The landing page will be `index.html` at the root of the project.
*   Calculators will be moved into a subfolder structure (which they currently are) but linked from the main page.
