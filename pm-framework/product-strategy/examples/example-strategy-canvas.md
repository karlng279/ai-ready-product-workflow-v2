# Example: Product Strategy Canvas — Shipment Visibility MVP

*This is a worked example following the strategy-canvas template. It demonstrates how to complete each section using a realistic logistics SaaS scenario.*

---

## Vision

> Become the single source of truth for every shipment moving through global supply chains — so that shippers, forwarders, and carriers never have to wonder "where is it?"

## Mission

> Help small and mid-size freight teams track and manage their shipments without the chaos of emails, spreadsheets, and carrier portals.

---

## Target Customer

**Primary segment:** Senior Operations Managers at mid-size freight forwarding companies (100–500 employees) in Southeast Asia and Australia who currently track 50+ active shipments manually.

**Customer Job:** Track the real-time status of all active shipments in one place, without calling carriers or checking multiple portals, so they can answer customer questions instantly.

**Current best alternative:** A combination of 3–5 carrier web portals + a shared Excel file + WhatsApp messages to forwarders.

---

## Value Proposition

> "For Operations Managers at mid-size freight forwarders who need to track 50+ shipments without chasing carriers, ShipTrack is a shipment visibility platform that gives them a live, consolidated view of every shipment across all carriers. Unlike checking each carrier portal manually, ShipTrack aggregates real-time status in one place with no manual data entry."

**Top 3 customer gains this product creates:**
1. Answers customer status questions in under 30 seconds (vs. 10+ minutes today)
2. Zero manual tracking spreadsheet maintenance
3. Proactive alerts when a shipment is delayed — before the customer calls

**Top 3 pains this product relieves:**
1. Logging into 5 carrier portals to get a complete picture
2. Maintaining a shared spreadsheet that's always out of date
3. Being caught off-guard when a customer calls about a delayed shipment

---

## Strategic Position

**Where we play:** Mid-size freight forwarders, SEA + AU, tracking-only use case (not full TMS)

**How we win:** Best time-to-value for the tracking job. Onboarding in under 30 minutes. No ERP integration required.

**Competitive moat:** Network of carrier API integrations (harder to build than to maintain once live) + data on shipment delays by lane (improves over time as more data accumulates).

---

## OKR Hierarchy (Q2 2026)

**Objective:** Make ShipTrack the default tracking tool for our first 50 freight forwarding customers.

| Key Result | Baseline | Target | Owner |
|------------|----------|--------|-------|
| KR1: 30-day retention rate | 38% | 60% | Core product |
| KR2: Time to first shipment tracked after signup | 4.5 days avg | < 1 day avg | Onboarding |
| KR3: NPS score | 22 | 45 | All teams |

**Top Initiatives (bets we're making this quarter):**
1. Rewrite onboarding flow — reduces time-to-first-shipment from 4.5 days to < 1 (drives KR2, KR1)
2. Launch proactive delay alerts — first push notification product (drives KR1, KR3)
3. Add top-5 SEA carriers to integration network (drives KR2, KR3)

---

## Strategic Bets

| Bet | Assumption Behind It | Evidence | What Would Prove It Wrong |
|-----|---------------------|----------|--------------------------|
| Simplicity beats features for SME | SME ops managers don't need TMS; they need a fast answer to "where is it?" | 12/15 interviews explicitly rejected complexity | SME customers churn because they want ERP integration or customs filing |
| SEA carriers are the unlock | 80% of our target customers' shipments move on SEA carrier lanes | Customer data shows 78% of shipments on 8 SEA carriers | Win rate is higher for AU-origin shipments than SEA |
| PLG beats SLG for this segment | SME ops managers can self-evaluate without a Sales demo | 60% of signups never requested a demo | Close rate drops below 5% for self-serve trial |

**Strategic non-bets (what we are explicitly NOT doing):**
- Not building customs filing / compliance features in 2026 — this is a separate job, different buyer, different competitive set
- Not targeting enterprise (>2,000 employees) — procurement complexity and SLA requirements exceed current team capacity

---

## Competitive Position Summary

| Competitor | Their Strength | Our Advantage | Our Weakness |
|-----------|---------------|--------------|-------------|
| Project44 | Enterprise-grade, deep integrations | Faster setup, lower price, SME-focused | Fewer carriers (we have 40, they have 400+) |
| Flexport | Full logistics management, brand | Tracking-only = simpler + cheaper | No freight booking or customs |
| Spreadsheet + portals | Free, familiar | Real-time data, no manual entry | Users must change habits |

---

## Success Metrics

| Metric | Type | Baseline | 12-Month Target |
|--------|------|----------|-----------------|
| Weekly Active Shippers (NSM) | Outcome | 87 | 500 |
| D30 retention rate | Leading | 38% | 65% |
| Time to first shipment tracked | Leading | 4.5 days | < 1 day |
| NPS | Lagging | 22 | 50 |
