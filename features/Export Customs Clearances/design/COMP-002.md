---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-002: ECC Booking Confirmation

**Component ID:** COMP-002  
**Wireframe:** WF-002 — ECC Booking Confirmation  
**Stories:** ST-007  
**Acceptance Criteria:** ST-007 AC-001..AC-007  
**Component Type:** Card

---

## Overview

**Purpose:** Confirms ECC is requested and sets support expectations after booking completion.  
**Context:** Booking completion screen for bookings completed with valid ECC request.  
**User Interaction:** Customer reviews status, support timing, booking reference, and next steps.  
**Key Functionality:** Confirmation visibility, service reference display, next-step access.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-002-EL-001 | Confirmation Card | Card | default | — | role: status | default, hidden |
| COMP-002-EL-002 | ECC Status Badge | Badge | secondary | default | label: ECC Requested | default |
| COMP-002-EL-003 | SLA Badge | Badge | outline | default | label: Within 24 hours | default |
| COMP-002-EL-004 | Booking Reference Card | Card | default | compact | booking reference fields | default |
| COMP-002-EL-005 | Customer-Owned Notice | Alert | default | — | advisory copy | default |
| COMP-002-EL-006 | View Next Steps | Button | outline | default | type: button | default, hover, focus |
| COMP-002-EL-007 | Back To Bookings | Button | default | default | type: button | default, hover, focus |

---

## Layout Structure

**Container:** Confirmation content area below completed booking header.  
**Layout System:** Desktop two-column grid; stacked cards on smaller screens.  
**Spacing:** gap-4 cards, p-4 compact card body.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Main confirmation card left; reference cards right. |
| Tablet (640px-1024px) | Cards stack with reference below confirmation. |
| Mobile (< 640px) | Single-column cards; actions full width. |

---

## Component Composition

```
Card
├── CardHeader
│   ├── Badge: "ECC Requested"
│   └── CardTitle: "Export Customs Clearances is attached"
├── CardContent
│   ├── SLA Badge
│   ├── Next steps list
│   └── Customer-owned information Alert
└── CardFooter
    ├── Button outline: "View Next Steps"
    └── Button default: "Back to Bookings"
```

---

## States

| State | Description |
|-------|-------------|
| Default | Booking completed with valid ECC request. |
| Hidden | Booking completed without ECC. |
| Loading | Confirmation reference is loading. |
| Error | ECC confirmation cannot load; booking confirmation still remains visible. |

---

## Validation and Error Handling

| Field | Rule | Error Message | Timing |
|-------|------|---------------|--------|
| ECC Confirmation | Requires valid ECC request on completed booking | "ECC request details are temporarily unavailable." | On confirmation render |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | Confirmation card uses role status and descriptive heading. |
| Keyboard Nav | Next steps and back actions are keyboard reachable. |
| Focus Management | Focus lands on booking completion heading after completion. |
| Screen Reader | ECC requested status announced once. |
| Touch Targets | Buttons meet 44x44px minimum. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| Status | Badge variants use semantic info/success tokens |
| Spacing | `gap-4`, `p-4` |
| Typography | `text-lg font-semibold` card title; `text-sm` metadata |
| Border radius | `rounded-md` |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| ECC requested card | COMP-002-EL-001, COMP-002-EL-002 | ST-007 AC-001, AC-003, AC-005 | Visible only for valid ECC |
| First action target | COMP-002-EL-003 | ST-007 AC-002 | 24-hour expectation |
| Booking reference | COMP-002-EL-004 | ST-007 AC-006 | Booking and service references |
| Customer-owned notice | COMP-002-EL-005 | ST-007 AC-007 | Responsibility clarity |
| Next steps action | COMP-002-EL-006 | ST-007 AC-004 | Opens next-step details |

**Coverage:**
- [x] All wireframe elements mapped.
- [x] All ACs addressed.
- [x] No orphaned elements.
