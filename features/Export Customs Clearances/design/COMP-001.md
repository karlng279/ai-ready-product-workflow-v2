---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-001: Booking ECC Offer Panel

**Component ID:** COMP-001  
**Wireframe:** WF-001 — Booking ECC Offer  
**Stories:** ST-001, ST-002, ST-003, ST-004, ST-005, ST-006  
**Acceptance Criteria:** ST-001 AC-001..AC-007; ST-002 AC-001..AC-007; ST-003 AC-001..AC-008; ST-004 AC-001..AC-007; ST-005 AC-001..AC-008; ST-006 AC-001..AC-008  
**Component Type:** Card / Form

---

## Overview

**Purpose:** Shows ECC availability, scope summary, next steps, and selection controls inside the booking service step.  
**Context:** Appears only for eligible export bookings in the booking flow.  
**User Interaction:** Customer reviews scope and selects, deselects, or skips ECC.  
**Key Functionality:** Eligibility-controlled visibility, optional VAS selection, safe unavailable state, booking guardrail.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-001-EL-001 | ECC Offer Container | Card | default | — | role: region | default, loading, hidden |
| COMP-001-EL-002 | Availability Badge | Badge | secondary | default | label: Available / Unavailable | default, warning |
| COMP-001-EL-003 | Included List | CardContent | — | — | content list | default |
| COMP-001-EL-004 | Excluded List | Alert | default | — | compliance-safe copy | default |
| COMP-001-EL-005 | Next Steps Summary | CardContent | — | — | includes 24-hour target | default |
| COMP-001-EL-006 | ECC Selection | Checkbox | default | default | checked, disabled | unchecked, checked, disabled, focus |
| COMP-001-EL-007 | Review Scope Action | Button | outline | default | type: button | default, hover, focus, disabled |
| COMP-001-EL-008 | Select ECC Action | Button | default | default | type: button | default, hover, focus, disabled, loading |
| COMP-001-EL-009 | Continue Booking Action | Button | default | default | type: button | default, hover, focus, loading |
| COMP-001-EL-010 | Selection Failure Message | Alert | destructive | — | role: alert | hidden, visible |

---

## Layout Structure

**Container:** Right-side card in desktop booking services layout.  
**Layout System:** Vertical stack with section separators.  
**Spacing:** ERP compact spacing: gap-3 between rows, gap-4 between sections, p-4 card padding.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Two-column booking layout; offer panel sits beside booking summary. |
| Tablet (640px-1024px) | Offer panel stacks below booking summary. |
| Mobile (< 640px) | Offer panel full-width; included/excluded/next-step sections collapse. |

---

## Component Composition

```
Card
├── CardHeader
│   ├── CardTitle: "Export Customs Clearances"
│   └── Badge: availability
├── CardContent
│   ├── Service summary
│   ├── Included list
│   ├── Excluded Alert
│   ├── Next steps summary
│   └── Checkbox: request ECC
└── CardFooter
    ├── Button outline: "Review Scope"
    └── Button default: "Select ECC"
```

---

## States

| State | Description |
|-------|-------------|
| Default | ECC is eligible and unselected. |
| Selected | ECC is selected and visibly attached to booking session. |
| Hidden | ECC is not eligible and no purchase/request control appears. |
| Loading | Eligibility or selection state is being resolved. |
| Error | Selection fails and customer can continue booking without ECC. |
| Disabled | ECC becomes unavailable after initial display. |

---

## Validation and Error Handling

| Field | Rule | Error Message | Timing |
|-------|------|---------------|--------|
| ECC Selection | Booking must remain eligible | "Export Customs Clearances is no longer available for this booking." | On select and before booking completion |
| Scope Content | Approved content version must exist | "Service details are unavailable. You can continue booking without this service." | On render |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | ECC card uses region label; checkbox has explicit label. |
| Keyboard Nav | Review, selection, and booking actions are reachable in logical order. |
| Focus Management | Focus remains in booking flow after selection or deselection. |
| Screen Reader | Selection failure alert uses role alert. |
| Touch Targets | Buttons and checkbox row meet 44x44px target. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| Primary | `bg-primary`, `text-primary-foreground` |
| Warning | `bg-warning`, `text-warning-foreground` for unsupported states |
| Spacing | `gap-3`, `gap-4`, `p-4` |
| Typography | Fira Sans body, Fira Code for compact status labels |
| Border radius | `rounded-md` |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| ECC offer card | COMP-001-EL-001 | ST-001 AC-001, ST-002 AC-001 | Eligibility-controlled display |
| Availability badge | COMP-001-EL-002 | ST-002 AC-001, AC-002, AC-005, AC-006 | Available/unavailable state |
| Scope sections | COMP-001-EL-003, COMP-001-EL-004 | ST-003 AC-001..AC-007 | Included/excluded/responsibilities |
| Next steps | COMP-001-EL-005 | ST-004 AC-001, AC-002, AC-006 | 24-hour target |
| Selection controls | COMP-001-EL-006, COMP-001-EL-008 | ST-005 AC-001..AC-007 | Select/deselect |
| Continue booking | COMP-001-EL-009 | ST-006 AC-001..AC-008 | Booking guardrail |
| Error alert | COMP-001-EL-010 | ST-005 AC-008 | Continue without ECC |

**Coverage:**
- [x] All wireframe elements mapped.
- [x] All UI-facing ACs addressed.
- [x] No orphaned elements.
