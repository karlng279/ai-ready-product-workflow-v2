---
artifact: WF
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-wireframe
upstream: po/usd/
downstream: design/COMP-001.md
---

# Export Customs Clearances Wireframes

**Theme Reference:** ERP / Dashboard  
**Design System:** Data-dense operational workflow, Fira Code / Fira Sans, compact cards, clear status badges, WCAG AA, no decorative gradients or unsupported clearance claims.

---

## WF-001: Booking ECC Offer

**Stories:** ST-001, ST-002, ST-003, ST-004, ST-005, ST-006  
**Addresses:** ST-001 AC-001..AC-007; ST-002 AC-001..AC-007; ST-003 AC-001..AC-008; ST-004 AC-001..AC-007; ST-005 AC-001..AC-008; ST-006 AC-001..AC-008

### Purpose

Shows the optional Export Customs Clearances offer inside an eligible export booking flow. The customer can understand availability, included/excluded scope, next steps, and select or skip the service without blocking booking completion.

### Layout Structure

**Desktop (> 1024px):**
- Header: Booking title, progress, booking reference.
- Main: Two-column layout with booking summary on the left and ECC offer panel on the right.
- Footer: Previous, continue booking, and complete booking actions.

**Tablet (640px-1024px):**
- Booking summary and ECC offer stack vertically.
- Action footer remains sticky at bottom.

**Mobile (< 640px):**
- Single-column layout.
- ECC scope details collapse behind expandable sections.
- Actions become full-width stacked buttons.

### ASCII Wireframe

```
+------------------------------------------------------------------------------+
| {Logo} Export Booking                                    Booking Ref: BK-... |
+------------------------------------------------------------------------------+
| Step 3 of 4: Services                                                        |
|                                                                              |
| +--------------------------------------+  +--------------------------------+ |
| | Booking Summary                      |  | Export Customs Clearances      | |
| | Origin: VNHPH                        |  | [Badge] Available              | |
| | Destination: USLAX                   |  |                                | |
| | Cutoff: 2026-08-18 16:00             |  | Reduce clearance delay risk    | |
| | Customer: ...                        |  | by starting support at booking.| |
| |                                      |  |                                | |
| | Standard services                    |  | Included                       | |
| | (☑) Ocean booking                    |  | - Carrier-side support start   | |
| | (☐) Other VAS                        |  | - Scope guidance               | |
| +--------------------------------------+  | - First action target: 24h     | |
|                                           |                                | |
|                                           | Not included                   | |
|                                           | - Guaranteed customs release   | |
|                                           | - Full broker replacement      | |
|                                           |                                | |
|                                           | What happens next              | |
|                                           | Support case created after     | |
|                                           | booking completion.            | |
|                                           |                                | |
|                                           | (☐) Request ECC for booking    | |
|                                           | [Review Scope] [Select ECC]    | |
|                                           +--------------------------------+ |
|                                                                              |
| [Previous]                                           [Continue] [Complete]   |
+------------------------------------------------------------------------------+
```

### Interactions

1. Eligibility evaluates during booking service step.
2. Customer opens `[Review Scope]` to inspect included, excluded, and responsibility details.
3. Customer selects ECC → checkbox selected and ECC attached to booking session.
4. Customer deselects ECC → ECC removed from booking session.
5. Customer completes booking with or without ECC.
6. If ECC becomes unavailable, the offer is removed and booking continues.

### Components Required

- ShadCN Card: booking summary and ECC offer panel
- ShadCN Badge: availability and warning states
- ShadCN Checkbox: ECC request selection
- ShadCN Button: review scope, select, previous, continue, complete
- ShadCN Alert: unsupported or selection failure states
- ShadCN Separator: panel sections
- ShadCN Collapsible or Accordion: mobile service scope

### AC Mapping

| AC | Addressed By |
|----|--------------|
| ST-001 AC-001..AC-006 | Eligibility-controlled ECC offer visibility and hidden state |
| ST-001 AC-007 | No guaranteed-clearance language in offer |
| ST-002 AC-001..AC-007 | Availability badge, optional language, continue path |
| ST-003 AC-001..AC-008 | Included/excluded scope, no guarantee, accessible details |
| ST-004 AC-001..AC-007 | Next-step summary and 24-hour target |
| ST-005 AC-001..AC-008 | Select/deselect ECC and failure state |
| ST-006 AC-001..AC-008 | Complete booking with or without ECC |

---

## WF-002: ECC Booking Confirmation

**Stories:** ST-007  
**Addresses:** ST-007 AC-001..AC-007

### Purpose

Confirms that ECC was requested after booking completion and explains next support expectations without asking the customer to repeat booking details.

### Layout Structure

**Desktop (> 1024px):**
- Header: Booking completed status.
- Main: Confirmation card with ECC status and next steps.
- Side panel: booking reference and support expectation summary.

**Tablet (640px-1024px):**
- Confirmation and reference panels stack.

**Mobile (< 640px):**
- Single-column card layout with full-width actions.

### ASCII Wireframe

```
+------------------------------------------------------------------------------+
| {Logo} Booking Complete                                      [View Booking]  |
+------------------------------------------------------------------------------+
|                                                                              |
| +------------------------------------------------+ +-----------------------+ |
| | [Badge] ECC Requested                          | | Booking Reference     | |
| | Export Customs Clearances is attached to       | | BK-2026-...           | |
| | this booking.                                  | | Lane: VNHPH -> USLAX  | |
| |                                                | | Cutoff: ...           | |
| | First support action target                    | +-----------------------+ |
| | [Badge] Within 24 hours                        |                         |
| |                                                | +-----------------------+ |
| | What happens next                              | | Customer-owned items  | |
| | - Carrier support record will be created       | | May still be needed   | |
| | - Operations may request missing information   | | after first review.   | |
| | - Broker/customer responsibilities remain      | +-----------------------+ |
| |                                                |                         |
| | [View Next Steps] [Back to Bookings]           |                         |
| +------------------------------------------------+                         |
|                                                                              |
+------------------------------------------------------------------------------+
```

### Interactions

1. Customer completes booking with ECC → confirmation appears.
2. Customer opens `[View Next Steps]` → next-step content is shown.
3. Booking without ECC does not show ECC confirmation.

### Components Required

- ShadCN Card
- ShadCN Badge
- ShadCN Button
- ShadCN Alert
- ShadCN Separator

### AC Mapping

| AC | Addressed By |
|----|--------------|
| ST-007 AC-001 | ECC requested badge and message |
| ST-007 AC-002 | First support action target section |
| ST-007 AC-003 | Confirmation after booking completion |
| ST-007 AC-004 | View Next Steps action |
| ST-007 AC-005 | Hidden state when no valid ECC request |
| ST-007 AC-006 | Booking and service reference panels |
| ST-007 AC-007 | Customer-owned information notice |

---

## WF-003: Operations ECC Support Record

**Stories:** ST-008, ST-009, ST-010  
**Addresses:** ST-008 AC-001..AC-009; ST-009 AC-001..AC-008; ST-010 AC-001..AC-009

### Purpose

Allows authorized operations users to identify ECC support records, inspect booking context, record first support actions, and handle blocked or unsupported cases.

### Layout Structure

**Desktop (> 1024px):**
- Header: Operations workspace and filters.
- Main: Support table on left, selected support record details on right.
- Detail area: action recording, SLA status, blocked controls.

**Tablet (640px-1024px):**
- Support table full-width; record detail opens below selected row.

**Mobile (< 640px):**
- Support table becomes card list; record details open as full-screen sheet.

### ASCII Wireframe

```
+------------------------------------------------------------------------------+
| ECC Operations                                      [Refresh] [Export]        |
+------------------------------------------------------------------------------+
| [🔍] <Search booking/customer_____> [Lane ▼] [Status ▼] [SLA ▼]              |
|                                                                              |
| +---------------------------------------------+ +--------------------------+ |
| | Support Records                             | | Support Record           | |
| | (☐) | Booking ↕ | Customer ↕ | SLA ↕ | ... | | BK-2026-...              | |
| |-----|-----------|------------|-------|-----| | Customer: ...            | |
| | ( ) | BK-001    | ACME       | 22h   |[View]| Lane: VNHPH -> USLAX     | |
| | ( ) | BK-002    | Beta       | Late  |[View]| Cutoff: 2026-08-18       | |
| | ( ) | BK-003    | Delta      | 8h    |[View]|                          | |
| +---------------------------------------------+ | [Badge] Awaiting action   | |
|                                                 | SLA due: 2026-...         | |
| Empty: No ECC support records found             |                          | |
|                                                 | First support action      | |
|                                                 | [Action Type ▼]           | |
|                                                 | <Notes________________>   | |
|                                                 | [Record First Action]     | |
|                                                 |                          | |
|                                                 | Blocked / Unsupported     | |
|                                                 | [Reason ▼]                | |
|                                                 | <Customer next step_____> |
|                                                 | [Mark Blocked]            | |
|                                                 +--------------------------+ |
+------------------------------------------------------------------------------+
```

### Interactions

1. Operations filters support records by lane, status, SLA, or search.
2. Operations selects a record → details load.
3. Operations records first support action with action type.
4. System displays whether action was within 24 hours.
5. Operations marks blocked/unsupported with approved reason and next-step message.
6. Unauthorized users cannot view support record data.

### Components Required

- TanStack Table with ShadCN table primitives
- ShadCN Input
- ShadCN Select
- ShadCN Button
- ShadCN Badge
- ShadCN Card
- ShadCN Textarea
- ShadCN Alert
- ShadCN Skeleton
- ShadCN Sheet for mobile detail

### AC Mapping

| AC | Addressed By |
|----|--------------|
| ST-008 AC-001..AC-004 | Support table and detail panel |
| ST-008 AC-005 | Creation failure flagged state |
| ST-008 AC-006..AC-008 | Record detail metadata and SLA due |
| ST-008 AC-009 | Authorized operations workspace |
| ST-009 AC-001..AC-008 | First action form, SLA status, blocked path |
| ST-010 AC-001..AC-009 | Blocked reason controls and customer next-step message |

---

## WF-004: ECC Feedback And Metrics

**Stories:** ST-011, ST-012  
**Addresses:** ST-011 AC-001..AC-009; ST-012 AC-001..AC-008

### Purpose

Captures post-support customer feedback and provides a reporting surface for product and operations teams to monitor ECC adoption, SLA, guardrails, and satisfaction.

### Layout Structure

**Desktop (> 1024px):**
- Feedback form is a compact card.
- Metrics dashboard uses KPI cards and a data table with filters.

**Tablet (640px-1024px):**
- KPI cards wrap two per row.
- Tables keep horizontal scroll.

**Mobile (< 640px):**
- Feedback fields stack.
- Metrics table becomes card list.

### ASCII Wireframe

```
+------------------------------------------------------------------------------+
| Export Customs Clearances                                      [Date Range ▼] |
+------------------------------------------------------------------------------+
|                                                                              |
| +----------------------------------+  +--------------------------------------+ |
| | Post-support feedback           |  | ECC Performance                      | |
| | Satisfaction                    |  | +----------+ +----------+ +---------+| |
| | ( ) 1 ( ) 2 ( ) 3 (•) 4 ( ) 5  |  | | Select % | | SLA %    | | CSAT   || |
| | Scope clarity                   |  | | 8.0%     | | 85%      | | 4.2/5  || |
| | ( ) 1 ( ) 2 ( ) 3 (•) 4 ( ) 5  |  | +----------+ +----------+ +---------+| |
| | Optional comments               |  |                                      | |
| | <Textarea_____________________> |  | [Lane ▼] [Segment ▼] [Export]       | |
| | [Skip] [Submit Feedback]        |  |                                      | |
| +----------------------------------+  | +----------------------------------+ | |
|                                     | | Metric ↕ | Current | Target | Status| |
| Empty metrics: No ECC data found    | | Select   | 8.0%    | 8.0%   |[OK]  | |
|                                     | | SLA      | 85%     | 85%    |[OK]  | |
|                                     | +----------------------------------+ | |
|                                     +--------------------------------------+ |
+------------------------------------------------------------------------------+
```

### Interactions

1. Customer submits numeric feedback with optional comments.
2. Customer skips optional free text and still submits scores.
3. Duplicate feedback is prevented.
4. Product/operations user filters metrics by date, lane, and segment.
5. Empty metrics state appears when no results match.

### Components Required

- ShadCN Card
- ShadCN RadioGroup
- ShadCN Textarea
- ShadCN Button
- ShadCN Select
- ShadCN Badge
- TanStack Table
- ShadCN Skeleton
- ShadCN Alert

### AC Mapping

| AC | Addressed By |
|----|--------------|
| ST-011 AC-001..AC-009 | Feedback form, score controls, confirmation, duplicate handling |
| ST-012 AC-001..AC-004 | Metrics dashboard, filters, empty state |
| ST-012 AC-005..AC-008 | Metric formulas and Won't-have scope note |

---

## Wireframe Quality Checklist

- [x] WF IDs assigned.
- [x] Story IDs referenced.
- [x] AC IDs mapped by story.
- [x] ASCII wireframes use standard symbols.
- [x] Desktop, tablet, and mobile behavior described.
- [x] Interactions listed.
- [x] ShadCN and TanStack components listed.
- [x] Empty, error, and unavailable states represented where required.
