---
artifact: USL
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: po-usm-to-usl
upstream: usm.md
downstream: usd/
---

# User Story List

**PRD:** PRD-001 - Export Customs Clearances  
**USM:** USM-001  
**Last Updated:** 2026-05-13

---

## Summary

| Priority | Count | Story Points |
|----------|-------|--------------|
| Must-have | 6 | 31 |
| Should-have | 4 | 19 |
| Could-have | 1 | 3 |
| Won't-have | 1 | 2 |
| **Total** | **12** | **55** |

---

## Stories by Module

### Eligibility

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-001](#st-001-evaluate-ecc-eligibility) | Evaluate ECC eligibility | Must-have | Draft | 5 |
| [ST-002](#st-002-communicate-service-availability) | Communicate service availability | Must-have | Draft | 3 |

### Service Scope

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-003](#st-003-explain-service-scope) | Explain service scope | Must-have | Draft | 5 |
| [ST-004](#st-004-explain-post-selection-next-steps) | Explain post-selection next steps | Should-have | Draft | 3 |

### Booking VAS Selection

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-005](#st-005-select-ecc-for-booking) | Select ECC for booking | Must-have | Draft | 5 |
| [ST-006](#st-006-complete-booking-with-or-without-ecc) | Complete booking with or without ECC | Must-have | Draft | 5 |

### Support Workflow

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-007](#st-007-confirm-ecc-request-to-customer) | Confirm ECC request to customer | Should-have | Draft | 3 |
| [ST-008](#st-008-create-support-record-from-booking) | Create support record from booking | Must-have | Draft | 8 |
| [ST-009](#st-009-record-first-support-action) | Record first support action | Should-have | Draft | 5 |
| [ST-010](#st-010-manage-blocked-or-unsupported-support) | Manage blocked or unsupported support | Should-have | Draft | 8 |

### Customer Feedback

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-011](#st-011-collect-post-support-feedback) | Collect post-support feedback | Could-have | Draft | 3 |

### Analytics

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-012](#st-012-track-ecc-performance-metrics) | Track ECC performance metrics | Won't-have | Draft | 2 |

---

## Story Details

### ST-001: Evaluate ECC eligibility

- **Activity:** ACT-001 / **Step:** STEP-001
- **Module:** Eligibility
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 5
- **Tags:** eligibility, alpha, compliance
- **Dependencies:** —
- **Jira:** —

> As a customer creating an export booking, I want my booking assessed for Export Customs Clearances availability, so that I only see the service when it can be supported.

### ST-002: Communicate service availability

- **Activity:** ACT-001 / **Step:** STEP-002
- **Module:** Eligibility
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 3
- **Tags:** eligibility, customer-communication
- **Dependencies:** ST-001
- **Jira:** —

> As a customer creating an export booking, I want to know whether Export Customs Clearances is available for my booking, so that I understand my support options without confusion.

### ST-003: Explain service scope

- **Activity:** ACT-002 / **Step:** STEP-003
- **Module:** Service Scope
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 5
- **Tags:** scope, compliance, trust
- **Dependencies:** ST-002
- **Jira:** —

> As a customer creating an export booking, I want to understand what Export Customs Clearances includes and excludes, so that I can decide whether the service fits my shipment needs.

### ST-004: Explain post-selection next steps

- **Activity:** ACT-002 / **Step:** STEP-004
- **Module:** Service Scope
- **Priority:** Should-have
- **Status:** Draft
- **Story Points:** 3
- **Tags:** scope, onboarding
- **Dependencies:** ST-003
- **Jira:** —

> As a customer creating an export booking, I want to understand what happens after I request Export Customs Clearances, so that I know what action to expect from the carrier and from my team.

### ST-005: Select ECC for booking

- **Activity:** ACT-003 / **Step:** STEP-005
- **Module:** Booking VAS Selection
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 5
- **Tags:** booking, selection, vas
- **Dependencies:** ST-002, ST-003
- **Jira:** —

> As a customer with an eligible export booking, I want to select or request Export Customs Clearances during booking, so that clearance support can start from the booking context.

### ST-006: Complete booking with or without ECC

- **Activity:** ACT-003 / **Step:** STEP-006
- **Module:** Booking VAS Selection
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 5
- **Tags:** booking, guardrail
- **Dependencies:** ST-005
- **Jira:** —

> As a customer creating an export booking, I want to complete my booking whether or not I select Export Customs Clearances, so that the support offer does not block shipment booking.

### ST-007: Confirm ECC request to customer

- **Activity:** ACT-004 / **Step:** STEP-007
- **Module:** Support Workflow
- **Priority:** Should-have
- **Status:** Draft
- **Story Points:** 3
- **Tags:** confirmation, support
- **Dependencies:** ST-005, ST-006
- **Jira:** —

> As a customer who requested Export Customs Clearances, I want confirmation of my request and next-step expectations, so that I know support is in motion.

### ST-008: Create support record from booking

- **Activity:** ACT-004 / **Step:** STEP-008
- **Module:** Support Workflow
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 8
- **Tags:** support, operations, booking-context
- **Dependencies:** ST-005
- **Jira:** —

> As a carrier operations specialist, I want a support record created from the booking context, so that I can start export clearance support without asking the customer to repeat core shipment details.

### ST-009: Record first support action

- **Activity:** ACT-005 / **Step:** STEP-009
- **Module:** Support Workflow
- **Priority:** Should-have
- **Status:** Draft
- **Story Points:** 5
- **Tags:** sla, operations, support
- **Dependencies:** ST-008
- **Jira:** —

> As a carrier operations specialist, I want to record the first carrier-side support action, so that the team can measure whether support started within 24 hours.

### ST-010: Manage blocked or unsupported support

- **Activity:** ACT-005 / **Step:** STEP-010
- **Module:** Support Workflow
- **Priority:** Should-have
- **Status:** Draft
- **Story Points:** 8
- **Tags:** exceptions, blocked-support
- **Dependencies:** ST-008
- **Jira:** —

> As a customer or operations specialist, I want blocked or unsupported ECC cases to show clear next steps, so that expectations stay accurate when support cannot proceed normally.

### ST-011: Collect post-support feedback

- **Activity:** ACT-006 / **Step:** STEP-011
- **Module:** Customer Feedback
- **Priority:** Could-have
- **Status:** Draft
- **Story Points:** 3
- **Tags:** feedback, csat
- **Dependencies:** ST-009
- **Jira:** —

> As a customer who received Export Customs Clearances support, I want to provide feedback after the service, so that the carrier can improve support quality and scope clarity.

### ST-012: Track ECC performance metrics

- **Activity:** ACT-006 / **Step:** STEP-012
- **Module:** Analytics
- **Priority:** Won't-have
- **Status:** Draft
- **Story Points:** 2
- **Tags:** analytics, reporting, future
- **Dependencies:** ST-001, ST-005, ST-008, ST-009, ST-011
- **Jira:** —

> As a product or operations manager, I want to track ECC adoption, SLA, booking guardrail, and satisfaction metrics, so that I can evaluate readiness for broader rollout.
