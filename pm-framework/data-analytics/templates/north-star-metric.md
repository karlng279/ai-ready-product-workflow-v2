# North Star Metric Framework

**Product / Team:** [Name]
**Date:** YYYY-MM-DD
**Owner:** [PM Name]

---

## What is Our North Star Metric?

The North Star Metric (NSM) is the single number that best captures the value our product delivers to customers. It is a leading indicator — it predicts long-term revenue and retention, but measures customer value directly.

---

## North Star Metric Definition

| Attribute | Value |
|-----------|-------|
| **NSM Name** | [e.g., "Weekly Active Shippers"] |
| **NSM Definition** | [Exact definition — what counts, what doesn't] |
| **Current Value** | [Baseline] |
| **Target (12 months)** | [Goal] |
| **Measurement frequency** | Weekly / Monthly |
| **Data source** | [Where this is tracked] |

**Why this is our NSM:**
> [1–2 sentence rationale: how does this metric capture customer value delivered? Why is it a leading indicator of long-term retention and revenue?]

**Counter-metrics (protect against gaming):**
- [Counter-metric 1 — e.g., "Customer satisfaction score must stay above 4.0"]
- [Counter-metric 2 — e.g., "Support ticket volume must not increase proportionally with NSM"]

---

## Input Metrics (NSM Drivers)

Each input metric is a lever that drives the NSM. Each team owns one.

| Input Metric | Definition | Current | Target | Owner Team |
|--------------|-----------|---------|--------|------------|
| [Metric 1 — e.g., New shipper activation rate] | [% of signups who complete first shipment within 7 days] | [X%] | [Y%] | [Onboarding team] |
| [Metric 2 — e.g., Shipments per active shipper] | [Avg shipments per WAU per week] | [X] | [Y] | [Core product team] |
| [Metric 3 — e.g., D30 retention] | [% of shippers active in week 1 still active in week 4] | [X%] | [Y%] | [Engagement team] |
| [Metric 4 — e.g., Referrals per active user] | [Avg invites sent per MAU per month] | [X] | [Y] | [Growth team] |

---

## NSM Decomposition Tree

```
North Star: [NSM Name]
│
├── [Input Metric 1: New shipper activation]
│   ├── Sub-metric: Signup-to-onboarding completion rate
│   └── Sub-metric: Time to first shipment tracked
│
├── [Input Metric 2: Shipments per active shipper]
│   ├── Sub-metric: Feature adoption rate (bulk upload)
│   └── Sub-metric: % users with 3+ shipments/week
│
├── [Input Metric 3: D30 retention]
│   ├── Sub-metric: Day 7 retention
│   └── Sub-metric: Notification open rate
│
└── [Input Metric 4: Referrals]
    ├── Sub-metric: NPS score
    └── Sub-metric: Referral invite acceptance rate
```

---

## NSM Dashboard

| Metric | This Week | Last Week | 4-Week Trend | Target |
|--------|-----------|-----------|--------------|--------|
| **NSM: [Name]** | | | ↑ / ↓ / → | |
| Input Metric 1 | | | | |
| Input Metric 2 | | | | |
| Input Metric 3 | | | | |
| Input Metric 4 | | | | |
| Counter-metric 1 | | | | |

---

## Alerting Thresholds

| Metric | Green | Yellow (Monitor) | Red (Act Immediately) |
|--------|-------|------------------|-----------------------|
| NSM | > [Target] | [Target - 10%] to [Target] | < [Target - 10%] |
| Input Metric 1 | > [X%] | [X-5]% to [X%] | < [X-5]% |
| Input Metric 2 | > [X] | [X-0.5] to [X] | < [X-0.5] |

---

## NSM Review Cadence

| Frequency | Who | Agenda |
|-----------|-----|--------|
| Weekly | Product team | Review NSM + input metrics, identify anomalies |
| Monthly | Product + Engineering | Assess trend, adjust initiatives |
| Quarterly | Leadership | OKR check-in, NSM vs. KR targets |
