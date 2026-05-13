---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-004: ECC Support Record Detail

**Component ID:** COMP-004  
**Wireframe:** WF-003 — Operations ECC Support Record  
**Stories:** ST-008, ST-009, ST-010  
**Acceptance Criteria:** ST-008 AC-002..AC-009; ST-009 AC-001..AC-008; ST-010 AC-001..AC-009  
**Component Type:** Form / Card

---

## Overview

**Purpose:** Displays selected ECC support record context and lets operations record first action or blocked/unsupported status.  
**Context:** Right-side detail panel in operations workspace; mobile Sheet.  
**User Interaction:** Operations reviews booking context, records first action, or marks case blocked/unsupported.  
**Key Functionality:** Booking context display, action type selection, SLA status, blocked reason handling, customer next-step message.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-004-EL-001 | Record Detail Card | Card | default | — | selected support record | default, loading, empty |
| COMP-004-EL-002 | Status Badge | Badge | secondary / destructive / outline | sm | by support status | default |
| COMP-004-EL-003 | Booking Context List | CardContent | — | compact | key-value pairs | default |
| COMP-004-EL-004 | Action Type | Select | default | default | required: true | default, open, error, disabled |
| COMP-004-EL-005 | Action Notes | Textarea | default | default | optional notes | default, focus, disabled |
| COMP-004-EL-006 | Record First Action | Button | default | default | disabled until action type selected | default, hover, focus, disabled, loading |
| COMP-004-EL-007 | Blocked Reason | Select | default | default | required when blocked | default, open, error |
| COMP-004-EL-008 | Customer Next Step | Textarea | default | default | required for customer-facing block | default, focus, error |
| COMP-004-EL-009 | Mark Blocked | Button | outline | default | disabled until reason valid | default, hover, focus, disabled, loading |
| COMP-004-EL-010 | Unsupported Alert | Alert | destructive | — | compliance-safe copy | hidden, visible |

---

## Layout Structure

**Container:** Detail card or Sheet with sections for context, first action, blocked/unsupported.  
**Layout System:** Vertical stack.  
**Spacing:** gap-4 between sections; compact key-value rows.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Fixed right detail panel next to records table. |
| Tablet (640px-1024px) | Detail panel appears below selected record. |
| Mobile (< 640px) | Full-screen Sheet with sticky action footer. |

---

## Component Composition

```
Card / Sheet
├── Header: Booking reference + status badge
├── Booking Context
├── First Support Action Form
│   ├── Select: action type
│   ├── Textarea: notes
│   └── Button: record first action
└── Blocked / Unsupported Form
    ├── Select: blocked reason
    ├── Textarea: customer next step
    ├── Alert: unsupported copy
    └── Button: mark blocked
```

---

## States

| State | Description |
|-------|-------------|
| Empty | No support record selected. |
| Default | Record selected and awaiting action. |
| First Action Recorded | Timestamp and SLA result visible. |
| Blocked | Blocked reason and customer next step visible. |
| Unsupported | Unsupported service message visible. |
| Error | Save failed; retry message visible. |
| Unauthorized | Detail hidden behind access denied state. |

---

## Validation and Error Handling

| Field | Rule | Error Message | Timing |
|-------|------|---------------|--------|
| Action Type | Required for first support action | "Select an action type before recording first action." | On submit |
| Blocked Reason | Required when marking blocked | "Select a blocked reason." | On submit |
| Customer Next Step | Required when customer-facing blocked message is needed | "Describe the next action for the customer." | On submit |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | All selects and textareas have labels. |
| Keyboard Nav | Forms follow top-to-bottom tab order. |
| Focus Management | Mobile Sheet traps focus and returns to selected row on close. |
| Screen Reader | Save errors announced via aria-live polite. |
| Touch Targets | Buttons and select triggers meet 44x44px. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| Status | Semantic Badge and Alert variants |
| Spacing | `gap-4`, `p-4` |
| Typography | Fira Code for references, Fira Sans for labels |
| Border radius | `rounded-md` |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| Record context | COMP-004-EL-001..003 | ST-008 AC-002, AC-004, AC-007, AC-008 | Booking context display |
| First action form | COMP-004-EL-004..006 | ST-009 AC-001..AC-007 | Action and SLA recording |
| Blocked controls | COMP-004-EL-007..009 | ST-010 AC-001..AC-008 | Blocked status and reason |
| Unsupported alert | COMP-004-EL-010 | ST-010 AC-006, AC-009 | Compliance-safe unsupported copy |
| Access control | COMP-004-EL-001 | ST-008 AC-009 | Permission protected |

**Coverage:**
- [x] All detail elements mapped.
- [x] Form validation specified.
- [x] All relevant ACs addressed.
