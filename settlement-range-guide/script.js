// script.js

// Simplified multiplier examples based on injury severity
const INJURY_MULTIPLIERS = {
    'minor': { low: 1.2, high: 2.0 },
    'moderate': { low: 2.5, high: 4.0 },
    'severe': { low: 4.5, high: 8.0 } // Often much higher, keeping conservative
};

// State-specific benefit rates (simplified for example)
const STATE_RATES = {
    'CA': 0.6667,
    'TX': 0.70,
    'NY': 0.6667,
    'FL': 0.6667,
    'IL': 0.6667
};

document.addEventListener('DOMContentLoaded', () => {
    const calculateBtn = document.getElementById('calculate-btn');

    // Inputs
    const stateSelect = document.getElementById('state-select');
    const injuryTypeSelect = document.getElementById('injury-type');
    const awwInput = document.getElementById('avg-weekly-wage');
    const weeksOutInput = document.getElementById('weeks-out');
    const medicalBillsInput = document.getElementById('medical-bills');
    const impairmentRatingInput = document.getElementById('impairment-rating');
    const permDisabilitySelect = document.getElementById('permanent-disability');

    // Outputs
    const resultsZone = document.getElementById('results-zone');
    const settlementRangeDisplay = document.getElementById('settlement-range');
    const estLostWagesDisplay = document.getElementById('est-lost-wages');
    const medicalFactorDisplay = document.getElementById('medical-factor');
    const impairmentValueDisplay = document.getElementById('impairment-value');

    calculateBtn.addEventListener('click', () => {
        // Validation
        if (!stateSelect.value || !awwInput.value || !weeksOutInput.value || !medicalBillsInput.value) {
            alert('Please fill out all required fields.');
            return;
        }

        const stateRate = STATE_RATES[stateSelect.value] || 0.6667;
        const aww = parseFloat(awwInput.value);
        const weeksOut = parseFloat(weeksOutInput.value);
        const medicalBills = parseFloat(medicalBillsInput.value);
        const impairmentRating = impairmentRatingInput.value ? parseFloat(impairmentRatingInput.value) : 0;
        const isPerm = permDisabilitySelect.value === 'yes';
        const severity = injuryTypeSelect.value;

        // 1. Calculate Lost Wages (Past)
        const weeklyBenefit = aww * stateRate;
        const lostWages = weeklyBenefit * weeksOut;

        // 2. Medical Multiplier (General Damages estimation)
        const multiplierRange = INJURY_MULTIPLIERS[severity];
        const medLow = medicalBills * multiplierRange.low;
        const medHigh = medicalBills * multiplierRange.high;

        // 3. Impairment Value (Highly simplified proxy: Rating * specific dollar value or weeks)
        // In reality, this is heavily state-dependent. We use a generic proxy here for V1.
        let impairmentValueLow = 0;
        let impairmentValueHigh = 0;

        if (isPerm || impairmentRating > 0) {
            // Rough estimate: Each % point is worth 3 weeks of pay (very generic)
            const weeksPerPoint = 3;
            const baseImpairment = (impairmentRating || 10) * weeksPerPoint * weeklyBenefit;
            impairmentValueLow = baseImpairment;
            impairmentValueHigh = baseImpairment * 1.5; // High end negotiation
        }


        // Total Settlement Range
        const totalLow = lostWages + medLow + impairmentValueLow;
        const totalHigh = lostWages + medHigh + impairmentValueHigh;

        // Format Currency
        const formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0 // Remove cents for ranges to look cleaner
        });

        // Update UI
        settlementRangeDisplay.textContent = `${formatter.format(totalLow)} - ${formatter.format(totalHigh)}`;
        estLostWagesDisplay.textContent = formatter.format(lostWages);
        medicalFactorDisplay.textContent = `${multiplierRange.low}x - ${multiplierRange.high}x`;
        impairmentValueDisplay.textContent = impairmentValueLow > 0 ? `${formatter.format(impairmentValueLow)}+` : 'N/A';

        // Show Results
        resultsZone.classList.remove('hidden');
        resultsZone.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
});
