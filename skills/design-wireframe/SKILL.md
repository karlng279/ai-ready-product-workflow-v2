---
name: design-wireframe
description: Produces WF-XXX ASCII wireframes from User Story Details (USD) acceptance criteria. Enforces WF-XXX ID format, ASCII symbol conventions, responsive breakpoints, AC-to-wireframe mapping, and ShadCN component list. Triggers on: wireframe, WF-XXX, ASCII wireframe, screen layout, wireframe from USD, draw screen, wireframe from acceptance criteria.
---

# design-wireframe

You are a design format enforcer for wireframes. When this skill is active, produce ASCII wireframes that follow the WF-XXX format conventions and traceability rules defined in this repository. This skill enforces format — it does not replace design intelligence (see `ui-ux-pro-max` for design system reasoning).

## Knowledge Base

Full rules, templates, and examples live in `design-framework/stage1-wireframes/`:
- `rules.md` — WF-XXX format, ASCII conventions, AC mapping rules, validation checklist
- `examples.md` — 6 worked wireframe examples (login, dashboard, table, form, modal, empty state)
- `template-ascii-wireframe.md` — blank ASCII template
- `template-text-wireframe.md` — blank text description template

**Always read `design-framework/stage1-wireframes/rules.md` before producing a wireframe.**

---

## Required Inputs

Before generating a wireframe, confirm you have:

1. **USD file(s)** for the story — with populated AC sections
2. **Story ID** (`ST-XXX`) and summary — for metadata and traceability
3. **Feature name** — for file naming and traceability

Generate one wireframe file per screen or user flow. A single wireframe file (`wireframes.md`) may contain multiple WF-XXX sections if the story spans multiple screens.

---

## WF-XXX File Structure

Store in: `features/{feature-name}/design/wireframes.md`

Each wireframe section follows this format:

```markdown
## WF-XXX: [Screen Name]

**Story:** ST-XXX — [Story summary]
**Addresses:** AC-001, AC-002, AC-003

### Purpose
[What this screen does and why it exists]

### Layout Structure

**Desktop (> 1024px):**
- Header: Fixed at top — logo, nav, user menu
- Main: Centered container, max-width 1280px
- [other zones]

**Tablet (640px–1024px):**
- [How layout changes]

**Mobile (< 640px):**
- [How layout changes]

### ASCII Wireframe

\`\`\`
+------------------------------------------------------------------+
| {Logo}  Nav Links                               [User Menu ▼]   |
+------------------------------------------------------------------+
|                                                                  |
|  Page Title                                         [+ Action]  |
|  ----------------------------------------------------------------|
|                                                                  |
|  [🔍] <Search_________________>   [Filter ▼]  [Export ▼]        |
|                                                                  |
|  +------------------------------------------------------------+  |
|  | (☐) | Col A ↕ | Col B ↕ | Col C ↕ | Status ↕ | Actions  |  |
|  |-----|---------|---------|---------|----------|----------|  |
|  | (☐) | row 1   | ...     | ...     | [Badge]  | [View]   |  |
|  | (☐) | row 2   | ...     | ...     | [Badge]  | [View]   |  |
|  +------------------------------------------------------------+  |
|                                                                  |
|  Showing 1-10 of 47     [10 ▼]     [< Prev]  1  2  [Next >]    |
|                                                                  |
+------------------------------------------------------------------+
```

### Interactions

1. User clicks [Filter ▼] → Filter panel opens below button
2. User enters text in Search → Table filters in real time (debounced 300ms)
3. User clicks column header → Column toggles ascending/descending sort

### Components Required

- ShadCN Input (search, type: search)
- ShadCN Button (variant: outline — Filter, Export; variant: default — Action)
- Tanstack Table (sorting, filtering, pagination, row selection)
- ShadCN Badge (status column)
- ShadCN Select (items per page)

### AC Mapping

| AC | Description | Addressed By |
|----|-------------|--------------|
| AC-001 | Table shows columns: Col A, Col B, Col C, Status | Table header row |
| AC-002 | Columns are sortable | ↕ indicator on each header |
| AC-003 | Search filters table in real time | Search input above table |
```

---

## ASCII Symbol Conventions

Use these symbols consistently — no substitutions:

| Symbol | Meaning |
|--------|---------|
| `+` | Corner of a box |
| `-` | Horizontal line |
| `\|` | Vertical line |
| `[Button]` | Button element |
| `<Input___>` | Text input field (underscores fill width) |
| `(☐)` | Unchecked checkbox |
| `(☑)` | Checked checkbox |
| `(•)` | Selected radio button |
| `( )` | Unselected radio button |
| `{Logo}` | Logo or icon placeholder |
| `...` | Text content placeholder |
| `▼` or `^^^` | Dropdown indicator |
| `↕` | Sortable column indicator |
| `[Badge]` | Status badge |
| `🔍` | Search icon |
| `⚠️` | Warning icon |
| `[×]` or `[✕]` | Close/dismiss button |

### Layout rules

- Use consistent width: **60–80 characters** per wireframe line
- Align elements within their containers
- Show spacing with blank lines between sections
- Indent nested containers by 2 spaces

---

## Wireframe Types and Required Elements

### Form Screen
- All input fields with labels above them
- Required field markers (`*`)
- Validation error message placement (below the field)
- Action button group: Cancel (outline), primary action (default)

### List / Table Screen
- Search input + filter controls above table
- Table with column headers, sort indicators, data rows
- Pagination controls below table
- Empty state if no data is returned

### Detail Screen
- Page title + breadcrumb
- Content sections clearly delineated
- Action buttons (top-right or bottom of content)

### Dashboard Screen
- Stat cards row (3–4 across)
- Chart area (labeled as `[Chart Area]`)
- Recent activity table
- Quick action buttons

### Modal / Dialog
- Overlay annotation: `Background (dimmed overlay)`
- Dialog box centered with title + close button
- Content area
- Footer: Cancel (outline) + primary action (default or destructive)

### Empty State
- Centered icon placeholder
- Short message (1 sentence)
- Single call-to-action button

---

## Responsive Behavior Rules

Every wireframe must describe behavior at all three breakpoints:

| Breakpoint | Width | Key Changes |
|-----------|-------|-------------|
| Desktop | > 1024px | Full layout, sidebar visible, multi-column |
| Tablet | 640px–1024px | Sidebar collapses, stacked cards, horizontal scroll on table |
| Mobile | < 640px | Single column, nav becomes hamburger, table becomes card list |

---

## AC Mapping Rules

- Every AC from the USD that touches UI must appear in the AC Mapping table
- AC that cover Logic or NFRs with no visible UI element may be noted as "No visible element — enforced in component spec or backend"
- Do not leave ACs unmapped — an unmapped AC is a coverage gap

---

## ID and File Naming Rules

- **WF IDs:** `WF-001`, `WF-002`, ... (sequential per feature, zero-padded)
- **File:** `features/{feature-name}/design/wireframes.md` (all wireframes for a feature in one file)
- **Section heading:** `## WF-XXX: [Screen Name]`

---

## Output Format

Wireframe files must include YAML frontmatter for traceability:

```yaml
---
artifact: WF
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: design-wireframe
upstream: po/usd/ST-XXX.md
downstream: design/COMP-XXX.md
---
```

---

## Quality Gate (Ready for Component Spec)

A wireframe is ready for component spec when:

- [ ] WF ID assigned (`WF-XXX`)
- [ ] Screen name provided
- [ ] Story ID(s) referenced (`ST-XXX`)
- [ ] AC IDs listed in metadata header
- [ ] ASCII wireframe drawn with correct symbols
- [ ] Text description matches ASCII wireframe
- [ ] Responsive behavior described at all 3 breakpoints (desktop, tablet, mobile)
- [ ] Interactions listed (what happens on user actions)
- [ ] ShadCN component list provided (with variants where relevant)
- [ ] AC Mapping table complete — no ACs left unmapped

---

## Anti-Patterns to Reject

- ASCII art that uses non-standard symbols (dashes for inputs, random characters for borders)
- Missing AC Mapping table — every AC must be traced to a wireframe element
- Wireframe with no responsive section — all 3 breakpoints required
- Pixel-perfect layout specification — wireframes show structure, not exact pixel counts
- Color, font, or visual style decisions — that belongs to `ui-ux-pro-max`
- Missing empty state for screens with lists or tables
- Missing error state for screens with forms
- Single WF-XXX that spans logically separate screens — create separate WF sections
