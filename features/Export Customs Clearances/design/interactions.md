---
artifact: INT
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-interactions
upstream: design/COMP-001.md
downstream: —
---

# Export Customs Clearances Interaction Specifications

**Theme Reference:** ERP / Dashboard  
**Theme Animation Constraints:** Functional animations only; row highlights 150ms, button/state transitions 150-200ms, filter or panel expansion 300ms, reduced-motion mode uses instant state changes.

---

## INT-001: Booking ECC Selection Flow

**Interaction ID:** INT-001  
**Component IDs:** COMP-001, COMP-002  
**Wireframe IDs:** WF-001, WF-002  
**Story IDs:** ST-001, ST-002, ST-003, ST-004, ST-005, ST-006, ST-007  
**Acceptance Criteria IDs:** ST-001 AC-001..AC-007; ST-002 AC-001..AC-007; ST-003 AC-001..AC-008; ST-004 AC-001..AC-007; ST-005 AC-001..AC-008; ST-006 AC-001..AC-008; ST-007 AC-001..AC-007  
**Interaction Type:** Multi-Step Form Flow

### Purpose

Defines how customers move from booking eligibility evaluation to ECC selection, booking completion, and ECC confirmation.

### State Diagram

```
→ +------------------+
  | Evaluating       |
  +------------------+
          |
          | eligibility ready [eligible] /show offer
          v
  +------------------+   review scope    +------------------+
  | Offer Available  | ----------------> | Scope Review     |
  +------------------+                   +------------------+
          |                                      |
          | select ECC /attach request           | return
          v                                      v
  +------------------+   deselect        +------------------+
  | ECC Selected     | ----------------> | Offer Available  |
  +------------------+                   +------------------+
          |
          | complete booking /persist selection
          v
  +------------------+   valid request   +------------------+
  | Completing       | ----------------> | Confirmed        | ⊗
  +------------------+                   +------------------+
          |
          | selection error /show alert
          v
  +------------------+
  | Selection Error  |
  +------------------+
          |
          | continue without ECC
          v
  +------------------+
  | Booking Complete | ⊗
  +------------------+
```

### State Definitions

| State ID | State | Component State | UI Appearance | Available Actions |
|----------|-------|-----------------|---------------|-------------------|
| INT-001-ST-001 | Evaluating | COMP-001 loading | Booking continues while ECC decision resolves | Continue booking if no decision |
| INT-001-ST-002 | Offer Available | COMP-001 default | ECC offer, scope summary, optional selection | Review scope, select ECC, continue |
| INT-001-ST-003 | Scope Review | COMP-001 default | Included/excluded/next-step details visible | Return, select ECC |
| INT-001-ST-004 | ECC Selected | COMP-001 selected | ECC selected state visible | Deselect, complete booking |
| INT-001-ST-005 | Completing | COMP-001 loading | Booking completion in progress | None |
| INT-001-ST-006 | Confirmed | COMP-002 default | ECC requested confirmation and next steps | View next steps, back to bookings |
| INT-001-ST-007 | Selection Error | COMP-001 error | Error alert and continue path | Continue without ECC, retry if eligible |

### Transition Definitions

| From | To | Trigger | Condition | Action | Error Handling |
|------|----|---------|-----------|--------|----------------|
| Evaluating | Offer Available | Eligibility ready | Eligible | Show ECC offer | If ineligible, hide ECC and continue booking |
| Offer Available | Scope Review | Review scope | Scope available | Show approved scope content | Show unavailable details alert |
| Offer Available | ECC Selected | Select ECC | Booking remains eligible | Attach ECC to booking session | Show selection error |
| ECC Selected | Offer Available | Deselect ECC | Selection exists | Remove ECC from booking session | Keep booking usable |
| ECC Selected | Completing | Complete booking | Booking valid | Persist booking and ECC request | Preserve booking and show error if ECC fails |
| Completing | Confirmed | Booking success | Valid ECC request | Show ECC confirmation | Hide ECC confirmation if no valid request |
| Selection Error | Booking Complete | Continue without ECC | Booking valid | Complete booking without ECC | No ECC support case created |

### Edge Cases And Error Scenarios

- ECC becomes unavailable after display: disable selection and allow booking without ECC.
- Scope version missing: show service details unavailable and continue booking.
- Selection save fails: show destructive alert and preserve booking progress.
- Customer completes without ECC: no ECC confirmation is shown.

### Data Flow

- Input: booking direction, lane, customer/account, cutoff, operations readiness.
- Captured: eligibility decision, scope content version, selection state, selected timestamp, price/request mode when available.
- Output: completed booking with or without valid ECC request.

### Accessibility

- Focus remains in booking flow after selection state changes.
- Scope review is keyboard reachable.
- Error alerts use screen-reader announcements.
- Reduced motion removes animated section expansion.

### Traceability

| State/Transition | Acceptance Criteria | Notes |
|------------------|---------------------|-------|
| Evaluating → Offer Available | ST-001 AC-001..AC-006; ST-002 AC-001..AC-006 | Eligibility and availability |
| Scope Review | ST-003 AC-001..AC-008; ST-004 AC-001..AC-007 | Scope and next steps |
| Offer Available → ECC Selected | ST-005 AC-001..AC-007 | Select ECC |
| Selection Error | ST-005 AC-008 | Selection failure |
| Completing | ST-006 AC-001..AC-008 | Booking guardrail |
| Confirmed | ST-007 AC-001..AC-007 | Post-booking confirmation |

---

## INT-002: Operations Support Handling Flow

**Interaction ID:** INT-002  
**Component IDs:** COMP-003, COMP-004  
**Wireframe IDs:** WF-003  
**Story IDs:** ST-008, ST-009, ST-010  
**Acceptance Criteria IDs:** ST-008 AC-001..AC-009; ST-009 AC-001..AC-008; ST-010 AC-001..AC-009  
**Interaction Type:** Data Table + Operational Form Flow

### Purpose

Defines how operations users find ECC support records, record first support action, and handle blocked or unsupported cases.

### State Diagram

```
→ +------------------+
  | Records Loading  |
  +------------------+
          |
          | data ready [has records]
          v
  +------------------+   select record   +------------------+
  | Records Ready    | ----------------> | Detail Open      |
  +------------------+                   +------------------+
          |                                      |
          | no records                           | record first action [valid]
          v                                      v
  +------------------+                   +------------------+
  | Empty Records    |                   | First Action     |
  +------------------+                   | Recorded         |
                                             +--------------+
                                                    |
                                                    | mark blocked [reason]
                                                    v
                                             +------------------+
                                             | Blocked          |
                                             +------------------+
                                                    |
                                                    | mark unsupported
                                                    v
                                             +------------------+
                                             | Unsupported      |
                                             +------------------+
```

### State Definitions

| State ID | State | Component State | UI Appearance | Available Actions |
|----------|-------|-----------------|---------------|-------------------|
| INT-002-ST-001 | Records Loading | COMP-003 loading | Skeleton rows | None |
| INT-002-ST-002 | Records Ready | COMP-003 default | Filterable support table | Search, filter, select |
| INT-002-ST-003 | Empty Records | COMP-003 empty | Empty state and clear filters | Clear filters |
| INT-002-ST-004 | Detail Open | COMP-004 default | Booking context and action forms | Record action, mark blocked |
| INT-002-ST-005 | First Action Recorded | COMP-004 first action recorded | Timestamp and SLA state shown | Mark blocked if needed |
| INT-002-ST-006 | Blocked | COMP-004 blocked | Blocked reason and customer next step | Update reason |
| INT-002-ST-007 | Unsupported | COMP-004 unsupported | Unsupported alert | Review/audit |

### Transition Definitions

| From | To | Trigger | Condition | Action | Error Handling |
|------|----|---------|-----------|--------|----------------|
| Records Loading | Records Ready | Data loaded | Records exist | Render table | Show error alert if load fails |
| Records Loading | Empty Records | Data loaded | No records | Show empty state | Clear filters available |
| Records Ready | Detail Open | Select record | Authorized user | Load record detail | Access denied if unauthorized |
| Detail Open | First Action Recorded | Save first action | Action type selected | Save timestamp and SLA status | Show validation error |
| Detail Open | Blocked | Mark blocked | Reason selected | Save blocked reason and next step | Show validation error |
| Detail Open | Unsupported | Mark unsupported | Unsupported reason selected | Save unsupported status | Use compliance-safe copy |

### Edge Cases And Error Scenarios

- Unauthorized user: table/detail data is replaced with access denied alert.
- Duplicate support record: only one active record can be opened for a booking.
- Missing action type: first action cannot save.
- Missing blocked reason: blocked status cannot save.
- Unsupported message must not imply customs clearance is impossible.

### Data Flow

- Input: support records from ECC booking requests.
- Captured: action type, action timestamp, blocked reason, customer next step, unsupported reason.
- Output: support record state, SLA status, audit references.

### Accessibility

- Table controls have labels.
- Selecting a record moves focus to detail heading.
- Mobile detail Sheet traps focus.
- Status badges include text labels, not color alone.

### Traceability

| State/Transition | Acceptance Criteria | Notes |
|------------------|---------------------|-------|
| Records Ready | ST-008 AC-001..AC-004 | Record discovery and context |
| Detail Open | ST-008 AC-007..AC-009 | Metadata and access |
| First Action Recorded | ST-009 AC-001..AC-008 | First action and SLA |
| Blocked | ST-010 AC-001..AC-005, AC-007 | Blocked support |
| Unsupported | ST-010 AC-006, AC-008, AC-009 | Unsupported handling |

---

## INT-003: Feedback And Metrics Flow

**Interaction ID:** INT-003  
**Component IDs:** COMP-005, COMP-006  
**Wireframe IDs:** WF-004  
**Story IDs:** ST-011, ST-012  
**Acceptance Criteria IDs:** ST-011 AC-001..AC-009; ST-012 AC-001..AC-008  
**Interaction Type:** Form Flow + Dashboard Flow

### Purpose

Defines post-support feedback submission and reporting interactions for measuring ECC service quality and adoption.

### State Diagram

```
→ +------------------+
  | Feedback Ready   |
  +------------------+
          |
          | submit [scores present]
          v
  +------------------+   success   +------------------+
  | Submitting       | ----------> | Submitted        | ⊗
  +------------------+             +------------------+
          |
          | validation fails
          v
  +------------------+
  | Feedback Error   |
  +------------------+

→ +------------------+  filters changed  +------------------+
  | Metrics Loaded   | ----------------> | Metrics Loading  |
  +------------------+                   +------------------+
          ^                                      |
          | data ready [has data]                | data ready [empty]
          +--------------------------------------+
                                                 v
                                          +------------------+
                                          | Metrics Empty    |
                                          +------------------+
```

### State Definitions

| State ID | State | Component State | UI Appearance | Available Actions |
|----------|-------|-----------------|---------------|-------------------|
| INT-003-ST-001 | Feedback Ready | COMP-005 default | Score controls and optional comments | Submit, skip |
| INT-003-ST-002 | Submitting | COMP-005 loading | Submit button loading | None |
| INT-003-ST-003 | Submitted | COMP-005 success | Confirmation message | None |
| INT-003-ST-004 | Feedback Error | COMP-005 error | Required field or duplicate error | Fix, submit |
| INT-003-ST-005 | Metrics Loaded | COMP-006 default | KPI cards and table | Filter, export |
| INT-003-ST-006 | Metrics Loading | COMP-006 loading | Skeleton cards/table | None |
| INT-003-ST-007 | Metrics Empty | COMP-006 empty | No data message | Clear filters |

### Transition Definitions

| From | To | Trigger | Condition | Action | Error Handling |
|------|----|---------|-----------|--------|----------------|
| Feedback Ready | Submitting | Submit feedback | Scores present | Save feedback | Missing scores show error |
| Submitting | Submitted | Save success | First submission | Show confirmation | Duplicate shows error |
| Feedback Ready | Submitted | Skip | Optional feedback skipped | Dismiss form | Numeric scores not saved |
| Metrics Loaded | Metrics Loading | Filter changes | Filters valid | Reload metrics | Keep prior state if reload fails |
| Metrics Loading | Metrics Loaded | Data ready | Data exists | Render metrics | — |
| Metrics Loading | Metrics Empty | Data ready | No matching data | Show empty state | Clear filters |

### Edge Cases And Error Scenarios

- Free text is empty: scores still submit.
- Duplicate submission: error shown and second record is not accepted.
- No matching metrics: empty state appears instead of blank table.
- ST-012 remains Won't-have: out-of-scope note appears if metrics dashboard is not pulled into delivery.

### Data Flow

- Feedback input: satisfaction score, scope clarity score, optional comment, booking ID, customer ID, support case ID.
- Metrics input: offer views, selections, booking completions, support records, first actions, completions, feedback.
- Metrics output: selection rate, SLA rate, booking abandonment guardrail, CSAT, scope clarity.

### Accessibility

- Radio groups have labelled score semantics.
- Feedback errors are announced via polite live region.
- Metric status is text plus badge, not color alone.
- Filter changes preserve focus.

### Traceability

| State/Transition | Acceptance Criteria | Notes |
|------------------|---------------------|-------|
| Feedback Ready | ST-011 AC-001..AC-004, AC-006, AC-009 | Feedback input |
| Submitted | ST-011 AC-005, AC-007, AC-008 | Confirmation and traceability |
| Metrics Loaded | ST-012 AC-001..AC-003, AC-005..AC-007 | Dashboard and formulas |
| Metrics Empty | ST-012 AC-004 | Empty state |
| Out-of-scope note | ST-012 AC-008 | Won't-have handling |

---

## Interaction Quality Checklist

- [x] Interaction IDs assigned.
- [x] Component and wireframe IDs referenced.
- [x] ASCII state diagrams provided.
- [x] States and transitions documented.
- [x] Edge cases and error scenarios included.
- [x] Accessibility and reduced motion considered.
- [x] AC traceability included.
