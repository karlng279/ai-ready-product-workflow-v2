# Example: Growth Loop Design — Shipment Visibility Platform

*This worked example shows the growth loops identified and activated for a logistics SaaS product.*

---

## Loop Inventory

### Loop 1: Collaborative Invite Loop (Viral)

**Type:** ☑ Viral

**Loop diagram:**
```
[Entry: Operations Manager signs up + tracks first shipment]
         ↓
[Action: Invites 2 colleagues — "Hey, stop updating the spreadsheet, use this"]
         ↓
[Output: Colleagues sign up; each one tracks shipments]
         ↓
[Re-entry: Each new user invites their own team members]
         ↑__________________|
```

**Entry point:** User who tracked ≥5 shipments in first week — high activation signal
**Core action:** Sends team invite from "Team Management" settings
**Output:** Invited colleagues register and track their first shipment
**Re-entry condition:** Each new colleague hits the same 5-shipment threshold and invites the next tier
**Loop metric:** Viral coefficient (K-factor) = invites sent × acceptance rate. Currently: K = 0.41 (below 1 — not yet viral)
**Current state:** ☑ Active (but weak — K < 1)

**Friction points:**
1. Invite flow buried in settings — most users don't find it
2. Invite email lands in spam for company email domains
3. Invited users still have to set up carrier integrations from scratch — high drop-off

**Fix plan:**
- In-app invite prompt after user tracks 5th shipment ("Your team is still updating a spreadsheet...")
- Pre-populated carrier config for invited users based on inviter's setup
- Target K-factor > 0.8 by Q3

---

### Loop 2: Referral + Word-of-Mouth Loop

**Type:** ☑ Viral (human-powered)

**Loop diagram:**
```
[Entry: Power user gets asked at industry event / LinkedIn "what do you use for tracking?"]
         ↓
[Action: Recommends ShipTrack + shares referral link]
         ↓
[Output: New company signs up; power user gets 1-month credit]
         ↓
[Re-entry: New company's power user becomes next advocate]
         ↑__________________|
```

**Entry point:** NPS promoter (score 9–10)
**Core action:** Shares referral link via LinkedIn, email, or in-person
**Output:** Referred company signs up for trial
**Re-entry condition:** Referred company activates + becomes NPS promoter
**Loop metric:** Referral-driven new company signups per month (currently: 3/month)
**Current state:** ☑ Active (latent — no formal referral program yet)

**Friction points:**
1. No formal referral program — users who want to refer have no easy mechanism
2. No referral tracking — we don't know when organic word-of-mouth converts

**Fix plan:**
- Launch referral program in Q2: 1-month credit for referrer + 30% off first month for referee
- Referral link in user account settings + post-NPS survey prompt

---

### Loop 3: Paid Acquisition Loop

**Type:** ☑ Paid

**Loop diagram:**
```
[Entry: LinkedIn ad targets Operations Managers at freight forwarders]
         ↓
[Action: Click → free trial signup → activation]
         ↓
[Output: Activated user converts to paid; revenue generated]
         ↓
[Re-entry: Revenue reinvested in ad spend → more users]
         ↑__________________|
```

**Entry point:** LinkedIn ad targeting (job title: Ops Manager / Logistics Manager, industry: freight/logistics)
**Core action:** Free trial signup + first shipment tracked
**Output:** Monthly recurring revenue from converted users
**Re-entry condition:** LTV:CAC ≥ 3:1 — profitable enough to reinvest
**Loop metric:** LTV:CAC ratio (currently: 2.1:1 — below 3:1 target; loop is not yet self-sustaining)
**Current state:** ☑ Active (not yet profitable enough to scale)

**Friction points:**
1. Trial-to-paid conversion: 9% (too low — need 15%+)
2. CAC from LinkedIn: $380 (too high given current ARPU of $140/month)
3. LTV limited by 38% D30 retention

**Fix plan:**
- Fix retention first (Loop 3 cannot scale on 38% D30 retention)
- Once D30 retention hits 55%, model predicts LTV:CAC crosses 3:1 threshold
- Scale paid at that point

---

## Primary Loop Selection

**Primary growth loop:** Loop 1 — Collaborative Invite Loop

**Why this is primary:** Freight forwarding is a team sport. Every customer has 3–10 ops team members who could use the platform. A loop that turns one user into 3–5 team users is more capital-efficient than paying to acquire each one through ads.

**Loops to activate next:** Loop 2 (Referral program, Q2) once NPS improves; Loop 3 (Paid, Q3) once retention hits 55%.

---

## PLG Flywheel Assessment

| Flywheel Stage | Current Friction | Fix |
|---------------|-----------------|-----|
| Awareness | Limited — word of mouth only | Loop 2 referral program (Q2) |
| Activation | 41% — users don't track first shipment quickly | Rewrite onboarding; reduce to < 1 day |
| Engagement | 38% D30 — users forget to return | "Today" dashboard + delay alerts |
| Expansion | 12% team invite rate — low | In-context invite prompt after 5th shipment |
| Advocacy | NPS 22 — too low to drive advocacy loop | Fix product experience first |

---

## Loop Health Metrics

| Loop | Metric | Current | Target | Status |
|------|--------|---------|--------|--------|
| Loop 1: Viral | K-factor | 0.41 | > 0.8 | 🟡 At risk |
| Loop 2: Referral | Referral signups/month | 3 | 15 | 🔴 Not launched |
| Loop 3: Paid | LTV:CAC | 2.1:1 | > 3:1 | 🔴 Not scalable yet |
