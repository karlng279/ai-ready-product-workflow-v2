# Example: Opportunity Solution Tree — Shipment Visibility Platform

*This worked example shows a completed OST for a logistics SaaS product. It demonstrates the full structure from desired outcome down through opportunities, solutions, and experiments.*

---

## Desired Outcome

> Increase 30-day retention rate from 38% to 60% by end of Q2 2026.

**Metric:** D30 retention (% of users active in week 1 still active in week 4)
**Baseline:** 38%
**Target:** 60%
**Deadline:** 2026-06-30

---

## Opportunity Space

### Opportunity 1: "I forget to check the platform when nothing urgent is happening"

**Evidence:** 8/12 churned-user interviews; quote: "I only remember to log in when a customer calls me about a shipment — and by then I'm already stressed."

**Customer impact:** High — directly drives week 2–4 drop-off
**Business impact:** High — retention is our #1 NSM input metric

**Sub-opportunities:**
- Sub-opportunity 1a: No trigger to return to the platform between "crisis" moments
- Sub-opportunity 1b: No summary view that shows "what needs my attention today" — **CHOSEN**

---

### Opportunity 2: "Setting up a new shipment takes too long"

**Evidence:** 5/12 interviews; average observed setup time: 8 minutes per shipment
**Customer impact:** Medium — frustrating but not causing churn alone
**Business impact:** Medium — affects activation rate more than retention

---

### Opportunity 3: "I don't trust the data — it's sometimes wrong"

**Evidence:** 3/12 interviews; carrier API reliability is 94.2% (known issue)
**Customer impact:** High when it happens — but infrequent
**Business impact:** Medium — trust issue compounds churn risk for Op 1

---

## Opportunity Prioritization

| Opportunity | Customer Impact | Business Impact | Evidence Strength | Priority |
|-------------|----------------|----------------|-------------------|----------|
| Opportunity 1b: No "what needs attention" view | High | High | Strong (8/12) | 🔴 High |
| Opportunity 2: Setup too slow | Medium | Medium | Medium (5/12) | 🟡 Medium |
| Opportunity 3: Data trust issues | High | Medium | Weak (3/12) | 🟡 Medium |

**Chosen opportunity this quarter:** Opportunity 1b — "No daily summary of what needs attention." This is the most direct driver of the retention gap between week 1 and week 4.

---

## Solution Space

*(For Opportunity 1b: No daily summary of what needs attention)*

### Solution A: Daily email digest

**Description:** Automated daily email at 8 AM with: # delayed shipments, # arriving today, # needing action.

**How it addresses the opportunity:** External trigger pulls users back to the platform when there's something actionable.

**Riskiest assumption:** Users will open a daily email and not mark it as spam.

**Estimated effort:** S (2–3 engineer-days)

---

### Solution B: In-app "Today" dashboard — CHOSEN

**Description:** A new default home screen showing: "Today's summary — 3 delayed, 2 arriving, 1 action required" with direct links to each item.

**How it addresses the opportunity:** Users who do log in see immediate value without searching — reinforces the habit.

**Riskiest assumption:** Users log in at least once per week organically (we need them to see the dashboard).

**Estimated effort:** M (1 sprint)

---

### Solution C: Push notifications (mobile)

**Description:** Native push notifications for delay alerts and arrival confirmations.

**How it addresses the opportunity:** Proactive trigger doesn't require user to remember to check.

**Riskiest assumption:** Users will grant push notification permissions and not turn them off.

**Estimated effort:** L (requires mobile app)

---

## Solution Selection

**Chosen solution:** Solution B — "Today" dashboard

**Rationale:** Highest impact for users who are already logging in (converts casual check-ins to habit-forming sessions). Lower effort than Solution C (no mobile app required). Solution A (email) tested via manual email digest with 10 users — open rate was 34%, not actionable enough. Build Solution A as a companion after B ships.

---

## Experiments

### Experiment 1 (pre-build validation)

**Assumption being tested:** Users who log in more than once in week 2 are significantly more likely to be retained at D30.

**Hypothesis:** "We believe users who return twice in week 2 have >80% D30 retention. If we look at behavioral data from the last 6 months, we expect to see this correlation. We'll know in 1 week if the data confirms this threshold."

**Test type:** SQL query on existing behavioral data (no product change needed)

**Test description:** Pull D30 retention rate by week-2 login frequency cohort. Confirm whether 2+ logins in week 2 is a strong predictor of retention.

**Success criteria:** Users with 2+ week-2 logins show ≥ 2× retention rate vs. 1 login. (If true, "Today" dashboard is designed to drive this behavior.)

**Result:** ✅ Confirmed — 2+ week-2 logins = 71% D30 retention vs. 29% for 1 login users. Dashboard will target driving a second login in week 2.

---

## OST Summary Diagram

```
Desired Outcome: D30 retention 38% → 60%
│
├── Opportunity 1: "I forget to check between crises"
│   ├── Sub-opportunity 1a: No re-engagement trigger
│   └── Sub-opportunity 1b: No "what needs attention" view ← CHOSEN
│       ├── Solution A: Daily email digest
│       ├── Solution B: "Today" dashboard ← CHOSEN
│       │   ├── Experiment 1: Confirm week-2 login correlation ← ✅ CONFIRMED
│       │   └── Experiment 2: Prototype test with 5 users ← RUNNING
│       └── Solution C: Push notifications (future)
│
├── Opportunity 2: Setup takes too long
│
└── Opportunity 3: Data trust issues
```
