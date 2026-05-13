---
artifact: MARKET-RESEARCH
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-market-research
upstream: discovery.md
downstream: analytics.md
---

# Export Customs Clearances Market Research

**Product / Research Context:** Export Customs Clearances value-added service for export bookings  
**Date:** 2026-05-13  
**Owner:** Product Team  
**Based on:** Strategy and discovery hypotheses; external market indicators; customer interviews pending

---

## Research Caveat

This is a first-pass market research artifact. Personas and journey maps are hypothesis-based until at least 5 qualified customer interviews are completed. Market sizing uses public trade and maritime data as directional anchors, but decision-grade SAM/SOM requires internal booking volume, eligible lane coverage, service pricing, and operations capacity.

---

## Segmentation Model

### Primary Segmentation

| Segment | Basis | Description | Priority |
|---------|-------|-------------|----------|
| Time-sensitive export shippers | Behavioral | Customers who create export bookings close to documentation or cargo cutoff and need faster clearance readiness. | High |
| Documentation-heavy exporters | Behavioral | Customers whose shipments commonly require repeated document checks, country-specific forms, or broker coordination. | High |
| Freight forwarders managing multiple exporters | Behavioral / firmographic | Forwarders who coordinate export clearance across many customer bookings and need predictable handoffs. | High |
| Self-managed SME exporters | Behavioral / firmographic | Exporters without mature in-house customs operations who rely on manual guidance, email, and external help. | Medium |
| Enterprise exporters with existing broker contracts | Firmographic | Large exporters with established brokerage processes and lower immediate need for carrier-provided support. | Lower initial priority |

### Behavioral Signals for Targeting

- Booking created near cargo/documentation cutoff.
- Trade lane or origin country known to require extra export documentation.
- Customer has prior documentation rework, customs hold, booking amendment, or export service escalation history.
- Customer selects other booking-time VAS options.
- Customer uses manual support channels after booking creation.

---

## Persona 1: Linh Tran, Export Operations Coordinator

**Persona Name:** Linh Tran  
**Product / Research Context:** Booking-time export clearance support  
**Date:** 2026-05-13  
**Based on:** Hypothesis from discovery; interview validation pending

### Profile

| Attribute | Value |
|-----------|-------|
| **Name** | Linh Tran |
| **Role / Title** | Export Operations Coordinator |
| **Industry** | Manufacturing exporter |
| **Company size** | 100-500 employees |
| **Experience in role** | 4-7 years |
| **Location** | Vietnam / Southeast Asia export market |
| **Tech comfort** | Medium |

### Jobs-to-be-Done

**Functional Job (Primary):**  
"When I create an export booking, I need to make sure clearance documents and responsibilities are clear before cargo cutoff."

**Functional Job (Secondary):**  
Coordinate with internal shipping, finance, warehouse, broker, and carrier teams without losing track of who owes what.

**Emotional Job:**  
Feel calm and in control before deadlines become urgent.

**Social Job:**  
Be seen internally as the person who prevents shipment delays and keeps export operations reliable.

### Current Solution

**What they use today:** Email, carrier portal, broker messages, spreadsheets, document folders, and phone calls.

**Why they settled for it:** It is familiar, low-cost, and already accepted by internal teams.

**What they like about it:** It is flexible and lets them escalate manually when a shipment becomes urgent.

### Pains

| # | Pain | Severity |
|---|------|----------|
| 1 | "I only realize something is missing when the deadline is already close." | High |
| 2 | Rechecking shipment and document details across email, portal, and broker messages takes too much time. | High |
| 3 | It is unclear whether the carrier, broker, or internal team owns the next action. | High |
| 4 | Paying for an extra service is hard to justify if the scope is vague. | Medium |

### Gains

| # | Gain | Importance |
|---|------|------------|
| 1 | Know exactly what export clearance support will cover before selecting it. | High |
| 2 | Receive confirmation that support has started within one business day. | High |
| 3 | Reduce last-minute document rework and cargo cutoff anxiety. | High |
| 4 | Have a simple status view after booking. | Medium |

### Switching Trigger

A shipment is at risk of rollover because export clearance preparation started late or a document issue was found close to cutoff.

**Trigger type:** Pain threshold reached

### Buying Behavior

| Attribute | Value |
|-----------|-------|
| **Decision-making role** | User / Influencer |
| **Budget authority** | Needs manager or commercial approval for recurring spend; can influence shipment-level VAS selection |
| **Evaluation criteria** | Clear scope, speed of first action, credible support ownership |
| **Preferred buying channel** | Self-serve add-on during booking with simple explanation |
| **Evaluation timeline** | Minutes during booking; longer if company policy requires approval |

### Product Implications

**What our product must do to win this persona:**
1. Explain service scope in plain language at booking time.
2. Confirm what happens next immediately after selection.
3. Start support within a visible SLA.

**What would delight this persona beyond the core job:**
1. A checklist of missing items and owners after booking.

**What would immediately disqualify our product:**
1. Hidden scope, unclear liability, or no visible action after purchase.

---

## Persona 2: Minh Pham, Freight Forwarder Customer Service Lead

**Persona Name:** Minh Pham  
**Product / Research Context:** Export clearance support for forwarder-managed bookings  
**Date:** 2026-05-13  
**Based on:** Hypothesis from discovery; interview validation pending

### Profile

| Attribute | Value |
|-----------|-------|
| **Name** | Minh Pham |
| **Role / Title** | Customer Service Lead |
| **Industry** | Freight forwarding |
| **Company size** | 50-300 employees |
| **Experience in role** | 6-10 years |
| **Location** | Vietnam / Southeast Asia export market |
| **Tech comfort** | Medium-high |

### Jobs-to-be-Done

**Functional Job (Primary):**  
"When I manage multiple export bookings, I need clearance issues surfaced early so I can protect my customer's schedule."

**Functional Job (Secondary):**  
Coordinate with brokers, carriers, and customers while keeping internal service teams informed.

**Emotional Job:**  
Feel prepared instead of reactive.

**Social Job:**  
Be perceived by exporters as a proactive logistics partner, not just a coordinator.

### Current Solution

**What they use today:** Forwarder TMS, carrier portals, broker partners, email templates, team chat, and manual exception lists.

**Why they settled for it:** It supports many customers and gives the forwarder control over relationships.

**What they like about it:** It is flexible and fits their existing service model.

### Pains

| # | Pain | Severity |
|---|------|----------|
| 1 | Carrier booking data and clearance coordination live in different workflows. | High |
| 2 | Export clearance support is difficult to standardize across lanes and customers. | High |
| 3 | The team spends too much time chasing missing information. | Medium |
| 4 | Carrier VAS can feel like competition if the scope is not partner-friendly. | Medium |

### Gains

| # | Gain | Importance |
|---|------|------------|
| 1 | Earlier visibility into clearance risk by booking. | High |
| 2 | Clear carrier-side support scope that complements forwarder work. | High |
| 3 | Less manual escalation near cutoff. | High |
| 4 | Lane-specific guidance for junior operators. | Medium |

### Switching Trigger

A key customer complains about repeated clearance-related delays or manual follow-up, prompting the forwarder to look for a more reliable support path.

**Trigger type:** External event / Pain threshold reached

### Buying Behavior

| Attribute | Value |
|-----------|-------|
| **Decision-making role** | Influencer / Champion |
| **Budget authority** | Limited; may pass cost through to exporter |
| **Evaluation criteria** | Partner fit, SLA, scope clarity, support responsiveness |
| **Preferred buying channel** | In-booking add-on, account manager enablement, and tariff/service guide |
| **Evaluation timeline** | Same-day for urgent shipments; quarterly for standardized adoption |

### Product Implications

**What our product must do to win this persona:**
1. Avoid positioning that replaces the forwarder relationship.
2. Provide lane and documentation guidance that reduces team workload.
3. Give a clear escalation path and support timestamp.

**What would delight this persona beyond the core job:**
1. A reusable service summary they can share with exporter customers.

**What would immediately disqualify our product:**
1. Ambiguous responsibility between carrier, broker, forwarder, and shipper.

---

## TAM / SAM / SOM Market Sizing

### Definitions

| Term | Definition | This Analysis |
|------|------------|---------------|
| **TAM** | Global export shipment universe where customs clearance support may be relevant. | Directional proxy only |
| **SAM** | Export bookings reachable through the carrier's digital booking flow and eligible service lanes. | Requires internal data |
| **SOM** | Realistic captured VAS revenue from eligible bookings in 3-5 years. | Modeled scenario |

### External Market Anchors

| Anchor | Data Point | Source |
|--------|------------|--------|
| Global trade scale | World trade in goods and commercial services reached US$34.65 trillion in 2025. | WTO World Trade Statistics 2025 |
| Merchandise trade momentum | WTO reported world merchandise trade value growth in 2025 and continued trade-policy uncertainty into 2026. | WTO Global Trade Outlook and Statistics 2025 |
| Maritime relevance | Over 80% of international goods trade volume is carried by sea. | UNCTAD Review of Maritime Transport |
| Maritime volume | Global maritime trade reached 12.3 billion tons in 2023 and was projected to continue growing. | UNCTAD Review of Maritime Transport 2024 |

### TAM - Top-Down Directional Estimate

**Method:** Use global goods/shipping scale as a proxy, then narrow to export-clearance serviceable activity.

| Step | Value | Source / Rationale |
|------|-------|--------------------|
| Global goods and services trade | US$34.65T | WTO 2025 world trade statistics |
| Estimated goods share | 72.4% | WTO reports services share at 27.6%; remainder treated as goods proxy |
| Estimated goods trade value | US$25.1T | 34.65T x 72.4% |
| Estimated sea-carried goods relevance | High | UNCTAD states over 80% of goods trade volume moves by sea |
| Clearance-support fee pool assumption | 0.01%-0.03% of relevant goods trade value | Directional proxy for transaction support services, not a validated market report |
| Directional TAM proxy | US$2.5B-US$7.5B | 25.1T x 0.01%-0.03% |

**Assumptions:**
- This is not the total customs brokerage market; it is a proxy for export clearance support value that could attach to ocean export transactions.
- Trade value is used only as a directional sizing anchor because shipment counts and clearance-support pricing are not yet available.
- This should be replaced with shipment-level bottom-up sizing once internal booking and pricing data are available.

### SAM - Bottom-Up Serviceable Estimate

**Method:** Count eligible digital export bookings reachable by the carrier and multiply by expected annual VAS revenue.

| Input | Value | Source / Assumption |
|-------|-------|---------------------|
| Annual digital export bookings | TBD | Internal booking analytics required |
| Percent in eligible pilot / launch lanes | 20%-40% | Assumption until operations and compliance define coverage |
| Percent with likely clearance-support need | 15%-30% | Assumption based on behavioral targeting hypothesis |
| Average VAS price per selected booking | US$75-US$250 | Pricing hypothesis; validate in GTM/pricing research |
| Gross SAM formula | Digital export bookings x eligible lane % x need % x price | Internal model |

**Example scenario for planning only:**  
If annual digital export bookings = 100,000, eligible lanes = 30%, likely-need bookings = 20%, and average VAS price = US$150, then SAM = 100,000 x 30% x 20% x US$150 = **US$900,000 annual serviceable revenue**.

### SOM - Realistic Capture Scenarios

**Method:** Apply attach rate and rollout maturity to serviceable eligible bookings.

| Scenario | Eligible Need Bookings | Attach Rate | Average Price | Annual SOM |
|----------|------------------------|-------------|---------------|------------|
| Conservative | 6,000 | 5% | US$100 | US$30,000 |
| Base | 6,000 | 12% | US$150 | US$108,000 |
| Optimistic | 6,000 | 20% | US$200 | US$240,000 |

**Largest variance drivers:**
1. Number of eligible export bookings in supported lanes.
2. True customer willingness to select the service during booking.
3. Price tolerance by segment and lane.
4. Operations capacity and gross margin after manual support cost.

### Reconciliation

| Method | TAM | SAM | SOM |
|--------|-----|-----|-----|
| Top-down proxy | US$2.5B-US$7.5B | Not reliable without carrier reach | Not reliable |
| Bottom-up model | Not applicable | US$900K example scenario | US$30K-US$240K example scenario |

**Variance explanation:** The top-down number is useful only to confirm that customs and trade support is a large enough global category. The bottom-up model is more reliable for this product because the first commercial constraint is not global trade value; it is the carrier's eligible digital booking volume, supported lanes, and operational capacity.

---

## Customer Journey Map

**Persona:** Linh Tran, Export Operations Coordinator  
**Journey:** Selecting and using Export Customs Clearances during an export booking  
**Date:** 2026-05-13  
**Owner:** Product Team

### Journey Overview

**Starting point:** Linh needs to create an export booking and is unsure whether clearance preparation will be smooth for this shipment.

**End point:** Clearance support has started, required next steps are clear, and Linh feels confident the shipment will not miss cutoff due to export clearance preparation.

**Key actors:** Export operations user, carrier booking platform, carrier operations/support team, customs broker or clearance specialist, warehouse/logistics team, commercial/account manager.

### Stage 1: Pre-Awareness

| Element | Content |
|---------|---------|
| **What the customer is doing** | Creating export bookings and managing clearance manually without thinking of carrier-side support as an option. |
| **Touchpoints** | Existing booking portal, email, broker communication, internal SOPs. |
| **Customer thoughts** | "This is just part of export operations; I need to keep chasing people." |
| **Emotion** | Frustrated |
| **Our actions** | Analyze booking patterns, support escalations, and lane risk to identify likely need. |
| **Opportunities** | Surface educational cues in booking; identify high-risk lanes; create support content for common clearance friction. |

### Stage 2: Awareness

| Element | Content |
|---------|---------|
| **What the customer is doing** | Notices Export Customs Clearances as a VAS option during booking. |
| **Touchpoints** | Booking service selection, tooltip, account manager communication. |
| **Customer thoughts** | "What exactly will the carrier help me with?" |
| **Emotion** | Neutral / cautious |
| **Our actions** | Present clear scope, benefits, price, and next step. |
| **Opportunities** | Use lane-specific copy; explain SLA; show when the service is recommended. |

### Stage 3: Consideration

| Element | Content |
|---------|---------|
| **What the customer is doing** | Decides whether the shipment is risky enough to justify paid support. |
| **Touchpoints** | VAS card, service details, pricing, policy/service guide. |
| **Customer thoughts** | "Is this different from what my broker already does?" |
| **Emotion** | Uncertain |
| **Our actions** | Clarify responsibilities and avoid overpromising compliance outcomes. |
| **Opportunities** | Compare included vs not included; show examples of helped scenarios; include "support starts within 24 hours" promise if operationally validated. |

### Stage 4: Decision

| Element | Content |
|---------|---------|
| **What the customer is doing** | Selects or rejects the VAS during booking. |
| **Touchpoints** | Booking checkout, service confirmation, quote/charge summary. |
| **Customer thoughts** | "I need to know this will not slow down my booking." |
| **Emotion** | Slightly anxious |
| **Our actions** | Confirm selection, price, and next steps without disrupting booking completion. |
| **Opportunities** | Keep selection low-friction; avoid long forms; offer "request support" for pilot before full paid checkout. |

### Stage 5: Onboarding

| Element | Content |
|---------|---------|
| **What the customer is doing** | Receives confirmation and waits for support to begin. |
| **Touchpoints** | Confirmation page, email, support case, operations contact. |
| **Customer thoughts** | "Has anyone actually started working on this?" |
| **Emotion** | Anxious until first contact |
| **Our actions** | Trigger operations workflow, assign owner, contact customer, request required information. |
| **Opportunities** | Provide support owner, SLA timestamp, document checklist, and current status. |

### Stage 6: Retention / Active Use

| Element | Content |
|---------|---------|
| **What the customer is doing** | Responds to support requests and tracks clearance readiness. |
| **Touchpoints** | Email, support dashboard, booking detail page, operations updates. |
| **Customer thoughts** | "I know what is pending and who owns it." |
| **Emotion** | Satisfied if updates are clear |
| **Our actions** | Maintain status, chase missing information, coordinate with clearance specialist or broker. |
| **Opportunities** | Add status labels; remind owners before cutoff; collect support outcome data. |

### Stage 7: Advocacy

| Element | Content |
|---------|---------|
| **What the customer is doing** | Reuses the service or recommends it internally for risky export shipments. |
| **Touchpoints** | Repeat bookings, post-service survey, account review, case study. |
| **Customer thoughts** | "This helped prevent a last-minute problem." |
| **Emotion** | Confident / relieved |
| **Our actions** | Ask for feedback, identify repeat-use patterns, package learnings into account-level recommendations. |
| **Opportunities** | Build saved preferences; recommend service for similar lanes; create account-level adoption reporting. |

### Emotion Arc

```
Delighted  |                                      *
Satisfied  |                                *
Neutral    |          *        *
Frustrated | *                          *
           +----------+--------+--------+--------+--------+----------+----------+
           Pre-aware  Aware    Consider Decision Onboard  Active Use Advocacy
```

### Key Insights

**Moment of Delight:** When the customer receives a clear first support action within the promised SLA.

**Moment of Friction:** Immediately after selecting the service if no owner, status, or next step is visible.

**Drop-off Risk Points:**
1. Consideration: customer does not understand scope or difference from broker support.
2. Decision: price appears as a vague surcharge rather than risk-reduction support.
3. Onboarding: no visible action after selection.

**Top 3 Opportunities:**
1. Make the VAS offer specific to shipment context and risk.
2. Provide clear service scope and responsibility boundaries.
3. Show first-action SLA, owner, and next step immediately after selection.

---

## Competitive Analysis Matrix

| Dimension | Export Customs Clearances | Freight Forwarder | Customs Broker | Substitute: Manual Email / Phone |
|-----------|---------------------------|-------------------|----------------|----------------------------------|
| Target customer | Export booking customers needing carrier-side support | Exporters outsourcing logistics coordination | Exporters needing formal customs expertise | Anyone coordinating clearance manually |
| Primary JTBD | Start clearance support earlier from booking context | Manage shipment execution end to end | Complete customs filing and compliance steps | Chase people until issue is resolved |
| Key differentiator | Booking-native timing and carrier shipment context | Broader service ownership | Specialized compliance depth | Flexible and familiar |
| Pricing | Per-booking VAS, TBD | Service fee / margin / contract | Brokerage fee / declaration fee | Internal labor cost |
| Distribution channel | Carrier booking flow and account teams | Sales/account relationships | Broker network and referrals | Existing behavior |
| Strengths | Timely, contextual, easy to select | Relationship trust, broad coordination | Expertise, compliance focus | No new tool or vendor needed |
| Weaknesses | Scope and liability must be clear; operations capacity required | May not be embedded in carrier booking moment | May be disconnected from booking workflow | Unstructured, hard to track, reactive |
| Strategic implication | Win by being the earliest, clearest support path at booking time | Position as complementary, not replacement | Partner or integrate where compliance depth is required | Beat manual process with visible SLA and accountability |

---

## Market Research Implications

1. The first beachhead should be behavior-based: customers and lanes where clearance risk is visible before or during booking.
2. The product must be careful with responsibility boundaries because forwarders and brokers are both competitors and potential partners.
3. The most important journey moment is not selection; it is the first visible support action after selection.
4. Market size should be governed by internal eligible booking data, not generic logistics market reports.
5. Research should now validate willingness to select the service, willingness to pay, trust requirements, and operational feasibility by lane.

---

## Source Notes

- WTO, World Trade Statistics 2025: world trade in goods and commercial services reached US$34.65 trillion in 2025, with services at 27.6% of global trade.
- WTO, Global Trade Outlook and Statistics Update October 2025: world merchandise trade volume and value context, trade growth, and uncertainty.
- UNCTAD, Review of Maritime Transport 2024: over 80% of international goods trade volume is carried by sea; global maritime trade reached 12.3 billion tons in 2023.

---

## Quality Checklist

- [ ] Persona is grounded in at least 5 real interviews.
- [x] Segmentation is behavioral and firmographic, not only demographic.
- [x] TAM/SAM/SOM uses both top-down and bottom-up methods.
- [x] Journey map covers Pre-awareness through Advocacy.
- [x] Competitive analysis includes substitutes.
- [x] Every pain has a severity; every gain has an importance rating.
- [x] Switching trigger describes a specific event.
