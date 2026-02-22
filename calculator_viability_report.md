# Workers' Compensation Calculators: Viability & Accuracy Analysis

This document evaluates all 20 of the proposed Workers' Compensation calculators. 

It breaks down exactly which tools provide **Mathematical Certainty** (based on strict state statutes), which run on **Subjective Estimation** (and thus cannot be relied on as legal advice without representation), and which tools require **Complex Real-World Databases** (like NCCI class codes or frequently updated state max/min tables) to function correctly.

> [!WARNING]
> None of these calculators constitute formal legal advice. Insurance adjusters and judges frequently dispute inputs (such as Average Weekly Wage or Impairment Ratings), which alters the final output. The math may be perfect, but the *inputs* are often contested in court.

---

## 🟢 Category 1: High Accuracy (Strict Statutory Math)
These calculators are highly accurate because they rely on hard math, calendar days, or direct state statutes. As long as the inputs are undisputed and the under-the-hood state maximum tables are updated annually, the formulas output the legal ground-truth.

1. **Average Weekly Wage (AWW) Calculator** 
   - *Accuracy:* Extremely High. Summing 52 weeks of pay divided by weeks worked is universally established math. 
   - *Data Needs:* Just user inputs (wages, overtime, weeks).
2. **Lost Wages Calculator**
   - *Accuracy:* High. Direct calculation of days missed multiplied by the weekly rate.
   - *Data Needs:* User dates and the AWW.
3. **Filing Deadline Checker**
   - *Accuracy:* High. It’s a strict calendar calculation from the date of injury against the state's Statute of Limitations (SOL).
   - *Data Needs:* Static state SOL rules (e.g., California is 1 year from injury date).
4. **State Weekly Benefit Cap Lookup**
   - *Accuracy:* Perfect. It is simply a data retrieval tool.
   - *Data Needs:* Requires a frequently updated database of state minimums and maximums for the given year of injury.
5. **Waiting Period Calculator**
   - *Accuracy:* High. State statutes clearly define exactly how many days you must wait before being paid, and when retroactive pay kicks in.
   - *Data Needs:* Static state waiting period data rules.
6. **Workers' Comp Coverage Requirement Checker**
   - *Accuracy:* High. The rules for whether an employer MUST carry insurance are usually a simple logical tree based on the number of full-time employees and industry type.
   - *Data Needs:* Static state rules threshold data.
7. **Attorney Fee Calculator**
   - *Accuracy:* High. Most states cap attorney fees at strict statutory percentages of the final award (e.g., 15% in California, 20% in New York).
   - *Data Needs:* Static state percentage caps.

---

## 🟡 Category 2: Moderate Accuracy (Reliant on Medical Data / Formulas)
These calculators execute strict mathematical formulas, but the primary variables are inherently subjective medical opinions that adjusters frequently challenge. 

8. **Weekly Benefit Calculator**
   - *Accuracy:* Moderate-High. The math is simple (e.g., 66.67% of AWW). The inaccuracy comes from the fact that adjusters heavily dispute the underlying AWW or use different formulas for piece-rate workers.
   - *Data Needs:* Annual state maximum benefit tables.
9. **Permanent Partial Disability (PPD) Calculator/Impairment Rating Payout**
   - *Accuracy:* Moderate. If you are handed an uncontested rating (e.g., 15% WPI), the calculation of the dollar award is pure math. However, the rating *itself* is extremely subjective and often contested.
   - *Data Needs:* Extensive state disability rating schedules or AMA Guides proxy values.
10. **Death Benefits Calculator**
   - *Accuracy:* Moderate. The formulas exist, but determining partial vs. total dependency for surviving family members is a highly litigated legal issue that an algorithm cannot reliably determine.
   - *Data Needs:* State maximums and burial allowance data.
11. **Body Part Injury Value Calculator (Scheduled Loss of Use)**
   - *Accuracy:* Moderate. Scheduled loss is heavily legislated (e.g., losing a thumb in NY is worth exactly 75 weeks of pay). However, determining whether a worker lost 10% vs 50% use of that thumb is highly subjective.
   - *Data Needs:* Exact state schedules for every body part.
12. **Social Security Offset Calculator**
   - *Accuracy:* Moderate-Low. The federal "80% ACE rule" formula is exact, but acquiring the correct initial Average Current Earnings (ACE) from the SSA is difficult for an average user to do accurately.
   - *Data Needs:* Complex interaction with federal SSA rules and calculations.
13. **Payroll Audit Estimator**
   - *Accuracy:* Moderate. Simple math (total payroll x rate/100). The inaccuracy lies in the fact that auditors have extreme discretion in reclassifying independent contractors as employees, thus inflating the final bill unexpectedly.
   - *Data Needs:* User inputs on payroll and their NCCI class rates.

---

## 🔴 Category 3: Low Accuracy / Estimation Only (Highly Subjective)
These calculators are purely indicative. They serve as marketing hooks or baseline expectations, but they do NOT output true legal reality. These are heavily influenced by venue, judge temperament, negotiation tactics, and litigation risk.

14. **Settlement Value Estimator**
   - *Accuracy:* Very Low. Compromise and Release settlements negotiate future medical care, which is entirely subjective (often using a 1x to 8x multiplier). No algorithm can accurately predict what a defense attorney is willing to pay to close a file without deep machine learning on local verdicts.
   - *Data Needs:* Arbitrary multipliers or highly localized historical settlement data.
15. **Future Medical Cost Estimator / Nurse Case Manager Cost Estimator**
   - *Accuracy:* Very Low. The cost of future medical care over a 30-year lifetime is wildly speculative.
   - *Data Needs:* Requires massive databases of Medicare Set-Aside (MSA) cost projections and localized healthcare fee schedules.
16. **Employer Penalty & Fine Estimator**
   - *Accuracy:* Low. State boards evaluate fines subjectively. While maximum penalties are codified (e.g., "up to $100,000 for uninsured employers"), the actual fine assessed is highly variable based on employer intent and judge discretion.
   - *Data Needs:* Complex state penalty matrices database.
17. **Vocational Rehabilitation Benefit Estimator**
   - *Accuracy:* Low. In many states (like CA's $6,000 voucher), the benefit is fixed, so it's a binary Yes/No. In other states where tuition isn't capped, predicting the cost of retraining a worker is wildly variable.
   - *Data Needs:* State-specific voucher rules.

---

## 🟣 Category 4: Enterprise Complexity (Requires Heavy External Data Integration)
These are mathematically sound, but an individual developer cannot easily build them without paying thousands of dollars for proprietary API access to institutional rating bureaus.

18. **Workers' Comp Premium Estimator**
   - *Accuracy:* Moderate. The formula is pure math.
   - *Data Needs:* **MASSIVE.** You need access to thousands of frequently changing NCCI or state-specific Class Codes and their associated base rates per $100 of payroll, which differ by state, carrier, and year. 
19. **Experience Modification (E-Mod) Calculator**
   - *Accuracy:* Moderate.
   - *Data Needs:* **EXTREME.** You need access to the NCCI's proprietary actuarial formula, the employer's audited payrolls for 3 years, and exact claims history values. This is incredibly difficult to build without direct integration into insurance carrier loss runs.

---

## Executive Summary: Is it worth making?

If your goal is to generate **high-quality leads** for a law firm or agency: **YES.**
Even the "Low Accuracy" estimators (like the Settlement Estimator) are incredibly valuable marketing tools because injured workers are desperate for ballpark numbers. As long as you display a prominent "Not Legal Advice" disclaimer and a "Connect with an Attorney" CTA, they succeed at their goal.

### What you should build next:
You should strongly consider building **Category 1** and **Category 2** tools, as they bring high value and are relatively easy to maintain. 

You should **AVOID** Category 4 (Premium Estimator, E-Mod Calculator) unless you are heavily funded and willing to license the proprietary NCCI class code tables, as doing that manually for 50 states is near impossible.
