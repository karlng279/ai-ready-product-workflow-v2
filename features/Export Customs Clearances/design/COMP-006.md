---
artifact: COMP
feature: Export Customs Clearances
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---

# COMP-006: ECC Performance Metrics Dashboard

**Component ID:** COMP-006  
**Wireframe:** WF-004 — ECC Feedback And Metrics  
**Stories:** ST-012  
**Acceptance Criteria:** ST-012 AC-001..AC-008  
**Component Type:** Dashboard / Table

---

## Overview

**Purpose:** Provides a reporting surface or export view for ECC adoption, support SLA, guardrails, and feedback metrics.  
**Context:** Product and operations reporting area.  
**User Interaction:** Users review KPI cards, filter data, inspect metric rows, and export results.  
**Key Functionality:** Metric display, filtering, empty state, formula traceability, Won't-have scope note.

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|------------------|---------|------|-------|--------|
| COMP-006-EL-001 | KPI Card: Selection Rate | Card | default | compact | metric value, target | default, loading |
| COMP-006-EL-002 | KPI Card: SLA Rate | Card | default | compact | metric value, target | default, warning |
| COMP-006-EL-003 | KPI Card: CSAT | Card | default | compact | metric value, target | default, warning |
| COMP-006-EL-004 | Date Range Filter | Select | default | default | date range values | default, open, focus |
| COMP-006-EL-005 | Lane Filter | Select | default | default | supported lanes | default, open, focus |
| COMP-006-EL-006 | Segment Filter | Select | default | default | customer segments | default, open, focus |
| COMP-006-EL-007 | Export Action | Button | outline | default | type: button | default, hover, focus, disabled, loading |
| COMP-006-EL-008 | Metrics Table | TanStack Table | — | compact | sortable, filterable | default, loading, empty, error |
| COMP-006-EL-009 | Scope Note | Alert | default | — | Won't-have note | visible when out of release scope |

---

## Data Table Configuration

**Table ID:** ecc-performance-metrics-table  
**ShadCN + TanStack Table**

### Columns

| # | Column | Accessor | Sortable | Filterable | Cell Rendering |
|---|--------|----------|----------|------------|----------------|
| 1 | Metric | `metricName` | Yes | Yes | Plain text |
| 2 | Current | `currentValue` | Yes | No | Number or percent |
| 3 | Target | `targetValue` | Yes | No | Number or percent |
| 4 | Status | `status` | Yes | Yes | Badge: OK / Monitor / Act |
| 5 | Updated | `updatedAt` | Yes | No | Formatted date/time |

### Table Settings

| Setting | Value |
|---------|-------|
| Pagination | Enabled, 10 rows default |
| Default Sort | `metricName` ASC |
| Multi-column Sort | Disabled |
| Global Search | Enabled, debounced 300 ms |
| Column Filters | Status |
| Row Selection | None |

### States

| State | Behavior |
|-------|----------|
| Empty | Show "No ECC data found" with clear filters action. |
| Loading | Show KPI and table skeletons. |
| Error | Show error alert with retry action. |
| Out of scope | Show Won't-have scope note. |

---

## Layout Structure

**Container:** Dashboard panel with KPI row, filter toolbar, and metrics table.  
**Layout System:** Grid for KPI cards, stack for filters and table.  
**Spacing:** gap-4 KPI cards, gap-3 filters.

**Responsive Behavior:**

| Breakpoint | Behavior |
|------------|----------|
| Desktop (> 1024px) | Three or four KPI cards in one row; full table. |
| Tablet (640px-1024px) | KPI cards wrap two per row; table scrolls horizontally. |
| Mobile (< 640px) | KPI cards stack; table becomes metric cards. |

---

## States

| State | Description |
|-------|-------------|
| Default | Metrics loaded and filterable. |
| Loading | Skeletons visible. |
| Empty | No matching data. |
| Error | Metrics unavailable. |
| Out of scope | Story is excluded from first delivery slice unless pulled in. |

---

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA Labels | KPI cards have descriptive labels. |
| Keyboard Nav | Filters, export, and table rows are reachable. |
| Focus Management | Filter changes keep focus on changed control. |
| Screen Reader | Metric status badges include text, not color alone. |
| Touch Targets | Filters and export action meet 44x44px. |

---

## Design Rules Applied

| Token Type | Value |
|------------|-------|
| Theme | ERP / Dashboard |
| KPI typography | Fira Code for metric values |
| Status | Semantic Badge variants |
| Spacing | `gap-4`, `p-4` |
| Border radius | `rounded-md` |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|--------------|---------------------|-------|
| KPI cards | COMP-006-EL-001..003 | ST-012 AC-001, AC-002 | Required metrics |
| Filters | COMP-006-EL-004..006 | ST-012 AC-003 | Date/lane/segment |
| Empty state | COMP-006-EL-008 | ST-012 AC-004 | No matching data |
| Metric formulas | COMP-006-EL-008 | ST-012 AC-005..AC-007 | Formula display / validation |
| Scope note | COMP-006-EL-009 | ST-012 AC-008 | Won't-have release note |

**Coverage:**
- [x] All wireframe elements mapped.
- [x] Table configuration complete.
- [x] All ACs addressed.
