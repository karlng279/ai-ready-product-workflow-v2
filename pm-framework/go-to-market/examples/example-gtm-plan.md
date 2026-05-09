# Example: GTM Plan — ShipTrack Proactive Delay Alerts

*This worked example shows a GTM plan for a major new feature launch on an existing product.*

---

## Launch Overview

| Attribute | Value |
|-----------|-------|
| **What we're launching** | Proactive delay alerts — push notifications + email when tracked shipments are delayed beyond threshold |
| **Target customer** | Existing active users (WAS) + new trial signups — Operations Managers at freight forwarders |
| **Primary launch goal** | 60% of Weekly Active Shippers have alerts enabled within 30 days of GA |
| **GTM motion** | PLG — existing users self-discover in-product; no Sales involvement |
| **Launch type** | Major feature (highest-impact product addition since MVP) |

---

## Phase 1: Alpha (Closed Beta)

**Goal:** Validate that alerts fire correctly, reach the right users, and trigger the intended behavior (users return to platform when alerted).

**Entry criteria:**
- [x] Alert logic works for top 8 SEA carriers without false positives
- [x] Email + in-app notification both functional
- [x] No P0 bugs in alpha environment

**Participants:** 12 power users (users with ≥10 shipments tracked in last 30 days) — recruited via direct Slack message from PM.

**Duration:** 2 weeks (2026-04-01 to 2026-04-14)

**Feedback collection:**
- Weekly 30-min check-in call with 3 participants each
- In-app thumbs up/down on each alert received
- Direct Slack channel with all alpha users

**Success metrics:**
| Metric | Target |
|--------|--------|
| Alert accuracy rate (correct delays alerted / total alerts) | > 95% |
| Alert click-through rate (user clicks alert → opens platform) | > 40% |
| False positive rate (alerts for non-delayed shipments) | < 2% |
| Alpha user NPS delta | + ≥10 points vs. their pre-alert NPS |

**Exit criteria:**
- [x] Alert accuracy ≥ 95%
- [x] Click-through rate ≥ 40%
- [x] No P0 or P1 bugs open
- [x] 3+ user quotes captured for marketing use

---

## Phase 2: Beta (Open Beta)

**Goal:** Validate activation and engagement at scale with 500+ users; test alert fatigue vs. value.

**Entry criteria:**
- Alpha exit criteria met ✅
- Email templates reviewed by CS team ✅
- Help center article published ✅

**Participants:** All Weekly Active Shippers (currently 94) + new trial signups during beta period. Total target: ~300 users.

**Duration:** 3 weeks (2026-04-15 to 2026-05-05)

**Marketing activities:**
- In-app banner: "New: Get alerts when your shipments are delayed"
- Email to all WAS: "Never be caught off-guard again"
- No external marketing — existing users only

**Success metrics:**
| Metric | Target |
|--------|--------|
| Alert opt-in rate (% WAS who enable alerts) | > 50% |
| Alert click-through rate | > 35% |
| D14 retention of alert-enabled users vs. non-enabled | Alert-enabled users ≥ 15pp higher D14 retention |
| Unsubscribe rate | < 5% |

**Exit criteria:**
- Opt-in rate ≥ 50% ✅
- No increase in support ticket rate ✅
- D14 retention signal confirmed directionally ✅
- All marketing assets ready for GA ✅

---

## Phase 3: General Availability (GA)

**Goal:** Drive 60% of all WAS to enable alerts within 30 days. Use feature as acquisition hook.

**Launch date:** 2026-05-12

### Marketing Checklist

**Product:**
- [x] In-app announcement modal for all users on next login
- [x] Empty state for "Alerts" tab updated
- [x] Onboarding checklist includes "Enable delay alerts" as step 3

**Content:**
- [x] Blog post: "Why we built proactive delay alerts — and what we learned from freight forwarders"
- [x] Help center: "How to set up delay alerts"
- [x] 60-second product demo video

**Email:**
- [x] Launch email to all users (WAS + dormant users): "Your shipments now alert you when they're delayed"
- [x] Onboarding email sequence: new step added at Day 2 about alerts

**Social:**
- [x] LinkedIn post with 3 customer quotes from alpha
- [ ] Product Hunt submission — scheduled for 2026-05-14

**Support:**
- [x] CS team briefed on alert logic + common questions
- [x] Canned responses for "why did I get alerted for X" questions

---

## Launch Success Metrics

| Metric | D7 Target | D30 Target |
|--------|-----------|-----------|
| % WAS with alerts enabled | 35% | 60% |
| WAS (NSM) impact | +5 WAS | +15 WAS |
| D30 retention (alert users) | — | ≥ 55% (vs. 38% baseline) |
| NPS delta (alert users vs. non) | — | +8 points |

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Alert fatigue — users get too many alerts and unsubscribe | Medium | High | Default threshold: 6h delay (not 1h); user can customize |
| Carrier API downtime causes missed alerts | Low | High | Alert system retries 3x with 30-min backoff; fallback to "check manually" email |
| Feature creates expectations we can't meet (wrong carrier) | Low | Medium | Clear carrier coverage list in onboarding; alert only fires for confirmed integrations |

---

## Post-Launch Review (D+30)

**What went well:**
- Opt-in rate hit 67% by D30 (target was 60%) — exceeded expectations
- D30 retention for alert-enabled users: 54% vs. 37% for non-enabled — statistically significant
- 4 customers mentioned alerts in unprompted NPS feedback as the #1 reason for positive score change

**What we'd do differently:**
- Beta was too short (3 weeks) — some alert fatigue issues only emerged after week 4 with heavy users. Would extend beta to 4 weeks next time.
- Product Hunt launch was delayed to May 14 — should have coordinated with main launch date

**Decision:** ☑ Accelerate investment — alerts are the #1 retention driver; expand to SMS notifications in Q3.
