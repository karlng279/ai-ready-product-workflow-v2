---
artifact: GROWTH-LOOP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-marketing-growth
upstream: analytics.md
downstream: gtm.md
---

# Export Customs Clearances Marketing Growth

**Product / Feature:** Export Customs Clearances  
**Date:** 2026-05-13  
**Owner:** Product Team  
**Growth Stage:** Pre-launch / pilot design

---

## Growth Context

Export Customs Clearances is a booking-native value-added service. The growth strategy should not start with broad acquisition spend. It should first prove that customers see the offer during relevant export bookings, understand the value, receive timely support, and select the service again for future eligible bookings.

Primary growth constraint today: activation and repeat value are unproven because the service is pre-launch and instrumentation is not live.

---

## Value Proposition Canvas

**Persona:** Linh Tran, Export Operations Coordinator  
**Source:** `market-research.md`, hypothesis-based until customer interviews are completed

### Customer Profile

#### Customer Jobs

| ID | Job | Type | Importance |
|----|-----|------|------------|
| J1 | Make sure clearance documents and responsibilities are clear before cargo cutoff. | Functional | High |
| J2 | Coordinate with internal shipping, finance, warehouse, broker, and carrier teams without losing track of who owes what. | Functional | High |
| J3 | Feel calm and in control before deadlines become urgent. | Emotional | High |
| J4 | Be seen internally as the person who prevents shipment delays. | Social | Medium |

**Most important job:** J1, because unclear clearance readiness before cutoff is the trigger for operational risk, escalation, and willingness to pay.

#### Customer Pains

| ID | Pain | Severity |
|----|------|----------|
| P1 | "I only realize something is missing when the deadline is already close." | Extreme |
| P2 | Rechecking shipment and document details across email, portal, and broker messages takes too much time. | Extreme |
| P3 | It is unclear whether the carrier, broker, or internal team owns the next action. | Extreme |
| P4 | Paying for an extra service is hard to justify if the scope is vague. | Moderate |

**Riskiest pain if unresolved:** P4, because unclear scope can stop purchase even when operational pain is real.

#### Customer Gains

| ID | Gain | Importance |
|----|------|------------|
| G1 | Know exactly what export clearance support will cover before selecting it. | Essential |
| G2 | Receive confirmation that support has started within one business day. | Essential |
| G3 | Reduce last-minute document rework and cargo cutoff anxiety. | Essential |
| G4 | Have a simple status view after booking. | Nice-to-have |

### Value Map

#### Products & Services

| Offering | Type |
|----------|------|
| Booking-time Export Customs Clearances VAS offer | Product / Service |
| Carrier-side support case triggered from booking | Service |
| Support scope explanation with included / not included details | Product content |
| First-action SLA and support owner confirmation | Service / Operational workflow |
| Optional clearance readiness checklist | Product feature |

#### Pain Relievers

| Pain ID | Pain Reliever | Relevance |
|---------|---------------|-----------|
| P1 | Offer clearance support during booking, before the shipment reaches cutoff pressure. | Strong |
| P2 | Create a support case using booking context so customers do not repeat shipment details across channels. | Strong |
| P3 | Show support owner, next action, and SLA after selection. | Strong |
| P4 | Explain service scope, responsibility boundaries, and next steps inside the offer. | Strong |

#### Gain Creators

| Gain ID | Gain Creator | Relevance |
|---------|--------------|-----------|
| G1 | Include concise "what we help with / what remains customer or broker responsibility" copy. | Strong |
| G2 | Commit to first support action within 24 hours during the pilot if operations capacity is available. | Strong |
| G3 | Use booking data and cutoff timing to start support earlier. | Strong |
| G4 | Add post-selection status and pending action summary in later iterations. | Partial |

### Fit Assessment

**Pain relief coverage:** 4/4 pains addressed, strong fit if operations can deliver the SLA and scope is legally/commercially clear.

**Gain creation coverage:** 3/4 essential or important gains addressed strongly; G4 is partially addressed and should become a roadmap candidate after pilot validation.

**Unaddressed pains / gaps:**
- Customers may still need formal customs broker execution, which this VAS may not cover in all lanes.
- Customers may need internal approval for paid VAS selection.
- Forwarders may worry the carrier is competing with their role unless partner positioning is explicit.

**Key insight:** Growth depends less on attracting new users and more on earning trust at a high-stakes booking moment. The product must make scope and first action visible immediately.

---

## Positioning Statement

### Completed Positioning Statement

> **For** export shippers and freight forwarders creating eligible ocean export bookings  
>
> **who** need clearance preparation to start before documentation or cargo cutoff risk becomes urgent,  
>
> **Export Customs Clearances** is a **booking-time value-added carrier support service**  
>
> **that** helps customers start export clearance support earlier with clear next steps and carrier-side shipment context.  
>
> **Unlike** manual broker coordination after booking through email and phone,  
>
> **our product** connects the service to the booking moment and triggers a carrier-side support workflow from the shipment data already provided.

### Positioning Components

| Component | Value |
|-----------|-------|
| **Target customer** | Export shippers and freight forwarders with eligible export bookings and visible clearance preparation risk |
| **Behavioral signal** | Booking close to cutoff, documentation-heavy lane, prior rework/escalation, or VAS interest |
| **Key need** | Start export clearance support early enough to reduce uncertainty before shipment deadlines |
| **Product category** | Booking-time VAS / carrier-side export clearance support |
| **Primary alternative** | Manual broker, forwarder, internal team, email, and phone coordination after booking |
| **Primary differentiator** | Native booking timing plus carrier shipment context |

### Alternative Positioning Options

| Option | Statement Summary | Score | Rationale |
|--------|-------------------|-------|-----------|
| A: Risk reduction | Helps customers reduce export clearance delay risk from the booking moment. | 9/10 | Best aligned with urgency, analytics test, and strongest customer pain. |
| B: Convenience | Makes export clearance coordination easier after booking. | 6/10 | Clear but weaker; may sound like administrative help rather than risk protection. |
| C: Premium support | Gives high-touch carrier support for complex export bookings. | 7/10 | Useful for enterprise or high-risk lanes, but may limit self-serve adoption. |

**Selected option:** A, risk reduction.

### Positioning Test Plan

| Test | Method | Success Signal |
|------|--------|----------------|
| Customer resonance | Read positioning cold in 5 customer interviews | At least 4/5 can explain what the service does and when they would use it |
| Commercial usability | Ask 3 sales/account users to pitch it in their own words | They preserve the booking-time risk reduction message |
| Competitive differentiation | Compare against broker and forwarder service language | Message clearly differentiates by timing and carrier context |

---

## Aha Moment

**Aha moment:** The customer sees that export clearance support has started, with an owner and next action, within 24 hours of selecting the service.

**Why this is the aha moment:** Selection alone is not value. Value becomes real when the customer can see that someone is acting on the booking and the clearance path is clearer than the manual alternative.

**Time-to-aha metric:** Median time from `booking_completed_with_ecc` to `ecc_first_support_action_completed`.

**Target:** 85% of selected services reach aha within 24 hours during pilot; 90% at scale.

---

## Growth Loop Inventory

### Loop 1: Booking Context Repeat-Use Loop

**Type:** Product-led

**Loop diagram:**

```
[Entry: Customer creates eligible export booking]
         |
         v
[Action: Customer selects Export Customs Clearances]
         |
         v
[Output: Support starts within 24h and reduces clearance uncertainty]
         |
         v
[Re-entry: Customer trusts service and selects it on future eligible bookings]
         ^______________________________________________________________|
```

**Entry point:** Customer creates an eligible export booking in a supported lane.

**Core action:** Customer selects Export Customs Clearances during booking.

**Output:** Customer receives timely support action, clearer next steps, and reduced clearance uncertainty.

**Re-entry condition:** Customer creates another eligible export booking and remembers the prior service value, or the product recommends the service based on similar risk signals.

**Loop metric:** 90-day repeat selection rate among customers with another eligible export booking.

**Current state:** Latent

**Friction points:**
- Customer may not understand service scope during first booking.
- Operations may not deliver first action quickly enough.
- Product may not recognize repeat eligible situations or remind the customer.

### Loop 2: Operations Proof-to-Account Expansion Loop

**Type:** Product-led / sales-assisted

**Loop diagram:**

```
[Entry: Customer uses ECC on one risky booking]
         |
         v
[Action: Support outcome and CSAT are captured]
         |
         v
[Output: Account-level proof of reduced uncertainty and timely support]
         |
         v
[Re-entry: Account manager recommends ECC for more lanes/customers]
         ^_________________________________________________________|
```

**Entry point:** A customer uses ECC and completes support with positive feedback.

**Core action:** Product and operations capture outcome, SLA, and feedback.

**Output:** Commercial team receives proof that can support repeat adoption or account-level enablement.

**Re-entry condition:** Account manager recommends ECC for similar bookings or lanes in the same account.

**Loop metric:** Account-level repeat adoption rate.

**Current state:** Latent

**Friction points:**
- Outcomes may not be captured in a shareable format.
- Account teams may not know which customers benefited.
- Customers may treat the service as one-off emergency help rather than a repeat operating pattern.

### Loop 3: Partner-Friendly Forwarder Enablement Loop

**Type:** Community / product-led

**Loop diagram:**

```
[Entry: Forwarder selects ECC for an exporter booking]
         |
         v
[Action: Forwarder receives clear support summary]
         |
         v
[Output: Forwarder uses summary to reassure exporter customer]
         |
         v
[Re-entry: Forwarder selects ECC for similar exporter shipments]
         ^______________________________________________________|
```

**Entry point:** Freight forwarder manages a booking in a lane where ECC support is relevant.

**Core action:** Forwarder selects ECC and receives a partner-friendly support summary.

**Output:** Forwarder can show exporter customers they are being proactive.

**Re-entry condition:** Forwarder uses ECC as part of their service toolkit for similar shipments.

**Loop metric:** Repeat selection rate among forwarder-managed eligible bookings.

**Current state:** Latent

**Friction points:**
- Forwarders may perceive ECC as competing with their service role.
- Summary may not be reusable or branded appropriately.
- Responsibility boundaries may be unclear.

---

## Primary Loop Selection

**Primary growth loop:** Booking Context Repeat-Use Loop

**Why this is primary:** It is most directly tied to the North Star Metric, requires the least external channel dependency, and compounds through repeated booking behavior. This loop also forces the product to prove activation, trust, and service delivery before broader acquisition or commercial scale-up.

**Loops to activate next:** Operations Proof-to-Account Expansion Loop after service outcomes and CSAT are reliable; Partner-Friendly Forwarder Enablement Loop after forwarder positioning is validated.

---

## PLG Flywheel

| Flywheel Stage | Goal | Current Friction | Fix | Key Metric |
|----------------|------|------------------|-----|------------|
| Awareness | Customer notices ECC when it is relevant | Offer may feel like a generic upsell | Show offer only for eligible / risk-relevant bookings | Eligible offer exposure rate |
| Activation | Customer reaches first visible value | Value is not real until support starts | Trigger support case and first action within 24h | First support action within 24h |
| Engagement | Customer tracks next steps and responds | Follow-up may happen outside product | Add owner, next action, and status summary | Support completion before cutoff |
| Expansion | Customer selects ECC again on similar bookings | Product may not remind or recommend repeat usage | Recommend ECC when similar risk signals appear | 90-day repeat selection rate |
| Advocacy | Customer or forwarder recommends ECC internally | Value proof may not be shareable | Create post-support summary and account insights | CSAT and account repeat adoption |

---

## Retention Mechanics

### Hook Model

| Element | ECC Design |
|---------|------------|
| **External trigger** | Booking flow offer appears when export clearance risk or eligibility is detected. |
| **Action** | Customer selects Export Customs Clearances with minimal added steps. |
| **Reward** | Customer receives visible first support action, owner, and next step within 24 hours. |
| **Investment** | Customer shares required documents or shipment context and learns the service is useful for similar bookings. |
| **Internal trigger** | On future risky export bookings, customer remembers ECC as the earlier, safer support path. |

### Retention Guardrail

Since D30 / 90-day repeat selection is not yet measured, the growth plan should not recommend paid acquisition. The next growth work should focus on activation, service reliability, repeat behavior, and account expansion proof.

---

## Loop Health Metrics

| Loop | Metric | Current | Target | Status |
|------|--------|---------|--------|--------|
| Booking Context Repeat-Use Loop | 90-day repeat selection rate | TBD | 25% | Red - not instrumented |
| Booking Context Repeat-Use Loop | First support action within 24h | 0% | 85% pilot | Red - not launched |
| Operations Proof-to-Account Expansion Loop | Account-level repeat adoption | TBD | TBD after pilot | Red - not instrumented |
| Partner-Friendly Forwarder Loop | Forwarder repeat selection rate | TBD | TBD after interviews | Red - not instrumented |

---

## Growth Experiments

| Priority | Experiment | Hypothesis | Owner | Timeline | Success Metric |
|----------|------------|------------|-------|----------|----------------|
| 1 | Risk-reduction vs convenience offer message | Risk-reduction copy will increase selection because customers care most about avoiding clearance delay risk. | Product / Data | Pilot | +20% relative lift in VAS selection |
| 2 | Included / not included scope module | Clear scope will increase trust and reduce non-selection due to ambiguity. | Product / CX | Pilot | 80% scope clarity score |
| 3 | First-action confirmation | Showing owner and SLA after selection will improve confidence and CSAT. | Product / Ops | Pilot | 4.2/5 CSAT and 85% first action within 24h |
| 4 | Repeat-booking recommendation | Reminding customers on similar future bookings will increase repeat selection. | Product / Commercial | Post-pilot | 25% 90-day repeat selection among repeat eligible customers |
| 5 | Forwarder support summary | A partner-friendly summary will reduce forwarder resistance and increase repeat use. | Product / Commercial | Post-interviews | Forwarder repeat selection target TBD |

---

## Messaging Architecture

### Core Message

Start export clearance support at the moment you book, before missing information becomes a cutoff risk.

### Supporting Messages

| Message | Customer Pain / Gain Mapped |
|---------|-----------------------------|
| "Know what happens next after you select the service." | P3, G1 |
| "Carrier-side support starts from the booking data you already provided." | P2, G2 |
| "Reduce late document rework and shipment cutoff anxiety." | P1, G3 |
| "Use it when the shipment, lane, or timing makes clearance feel risky." | P4, G1 |

### Messages to Avoid

- "Guaranteed clearance" because this may create compliance and liability risk.
- "Fastest clearance" because speed depends on customer documents, broker execution, and regulatory factors.
- "Replaces your broker" because forwarders and brokers may be partners or required execution parties.

---

## Growth Roadmap

| Phase | Focus | Work | Exit Criteria |
|-------|-------|------|---------------|
| Phase 1: Pilot activation | Prove customers select and reach aha | Offer message test, support case workflow, first-action SLA | 8% selection, 85% first action within 24h |
| Phase 2: Retention proof | Prove repeat value | Repeat-booking recommendation, status summary, CSAT loop | 25% 90-day repeat selection among repeat eligible customers |
| Phase 3: Account expansion | Prove commercial repeatability | Account reporting, sales enablement, forwarder summary | Account-level repeat adoption target achieved |
| Phase 4: Scaled growth | Expand lanes and segments | Eligibility expansion, pricing optimization, GTM launch | Positive unit economics and stable service quality |

---

## Quality Checklist

- [x] Value Proposition Canvas maps every pain reliever to a named pain.
- [x] Value Proposition Canvas maps every gain creator to a named gain.
- [x] Positioning statement includes an explicit "unlike" clause.
- [x] Growth loop is circular and output feeds re-entry.
- [x] Primary loop is selected.
- [x] Loop metric is defined for each loop.
- [x] Retention is not assumed; repeat selection must be measured before acquisition scale-up.
- [x] NSM is linked to growth levers.
