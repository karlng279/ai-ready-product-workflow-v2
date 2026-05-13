---
artifact: PRD
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: po-brief-to-prd
upstream: brief.md
downstream: usm.md
---

# PRD: Export Customs Clearances
id: PRD-001
version: 0.1
owner: Product Team
status: draft
last_updated: 2026-05-13

---

## 1. Summary

Export Customs Clearances lets eligible export booking customers request carrier-side export clearance support at booking time. The feature helps export shippers and freight forwarders understand service scope, request support without disrupting booking completion, and receive timely first action so clearance preparation starts before shipment deadlines become urgent.

---

## 2. Problem Statement

### 2.1 Pain Points

- Export customers often discover missing clearance information close to documentation or cargo cutoff.
- Customers coordinate clearance support through disconnected email, phone, broker, forwarder, and internal workflows.
- Customers do not always know whether the carrier, broker, forwarder, or internal team owns the next action after booking.
- Freight forwarders need earlier carrier-side visibility so they can protect customer schedules without manual escalation.
- Customers may avoid paid support when service scope, responsibility boundaries, or next steps are unclear.

### 2.2 Opportunities

- Offer export clearance support at the booking moment, when shipment context and deadline risk are already known.
- Create a repeatable VAS path that can increase service adoption while protecting booking conversion.
- Establish a measurable support workflow for first action, support completion, customer satisfaction, and repeat selection.

---

## 3. Goals & Non-Goals

### 3.1 Business Goals

- Increase booking-time ECC selection/request rate from 0% to 8% of eligible exposed bookings by 2026-08-31.
- Ensure 85% of selected/requested ECC services receive first carrier-side support action within 24 hours by 2026-08-31.
- Maintain post-support CSAT at or above 4.2/5 during Alpha and Beta.
- Keep booking abandonment after ECC offer exposure from increasing by more than 2 percentage points.
- Establish a 90-day repeat selection baseline and target 25% repeat selection among customers with another eligible booking after launch maturity.

### 3.2 User Goals

- Know whether Export Customs Clearances is available for the current export booking.
- Understand what the service includes, what it excludes, and what happens after selection.
- Select or request ECC during booking without losing progress or slowing booking completion.
- Receive confirmation that support has started or will start, including owner and next-step expectations.
- Provide feedback after support to improve future service quality.

### 3.3 Non-Goals

- Build a full customs brokerage marketplace.
- Guarantee customs clearance or regulatory approval outcomes.
- Roll out ECC to all countries, all lanes, or all export bookings.
- Fully automate customs filing.
- Replace freight forwarders, customs brokers, or customer-owned compliance responsibilities.

---

## 4. Narrative / Use Cases

An export operations coordinator creates an ocean export booking in a supported lane. The booking is evaluated for ECC eligibility, and when eligible, the customer sees that export clearance support is available for the shipment. The customer reviews what is included, what is excluded, and what happens next before deciding whether to request the service.

A freight forwarder managing a customer booking sees ECC during booking for a shipment with clearance preparation risk. They review the service scope to confirm it complements their role, select the service, and complete the booking without losing progress. After booking confirmation, they receive confirmation that ECC has been attached and that carrier-side support will begin.

An operations team receives a support case created from booking context after ECC is selected. The team performs the first support action within 24 hours, records the action, and communicates the next step or missing customer-owned information. If the lane or booking is not supportable, ECC is not offered or the customer receives a clear unavailable state.

After support is completed or handed off, the customer receives a feedback request. Their feedback captures satisfaction and scope clarity, helping the team monitor whether the service delivered value and whether repeat selection is likely.

---

## 5. Scope & Constraints

### 5.1 In Scope

- Evaluate ECC eligibility using lane, customer, booking, and operations-readiness signals.
- Show ECC availability only for eligible export bookings.
- Explain ECC service scope, exclusions, and next steps.
- Allow eligible customers to select or request ECC during booking.
- Preserve booking completion even if the customer does not select ECC.
- Confirm ECC selection/request after booking completion.
- Create a support case from booking context after ECC is selected/requested.
- Track first carrier-side support action against a 24-hour target.
- Capture support completion or formal handoff before cutoff when applicable.
- Capture post-support CSAT and scope clarity feedback.
- Instrument key analytics events for exposure, selection, completion, support workflow, and feedback.

### 5.2 Out of Scope

- Public GA pricing page.
- Automated customs declaration filing.
- Broker marketplace selection or matching.
- Unsupported lane request handling beyond clear unavailability or exclusion.
- Enterprise custom contract workflow.
- Detailed operational SOP content beyond product requirements.

### 5.3 Constraints & Assumptions

- ECC can only be offered where lane, compliance, and operations readiness are approved.
- Service language must avoid promises of guaranteed clearance, guaranteed speed, or replacement of broker responsibilities.
- Alpha launch is limited to selected ICP customers in supported lanes.
- Pricing is not final and must remain configurable or controlled during Alpha/Beta.
- Existing booking, support, and analytics systems must provide stable identifiers for booking, customer, lane, and support case.
- Support team capacity may limit exposure volume during Alpha and Beta.

---

## 6. Success Metrics

- metric_id: MET-001
  description: ECC selection/request rate among eligible exposed bookings.
  target: Increase from 0% to 8% by 2026-08-31.
- metric_id: MET-002
  description: Selected/requested ECC services with first support action within 24 hours.
  target: At least 85% by 2026-08-31.
- metric_id: MET-003
  description: Booking abandonment change after ECC offer exposure.
  target: No more than +2 percentage points during Alpha/Beta.
- metric_id: MET-004
  description: Post-support customer satisfaction.
  target: At least 4.2/5 during Alpha/Beta.
- metric_id: MET-005
  description: Scope clarity positive response rate after support.
  target: At least 80% positive during Alpha/Beta.
- metric_id: MET-006
  description: 90-day repeat selection among customers with another eligible booking.
  target: Establish baseline during Beta; target 25% after launch maturity.

---

## 7. Links

- design_figma: N/A
- wireframe_text: N/A
- special_notes: ../pm/gtm.md

---

## 8. Technical Considerations

The feature depends on the digital booking flow, an eligibility decision point, a way to attach ECC selection/request to the booking, support case creation from booking context, and analytics instrumentation. Implementation should preserve core booking completion and avoid exposing ECC where compliance or operations support is unavailable. Support workflow events need stable identifiers so booking, support, feedback, and repeat-selection analytics can be joined.

---

## 9. Risks & Open Questions

### 9.1 Risks

- id: RISK-001
  description: Customers misunderstand ECC as guaranteed customs clearance.
  mitigation: Use clear included, excluded, and next-step language; require compliance review before Alpha.
- id: RISK-002
  description: Operations cannot meet the 24-hour first-action target at pilot volume.
  mitigation: Limit eligibility and exposure during Alpha/Beta; monitor SLA dashboard and pause exposure if SLA drops below threshold.
- id: RISK-003
  description: ECC offer increases booking abandonment.
  mitigation: Keep selection low-friction, allow customers to continue without ECC, and monitor abandonment guardrail.
- id: RISK-004
  description: Freight forwarders perceive ECC as channel conflict.
  mitigation: Position ECC as carrier-side support that complements broker and forwarder responsibilities.

### 9.2 Open Questions

- id: Q-001
  description: Which lanes are approved for Alpha eligibility?
  owner: Product / Operations / Compliance
- id: Q-002
  description: What price or request model should be shown during Alpha?
  owner: Product / Commercial
- id: Q-003
  description: Which system owns support case creation and first-action tracking?
  owner: Product / Engineering / Operations
- id: Q-004
  description: What support scope language is approved by compliance and legal?
  owner: Product / Compliance / Legal
