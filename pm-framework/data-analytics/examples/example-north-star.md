# Example: North Star Metric — Shipment Visibility Platform

*This worked example shows a completed NSM framework for a logistics SaaS product.*

---

## North Star Metric Definition

| Attribute | Value |
|-----------|-------|
| **NSM Name** | Weekly Active Shippers (WAS) |
| **NSM Definition** | Count of distinct registered users who tracked at least 1 shipment status update in the last 7 days |
| **Current Value** | 87 WAS |
| **Target (12 months)** | 500 WAS |
| **Measurement frequency** | Weekly (every Monday, covering Mon–Sun prior week) |
| **Data source** | Product analytics (Mixpanel: `shipment_status_viewed` event, deduplicated by user_id) |

**Why this is our NSM:**
> "Weekly Active Shippers" captures whether customers are getting real value from the product — not just signing up and abandoning it. A shipper only tracks a shipment if they have active freight AND trust the platform enough to return to it. This metric leads revenue (paid plans are gated by active usage) and predicts retention better than any single-session metric.

**Counter-metrics:**
- Average shipments per WAS must not decrease (signals users tracking fewer shipments per session — quality decline)
- Monthly support ticket rate per WAS must stay below 0.3 (signals we're not growing through a degraded experience)

---

## Input Metrics

| Input Metric | Definition | Current | Target | Owner Team |
|--------------|-----------|---------|--------|------------|
| New shipper activation rate | % of new signups who track their first shipment within 7 days of signup | 41% | 70% | Onboarding |
| Shipments tracked per WAS | Average shipments tracked per weekly active user per week | 3.2 | 6.0 | Core product |
| D30 retention | % of users active in week 1 still active in week 4 | 38% | 60% | Engagement |
| Referral rate | % of WAS who invited ≥1 colleague in the last 30 days | 6% | 15% | Growth |

---

## NSM Decomposition Tree

```
North Star: Weekly Active Shippers (WAS)
│
├── New shipper activation rate [41% → 70%]
│   ├── Sub: Signup-to-first-shipment time (currently 4.5 days avg → target: < 1 day)
│   └── Sub: % completing onboarding checklist (currently 38% → target: 70%)
│
├── Shipments per WAS [3.2 → 6.0]
│   ├── Sub: % users with bulk CSV upload enabled (currently 12% → target: 35%)
│   └── Sub: % users tracking 5+ shipments/week (currently 21% → target: 45%)
│
├── D30 retention [38% → 60%]
│   ├── Sub: Week-2 login rate (currently 44% → target: 65%)
│   └── Sub: Proactive alert engagement rate (currently N/A → target: 30% click-through)
│
└── Referral rate [6% → 15%]
    ├── Sub: NPS ≥ 9 ("promoters") rate (currently 18% → target: 35%)
    └── Sub: Referral invite acceptance rate (currently 22% → target: 35%)
```

---

## NSM Dashboard (Sample Week)

| Metric | This Week | Last Week | 4-Week Trend | Target |
|--------|-----------|-----------|--------------|--------|
| **WAS (NSM)** | **94** | 87 | ↑ +8% | 500 by EOY |
| New activation rate | 44% | 41% | ↑ | 70% |
| Shipments per WAS | 3.4 | 3.2 | → | 6.0 |
| D30 retention | 39% | 38% | ↑ | 60% |
| Referral rate | 7% | 6% | ↑ | 15% |
| Counter: Tickets/WAS | 0.18 | 0.21 | ↓ Good | < 0.30 |

---

## Alerting Thresholds

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| WAS (NSM) | > 90 | 75–90 | < 75 |
| Activation rate | > 55% | 40–55% | < 40% |
| D30 retention | > 50% | 38–50% | < 38% |
| Support tickets/WAS | < 0.20 | 0.20–0.30 | > 0.30 |

---

## NSM Review Cadence

| Frequency | Who | Agenda |
|-----------|-----|--------|
| Weekly (Monday) | Core product team | Review WAS + input metrics; identify anomalies; set weekly focus |
| Monthly | Product + Eng + Design | Assess trend vs. OKR targets; adjust initiatives |
| Quarterly | Full leadership | OKR check-in; NSM projection; resource allocation |
