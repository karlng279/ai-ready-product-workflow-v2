# Assumption Map

**Solution / Idea being tested:** [Name of the solution or feature]
**Date:** YYYY-MM-DD
**Owner:** [PM Name]
**Related OST:** [Link to opportunity-solution-tree.md]

---

## What is an Assumption Map?

An assumption map surfaces ALL the assumptions behind a product idea and prioritizes which ones to test first. Assumptions are organized by type and prioritized by Risk × Uncertainty (not confidence).

**Test the assumption that, if wrong, would kill the idea.**

---

## Assumption Types

### Desirability Assumptions
*(Do customers want this?)*

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|-----------|-----------------|--------------|-------------|----------|
| D1 | [Customers experience problem X frequently enough to pay for a solution] | [Interviews: 4/5 mentioned it] | High | Medium | 🔴 Test |
| D2 | [Customers prefer [our approach] over [alternative approach]] | [None yet] | High | High | 🔴 Test |
| D3 | [Customers are willing to pay $[X]/month for this] | [Pricing survey — n=20] | High | Low | 🟡 Monitor |

### Usability Assumptions
*(Can customers figure out how to use it?)*

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|-----------|-----------------|--------------|-------------|----------|
| U1 | [Users can complete the core flow without instruction] | [None — not built yet] | Medium | High | 🔴 Prototype test |
| U2 | [Users understand what the status labels mean] | [Assumed] | Low | Medium | 🟡 Monitor |

### Feasibility Assumptions
*(Can we build it?)*

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|-----------|-----------------|--------------|-------------|----------|
| F1 | [API X provides the data we need in real time] | [API docs reviewed] | High | Low | 🟢 De-risked |
| F2 | [We can process [N] events/second within current infrastructure] | [Load test needed] | High | High | 🔴 Spike |

### Viability Assumptions
*(Does this work for the business?)*

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|-----------|-----------------|--------------|-------------|----------|
| V1 | [COGS per user stays below $[X] at scale] | [Estimated, not validated] | High | High | 🔴 Financial model |
| V2 | [This won't cannibalize [existing product] revenue] | [None] | Medium | Medium | 🟡 Monitor |

---

## Prioritization Matrix

Map assumptions on this 2×2. Focus experiments on **top-right quadrant**.

```
High Risk  |  F2, D2, V1  |  D1, U1      |
           |  (Test ASAP)  |  (Test ASAP) |
           |               |              |
Low Risk   |  U2          |  F1          |
           |  (Monitor)   |  (De-risked) |
           +---------------+--------------+
             High Uncertainty  Low Uncertainty
```

---

## Riskiest Assumption & Test Plan

**Riskiest assumption:** [The one assumption that, if wrong, kills the idea]

**Why it's riskiest:** [If this is false, here's the impact...]

**Experiment to test it:**

**Hypothesis:** "We believe [assumption]. If we [action], then [measurable outcome]. We'll know in [X weeks] if [specific metric] moves by [amount]."

**Test method:** [Fake door / Landing page / Prototype / Wizard of Oz / A/B / Customer interview]

**Minimum success criteria:** [What result = assumption confirmed?]

**Result:** [Confirmed ✅ / Refuted ❌ / Inconclusive — fill in after running]

---

## Learnings & Next Steps

**What we learned:** [Summary of test results]

**Impact on the solution:** [Continue / Pivot / Kill / Build]

**Next riskiest assumption to test:** [Which one is next in priority?]
