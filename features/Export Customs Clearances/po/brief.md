---
artifact: BRIEF
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: pm-to-po-handoff
upstream: ../pm/gtm.md
downstream: prd.md
---

# Feature Brief: Export Customs Clearances

**Feature:** Export Customs Clearances  
**Owner:** Product Team  
**Status:** draft  
**Last Updated:** 2026-05-13

---

## 1. Summary

Export Customs Clearances is a booking-time value-added service for eligible ocean export bookings. It allows export shippers and freight forwarders to request carrier-side clearance support during booking so that support starts earlier, scope is clearer, and clearance-related uncertainty is reduced before documentation or cargo cutoff risk becomes urgent.

---

## 2. Problem Statement

Export customers often coordinate export clearance through disconnected email, phone, broker, forwarder, and internal operations workflows. They may not know what is missing until shipment deadlines are close, and they may not have clear ownership of the next action after booking. This creates late rework, escalation, customer anxiety, and shipment delay risk.

---

## 3. Target Users And Segments

- Export Operations Coordinators at manufacturing exporters who create recurring ocean export bookings.
- Freight Forwarder Customer Service Leads who manage multiple exporter bookings and need earlier visibility into clearance risk.
- Logistics Managers or Operations Leads who influence shipment-level VAS adoption and account-level service usage.

Initial beachhead: Vietnam / Southeast Asia export customers using digital carrier booking for supported lanes with recurring clearance coordination pain.

---

## 4. Business Goals

- Increase booking-time Export Customs Clearances selection/request rate from 0% to 8% of eligible exposed bookings by 2026-08-31.
- Ensure 85% of selected/requested services receive first carrier-side support action within 24 hours by 2026-08-31.
- Maintain post-support CSAT at or above 4.2/5 during Alpha and Beta.
- Keep booking abandonment after ECC offer exposure from increasing by more than 2 percentage points.
- Establish baseline for 90-day repeat selection and target 25% among repeat eligible customers after launch maturity.

---

## 5. User Goals

- Understand whether Export Customs Clearances is available for the current booking.
- Understand what the service includes, what it excludes, and what happens after selection.
- Select or request ECC without disrupting booking completion.
- Receive confirmation that support has started and know the next action owner.
- Provide feedback after support to help improve future service quality.

---

## 6. Launch Scope

### In Scope

- Eligibility control by lane, customer, booking attributes, and operations readiness.
- Booking-time ECC offer for eligible export bookings.
- Service scope explanation with included, excluded, and next-step information.
- ECC selection/request during booking.
- Booking confirmation that includes ECC status and next steps.
- Support case creation from booking context.
- First support action tracking against a 24-hour target.
- Post-support feedback capture.
- Analytics instrumentation for offer exposure, selection, booking completion, support case creation, first support action, support completion, and feedback.

### Out Of Scope

- Full customs brokerage marketplace.
- Guaranteed customs clearance outcome.
- All-country or all-lane rollout.
- Full automation of customs filing.
- Replacing freight forwarders, brokers, or customer-owned compliance responsibilities.

---

## 7. Constraints And Assumptions

- ECC must only appear where compliance, lane, and operations support are ready.
- Service wording must avoid unsupported claims such as "guaranteed clearance" or "fastest clearance".
- Alpha starts with selected ICP customers and supported lanes before Beta or GA.
- Pricing remains hypothesis-based until at least 5 customer pricing conversations are completed.
- Customer interviews and production instrumentation are not complete yet; validation gaps remain open.
- Existing digital booking, support case, and analytics capabilities must be available or extended.

---

## 8. Source PM Artifacts

- Strategy: `../pm/strategy.md`
- Discovery: `../pm/discovery.md`
- Market Research: `../pm/market-research.md`
- Analytics: `../pm/analytics.md`
- Growth: `../pm/growth.md`
- Go-To-Market: `../pm/gtm.md`

---

## 9. Open Questions

- Which exact origin/destination lanes are approved for Alpha eligibility?
- What is the final Alpha service scope after compliance and legal review?
- What support team owns first action and escalation for each pilot lane?
- What pricing, if any, should be shown during Alpha?
- Which existing systems will own support case creation and status updates?
