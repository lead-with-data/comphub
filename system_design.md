# System Architecture & Design Plan

## 1. Core Technology Stack
- **Frontend Framework:** Vanilla HTML, CSS, JavaScript (No heavy frameworks like React/Vue).
- **Styling:** Custom CSS with CSS variables for theming, ensuring ease of maintenance and a premium look.
- **Responsiveness:** CSS Grid and Flexbox for mobile-first layout (usable on phones).
- **Hosting/Deployment:** Can be hosted anywhere (GitHub Pages, Vercel, Netlify, or embedded via iframe into WordPress/Webflow).

## 2. Design Aesthetics (Adhering to Master Build List)
- **Typography:** 'Syne' for bold headers, 'Literata' for body text, 'DM Mono' for data/labels.
- **Color Palette:** 
    - Backgrounds: Off-white (`#F7F4EF`, `#F0EDE8`)
    - Text: Dark Ink (`#1C1917`, `#57534E`)
    - Accents: Gold (`#B45309`, `#FCD34D`), Green (`#15803D`), Red (`#DC2626`)
- **Interactivity:** Soft shadows on hover, smooth transitions for inputs and results.

## 3. Component Architecture
Each calculator will follow a standardized markup and logic structure to maintain consistency:
1. **Header Zone:** Calculator Title & Brief Description.
2. **Input Zone:** Form fields (Dropdowns, Number Inputs, Date Pickers, Toggles).
3. **Action Zone:** Calculate Button.
4. **Results Zone:** Hidden strictly by default, displayed cleanly with animations upon calculation. Contains primary output (e.g., Weekly Benefit $) and secondary outputs (e.g., State Cap Note).

## 4. State Management & Data Handling
- **State Data:** State-specific maximum caps and formulas (e.g., California max weekly benefit $1,620) will be stored in a centralized JavaScript constant/JSON object. This allows for easy annual updates without touching core calculation logic.
- **Calculations:** Pure JavaScript functions handling inputs, applying state rules, and returning formatted output (currency).
- **Validation:** Basic HTML5 validation (`required`, `min`, `max`) coupled with JS checks to prevent erroneous negative number calculations.

## 5. Extensibility
The architecture is designed so that adding the remaining 19 calculators involves:
- Copying the base HTML/CSS layout.
- Defining the new inputs.
- Writing the specific mathematical logic function.
- Hooking the calculate button to the new function.

## 6. Development Workflow (Calculator 1: Weekly Benefit)
1. **Setup base CSS/HTML structure.**
2. **Implement Input UI:** State Dropdown, Gross Weekly Wage Input, Date Picker (if needed for caps), Disability Type.
3. **Implement Logic:** `Wage * 0.6667`, apply state-specific cap lookup from data object.
4. **Implement Results UI:** Display formatted output.
