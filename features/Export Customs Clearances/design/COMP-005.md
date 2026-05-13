---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-005: Post-Support Feedback Form

**Component ID:** COMP-005  
**Wireframe:** WF-004 — ECC Feedback And Metrics  
**Stories:** ST-011  
**Acceptance Criteria:** ST-011 AC-001..AC-009  
**Component Type:** Form

---

## Overview

**Purpose:** Captures customer satisfaction, scope clarity, and optional feedback after ECC support.  
**Context:** Post-support completion or handoff experience.  
**User Interaction:** Customer selects scores, optionally enters comments, and submits feedback.  
**Key Functionality:** Numeric scores, optional free text, confirmation, duplicate prevention.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-005-EL-001 | Feedback Card | Card | default | — | role: form region | default, submitted |
| COMP-005-EL-002 | Satisfaction Score | RadioGroup | default | default | values: 1-5, required | default, selected, focus, error |
| COMP-005-EL-003 | Scope Clarity Score | RadioGroup | default | default | values: 1-5, required | default, selected, focus, error |
| COMP-005-EL-004 | Optional Comments | Textarea | default | default | required: false | default, focus, disabled |
| COMP-005-EL-005 | Skip Action | Button | outline | default | type: button | default, hover, focus |
| COMP-005-EL-006 | Submit Feedback | Button | default | default | type: submit | default, hover, focus, disabled, loading |
| COMP-005-EL-007 | Confirmation Message | Alert | default | — | role: status | hidden, visible |

---

## Layout Structure

**Container:** Compact card that can appear after support completion or handoff.  
**Layout System:** Vertical form stack.  
**Spacing:** gap-4 between score groups; footer actions right-aligned on desktop.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Score options horizontal; actions right aligned. |
| Tablet (640px-1024px) | Score options wrap; card full width. |
| Mobile (< 640px) | Score options stack in two rows; buttons full width. |

---

## Component Composition

```
Form
└── Card
    ├── CardHeader: "Post-support feedback"
    ├── CardContent
    │   ├── RadioGroup: satisfaction
    │   ├── RadioGroup: scope clarity
    │   └── Textarea: optional comments
    └── CardFooter
        ├── Button outline: "Skip"
        └── Button default: "Submit Feedback"
```

---

## States

| State | Description |
|-------|-------------|
| Default | Form ready for feedback. |
| Error | Required numeric score is missing. |
| Loading | Feedback submission in progress. |
| Success | Confirmation shown after submission. |
| Duplicate | Existing feedback prevents a second submission. |
| Disabled | Feedback no longer available. |

---

## Validation and Error Handling

| Field | Rule | Error Message | Timing |
|-------|------|---------------|--------|
| Satisfaction Score | Required | "Select a satisfaction score." | On submit |
| Scope Clarity Score | Required | "Select a scope clarity score." | On submit |
| Optional Comments | Not required | — | Never blocks submission |
| Duplicate Submission | One submission per contact per support case | "Feedback has already been submitted for this case." | On load or submit |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | Radio groups use fieldset/legend or equivalent labels. |
| Keyboard Nav | Arrow keys move between score options. |
| Focus Management | Success message receives polite announcement. |
| Screen Reader | Errors announced via aria-live polite. |
| Touch Targets | Radio options and buttons meet 44x44px. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| Primary action | `Button default` |
| Secondary action | `Button outline` |
| Spacing | `gap-4`, `p-4` |
| Typography | `text-sm` labels, `text-base` control labels |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| Satisfaction score | COMP-005-EL-002 | ST-011 AC-001 | Required numeric score |
| Scope clarity score | COMP-005-EL-003 | ST-011 AC-002 | Required numeric score |
| Comments | COMP-005-EL-004 | ST-011 AC-003, AC-006, AC-009 | Optional |
| Submit | COMP-005-EL-006 | ST-011 AC-004, AC-005, AC-007, AC-008 | Linked submission |
| Confirmation | COMP-005-EL-007 | ST-011 AC-005 | Submission feedback |

**Coverage:**
- [x] All wireframe elements mapped.
- [x] All ACs addressed.
- [x] Validation and duplicate states specified.
