---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-003: ECC Support Records Table

**Component ID:** COMP-003  
**Wireframe:** WF-003 — Operations ECC Support Record  
**Stories:** ST-008, ST-009, ST-010  
**Acceptance Criteria:** ST-008 AC-001..AC-009; ST-009 AC-001..AC-008; ST-010 AC-001..AC-009  
**Component Type:** Table

---

## Overview

**Purpose:** Lets authorized operations users find and select ECC support records.  
**Context:** Operations workspace for ECC support handling.  
**User Interaction:** Search, filter, sort, paginate, and open support records.  
**Key Functionality:** Support record discovery, SLA visibility, empty/loading/error states, permission-protected access.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-003-EL-001 | Search Field | Input | default | default | type: search, placeholder: "Search booking/customer" | default, focus, disabled |
| COMP-003-EL-002 | Lane Filter | Select | default | default | options: supported lanes | default, open, focus, disabled |
| COMP-003-EL-003 | Status Filter | Select | default | default | options: Awaiting, In progress, Blocked, Unsupported | default, open, focus |
| COMP-003-EL-004 | SLA Filter | Select | default | default | options: On track, Due soon, Late | default, open, focus |
| COMP-003-EL-005 | Records Table | TanStack Table | — | compact | sortable, filterable | default, loading, empty, error |
| COMP-003-EL-006 | SLA Badge | Badge | secondary / destructive / outline | sm | by SLA value | default |
| COMP-003-EL-007 | View Action | Button | ghost | sm | type: button | default, hover, focus |
| COMP-003-EL-008 | Refresh Action | Button | outline | sm | type: button | default, hover, focus, loading |

---

## Data Table Configuration

**Table ID:** ecc-support-records-table  
**ShadCN + TanStack Table**

### Columns

| # | Column | Accessor | Sortable | Filterable | Cell Rendering |
|---|--------|----------|----------|------------|----------------|
| 1 | Booking | `bookingReference` | Yes | Yes | Plain text |
| 2 | Customer | `customerName` | Yes | Yes | Plain text |
| 3 | Lane | `lane` | Yes | Yes | Plain text |
| 4 | Status | `status` | Yes | Yes | Badge by status |
| 5 | SLA | `slaStatus` | Yes | Yes | Badge by on track / due soon / late |
| 6 | Cutoff | `cutoffAt` | Yes | No | Formatted date/time |
| 7 | Actions | — | No | No | Button: View |

### Table Settings

| Setting | Value |
|---------|-------|
| Pagination | Enabled, 10 rows default, options 10/25/50 |
| Default Sort | `slaDueAt` ASC |
| Multi-column Sort | Enabled |
| Global Search | Enabled, debounced 300 ms |
| Column Filters | Lane, Status, SLA |
| Row Selection | Single selection |

### States

| State | Behavior |
|-------|----------|
| Empty | Show "No ECC support records found" and clear filters action. |
| Loading | Show skeleton rows matching visible columns. |
| Error | Show error alert with retry action. |
| Unauthorized | Show access denied alert instead of table data. |

---

## Layout Structure

**Container:** Left panel of operations workspace.  
**Layout System:** Stack filters over TanStack table.  
**Spacing:** gap-3 controls; compact table row height.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Table left, detail panel right. |
| Tablet (640px-1024px) | Table full width; detail appears below selected row. |
| Mobile (< 640px) | Table becomes card list; detail opens as Sheet. |

---

## States

| State | Description |
|-------|-------------|
| Default | Records loaded with filters available. |
| Loading | Skeleton rows displayed. |
| Empty | No records match filters. |
| Error | Records cannot be loaded. |
| Unauthorized | User lacks operational access. |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | Search and filters have labels. |
| Keyboard Nav | Table rows and view actions are keyboard reachable. |
| Focus Management | Selecting View moves focus to support detail heading. |
| Screen Reader | SLA and status badges include text labels. |
| Touch Targets | Row actions meet 44x44px on mobile. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| Table density | Compact rows with readable spacing |
| Status | Semantic Badge variants |
| Typography | `text-sm` cells, Fira Code for booking refs |
| Borders | `border-border`, `rounded-md` container |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| Support records table | COMP-003-EL-005 | ST-008 AC-001..AC-004 | Identify and open support records |
| SLA badge | COMP-003-EL-006 | ST-009 AC-004, AC-006 | SLA visibility |
| Filters/search | COMP-003-EL-001..004 | ST-008 AC-001, ST-010 AC-007 | Operational discovery |
| Unauthorized state | COMP-003-EL-005 | ST-008 AC-009 | Access protection |
| Empty state | COMP-003-EL-005 | ST-012 AC-004 | No matching data pattern |

**Coverage:**
- [x] All table elements mapped.
- [x] Table configuration complete.
- [x] Relevant ACs addressed.
