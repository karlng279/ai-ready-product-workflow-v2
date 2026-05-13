---
artifact: OST
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-product-discovery
upstream: strategy.md
downstream: po/prd.md
---

# Export Customs Clearances Product Discovery

**Product / Team:** Export Customs Clearances  
**Quarter:** Q3 2026  
**Owner:** Product Team  
**Last Updated:** 2026-05-13

---

## Discovery Context

This artifact starts the discovery cycle for the Export Customs Clearances value-added service. The strategy hypothesis is that customers creating export bookings will buy carrier-side clearance support when it helps them reduce documentation friction, cutoff risk, and operational uncertainty.

No customer interviews have been completed yet in this discovery cycle. Opportunity evidence below is therefore marked as **hypothesis-based** until at least 5 qualified customer interviews are completed.

---

## Desired Outcome

> Increase booking-time adoption of Export Customs Clearances among eligible export bookings from 0% to 8% by 2026-08-31.

**Metric:** Eligible export booking attach rate  
**Baseline:** 0%  
**Target:** 8%  
**Deadline:** 2026-08-31

---

## Jobs-to-be-Done

**Main Job:** When I create an export booking, I need to make sure customs clearance can be completed correctly and on time so my cargo is not delayed before departure.

**Micro Jobs:**
1. Understand whether my shipment needs export clearance support.
2. Know what documents, data, and actions are required.
3. Coordinate with the right party before cutoff risk becomes urgent.
4. Track whether clearance support has started and what is still pending.

**Emotional Job:** Feel in control of a process that is often time-sensitive, regulated, and hard to recover from when something goes wrong.

**Social Job:** Be seen by customers, internal teams, and partners as reliable, proactive, and operationally competent.

---

## Opportunity Space

### Opportunity 1: "I do not know what clearance support I need until the shipment is already under time pressure."

**Evidence:** Hypothesis-based; to validate through customer interviews with export shippers and freight forwarders.

**Customer impact:** High

**Business impact:** High

**Sub-opportunities:**
- Customers do not know whether their booking is eligible for carrier-side export clearance support.
- Customers do not understand the operational consequences of starting clearance preparation late.
- Customers need service recommendations that are specific to origin, destination, cargo, schedule, and customer profile.

### Opportunity 2: "I spend too much time coordinating documents and status through disconnected email or phone threads."

**Evidence:** Hypothesis-based; aligned with the strategy's substitute analysis around email, phone, spreadsheets, and manual process.

**Customer impact:** High

**Business impact:** Medium

**Sub-opportunities:**
- Customers do not have one place to see what is needed for export clearance preparation.
- Operations teams receive incomplete or inconsistent information after booking.
- Customers cannot easily tell whether support has started, stalled, or requires action from them.

### Opportunity 3: "I am not sure the carrier's paid support will be faster or better than my current broker or internal process."

**Evidence:** Hypothesis-based; must validate through interviews and pricing/offer experiments.

**Customer impact:** Medium

**Business impact:** High

**Sub-opportunities:**
- Customers need a clear promise about what the carrier will do after purchase.
- Customers need trust signals, such as SLA, support scope, and escalation path.
- Customers need pricing that feels justified relative to delay risk and manual effort.

### Opportunity 4: "I need export clearance help only for certain shipments, not every booking."

**Evidence:** Hypothesis-based; likely because clearance complexity varies by trade lane, customer capability, cargo type, and urgency.

**Customer impact:** Medium

**Business impact:** Medium

**Sub-opportunities:**
- Customers need the offer to appear only when relevant.
- The business needs eligibility rules to avoid overselling support where it is not operationally ready.
- Operations teams need manageable volume while the service is being validated.

---

## Opportunity Prioritization

Scores use 1-5 where 5 is highest. Evidence strength remains weak until interviews are completed.

| Opportunity | Reach | Frequency | Intensity | Strategic Fit | Total | Evidence Strength | Priority |
|-------------|-------|-----------|-----------|---------------|-------|-------------------|----------|
| Opportunity 1: Unclear need before time pressure | 4 | 4 | 5 | 5 | 18 | Weak | High |
| Opportunity 2: Disconnected document/status coordination | 4 | 4 | 4 | 4 | 16 | Weak | High |
| Opportunity 3: Unclear value vs broker/internal process | 3 | 3 | 4 | 5 | 15 | Weak | Medium |
| Opportunity 4: Support needed only for certain shipments | 3 | 3 | 3 | 4 | 13 | Weak | Medium |

**Chosen opportunity this quarter:** Opportunity 1, because booking-time uncertainty is the earliest moment where the carrier can intervene and directly influence attach rate, support start time, and downstream clearance confidence.

---

## Solution Space

### Solution A: Booking-Time Clearance Recommendation

**Description:** Show an eligible Export Customs Clearances VAS offer during booking with concise service scope, expected benefit, and next-step explanation.

**How it addresses the opportunity:** It helps customers understand that clearance support is available before they reach operational time pressure.

**Riskiest assumption:** Customers recognize the need and select the service when the offer appears inside booking.

**Estimated effort:** M

### Solution B: Clearance Readiness Checklist

**Description:** Provide a structured checklist after booking that shows required documents, data, owner, status, and deadline for export clearance preparation.

**How it addresses the opportunity:** It makes the required work visible and reduces ambiguity after the customer buys or requests support.

**Riskiest assumption:** Customers will complete or upload required information when the checklist is presented digitally.

**Estimated effort:** M

### Solution C: Concierge Clearance Support Pilot

**Description:** Offer the service in selected lanes and route purchased requests to an operations team that manually coordinates support while tracking SLA and outcomes.

**How it addresses the opportunity:** It validates whether customers value carrier-side support before building full automation.

**Riskiest assumption:** Operations can deliver the promised support quickly enough to create visible value.

**Estimated effort:** S

### Solution D: Risk-Based Offer Targeting

**Description:** Use booking attributes to show the VAS offer only when shipment characteristics suggest higher clearance friction or urgency.

**How it addresses the opportunity:** It avoids generic upsell fatigue and improves relevance.

**Riskiest assumption:** We have enough reliable booking data to infer clearance-support relevance.

**Estimated effort:** L

---

## Solution Selection

**Chosen solution:** Solution A plus Solution C as a discovery pilot.

**Rationale:** A booking-time recommendation directly tests demand at the moment of booking, while a concierge pilot lets the team deliver support manually before investing in deeper workflow automation. This combination gives faster desirability and viability evidence than building the full checklist or risk-targeting engine first.

---

## Experiments

### Experiment 1: Fake Door Offer in Booking

**Assumption being tested:** Customers will show intent to buy Export Customs Clearances when it is offered during eligible export booking creation.

**Hypothesis:** We believe eligible export booking customers experience enough clearance uncertainty to request support during booking. If we show a clear VAS offer in the booking flow, then at least 8% of eligible customers will click or select the service within 4 weeks.

**Test type:** Fake door

**Test description:** Display the Export Customs Clearances service option for selected eligible export bookings. If selected, collect intent and route the customer to a "support team will contact you" confirmation rather than a fully automated paid flow.

**Success criteria:** At least 8% selection rate among eligible exposed bookings, with no material increase in booking abandonment.

**Result:** Pending

### Experiment 2: Concierge Fulfillment Pilot

**Assumption being tested:** Operations can start export clearance support within 24 hours for customers who request the service.

**Hypothesis:** We believe carrier-side operations can deliver visible support quickly enough to create customer value. If selected requests are handled through a concierge workflow, then 85% of requests will receive first support action within 24 hours over a 4-week pilot.

**Test type:** Concierge

**Test description:** For selected requests, an operations specialist contacts the customer, verifies required shipment information, explains next steps, and logs support start time, missing information, and outcome.

**Success criteria:** 85% of purchased or requested services receive first action within 24 hours, and at least 70% of customers rate the support as helpful.

**Result:** Pending

### Experiment 3: Value Message A/B Test

**Assumption being tested:** Customers respond more strongly to delay-risk reduction than to convenience messaging.

**Hypothesis:** We believe customers buy this service to reduce operational risk more than to save administrative time. If we compare risk-reduction messaging against convenience messaging, then the risk-reduction variant will produce at least 20% higher selection intent over 4 weeks.

**Test type:** A/B test

**Test description:** Test two offer messages in the booking flow for eligible shipments: one focused on avoiding clearance delays and one focused on easier document coordination.

**Success criteria:** One message produces at least 20% higher selection rate without increasing booking abandonment.

**Result:** Pending

---

## Assumption Map

### Desirability Assumptions

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|------------|------------------|---------------|-------------|----------|
| D1 | Customers experience export clearance uncertainty frequently enough to consider paid support. | Strategy hypothesis; no interviews yet. | High | High | Test |
| D2 | Customers will select the service during booking rather than waiting for a problem later. | No behavioral evidence yet. | High | High | Test |
| D3 | Customers understand the value proposition from a short booking-flow offer. | No usability evidence yet. | Medium | High | Test |
| D4 | Freight forwarders and direct shippers both see value in carrier-side support. | Segment hypothesis only. | Medium | High | Test |

### Usability Assumptions

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|------------|------------------|---------------|-------------|----------|
| U1 | Customers can understand what is included in Export Customs Clearances without reading a long policy page. | No prototype test yet. | High | High | Test |
| U2 | Customers can distinguish this VAS from standard booking, documentation, and customs broker responsibilities. | No prototype test yet. | High | High | Test |
| U3 | Customers know what happens after selecting the service. | No prototype test yet. | Medium | High | Test |

### Feasibility Assumptions

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|------------|------------------|---------------|-------------|----------|
| F1 | Booking data can support basic eligibility rules for the pilot. | Booking flow likely has origin, destination, cargo, and schedule data. | High | Medium | Test |
| F2 | Operations can receive and act on requests within 24 hours. | No pilot data yet. | High | High | Test |
| F3 | Compliance boundaries can be defined clearly by lane and support model. | Needs legal/compliance review. | High | High | Test |

### Viability Assumptions

| # | Assumption | Evidence we have | Risk if wrong | Uncertainty | Priority |
|---|------------|------------------|---------------|-------------|----------|
| V1 | The service can generate incremental VAS revenue without excessive manual cost. | No pricing or effort data yet. | High | High | Test |
| V2 | Offering this service does not create unacceptable liability or customer expectation risk. | Needs compliance and service-scope review. | High | High | Test |
| V3 | Commercial teams can position this as an optional value-added service rather than a confusing booking surcharge. | No sales feedback yet. | Medium | Medium | Monitor |

### Prioritization Matrix

```
High Risk  | D1, D2, U1, U2, F2, F3, V1, V2 | F1
           | Test ASAP                         | Monitor closely
           |
Low Risk   | D3, D4, U3                        | V3
           | Test in prototype/interviews       | Monitor
           +-----------------------------------+----------------
             High Uncertainty                   Lower Uncertainty
```

---

## Riskiest Assumption Test Plan

**Riskiest assumption:** Customers will select export clearance support during booking when the service is clearly offered.

**Why it's riskiest:** If customers do not show intent at booking time, the product's core strategic position as a booking-native VAS is weak.

**Experiment to test it:** Fake Door Offer in Booking

**Hypothesis:** We believe customers have enough export clearance uncertainty during booking to request support. If eligible users see a concise VAS offer, then at least 8% will select it within 4 weeks.

**Test method:** Fake door

**Minimum success criteria:** 8% selection rate among exposed eligible bookings, booking abandonment does not increase materially, and at least 5 customers agree to follow-up interviews.

**Result:** Pending

**Next riskiest assumption to test:** Operations can start support within 24 hours and deliver a customer-visible benefit through a concierge workflow.

---

## Customer Interview Guide

**Interview Purpose:** Discovery and opportunity mining  
**Target Participant Profile:** Export shippers, freight forwarders, and customer operations users who have created or managed ocean export bookings in the last 90 days.  
**Interview Duration:** 45-60 minutes  
**Interviewer:** Product Team

### Screener

Qualified participants should meet at least three of these criteria:
- Created or managed at least one export booking in the last 90 days.
- Was responsible for export customs documentation, coordination, or escalation.
- Experienced shipment delay risk, documentation rework, or clearance uncertainty.
- Uses a freight forwarder, customs broker, internal operations team, or manual process today.
- Has authority or influence over purchasing VAS, brokerage, or operational support services.

### Hypothesis to Explore

Customers face meaningful export clearance uncertainty during or immediately after booking, and the booking moment is early enough to offer support before operational risk escalates.

### Top 3 Questions We Must Answer

1. What triggers customers to seek export clearance help, and when does that happen relative to booking?
2. What makes the current clearance coordination process slow, risky, or frustrating?
3. What would make customers trust a carrier-provided clearance support service?

### Interview Script

#### Warm-Up

"Thanks for taking the time today. I am here to learn from your actual export booking and clearance experience, not to pitch a solution. There are no right or wrong answers. Is it okay if I take notes for our research?"

"Can you tell me about your role and how you are involved in export bookings?"

#### Context Setting - The Job

"Walk me through the last time you created or managed an export booking that required customs clearance coordination. What triggered it?"

Follow-up prompts:
- "What were you doing before the booking was created?"
- "Walk me through the process step by step."
- "Who else was involved?"
- "What tools, documents, emails, or systems did you use?"
- "At what point did you know clearance support or documentation work was needed?"

#### Pain and Friction Discovery

"What was the hardest part of getting export clearance ready for that shipment?"

Follow-up prompts:
- "Where did the process slow down?"
- "What information was missing, unclear, or duplicated?"
- "Was there a point where the shipment felt at risk?"
- "What did you try that did not work?"
- "How did you know the issue was resolved?"

#### Switching Story

"Have you changed how you handle export clearance coordination recently?"

Follow-up prompts:
- "What made you change?"
- "What did you use before?"
- "What made you choose the current broker, forwarder, internal process, or workaround?"
- "Was there anything that almost stopped you from switching?"

#### Desired Outcome and Gains

"If this process were perfect, what would be different the next time you create an export booking?"

Follow-up prompts:
- "What would success look like before cargo cutoff?"
- "What would you want to know immediately after booking?"
- "What would make you feel confident that clearance is on track?"
- "What would make you trust carrier-side support?"

#### Wrap-Up

"Is there anything important I did not ask about export clearance that I should understand?"

"Who else should we talk to who has a different perspective on this process?"

---

## OST Summary Diagram

```
Desired Outcome: Eligible export booking attach rate from 0% to 8% by 2026-08-31
|
+-- Opportunity 1: I do not know what clearance support I need until the shipment is already under time pressure. <-- CHOSEN
|   +-- Sub-opportunity: Customers do not know whether their booking is eligible.
|   +-- Sub-opportunity: Customers do not understand late-clearance consequences.
|   +-- Sub-opportunity: Customers need shipment-specific service recommendations.
|       +-- Solution A: Booking-Time Clearance Recommendation <-- CHOSEN
|       |   +-- Experiment 1: Fake Door Offer in Booking <-- RUNNING NEXT
|       +-- Solution B: Clearance Readiness Checklist
|       +-- Solution C: Concierge Clearance Support Pilot <-- CHOSEN
|       |   +-- Experiment 2: Concierge Fulfillment Pilot
|       +-- Solution D: Risk-Based Offer Targeting
|
+-- Opportunity 2: I spend too much time coordinating documents and status through disconnected email or phone threads.
|
+-- Opportunity 3: I am not sure the carrier's paid support will be faster or better than my current broker or internal process.
|
+-- Opportunity 4: I need export clearance help only for certain shipments, not every booking.
```

---

## Discovery Plan

1. Interview at least 5 qualified customers before finalizing the opportunity priority.
2. Run the fake door booking offer for selected eligible export bookings.
3. Run a concierge fulfillment pilot for customers who express intent.
4. Review compliance and service-scope boundaries before converting intent into paid purchase.
5. Update this OST weekly with interview evidence, experiment results, and opportunity priority changes.

---

## Quality Checklist

- [x] Desired outcome is a specific metric.
- [x] Opportunities are customer needs, not features.
- [x] Each selected solution is paired with an experiment before building.
- [x] Assumption map identifies at least 3 riskiest assumptions.
- [x] Interview guide uses JTBD questions and avoids leading solution validation.
- [x] OST shows the selected opportunity and rationale.
- [ ] At least 5 customer interviews completed.
