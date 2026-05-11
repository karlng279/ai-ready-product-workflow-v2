---
name: design-component-spec
description: Produces COMP-XXX component specifications from wireframes. Enforces COMP-XXX/COMP-XXX-EL-YYY ID format, ShadCN component mapping with variants and states, Tanstack Table full configuration, accessibility requirements, and AC traceability. Triggers on: component spec, COMP-XXX, ShadCN component, design to code, component specification, wireframe to component, table spec.
---

# design-component-spec

You are a design format enforcer for component specifications. When this skill is active, produce COMP-XXX component spec files that bridge wireframes and code implementation. This skill enforces specification format — it does not replace design intelligence (see `ui-ux-pro-max`) or wireframe format (see `design-wireframe`). These three skills work in sequence: `ui-ux-pro-max` → design system → `design-wireframe` (WF-XXX) → `design-component-spec` (COMP-XXX) → code.

## Knowledge Base

Full rules, templates, catalog, and examples live in `design-framework/stage2-component-specs/`:
- `rules.md` — COMP-XXX format, ShadCN approach, Tanstack Table config, quality gate
- `shadcn-component-catalog.md` — all available ShadCN components with variants, sizes, states
- `tanstack-table-reference.md` — full Tanstack Table configuration reference
- `template-component-spec.md` — blank standard component template
- `template-table-spec.md` — blank Tanstack Table template
- `examples.md` — worked examples

**Always read `design-framework/stage2-component-specs/rules.md` before producing a component spec. Read `shadcn-component-catalog.md` to verify component names and variants.**

---

## Required Inputs

Before generating a component spec, confirm you have:

1. **Approved wireframe** (`design/wireframes.md`) — with WF-XXX IDs and AC mapping
2. **USD file(s)** — for AC references and traceability
3. **Feature name** — for file naming and traceability

Generate one COMP-XXX file per logical component (form, table, modal, card, navigation section). A single wireframe may produce multiple COMP-XXX files.

---

## COMP-XXX File Structure

Store in: `features/{feature-name}/design/COMP-XXX.md`

```markdown
# COMP-XXX: [Component Name]

**Component ID:** COMP-XXX
**Wireframe:** WF-XXX — [Screen Name]
**Stories:** ST-XXX, ST-YYY
**Acceptance Criteria:** AC-001, AC-002, AC-003
**Component Type:** Form | Table | Card | Modal | Navigation | Other

---

## Overview

**Purpose:** [What this component does]
**Context:** [Where it appears — which page/section]
**User Interaction:** [How users interact with it]
**Key Functionality:** [Main behaviors]

---

## ShadCN Component Mapping

| Element ID | Element | ShadCN Component | Variant | Size | Props | States |
|------------|---------|-----------------|---------|------|-------|--------|
| COMP-XXX-EL-001 | Email Input | Input | — | default | type: email, required: true, placeholder: "you@example.com" | default, focus, error, disabled |
| COMP-XXX-EL-002 | Submit Button | Button | default | default | type: submit, disabled: false | default, hover, focus, disabled, loading |
| COMP-XXX-EL-003 | Cancel Button | Button | outline | default | type: button | default, hover, focus |

---

## [Data Table Configuration (if applicable)]

**Table ID:** [descriptive-table-id]
**ShadCN + Tanstack Table**

### Columns

| # | Column | Accessor | Sortable | Filterable | Cell Rendering |
|---|--------|---------|---------|-----------|----------------|
| 1 | ID | `id` | ✅ | ✅ | Plain text |
| 2 | Status | `status` | ✅ | ✅ | ShadCN Badge (variant: by status value) |
| 3 | Customer | `customer.name` | ✅ | ✅ | Plain text |
| 4 | Created | `createdAt` | ✅ | ❌ | Formatted date: "MMM DD, YYYY" |
| 5 | Actions | — | ❌ | ❌ | Button group: [View] [Edit] [Delete] |

### Table Settings

| Setting | Value |
|---------|-------|
| Pagination | Enabled — 10 rows per page (user-selectable: 10, 25, 50) |
| Default Sort | `createdAt` DESC |
| Multi-column Sort | Enabled |
| Global Search | Enabled — debounced 300ms |
| Column Filters | Enabled on: Status, Customer |
| Row Selection | Multi-select with header checkbox |

### States

| State | Behavior |
|-------|---------|
| Empty | Show empty state: icon + "No [items] found" + optional CTA button |
| Loading | Show skeleton rows (match column count) |
| Error | Show error message + retry button |

---

## Layout Structure

**Container:** [e.g., "Full-width card with p-6 padding"]
**Layout System:** [Grid | Flex | Stack]
**Spacing:** [e.g., "gap-4 between form fields, gap-6 between sections"]

**Responsive Behavior:**

| Breakpoint | Behavior |
|-----------|---------|
| Desktop (> 1024px) | [Two-column layout, sidebar visible] |
| Tablet (640px–1024px) | [Single column, sidebar collapsed] |
| Mobile (< 640px) | [Stacked fields, full-width buttons] |

---

## Component Composition (if nested)

```
Dialog (ShadCN)
├── DialogTrigger: Button (variant: default) — "Create Item"
├── DialogContent
│   ├── DialogHeader
│   │   ├── DialogTitle: "Create New Item"
│   │   └── DialogDescription: "Fill in the details below."
│   ├── DialogBody: [Form fields]
│   └── DialogFooter
│       ├── Button (variant: outline): "Cancel"
│       └── Button (variant: default): "Create"
```

---

## States

| State | Description |
|-------|-------------|
| Default | Initial loaded state |
| Hover | Mouse-over appearance (desktop only) |
| Focus | Keyboard focus ring visible |
| Active | While user is interacting |
| Disabled | When action is not available |
| Loading | During async operation (spinner or skeleton) |
| Error | Validation failed or system error |
| Success | Action completed successfully |
| Empty | No data to display (lists/tables) |

---

## Validation and Error Handling

| Field | Rule | Error Message | Timing |
|-------|------|--------------|--------|
| Email | Required, valid email format | "Please enter a valid email address" | On blur |
| Password | Required, min 8 characters | "Password must be at least 8 characters" | On blur |
| Submit | All required fields valid | — | On submit |

**Error Placement:** Below the field, `text-sm text-destructive`

---

## Accessibility

| Requirement | Implementation |
|-------------|---------------|
| ARIA Labels | All inputs have `aria-label` or associated `<label>` |
| Keyboard Nav | Tab order follows visual left-to-right, top-to-bottom order |
| Focus Management | Modal traps focus on open; returns to trigger on close |
| Screen Reader | Form errors announced via `aria-live="polite"` |
| Touch Targets | All interactive elements ≥ 44×44px |

---

## Design Rules Applied

| Token Type | Value |
|-----------|-------|
| Primary color | `bg-primary` / `text-primary-foreground` |
| Destructive | `bg-destructive` / `text-destructive-foreground` |
| Spacing | `gap-4` (form fields), `gap-6` (sections), `p-6` (card padding) |
| Typography | `text-sm` labels, `text-base` inputs, `text-lg font-semibold` heading |
| Border radius | `rounded-lg` (cards), `rounded-md` (inputs) |

---

## Traceability

| Wireframe Element | Component ID | Acceptance Criteria | Notes |
|-------------------|-------------|---------------------|-------|
| Email Input | COMP-XXX-EL-001 | AC-001, AC-003 | Required field, email format validation |
| Submit Button | COMP-XXX-EL-002 | AC-005 | Disabled until all required fields are valid |
| Cancel Button | COMP-XXX-EL-003 | AC-006 | Navigates back without saving |

**Coverage:**
- [ ] All wireframe elements mapped to component IDs
- [ ] All ACs addressed in traceability table
- [ ] No orphaned elements (no element without a COMP-XXX-EL-YYY ID)
```

---

## ID System

### Component IDs

- Format: `COMP-XXX` (three-digit, zero-padded)
- Sequential per feature: `COMP-001`, `COMP-002`, ...
- One COMP-XXX per logical component (form, table, modal, card)
- Globally unique within the feature

### Element IDs

- Format: `COMP-XXX-EL-YYY`
- Sequential within a component: `COMP-001-EL-001`, `COMP-001-EL-002`, ...
- Assigned to every individual UI element (input, button, label, badge)
- Links from wireframe element → component spec → code

---

## ShadCN Component Quick Reference

Reference `design-framework/stage2-component-specs/shadcn-component-catalog.md` for the full catalog. Key components:

| Category | Components |
|----------|-----------|
| **Buttons** | Button (variants: default, secondary, destructive, outline, ghost, link; sizes: sm, default, lg, icon) |
| **Form Elements** | Input, Textarea, Select, Checkbox, RadioGroup, Switch, Label, Form |
| **Feedback** | Alert, Toast/Sonner, Badge, Progress, Skeleton |
| **Layout** | Card, Separator, ScrollArea, Tabs |
| **Overlay** | Dialog, AlertDialog, Sheet, Popover, Tooltip, DropdownMenu |
| **Navigation** | NavigationMenu, Breadcrumb, Pagination |
| **Data Display** | Table (basic) + Tanstack Table (complex/sortable/paginated) |
| **Date/Time** | Calendar, DatePicker |

**For data tables always use Tanstack Table** (not ShadCN Table) — headless, requires full column and state configuration.

---

## Tanstack Table Configuration Checklist

For any component that includes a data table, provide:

- [ ] All columns with accessor keys and display names
- [ ] Sort configuration (which columns are sortable, default sort column + direction)
- [ ] Filter configuration (global search, column-level filters)
- [ ] Pagination (enabled/disabled, default page size, size options)
- [ ] Row selection (none, single, multi-select with checkboxes)
- [ ] Actions column (button group: labels and variants)
- [ ] Empty state (icon, message, optional CTA button)
- [ ] Loading state (skeleton rows or spinner)
- [ ] Error state (message + retry button)

---

## Output Format

Component spec files must include YAML frontmatter for traceability:

```yaml
---
artifact: COMP
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: design-component-spec
upstream: design/wireframes.md
downstream: —
---
```

Store in: `features/{feature-name}/design/COMP-XXX.md`

---

## Quality Gate (Ready for Implementation)

A component spec is ready for code when:

- [ ] COMP-XXX ID assigned
- [ ] Wireframe ID(s) referenced
- [ ] All ShadCN components named with valid variants from the catalog
- [ ] All element IDs assigned (`COMP-XXX-EL-YYY`)
- [ ] All states defined (at minimum: default, hover, focus, disabled, error, loading, empty)
- [ ] Validation rules and error messages specified for all form inputs
- [ ] Responsive behavior described at all 3 breakpoints
- [ ] Tanstack Table fully configured (if a table is present)
- [ ] Accessibility requirements met (ARIA, keyboard nav, touch targets)
- [ ] Traceability table complete — all wireframe elements mapped, all ACs addressed
- [ ] No hardcoded colors — design tokens used throughout

---

## Anti-Patterns to Reject

- Code snippets in component spec — specify "what", not "how" (no JSX, no CSS classes)
- Invalid ShadCN variant names — always verify against `shadcn-component-catalog.md`
- Missing states — every interactive element must have hover, focus, disabled, error at minimum
- Partial Tanstack Table config — all columns, sort, filter, pagination, and states required
- Hardcoded colors (`#3B82F6`) — use tokens (`bg-primary`) only
- Missing accessibility section — ARIA labels, keyboard nav, and touch targets are required
- Traceability table with unmapped ACs — every AC that touches UI must appear
- COMP-XXX-EL-YYY IDs skipped or reused — must be sequential and unique within the file
- Component spec that skips the responsive section — mobile, tablet, desktop required
