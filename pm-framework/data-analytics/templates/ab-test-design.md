# A/B Test Design Document

**Test Name:** [Descriptive name — e.g., "Onboarding Step 2 — Add Progress Bar"]
**Test Owner:** [PM Name]
**Date:** YYYY-MM-DD
**Status:** Draft / Running / Concluded

---

## Background

**Problem / Opportunity:**
> [What user problem or business metric gap is this test designed to address?]

**Hypothesis (full):**
> "We believe that [change] will [improve / increase / reduce] [primary metric] for [user segment] because [reason]. We'll know we're right if [metric] changes by [minimum detectable effect] within [test duration]."

---

## Test Design

### Variants

| Variant | Description | Visual / Technical change |
|---------|-------------|--------------------------|
| **Control (A)** | Current experience — no change | [Description or link to screenshot] |
| **Treatment (B)** | [What changes] | [Description or link to mock] |
| *(Optional) Treatment (C)* | [Alternative change] | [Description] |

### Audience

| Attribute | Value |
|-----------|-------|
| **Target segment** | [Who is eligible for this test? New users / returning users / all / specific cohort] |
| **Traffic split** | [50/50 / 80/20 / other — rationale] |
| **Geographic scope** | [All regions / specific region] |
| **Exclusions** | [Any users who should be excluded — e.g., internal accounts, admins] |

---

## Metrics

### Primary Metric
| Metric | Current Value | Minimum Detectable Effect (MDE) | Expected Lift |
|--------|--------------|--------------------------------|---------------|
| [Metric name — e.g., Onboarding completion rate] | [X%] | [+Y% absolute or +Y% relative] | [Expected improvement] |

*The test is only considered a success if the primary metric improves significantly.*

### Secondary Metrics (directional)
| Metric | Direction | Notes |
|--------|-----------|-------|
| [Metric 2] | ↑ Increase / ↓ Decrease | [What it tells us] |
| [Metric 3] | ↑ / ↓ | |

### Guard-rail Metrics (must NOT regress)
| Metric | Threshold | Why |
|--------|-----------|-----|
| [e.g., Revenue per user] | Must not decrease by >2% | [Protect against conversion cannibalization] |
| [e.g., Support ticket rate] | Must not increase by >5% | [Protect against usability regression] |

---

## Statistical Design

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Confidence level** | 95% | Standard |
| **Statistical power** | 80% | Standard |
| **Minimum detectable effect** | [X% relative] | [Smallest change worth detecting] |
| **Baseline conversion rate** | [X%] | [Current primary metric value] |
| **Required sample size** | [N per variant] | [Calculated via power analysis] |
| **Estimated daily traffic** | [N users/day] | [From analytics] |
| **Required test duration** | [N days] | [Sample size ÷ daily traffic] |
| **Minimum test duration** | 14 days | [Run for ≥2 full business cycles regardless] |

*Sample size calculator used:* [Tool name / link]

---

## Implementation

**Engineering ticket:** [Link]

**Feature flag / experiment key:** [Key name in analytics tool]

**Analytics events to instrument:**
| Event Name | Trigger | Properties |
|-----------|---------|------------|
| [event_name] | [When it fires] | [key: value] |

**QA checklist:**
- [ ] Control shows unchanged experience for 50% of traffic
- [ ] Treatment shows changed experience for 50% of traffic
- [ ] All analytics events fire correctly in both variants
- [ ] Guard-rail metrics instrumented and alerting set up
- [ ] No leakage between variants (verify with AA test if needed)

---

## Test Timeline

| Milestone | Date |
|-----------|------|
| Test design approved | YYYY-MM-DD |
| Engineering implementation | YYYY-MM-DD |
| QA complete | YYYY-MM-DD |
| Test launch | YYYY-MM-DD |
| Interim check (50% of duration) | YYYY-MM-DD |
| Test conclusion (planned) | YYYY-MM-DD |
| Decision & shipping | YYYY-MM-DD |

---

## Decision Rules

**Ship (Treatment wins):** Primary metric improves by ≥ MDE with p < 0.05, and no guard-rail metrics regress beyond threshold.

**Iterate:** Primary metric shows directional improvement but does not reach significance. Review learnings and redesign.

**Kill (Control wins):** Primary metric does not improve, or guard-rail metrics regress significantly.

---

## Results

*(Fill in after test concludes)*

| Metric | Control | Treatment | Lift | p-value | Significant? |
|--------|---------|-----------|------|---------|--------------|
| Primary metric | | | | | ✅ / ❌ |
| Secondary metric | | | | | |
| Guard-rail metric | | | | | ✅ Not regressed |

**Decision:** ☐ Ship ☐ Iterate ☐ Kill

**Rationale:** [Why this decision?]

**Learnings:** [What did you learn beyond the primary result?]
