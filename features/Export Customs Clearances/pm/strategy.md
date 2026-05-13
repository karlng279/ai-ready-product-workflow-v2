---
artifact: STRATEGY
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-product-strategy
upstream: user-idea
downstream: discovery.md
---

# Export Customs Clearances Product Strategy

**Product:** Export Customs Clearances  
**Date:** 2026-05-13  
**Owner:** Product Team  
**Version:** 0.1

---

## Vision

Every exporter can move booked cargo across borders with clearance confidence before vessel departure.

## Mission

We help exporters complete export customs clearance faster by coordinating carrier-side support, documentation guidance, and process visibility at the moment they create a booking.

---

## Target Customer

**Primary segment:** Export shippers and freight forwarders who book ocean shipments directly through the carrier's digital booking flow and need reliable export customs support before cargo cutoff.

**Customer Job:** When creating a booking, customers want confidence that export customs clearance will be completed correctly and on time so their cargo is not delayed, rolled, or exposed to avoidable penalties.

**Current best alternative:** Customers coordinate export clearance manually through internal operations teams, customs brokers, freight forwarders, email threads, phone calls, and offline document checks.

---

## Value Proposition

For export shippers and freight forwarders who need clearance certainty during booking, Export Customs Clearances is a value-added carrier service that accelerates export clearance preparation and coordination. Unlike manual broker coordination after booking, Export Customs Clearances is offered at booking time and connects carrier-side support to the shipment before documentation and cutoff risks become urgent.

**Top 3 customer gains this product creates:**
1. Faster clearance preparation by starting support at booking creation instead of after operational issues appear.
2. Higher confidence that documentation, shipment details, and cutoff timing are aligned before cargo movement.
3. A simpler service-buying experience by adding export clearance support inside the booking workflow.

**Top 3 pains this product relieves:**
1. Uncertainty about export clearance status and required next steps.
2. Rework caused by missing, late, or inconsistent documentation.
3. Operational escalation close to cargo cutoff or vessel departure.

---

## Strategic Position

**Where we play:** Carrier digital booking flows for export shipments where customers can purchase value-added operational support at the time of booking.

**How we win:** Niche focus through workflow timing and carrier-side operational context. We win by embedding export clearance support into the booking moment, where shipment intent, route, deadlines, and customer urgency are already known.

**Competitive moat:** Distribution through the carrier booking channel, shipment data already captured during booking, operational knowledge of carrier cutoffs and documentation dependencies, and increasing switching costs as customers rely on a single booking-to-clearance workflow.

---

## OKR Hierarchy (Current Quarter)

**Objective:** Prove that booking-time export clearance support creates measurable customer and revenue value.

| Key Result | Baseline | Target | Owner |
|------------|----------|--------|-------|
| KR1: Booking attach rate for Export Customs Clearances | 0% | 8% of eligible export bookings by 2026-08-31 | Product / Commercial |
| KR2: Clearance support requests started within 24 hours of booking | 0% | 85% of purchased services by 2026-08-31 | Operations |
| KR3: Customer-reported confidence in export clearance process | TBD | 4.2/5 average post-service rating by 2026-08-31 | Product / CX |

**Top Initiatives (bets we're making this quarter):**
1. Add a booking-flow VAS selection point for eligible export shipments, driving KR1.
2. Define the carrier-side export clearance support workflow and handoff SLA, driving KR2.
3. Instrument service purchase, support start time, clearance progress, and customer feedback events, driving KR1, KR2, and KR3.

---

## Strategic Bets

| Bet | Assumption Behind It | Evidence | What Would Prove It Wrong |
|-----|----------------------|----------|---------------------------|
| Booking-time offer | Customers are more likely to buy clearance support when they are already creating a shipment booking. | Booking is the moment when export route, schedule, cargo readiness, and service intent are active. | Attach rate remains below 3% after eligible customers see the offer with clear pricing and value messaging. |
| Carrier-side coordination | The carrier can reduce customer friction by connecting clearance support to booking, cutoff, and shipment data. | Carriers already manage operational milestones that influence export shipment readiness. | Purchased services still require the same customer effort and escalation rate as manual coordination. |
| Operational speed as value | Customers will pay for faster, more predictable clearance preparation rather than only for lowest-cost brokerage. | Export delays can create rollovers, storage costs, penalties, and customer service escalation. | Customers cite price as the dominant reason for non-purchase and do not convert even for high-risk shipments. |

**Strategic non-bets (what we are explicitly NOT doing):**
- We are not building a full customs brokerage marketplace in the first version because the initial advantage is carrier workflow timing, not marketplace breadth.
- We are not automating customs filing end-to-end in the first version because operational support quality and compliance boundaries must be validated first.
- We are not offering this service for every trade lane immediately because eligibility, regulatory process, and support capacity should be proven in focused lanes first.

---

## Competitive Position Summary

| Competitor | Type | Their Strength | Our Advantage | Our Weakness |
|------------|------|----------------|---------------|--------------|
| Freight forwarders | Direct / indirect | Own broader shipment management and customs coordination relationship. | We can offer support at the exact booking moment with carrier shipment data and cutoff context. | They may have deeper local customs expertise and existing customer trust. |
| Customs brokers | Direct | Specialized customs knowledge, local compliance experience, and filing processes. | We can simplify discovery and initiation by embedding support inside booking. | We may still depend on broker execution or country-specific expertise. |
| Customer internal operations | Substitute | Familiar process, existing controls, and no new vendor onboarding. | We reduce manual coordination and provide shipment-specific carrier support. | Internal teams may resist paying for support they believe they can manage themselves. |
| Email and phone escalation | Substitute | Flexible, low-friction, and already used by customers. | We create a structured, measurable service with clearer next steps and accountability. | Ad hoc escalation can feel faster for urgent edge cases. |

---

## Competitive Analysis

**Market category:** Carrier value-added export clearance support for ocean shipment bookings.

**Competitive intensity:** Medium

**Our strategic position:** We are not trying to replace the entire customs brokerage market at launch. We are creating a booking-native service that helps customers start export clearance support earlier, with better carrier context and fewer handoff gaps.

### Competitive Matrix

Rate each dimension 1-5. 5 = clear leader, 1 = significant weakness.

| Dimension | Us | Freight Forwarders | Customs Brokers | Manual Internal Process |
|-----------|----|--------------------|-----------------|-------------------------|
| Ease of purchase | 5 | 3 | 2 | 4 |
| Time to value | 4 | 3 | 3 | 2 |
| Carrier shipment context | 5 | 3 | 2 | 2 |
| Compliance depth | 3 | 4 | 5 | 3 |
| Price-to-value clarity | 4 | 3 | 3 | 4 |
| Support accountability | 4 | 4 | 4 | 2 |
| Digital tracking | 3 | 3 | 2 | 1 |
| Scale across lanes | 3 | 4 | 3 | 2 |

### Porter's Five Forces Assessment

| Force | Intensity | Notes |
|-------|-----------|-------|
| Threat of new entrants | Medium | Digital forwarders and broker platforms can package similar services, but they lack native carrier booking distribution. |
| Supplier bargaining power | Medium | Local customs expertise, broker partnerships, and compliance capacity may be required by country or trade lane. |
| Buyer bargaining power | High | Customers can choose existing forwarders, brokers, or internal teams if pricing or support quality is unclear. |
| Threat of substitutes | High | Many customers already use email, phone, spreadsheets, and internal checklists to coordinate clearance. |
| Competitive rivalry | Medium | The space is crowded operationally, but booking-native carrier-side VAS is a narrower position. |

**Overall attractiveness:** Medium

**Strategic implications:**
- Invest first in eligibility rules, service clarity, and operational SLA because trust is the purchase driver.
- Use booking data to personalize when and how the service is offered instead of showing a generic upsell.
- Validate lane-by-lane support quality before expanding service availability.

---

## Success Metrics

| Metric | Type | Baseline | 12-Month Target |
|--------|------|----------|-----------------|
| Eligible booking attach rate | North Star / Outcome | 0% | 15% |
| Purchased services started within SLA | Leading | 0% | 90% |
| Clearance-related booking escalations for purchased services | Guardrail | TBD | 25% lower than comparable non-purchased bookings |
| Customer satisfaction for export clearance support | Outcome | TBD | 4.4/5 |
| VAS revenue per eligible export booking | Business | 0 | TBD after pricing validation |

---

## Framework Grounding

This strategy applies:
- Product Strategy Canvas for vision, target customer, value proposition, strategic position, and metrics.
- Jobs-to-be-Done for the core customer job: completing export clearance correctly and on time after booking.
- OKR Hierarchy for the current-quarter execution focus.
- Porter's Five Forces for competitive and substitute pressure.
- Strategic Bets and Non-Bets to make trade-offs explicit.

---

## Quality Checklist

- [x] Vision is one sentence, present tense, and aspirational.
- [x] Positioning formula includes an explicit "unlike" clause.
- [x] OKRs measure outcomes instead of outputs.
- [x] Competitive analysis includes substitutes.
- [x] Strategic bets are paired with explicit non-bets.
- [x] Every major section is grounded in a named framework.
