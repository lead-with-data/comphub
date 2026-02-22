// script.js

// State Data (2024 Maximums - Examples)
const STATE_DATA = {
    'CA': { name: 'California', maxWeeklyBenefit: 1619.15, rate: 0.6667 },
    'TX': { name: 'Texas', maxWeeklyBenefit: 1195.00, rate: 0.70 }, // Texas pays 70%
    'NY': { name: 'New York', maxWeeklyBenefit: 1145.43, rate: 0.6667 },
    'FL': { name: 'Florida', maxWeeklyBenefit: 1260.00, rate: 0.6667 },
    'IL': { name: 'Illinois', maxWeeklyBenefit: 1873.17, rate: 0.6667 }
};

document.addEventListener('DOMContentLoaded', () => {
    const calculateBtn = document.getElementById('calculate-btn');
    const stateSelect = document.getElementById('state-select');
    const grossWageInput = document.getElementById('gross-wage');
    const injuryDateInput = document.getElementById('injury-date');

    // Results Elements
    const resultsZone = document.getElementById('results-zone');
    const weeklyBenefitAmountDisplay = document.getElementById('weekly-benefit-amount');
    const stateMaxAmountDisplay = document.getElementById('state-max-amount');
    const benefitNoteDisplay = document.getElementById('benefit-note');

    // Default injury date to today
    injuryDateInput.valueAsDate = new Date();

    calculateBtn.addEventListener('click', () => {
        // Basic Validation
        const stateCode = stateSelect.value;
        const grossWage = parseFloat(grossWageInput.value);

        if (!stateCode) {
            alert('Please select a state.');
            return;
        }
        if (isNaN(grossWage) || grossWage <= 0) {
            alert('Please enter a valid Gross Weekly Wage.');
            return;
        }

        // Get State Rules
        const stateRules = STATE_DATA[stateCode];

        // Calculate Benefit
        let calculatedBenefit = grossWage * stateRules.rate;
        let isCapped = false;

        if (calculatedBenefit > stateRules.maxWeeklyBenefit) {
            calculatedBenefit = stateRules.maxWeeklyBenefit;
            isCapped = true;
        }

        // Format Currency
        const formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2
        });

        // Update UI
        weeklyBenefitAmountDisplay.textContent = formatter.format(calculatedBenefit);
        stateMaxAmountDisplay.textContent = formatter.format(stateRules.maxWeeklyBenefit);

        // Update Note
        const ratePercent = (stateRules.rate * 100).toFixed(2);
        if (isCapped) {
            benefitNoteDisplay.textContent = `You hit the ${stateRules.name} state maximum cap.`;
            benefitNoteDisplay.style.color = '#F59E0B'; // Amber - Warning Glow
        } else {
            benefitNoteDisplay.textContent = `Based on ${ratePercent}% of your gross weekly wage.`;
            benefitNoteDisplay.style.color = '#10B981'; // Emerald - Success Glow
        }

        // Show Results
        resultsZone.classList.remove('hidden');

        // Scroll to results smoothly
        resultsZone.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
});
