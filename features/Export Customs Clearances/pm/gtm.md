---
artifact: GTM-PLAN
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-go-to-market
upstream: growth.md
downstream: po/brief.md
---

# Export Customs Clearances Go-To-Market Plan

**Feature / Product:** Export Customs Clearances  
**Launch Target:** Pilot in Q3 2026, GA target TBD after Beta  
**PM Owner:** Product Team  
**Date:** 2026-05-13  
**Data basis:** Strategy, discovery, market research, analytics, and growth artifacts; customer and pricing validation pending

---

## GTM Summary

Export Customs Clearances should launch as a focused, booking-native value-added service for customers with eligible ocean export bookings where clearance preparation risk is visible. The GTM should start with a closed Alpha among high-trust customers and selected lanes, then expand only after service quality, support SLA, and customer willingness to pay are validated.

**Primary GTM decision:** Use a hybrid motion: product-led in the booking flow for selection and activation, with sales/account support for education, objections, pricing feedback, and account-level expansion.

---

## Ideal Customer Profile

### B2B ICP

#### Firmographic Attributes

| Attribute | ICP Definition | Disqualifier |
|-----------|----------------|--------------|
| **Industry / Vertical** | Export manufacturers, trading companies, and freight forwarders managing ocean export bookings | Import-only customers, purely domestic logistics users |
| **Company size (employees)** | 50-500 for exporters; 30-300 for freight forwarders | Very small shippers with rare export volume; very large enterprise requiring custom procurement before pilot |
| **Company size (shipment volume)** | Repeated export bookings in supported lanes; enough recurrence to measure repeat selection | One-off or sporadic export bookings |
| **Geography** | Initial pilot lanes from Vietnam / Southeast Asia origins where carrier operations can support export clearance workflows | Countries or lanes without compliance and operations readiness |
| **Tech stack / workflow** | Uses digital carrier booking flow and email/manual coordination for clearance | Fully offline booking process or no access to digital booking |
| **Business model** | Exporter shipping goods internationally, or forwarder managing exporter shipments | Broker-only business with no booking ownership |

#### Role-Level Attributes

| Attribute | ICP Definition |
|-----------|----------------|
| **Champion role** | Export Operations Coordinator, Logistics Manager, Forwarder Customer Service Lead |
| **Economic buyer role** | Logistics Manager, Head of Operations, Commercial/Procurement owner for recurring service spend |
| **Decision-making process** | Shipment-level selection by user or manager approval; account-level adoption via commercial/account team |
| **Evaluation criteria** | Clear scope, first support action speed, price-to-risk value, responsibility boundaries, operational trust |

#### Behavioral Attributes

| Attribute | ICP Definition |
|-----------|----------------|
| **Current solution** | Manual coordination through broker, forwarder, internal team, email, phone, spreadsheets, and carrier portal |
| **Pain severity** | Has experienced documentation rework, clearance uncertainty, late escalation, or cutoff anxiety |
| **Buying trigger** | A shipment is at risk of delay or the customer is booking in a lane/timing context where clearance feels uncertain |
| **Decision speed** | Minutes for in-booking intent; days to weeks for repeat account adoption |
| **Expansion pattern** | Starts with risky shipments, repeats on similar lanes, then adopts as recommended service for selected booking types |

### ICP Scoring Model

| Attribute | 3 points | 1 point | 0 points |
|-----------|----------|---------|----------|
| Export booking frequency | Recurring export bookings in supported lanes | Occasional export bookings | Rare/no export bookings |
| Clearance risk signal | Prior rework/escalation or close-to-cutoff booking | Possible documentation complexity | Low-risk/simple process |
| Digital booking usage | Uses carrier digital booking directly | Uses mixed digital/manual process | Fully offline |
| Champion fit | Ops or forwarder user owns booking/clearance coordination | Adjacent logistics role | No clear owner |
| Operations supportability | Lane and support model ready | Partially ready | Not supportable yet |

**ICP threshold:** 10+ points = Alpha/Beta target. 6-9 points = monitor or include later. Below 6 = deprioritize.

### ICP Validation Gaps

| Assumption | How to Validate |
|------------|-----------------|
| Customers will select ECC during booking when scope and value are clear | Fake-door offer and customer interviews |
| The highest-retention segment is time-sensitive exporters, not all exporters | Cohort analysis by timing, lane, and customer type |
| Forwarders will treat ECC as complementary rather than competitive | Forwarder interviews and partner-friendly summary test |
| Price tolerance supports positive unit economics | 5+ pricing conversations and pilot pricing test |

---

## Beachhead Market

| Attribute | Value |
|-----------|-------|
| **Beachhead segment** | Vietnam / Southeast Asia export customers using digital carrier booking for supported lanes with recurring clearance coordination pain |
| **Why this segment** | Strong export activity, direct relevance to ocean booking, visible clearance/documentation friction, and operational proximity for pilot learning |
| **Estimated SAM of beachhead** | TBD; requires internal eligible digital export booking volume and lane coverage |
| **Winning criterion** | Capture >50% of ECC-eligible bookings among Alpha/Beta design partner accounts within 18-24 months |
| **Next segment after beachhead** | Freight forwarders managing multiple exporter customers in the same supported lanes |
| **Expansion after that** | Additional Southeast Asia origin lanes where compliance, broker, and operations support are validated |

### Negative ICP

| Profile | Why They Are Not ICP | Action |
|---------|----------------------|--------|
| Customers with one-off, low-risk export bookings | Low repeat potential and weak urgency | Show only if highly eligible; do not target |
| Enterprise exporters requiring custom legal/procurement approval before any VAS | Slow sales cycle; not ideal for pilot learning | Defer to later enterprise program |
| Lanes without validated compliance or operations support | High service-quality and liability risk | Block eligibility |
| Customers expecting guaranteed customs clearance outcome | Risk of overpromising beyond carrier control | Clarify scope or disqualify |
| Brokers who do not own booking decisions | May not be able to purchase or activate the service | Treat as partner/channel research, not initial ICP |

---

## GTM Motion Selection

**Selected motion:** Hybrid PLG + SLG

| Motion Component | Role |
|------------------|------|
| **PLG** | Booking flow exposes the offer, explains value, captures intent/selection, and triggers support workflow. |
| **Sales/account-assisted** | Account teams educate target customers, collect objections, support pricing validation, and expand adoption after proof. |
| **Operations-led trust** | Support team delivers first-action SLA, which is the real activation moment. |

**Why hybrid is right:** The purchase moment is self-serve and embedded in booking, but the service touches compliance, responsibility boundaries, pricing trust, and operational delivery. Those require account and operations support during Alpha/Beta.

**Why not pure PLG yet:** Customers may not understand service scope or trust the support promise without education.

**Why not pure SLG:** Shipment-level VAS selection needs to happen in the booking flow, at the moment of need.

---

## Pricing Strategy

### Recommended Pricing Model

**Initial model:** Per-booking value-based VAS fee, validated in Alpha/Beta.

**Rationale:** The customer evaluates the service per shipment based on delay risk, document effort, and support clarity. Per-booking pricing fits the buying moment better than subscription pricing for the pilot.

### Pricing Hypotheses

| Tier / Model | Description | Price Hypothesis | Use Case |
|--------------|-------------|------------------|----------|
| Pilot intent | Request support, no public price or limited controlled price | TBD | Validate demand and operations before public pricing |
| Standard ECC | Booking-time support initiation, scope guidance, first support action SLA | US$75-US$150 per booking | Lower-complexity supported lanes |
| Priority ECC | Faster response target, enhanced coordination, account-visible summary | US$150-US$250 per booking | Time-sensitive or higher-risk bookings |

### Pricing Validation Plan

Use at least 5 customer conversations before committing to public pricing.

| Question Type | Question |
|---------------|----------|
| Too cheap | At what price would this feel so cheap you would question service quality? |
| Good value | At what price would this feel like a good value for a risky export booking? |
| Expensive but acceptable | At what price would this feel expensive but still worth considering? |
| Too expensive | At what price would you stop considering it? |

### Pricing Guardrails

- Do not publish a broad public price until operations cost and SLA reliability are measured.
- Do not price below manual support cost plus target margin.
- Do not bundle vague "premium support" language without scope clarity.
- Keep refund/exception policy explicit before Beta.

---

## Launch Plan

### Launch Overview

| Attribute | Value |
|-----------|-------|
| **What we're launching** | Booking-time Export Customs Clearances VAS selection and carrier-side support workflow for eligible export bookings. |
| **Target customer** | ICP customers in supported pilot lanes with recurring clearance preparation pain. |
| **Primary launch goal** | Prove customers select the service and receive timely support that improves confidence. |
| **GTM motion** | Hybrid PLG + SLG |
| **Launch type** | New value-added service / Alpha-to-GA launch |

### Phase 1: Alpha (Closed Beta)

**Goal:** Validate core value with high-trust design partners before marketing or broad eligibility.

**Entry criteria:**
- [ ] Eligibility rules defined for pilot lanes.
- [ ] Service scope, responsibility boundaries, and legal/compliance review completed.
- [ ] Support workflow can create case from booking and log first action.
- [ ] No P0 bugs in booking selection and support routing.
- [ ] Alpha support team trained on SLA, scope, escalation, and documentation.

**Participants:** 10-20 selected customers from ICP accounts, including exporters and freight forwarders who participated in discovery or account conversations.

**Duration:** 2-4 weeks.

**What participants can do:**
- See ECC offer on eligible bookings.
- Select or request ECC support.
- Receive first carrier-side support action.
- Provide post-support feedback.

**Feedback collection:**
- Weekly check-in calls with selected participants.
- Post-support CSAT and scope clarity survey.
- Internal Ops debrief on every support case.
- Sales/account feedback on objections and pricing concerns.

**Success metrics:**

| Metric | Target |
|--------|--------|
| VAS selection / request rate among eligible exposed bookings | >= 8% |
| First support action within 24h | >= 85% |
| Scope clarity score | >= 80% positive |
| Post-support CSAT | >= 4.2/5 |
| P0/P1 bugs | 0 open at exit |

**Exit criteria:**
- [ ] All Alpha success metrics met or clearly explained with action plan.
- [ ] At least 3 customer quotes captured.
- [ ] No unresolved compliance or liability blocker.
- [ ] Operations confirms support capacity for Beta volume.
- [ ] Pricing range narrowed through at least 5 customer conversations.

### Phase 2: Beta (Limited Open Beta)

**Goal:** Validate activation, support load, repeat intent, and pricing with a broader eligible audience.

**Entry criteria:**
- [ ] Alpha exit criteria met.
- [ ] Help center/service scope article ready.
- [ ] Support dashboard and alerting live.
- [ ] Account teams trained with one-pager and objection handling.
- [ ] Refund/exception policy approved.

**Participants:** 100-500 eligible booking users across supported lanes, recruited through in-app eligibility, account team invite, and controlled email to selected accounts.

**Duration:** 4-6 weeks.

**Marketing activities:**
- In-app offer for eligible bookings.
- Account manager enablement for selected accounts.
- Targeted email to eligible ICP customers.
- Help center/service guide.

**Success metrics:**

| Metric | Target |
|--------|--------|
| VAS selection rate | >= 8% |
| Booking abandonment after offer exposure | No more than +2pp |
| First support action within 24h | >= 85% |
| Support completion or handoff before cutoff | >= 80% |
| Post-support CSAT | >= 4.2/5 |
| Repeat intent among surveyed users | >= 50% say they would use for similar shipment |

**Exit criteria:**
- [ ] Beta success metrics met.
- [ ] No P0/P1 bugs open.
- [ ] Support SLA stable for projected GA volume.
- [ ] Final service scope and pricing recommendation approved.
- [ ] GA marketing, sales, and support assets ready.

### Phase 3: General Availability

**Goal:** Scale adoption across validated lanes and ICP accounts while protecting support quality.

**Entry criteria:**
- [ ] Beta exit criteria met.
- [ ] GA eligibility rules approved.
- [ ] Support team staffed and trained.
- [ ] Pricing and billing flow approved.
- [ ] Sales/account enablement complete.
- [ ] Help center, FAQs, and escalation playbook complete.

**Launch date:** TBD after Beta.

#### GA Marketing Checklist

**Product:**
- [ ] In-booking VAS offer live for GA-eligible lanes.
- [ ] Booking confirmation includes ECC next steps.
- [ ] Support status / owner visible or communicated.

**Content:**
- [ ] Service overview page.
- [ ] Help center article: included, not included, and what happens next.
- [ ] FAQ for exporters and freight forwarders.

**Email / In-App:**
- [ ] Targeted email to ICP accounts.
- [ ] In-app announcement for eligible customers.
- [ ] Post-service feedback email.

**Sales / Account:**
- [ ] One-pager with ICP, value proposition, pricing, and scope.
- [ ] Demo script.
- [ ] Objection handling guide.
- [ ] Battlecards for broker/manual process and freight forwarder concerns.

**Support / Operations:**
- [ ] Escalation playbook.
- [ ] SLA dashboard.
- [ ] Compliance exception guide.

### Launch Success Metrics

| Metric | D7 Target | D30 Target | D90 Target |
|--------|-----------|------------|------------|
| Weekly Clearance-Supported Export Bookings | Baseline established | 8% selection rate in eligible bookings | 15% selection rate in mature eligible lanes |
| First support action within 24h | >= 85% | >= 90% | >= 90% |
| Post-support CSAT | >= 4.2/5 | >= 4.3/5 | >= 4.4/5 |
| Booking abandonment guardrail | <= +2pp | <= +2pp | <= +1pp |
| 90-day repeat selection | N/A | Baseline established | >= 25% among repeat eligible customers |

### Rollback Plan

| Trigger | Rollback Action | Owner |
|---------|-----------------|-------|
| Booking abandonment increases by >2pp | Disable offer for affected lane or segment | Product / Engineering |
| First support action within 24h falls below 70% | Pause new service exposure until operations capacity recovers | Operations |
| Compliance or liability issue emerges | Disable affected lane and route to manual review | Compliance / Product |
| CSAT falls below 3.8/5 | Pause expansion and run root-cause review | Product / CX / Ops |

---

## Sales Enablement

### One-Line Pitch

Export Customs Clearances helps eligible export customers start carrier-side clearance support at booking time, before missing information becomes a cutoff risk.

### Discovery Questions for Account Teams

1. Which export lanes create the most clearance coordination stress for your team?
2. When do you usually know export clearance support is needed: before booking, during booking, or after a problem appears?
3. What information is most often missing or reworked close to cutoff?
4. Who owns export clearance coordination today: your team, broker, forwarder, or carrier contact?
5. What would make a paid carrier-side support service feel worth using?

### Top Objections and Responses

| Objection | Response |
|-----------|----------|
| "We already use a broker." | ECC is not positioned to replace your broker. It starts carrier-side support from the booking context and clarifies next steps earlier. |
| "Can you guarantee clearance?" | No. The service supports earlier coordination and clearer next steps, but customs outcomes depend on documents, regulatory review, and responsible parties. |
| "Why should I pay for this?" | The value is reducing late rework, uncertainty, and escalation risk for shipments where clearance preparation is time-sensitive. |
| "Will this slow down my booking?" | The offer is designed as a low-friction booking add-on; booking abandonment is a launch guardrail. |
| "Who is responsible after I select it?" | The service confirmation should identify support owner, first-action SLA, and any customer-owned next steps. |

---

## Battlecard 1: Export Customs Clearances vs. Manual Email / Phone Coordination

**Last Updated:** 2026-05-13  
**Owner:** Product / PMM  
**Usage:** Sales, account, CX, and operations teams

### Quick Summary

**Who chooses manual coordination:** Customers who are used to flexible ad hoc processes, have low urgency, or do not trust paid VAS scope yet.

**Why manual coordination wins:** It is familiar, feels free, and lets customers escalate informally.

**Why we win:** ECC starts earlier in the booking workflow, uses shipment context, and creates measurable support ownership and SLA.

### Our Strengths

| # | Our Strength | Evidence / Proof Point |
|---|--------------|------------------------|
| 1 | Booking-native timing | Offer appears when shipment context and deadlines are active |
| 2 | Structured support workflow | Support case and first-action SLA can be measured |
| 3 | Clearer ownership | Confirmation can show support owner and next step |
| 4 | Repeatable service model | Can scale beyond individual email threads |

### Their Strengths vs. Us

| # | Their Strength | Our Response |
|---|----------------|--------------|
| 1 | Familiar and flexible | Acknowledge, then show where flexibility becomes tracking and ownership risk |
| 2 | No visible extra fee | Reframe around cost of delay, rework, and escalation |
| 3 | Works for edge cases | Keep manual escalation path for exceptions; use ECC for repeatable supported scenarios |

### Landmines to Plant

1. "How do you know who owns the next action after booking?"
2. "How often do clearance issues get discovered close to cutoff?"
3. "Can your team measure whether support started within 24 hours today?"

### Trap Questions and Redirects

| Trap Question | What It Implies | Response |
|---------------|-----------------|----------|
| "Isn't email faster?" | Informal escalation is enough | Email can be fast for one person, but it is hard to measure, hand off, or scale. ECC creates ownership from the booking. |
| "Why pay for something we already do?" | Current labor cost is ignored | Use ECC for shipments where delay risk and coordination cost are higher than the fee. |

### When to Walk Away

- Customer has low-volume, low-risk export bookings.
- Customer expects guaranteed customs release.
- Customer refuses to share required documents or shipment context.

---

## Battlecard 2: Export Customs Clearances vs. Customs Broker / Freight Forwarder Support

**Last Updated:** 2026-05-13  
**Owner:** Product / PMM  
**Usage:** Sales, account, CX, and operations teams

### Quick Summary

**Who chooses broker/forwarder support:** Customers who need formal customs filing, broad logistics management, or already have a trusted provider.

**Why they win:** They may own compliance execution, local expertise, and customer relationship across more logistics steps.

**Why we win:** ECC is embedded at booking time and can start carrier-side support with shipment context earlier than after-the-fact coordination.

### Our Strengths

| # | Our Strength | Evidence / Proof Point |
|---|--------------|------------------------|
| 1 | Native booking moment | Customer can request support while booking details are fresh |
| 2 | Carrier shipment context | Support starts from actual booking data, route, and cutoff context |
| 3 | Complementary support | Can clarify carrier-side actions without claiming to replace broker execution |
| 4 | Measurable SLA | First support action can be tracked and improved |

### Their Strengths vs. Us

| # | Their Strength | Our Response |
|---|----------------|--------------|
| 1 | Formal customs expertise | Acknowledge; ECC must define what is support vs. what remains broker or customer responsibility |
| 2 | Existing relationship trust | Use Alpha/Beta proof and account enablement to build trust gradually |
| 3 | Broader logistics ownership | Position ECC as booking-time carrier support, not a full logistics replacement |

### Landmines to Plant

1. "Does your current process start clearance support at the booking moment, or only after follow-up?"
2. "How do you track carrier-side next actions separately from broker-owned tasks?"
3. "What happens when booking data changes and clearance coordination has already started?"

### Trap Questions and Redirects

| Trap Question | What It Implies | Response |
|---------------|-----------------|----------|
| "Are you replacing my broker?" | Carrier is overstepping | No. ECC clarifies and starts carrier-side support from booking context; broker responsibilities remain explicit. |
| "Do you handle all countries and lanes?" | Coverage is universal or not useful | We only expose ECC where service and compliance support are ready. Controlled eligibility protects service quality. |

### When to Walk Away

- Customer requires full brokerage execution in unsupported jurisdictions.
- Forwarder sees ECC as channel conflict and will not engage unless partner model is clarified.
- Customer needs a custom enterprise contract before any pilot learning.

---

## Launch Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Service scope misunderstood | Medium | High | Include clear included/not included copy, legal review, and confirmation messaging |
| Operations cannot meet SLA | Medium | High | Limit Alpha/Beta eligibility, staff support team, monitor SLA dashboard |
| Low selection rate | Medium | Medium | Test risk-reduction messaging, scope clarity, and pricing |
| Forwarder channel conflict | Medium | Medium | Use partner-friendly positioning and summary; interview forwarders before GA |
| Pricing too high or low | Medium | High | Run 5+ pricing conversations and monitor selection/conversion |
| Compliance liability | Low/Medium | High | Lane-level eligibility controls and compliance review before exposure |

---

## PM to PO Handoff

The PM workflow is complete when these GTM assumptions are accepted as the starting point for requirements:

- Beachhead: supported Vietnam / Southeast Asia export lanes with digitally booked ocean exports.
- ICP: recurring export shippers and freight forwarders with visible clearance preparation risk.
- Primary product motion: booking-time VAS offer plus support workflow.
- Activation requirement: first carrier-side support action within 24 hours.
- Guardrails: booking abandonment, CSAT, SLA breach, compliance exceptions.
- Launch path: Alpha -> Beta -> GA, with controlled eligibility.

Recommended next artifact: `features/Export Customs Clearances/po/brief.md`, then PRD via `po-brief-to-prd`.

---

## Quality Checklist

- [x] ICP includes firmographic, behavioral, and situational attributes.
- [x] Negative ICP section included.
- [x] GTM motion selected and justified.
- [x] Launch plan has Alpha, Beta, and GA phases.
- [x] Exit criteria are written before each phase.
- [ ] Pricing validated with customer conversations.
- [x] Battlecards include competitor strengths and weaknesses.
- [ ] ICP validated against retained customer data.
