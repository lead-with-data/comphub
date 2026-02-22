# Workers' Compensation Calculators - Implementation Documentation

This document outlines the **11 calculators** that have been fully built, structured, and integrated into the application so far. Below is a detailed breakdown of the mathematical formulas, logic, and state-specific variables each model executes.

---

## 1. Average Weekly Wage (AWW) Calculator
**Slug:** `aww-calculator`
**Purpose:** Calculates the foundational metric (AWW) upon which almost all workers' comp benefits are based.

**Formula & Logic:**
```
Total Annual Earnings = (Hourly Rate * Hours Per Week * 52) 
                        + Annual Overtime 
                        + Annual Bonuses 
                        + (Value of Employer Paid Meals/Housing) 
                        + Concurrent Employment (Earnings from 2nd jobs)

Gross AWW = Total Annual Earnings / 52
```
*Note: The model scales regular wages to an annual figure and adds additional non-standard compensation before taking the weekly average, ensuring accurate representation of the worker's true earning capacity.*

---

## 2. Weekly Benefit Calculator (TTD/TPD Base)
**Slug:** `weekly-benefit-calculator`
**Purpose:** Determines the exact weekly check amount an injured worker is legally entitled to while totally off work.

**Formula & Logic:**
```
Uncapped Benefit = AWW * State Compensation Rate (Typically 66.67%, but 70% in TX)

If (Uncapped Benefit > State Statutory Maximum):
    Actual Check = State Statutory Maximum
Else If (Uncapped Benefit < State Statutory Minimum):
    Actual Check = State Statutory Minimum
Else:
    Actual Check = Uncapped Benefit
```
*Variables Built-in:*
*   **CA:** 66.67% rate. Max: $1,619.15. Min: $242.86.
*   **TX:** 70.00% rate. Max: $1,195.00. Min: $179.00.
*   **NY:** 66.67% rate. Max: $1,145.43. Min: $275.00.
*   **FL:** 66.67% rate. Max: $1,260.00. Min: $20.00.
*   **IL:** 66.67% rate. Max: $1,873.17. Min: $351.22.

---

## 3. Lost Wages Calculator (Back-Pay)
**Slug:** `lost-wages-calculator`
**Purpose:** Calculates the exact retroactive lump-sum wage replacement owed for past periods of missed work, factoring in partial earnings.

**Formula & Logic:**
```
1. Calculate Weeks Missed = (End Date - Start Date) in Days / 7

2. If (Post-Injury Earnings == 0) -> Total Disability Mode:
   Gross Owed = (AWW * State Rate [e.g., 0.6667], capped at State Max) * Weeks Missed

3. If (Post-Injury Earnings > 0) -> Partial Disability Mode:
   Weekly Wage Loss = (AWW - Post-Injury Earnings)
   Weekly Partial Rate = Weekly Wage Loss * State Rate [e.g., 0.6667]
   Gross Owed = Weekly Partial Rate * Weeks Missed

Net Back-Pay Owed = Gross Owed - Benefits Already Paid by Insurance
```

---

## 4. Filing Deadline Checker (Statute of Limitations)
**Slug:** `filing-deadline-checker`
**Purpose:** Calendar math to determine the absolute final date to file a formal state claim before the worker's rights evaporate.

**Formula & Logic:**
```
State SOL Duration = Look up State (e.g., CA=1 year, TX=1 year, NY=2 years, FL=2 years, IL=3 years)

Absolute Deadline = Date of Injury + State SOL Duration (in years)

Status = If (Current Date > Absolute Deadline) 
            -> "EXPIRED" 
         Else 
            -> "ACTIVE: X Days Remaining"
```

---

## 5. State Benefit Cap Lookup
**Slug:** `state-benefit-cap-lookup`
**Purpose:** A pure data table lookup to instantly inform high-earners of their exact statutory caps based on the state and year of injury.

**Formula & Logic:**
```
Max Cap = Lookup(State, Injury Year)
Min Cap = Lookup(State, Injury Year)

Wage Required to Hit Max = Max Cap / State Rate (e.g., 0.6667)
```
*Logic: Shows workers exactly how much pre-injury salary they must earn to max out the system, proving that high earners lose a massive percentage of their income under comp.*

---

## 6. Waiting Period Calculator
**Slug:** `waiting-period-calculator`
**Purpose:** Determines when the first check is legally due and if the worker missed enough days to get paid retroactively for the initial unpaid "waiting days."

**Formula & Logic:**
```
Total Missed Days = First Day Off until Return Date (or Today)

If (Total Missed Days <= State Wait Days):
    Status: "Currently Unpaid" (You haven't breached the waiting period)

Else If (Total Missed Days > State Wait Days AND Total Missed Days < State Retroactive Threshold):
    Status: "Paid, BUT initial wait days remain unpaid."

Else If (Total Missed Days >= State Retroactive Threshold):
    Status: "100% Qualified." (You are out long enough that the insurance company MUST retroactively pay you for the initial wait days.)
```
*Variables (Wait Days / Retroactive Days):*
*   CA: 3 / 14
*   TX: 7 / 14
*   NY: 7 / 14
*   FL: 7 / 21

---

## 7. Impairment Rating Payout (Whole Person PPD)
**Slug:** `impairment-rating-payout` (Formerly PPD Calculator)
**Purpose:** Calculates the permanent partial disability payout based strictly on an assigned Whole Person Impairment (WPI) rating.

**Formula & Logic:**
```
1. Applicable PPD Rate = AWW * 0.6667 (Capped at highly restricted State PPD Maxes, which are much lower than TTD Maxes).
2. Weeks of Entitlement = State Maximum PPD Weeks * (Impairment Rating %)
   
Total Award = Weeks of Entitlement * Applicable PPD Rate
```
*Variables (Max Weeks / Max PPD Rate):* CA (400 / $290), TX (401 / $836), NY (525 / $1145), FL (348 / $1260).

---

## 8. Body Part Scheduled Award (Loss of Use)
**Slug:** `body-part-scheduled-award`
**Purpose:** Calculates payouts for the specific loss of use of a scheduled member (arm, leg, eye, etc.) utilizing state-mandated schedules.

**Formula & Logic:**
```
State Scheduled Weeks = Lookup State & Body Part (e.g., NY Arm = 312 weeks, TX Arm = 200 weeks).

Awarded Weeks = State Scheduled Weeks * (Percentage of Loss / 100)

Total Payout = Awarded Weeks * Client's Inputted PPD Rate
```

---

## 9. Settlement Range Guide
**Slug:** `settlement-range-guide` (Formerly Settlement Estimator)
**Purpose:** Forecasts potential lump-sum resolution ranges using medical multipliers and indemnity projections. It outputs a Low/Mid/High range rather than a single number.

**Formula & Logic:**
```
1. Projected Future Medical = (Monthly Medical Cost * 12) * Projected Years of Treatment
2. Projected Future Wages = (AWW * 0.6667, capped) * Projected Weeks Off Work
3. Known PPD/Impairment Value = Inputted by User

Base Value = Projected Medical + Projected Wages + PPD Value

Low Estimate = Base Value * 0.70 (Aggressive insurance deductions / weak liability)
Mid Estimate = Base Value * 1.00 (Standard expectation)
High Estimate = Base Value * 1.30 (Strong liability, high medical cost risk)
```

---

## 10. Vocational Rehab Benefit Guide
**Slug:** `vocational-rehab-guide`
**Purpose:** A binary logic tree outlining state-specific retraining/voucher rights if a worker cannot return to their prior employment.

**Formula & Logic:**
```
If (User Can Return to Work == Yes):
    Status: "Not Eligible"

Else If (Still Treating/Undecided):
    Status: "Too Early to Tell" (Must reach MMI first)

Else (Cannot Return to Work):
    CA -> "$6,000 State Voucher + $5,000 Return to Work Fund Cash"
    TX -> "State Agency Referral (Texas Workforce Commission)"
    NY -> "Variable Retraining via ACCES-VR"
    FL -> "Up to 52 Weeks Retraining (Requires heavy pre-approval)"
```

---

## 11. Death Benefits Calculator
**Slug:** `death-benefits-calculator`
**Purpose:** Estimates statutory survivor benefits and maximum burial allowances payable to dependents.

**Formula & Logic:**
```
If (Dependents == 0):
    Payout = $0 to estate. Max Burial applied.

If (Dependents > 0):
    Weekly Installment to Dependents = Deceased's AWW * State Dependent Rate (e.g., 66.67%, or 75% in TX) capped at State Max.
    Total Cap = Lookup State Rules based on dependent count (e.g., CA 1 dep = $250k, 2 deps = $290k).
    Payout Duration = State Rules (e.g., TX = 360 weeks, NY = Lifelong Pension, FL = Until $150k cap).

Fixed Burial Expense = Lookup State Burial Cap (e.g., CA = $10,000, NY = $12,500).
```

---

## 12. Coverage Requirement Checker
**Slug:** `coverage-requirement-checker`
**Purpose:** A state-specific logic filter to determine if an employer is legally mandated to carry workers' compensation insurance.

**Formula & Logic:**
```
CA: Always Required if Employees >= 1.
NY: Always Required if Employees >= 1 (includes part-time & domestic).
TX: Never strictly required (Optional), but massive non-subscriber liability risks exist.
FL: 
  - Construction: Required if Employees >= 1.
  - Agriculture: Required if Regular Employees >= 6.
  - General Business: Required if Employees >= 4.
```

---

## 13. Attorney Fee Calculator
**Slug:** `attorney-fee-calculator`
**Purpose:** Estimates the maximum statutory attorney fees capped by state laws when securing a settlement or award.

**Formula & Logic:**
```
CA Standard: Total Award * 0.15 (15%)
TX Maximum: Total Award * 0.25 (25%)
NY Proxy: Total Award * 0.15 (Judges typically approve 10-15%)
FL Sliding Scale: 
    - 20% of first $5,000
    - 15% of next $5,000
    - 10% of remaining balance
```

---

## 14. Employer Penalty Estimator
**Slug:** `employer-penalty-estimator`
**Purpose:** Calculates the devastating statutory fines levied against businesses operating without legally mandated insurance.

**Formula & Logic:**
```
CA Penalty = (Employees * $10,000) + (Employees * $1,000 Stop Order fine)
NY Penalty = (Days Uninsured / 10) * $2,000
FL Penalty = $1,000 Stop Order Base + (2x Avoided Premium for past 2 years)
TX Penalty = No fine for being uninsured, but up to $25k/day if "non-subscriber" notice isn't filed.
```

---

## 15. Social Security (SSDI) Offset Explainer
**Slug:** `ss-offset-calculator`
**Purpose:** Explains and calculates the federal 80% ceiling limit on combined SSDI and Workers' Comp benefits.

**Formula & Logic:**
```
1. Federal Income Cap = ACE (Average Current Earnings) * 0.80
2. Combined Benefits = Monthly SSDI + Monthly Workers' Comp

If (Combined Benefits > Federal Income Cap):
    Offset Required = Combined Benefits - Federal Income Cap
    (Offset is capped at the total SSDI amount)
Else:
    Offset Required = $0
```
*Note: Evaluates whether the claimant triggers the offset, and outputs a warning about 'reverse offset' states where the comp carrier takes the offset instead of the SSA.*
