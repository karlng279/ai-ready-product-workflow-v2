# Data & Analytics — Rules

## What Data Analytics Is for Product

Data analytics answers: Is the product working? Where are users dropping off? What should we optimize? It converts user behavior into decisions — but only if the metrics are defined before you look at the data, not after.

Good product analytics starts with a clear success definition (North Star), not with a dashboard. Metrics cascade from that North Star to diagnostic metrics that explain why the number is moving.

---

## Required Components

### 1. North Star Metric (NSM)
One metric that best captures the value your product delivers to customers. Rules:
- Measures **customer value delivered**, not revenue or engagement.
- Leading indicator, not lagging. (Revenue is a lagging outcome, not a NSM.)
- Actionable: the product team can influence it directly.
- Example: Airbnb = Nights Booked. Spotify = Time Listening. Slack = Messages Sent.

**NSM Framework:**
- North Star: 1 metric
- Input metrics: 4–6 metrics that drive the NSM (each team owns one)
- Counter-metrics: 1–2 metrics to ensure you're not gaming the NSM

### 2. HEART Framework (Google)
Use for: holistic measurement of UX quality.
| Dimension | Definition | Example metric |
|-----------|------------|----------------|
| Happiness | Subjective satisfaction | CSAT, NPS |
| Engagement | Depth of usage | DAU/MAU, sessions per user |
| Adoption | New feature/product uptake | % users who used feature in last 30 days |
| Retention | Continued usage over time | 30-day retention rate |
| Task Success | Completion of intended tasks | Task completion rate, error rate |

### 3. Funnel Analysis
Map the conversion funnel stage by stage:
- **AARRR (Pirate Metrics):** Acquisition → Activation → Retention → Referral → Revenue
- **RARRA (retention-first):** Retention → Activation → Referral → Revenue → Acquisition
- For each stage: define the metric, measure current rate, set target, identify drop-off causes.
- Rule: Fix retention before scaling acquisition. Growth on a leaky funnel wastes budget.

### 4. A/B Test Design
Every experiment must be designed before it runs:
- **Hypothesis:** "We believe [change] will [improve metric] for [user segment] because [reason]."
- **Primary metric:** One metric the test must move to succeed.
- **Guard-rail metrics:** Metrics that must NOT regress.
- **Sample size:** Calculate minimum detectable effect (MDE) and required sample size before starting.
- **Duration:** Run for at least 2 full business cycles to account for day-of-week effects.
- **Decision rule:** Define ahead of time: what outcome = ship, what outcome = iterate, what outcome = kill.

### 5. Cohort Analysis
Used for retention and lifecycle analysis:
- Cohort = group of users who joined / activated in the same time period.
- Track their behavior week-over-week or month-over-month.
- Goal: identify whether retention is improving across cohorts (product is getting better) or flat/declining.
- Healthy retention curve: steep initial drop, then flattens. The flatten point is your retained audience.

---

## Frameworks to Apply

### North Star Metric + Input Metrics
Use for: aligning the team on what success looks like.
Tree structure: NSM ← [Input Metric A, Input Metric B, Input Metric C, ...]

### HEART (Google)
Use for: product health dashboard covering 5 dimensions of user experience.

### AARRR / RARRA
Use for: funnel-stage diagnosis. AARRR works when acquisition is the bottleneck. RARRA when retention is.

### A/B Testing
Use for: validating product changes with statistical rigor. Not appropriate for low-traffic surfaces (use qualitative methods instead).

### Cohort Analysis
Use for: understanding retention dynamics and whether product improvements translate to better long-term retention.

---

## SQL Patterns for Product Analytics

### DAU / MAU ratio (stickiness)
```sql
SELECT
  COUNT(DISTINCT CASE WHEN event_date = CURRENT_DATE THEN user_id END) AS dau,
  COUNT(DISTINCT CASE WHEN event_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY) THEN user_id END) AS mau,
  ROUND(dau / mau * 100, 1) AS stickiness_pct
FROM events
WHERE event_name = 'session_start';
```

### Retention by cohort
```sql
SELECT
  DATE_TRUNC(first_seen, WEEK) AS cohort_week,
  DATE_DIFF(event_date, first_seen, WEEK) AS weeks_since_join,
  COUNT(DISTINCT e.user_id) AS retained_users
FROM events e
JOIN (SELECT user_id, MIN(event_date) AS first_seen FROM events GROUP BY user_id) AS cohorts
  ON e.user_id = cohorts.user_id
GROUP BY 1, 2
ORDER BY 1, 2;
```

### Funnel conversion
```sql
SELECT
  COUNT(DISTINCT CASE WHEN event_name = 'signup' THEN user_id END) AS step1_signup,
  COUNT(DISTINCT CASE WHEN event_name = 'onboarding_complete' THEN user_id END) AS step2_onboarding,
  COUNT(DISTINCT CASE WHEN event_name = 'first_value_action' THEN user_id END) AS step3_activation,
  ROUND(step2_onboarding / step1_signup * 100, 1) AS step1_to_2_pct,
  ROUND(step3_activation / step2_onboarding * 100, 1) AS step2_to_3_pct
FROM events
WHERE event_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY);
```

---

## Quality Checklist

Before finalizing an analytics artifact:
- [ ] North Star Metric defined; measures customer value, not revenue
- [ ] 4–6 input metrics identified; each owned by one team
- [ ] Counter-metrics defined to prevent gaming
- [ ] Funnel stages defined with current conversion rates
- [ ] A/B tests have a pre-defined hypothesis, sample size, and decision rule
- [ ] Cohort analysis shows trend over time, not just point-in-time

---

## Anti-Patterns to Avoid

- **Revenue as North Star:** Revenue is an outcome, not a value signal. Correlates with NSM, doesn't replace it.
- **Engagement for engagement's sake:** DAU/MAU without context can be gamed. Measure value-delivering actions.
- **Running A/B tests without sufficient sample size:** Underpowered tests produce false positives. Always calculate power before starting.
- **Ignoring cohort trends:** Average retention hides whether you're improving. Cohort-level view shows the real trajectory.
- **Defining success metrics after seeing results:** HARKing (Hypothesizing After Results are Known) corrupts data-driven culture.
