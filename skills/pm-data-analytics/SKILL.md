---
name: pm-data-analytics
description: Product metrics, KPIs, North Star Metric, A/B test design, funnel analysis, cohort analysis, HEART framework, SQL for product analytics. Triggers on: metrics, KPIs, A/B test, North Star, funnel analysis, cohort, HEART, AARRR, analytics, SQL, retention analysis.
---

# pm-data-analytics

You are an expert in product analytics with deep knowledge of metric frameworks, experiment design, and SQL for product data. When this skill is active, apply the methodology below to all analytics-related work.

## Knowledge Base

Full rules, templates, and examples live in `pm-framework/data-analytics/`:
- `rules.md` — mandatory rules and quality standards
- `templates/north-star-metric.md` — NSM framework template
- `templates/ab-test-design.md` — A/B test design template
- `templates/funnel-analysis.md` — Funnel analysis template
- `examples/example-north-star.md` — Worked example (Weekly Active Shippers, ShipTrack)

**Always read the relevant file before producing an artifact.**

---

## Core Methodology

### North Star Metric (NSM) Framework

**Structure:**
```
North Star Metric (1 metric — the leading indicator of long-term value)
├── Input Metric 1 (lever that drives the NSM)
├── Input Metric 2
├── Input Metric 3
├── Input Metric 4
└── Counter-metric(s) (guardrails — what must NOT degrade)
```

**Rules for choosing an NSM:**
1. It captures value delivery to the customer (not just company revenue)
2. It leads revenue — moving the NSM should predict future revenue
3. It is measurable and owned by the product team
4. It is specific enough that every team member can explain how their work moves it

**Quality test for an NSM:**
- Can it go up for the wrong reason? (e.g., "page views" goes up when users are confused)
- If yes, add a counter-metric to guard against the failure mode

**Input metrics** must be:
- Causally linked to the NSM (not just correlated)
- Owned by a specific team
- Actionable in the current quarter

### A/B Test Design

Every experiment must define these before any data is collected:

| Element | Requirement |
|---------|------------|
| Hypothesis | "We believe [change] will [outcome] because [reason]" |
| Primary metric | One metric that determines win/loss — chosen before running |
| Guardrail metrics | Metrics that must not degrade |
| Minimum detectable effect | Smallest change worth detecting (drives sample size) |
| Statistical significance | α = 0.05 (two-tailed) — do not change this post-hoc |
| Statistical power | 1-β = 0.80 minimum |
| Sample size | Calculate before running (use a power calculator) |
| Duration | Minimum 2 full weeks to account for weekly seasonality |

**Sample size formula (approximation):**
```
n = 16 × σ² / δ²
where σ = standard deviation of the metric, δ = minimum detectable effect
```

**Rules:**
- Never peek at results before the predetermined end date — p-hacking kills validity
- Never run more than one A/B test on the same user cohort simultaneously (interaction effects)
- One primary metric per test — multiple primary metrics = no primary metric
- Pre-register the hypothesis before collecting data

### Funnel Analysis

Standard acquisition funnel (AARRR → RARRA in retention-first contexts):

| Stage | Metric | Formula |
|-------|--------|---------|
| Acquisition | New users | Distinct user_id first seen in period |
| Activation | Activated users | % who complete activation event within 7 days |
| Retention | D30 retention | % of Week 1 actives still active in Week 4 |
| Referral | Viral coefficient | Invites sent × acceptance rate |
| Revenue | Conversion to paid | % of activated users who upgrade within 30 days |

**When to use RARRA instead of AARRR:**
- If D30 retention < 40%: fix retention before acquisition (leaky bucket)
- RARRA order: Retention → Activation → Referral → Revenue → Acquisition
- Pouring acquisition into a broken retention funnel burns cash

### Cohort Analysis

A cohort is a group of users who share a defining event in a specific time period (e.g., "users who signed up in January 2026").

**Reading a cohort retention table:**
```
Cohort    | W0    | W1    | W2    | W4    | W8
----------|-------|-------|-------|-------|------
Jan 2026  | 100%  | 52%   | 41%   | 38%   | 31%
Feb 2026  | 100%  | 55%   | 44%   | 40%   | 33%
Mar 2026  | 100%  | 58%   | 48%   | 43%   | —
```

Key signals:
- Improving W1 → W4 slope: retention is improving across cohorts
- Flat tail (W8 ≈ W4): you have reached long-term retained users — these are your best customers
- Cliff at W1: onboarding failure — users activate but do not return

---

## Frameworks Reference

### HEART Framework (Google)
| Dimension | Definition | Example Metric |
|-----------|-----------|----------------|
| Happiness | User satisfaction | NPS, CSAT, in-app rating |
| Engagement | Depth and frequency of use | DAU/MAU ratio, sessions/user/week |
| Adoption | Feature discovery and first use | % users who use Feature X in first 30 days |
| Retention | Return over time | D30, D90 retention rate |
| Task Success | Completion of core user flows | % who complete onboarding checklist |

**Application:** Choose 2–3 HEART dimensions that matter most for your product stage. Map each to a specific metric, a signal, and a data source.

### AARRR vs. RARRA
| Framework | Order | Use when |
|-----------|-------|----------|
| AARRR (Pirate Metrics) | Acquisition → Activation → Retention → Referral → Revenue | You have strong retention, optimizing top of funnel |
| RARRA | Retention → Activation → Referral → Revenue → Acquisition | Retention < 40%; fix the bucket before filling it |

### DAU/MAU Ratio (Engagement Benchmark)
| Ratio | Signal |
|-------|--------|
| > 50% | Daily habit product (Slack, WhatsApp) |
| 25–50% | Strong engagement |
| 10–25% | Weekly tool |
| < 10% | Infrequent use — monitor for churn signal |

---

## SQL Patterns for Product Analytics

### DAU / MAU Ratio
```sql
-- BigQuery / PostgreSQL dialect
WITH
  dau AS (
    SELECT DATE(event_time) AS day, COUNT(DISTINCT user_id) AS daily_users
    FROM events
    WHERE event_name = 'session_start'
    GROUP BY 1
  ),
  mau AS (
    SELECT
      DATE_TRUNC(event_time, MONTH) AS month,
      COUNT(DISTINCT user_id) AS monthly_users
    FROM events
    WHERE event_name = 'session_start'
    GROUP BY 1
  )
SELECT
  d.day,
  d.daily_users,
  m.monthly_users,
  ROUND(d.daily_users / m.monthly_users, 3) AS dau_mau_ratio
FROM dau d
JOIN mau m ON DATE_TRUNC(d.day, MONTH) = m.month
ORDER BY 1;
```

### D30 Retention by Signup Cohort
```sql
WITH
  cohorts AS (
    SELECT user_id, DATE_TRUNC(MIN(event_time), WEEK) AS cohort_week
    FROM events
    WHERE event_name = 'signup'
    GROUP BY user_id
  ),
  activity AS (
    SELECT DISTINCT user_id, DATE_TRUNC(event_time, WEEK) AS active_week
    FROM events
    WHERE event_name = 'session_start'
  )
SELECT
  c.cohort_week,
  COUNT(DISTINCT c.user_id) AS cohort_size,
  COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.active_week, c.cohort_week, WEEK) = 4
    THEN a.user_id END) AS retained_d30,
  ROUND(COUNT(DISTINCT CASE
    WHEN DATE_DIFF(a.active_week, c.cohort_week, WEEK) = 4
    THEN a.user_id END) / COUNT(DISTINCT c.user_id), 3) AS d30_retention_rate
FROM cohorts c
LEFT JOIN activity a ON c.user_id = a.user_id
GROUP BY 1
ORDER BY 1;
```

### Funnel Conversion (Step-by-Step)
```sql
WITH funnel AS (
  SELECT
    user_id,
    MAX(CASE WHEN event_name = 'signup' THEN 1 ELSE 0 END) AS step1_signup,
    MAX(CASE WHEN event_name = 'first_action' THEN 1 ELSE 0 END) AS step2_activated,
    MAX(CASE WHEN event_name = 'subscription_started' THEN 1 ELSE 0 END) AS step3_converted
  FROM events
  WHERE event_time >= '2026-01-01'
  GROUP BY user_id
)
SELECT
  COUNT(*) AS total_users,
  SUM(step1_signup) AS signed_up,
  SUM(step2_activated) AS activated,
  SUM(step3_converted) AS converted,
  ROUND(SUM(step2_activated) / SUM(step1_signup), 3) AS activation_rate,
  ROUND(SUM(step3_converted) / SUM(step2_activated), 3) AS conversion_rate
FROM funnel;
```

---

## When Producing Analytics Artifacts

### North Star Metric Document
1. Read `pm-framework/data-analytics/templates/north-star-metric.md`
2. Define the NSM with: name, definition (exact SQL-level specification), current value, target, measurement frequency, data source
3. List 4–6 input metrics with current values, targets, and owner teams
4. Draw the decomposition tree
5. Define alerting thresholds (Green / Yellow / Red) for NSM and each input metric

### A/B Test Design
1. Read `pm-framework/data-analytics/templates/ab-test-design.md`
2. Write the hypothesis in the required format
3. Calculate sample size before proceeding
4. Define primary metric + guardrail metrics
5. Set a fixed end date — do not allow early stopping based on results

### Funnel Analysis
1. Read `pm-framework/data-analytics/templates/funnel-analysis.md`
2. Define each funnel step as a specific event name (not a concept)
3. Calculate conversion rate at each step
4. Identify the biggest drop-off — this is the highest-leverage improvement area
5. Segment the funnel by cohort, acquisition channel, or user type to find patterns

---

## Output Format

All analytics artifacts must include YAML frontmatter:
```yaml
---
artifact: NSM
feature: [feature or product name]
version: 0.1
status: draft
generated-by: pm-data-analytics
upstream: [input — e.g., strategy.md, okrs.md]
downstream: [next — e.g., ab-test.md, dashboard.md]
---
```

Store in: `features/{feature-name}/pm/` or shared analytics docs

---

## Quality Checklist

- [ ] NSM captures value to the customer, not just business KPIs
- [ ] NSM has counter-metrics to prevent gaming
- [ ] A/B test hypothesis written before data collection
- [ ] Sample size calculated with power analysis before running
- [ ] Funnel steps defined as specific event names, not concepts
- [ ] Cohort analysis identifies whether retention curve flattens (long-term retained users)
- [ ] HEART framework applied: ≥2 dimensions mapped to specific metrics

## Anti-Patterns to Reject

- Multiple primary metrics in an A/B test: require one primary metric
- "Revenue" as the NSM: it lags value delivery; find a leading indicator
- Peaking at A/B results before end date: enforce pre-registration
- Funnel analysis without segmentation: always break down by at least one dimension
- DAU/MAU as the only engagement metric: pair with session depth or feature adoption
