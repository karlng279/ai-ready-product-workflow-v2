# /design-pipeline

Generate wireframes and component specs from User Story Details (USD) for a feature.

## Usage

```
/design-pipeline [feature-name]
```

If `feature-name` is omitted, ask for it before starting. The USD files for the feature must already exist (`features/{feature-name}/po/usd/ST-XXX.md`).

---

## What This Command Does

Executes the 2-stage design artifact pipeline for a feature. Each stage produces traceable design artifacts stored in `features/{feature-name}/design/`.

| Stage | Skill | Input | Output |
|-------|-------|-------|--------|
| 1 | `design-wireframe` | `usd/ST-XXX.md` (AC-XXX) | `design/WF-XXX.md` per screen |
| 2 | `design-component-spec` | `design/WF-XXX.md` | `design/COMP-XXX.md` per component |

---

## Pre-flight Checks

Before starting, verify:

1. `features/{feature-name}/po/usd/` exists and contains at least one `ST-XXX.md` file
2. `features/{feature-name}/design/` folder exists (create if not)
3. Ask the user: "Which theme? (mds / corporate / ecommerce / erp) — default: mds"
4. Ask: "Generate wireframes for all stories, or specific ones? (all / ST-001, ST-002, ...)"

If USD files are missing, stop and tell the user to run `/po-pipeline` first.

---

## Execution Steps

### Step 1 — Wireframes (`design-wireframe`)

For each selected story:

1. Read `features/{feature-name}/po/usd/ST-XXX.md`
2. Activate `design-wireframe` skill
3. Identify the screens implied by the ACs (one wireframe per distinct screen or major view)
4. Assign sequential WF-XXX IDs across all stories in this feature
5. Generate `features/{feature-name}/design/WF-XXX.md` for each screen

Each WF-XXX file must include:
- Metadata header (ID, screen name, story, ACs, theme)
- Text description (purpose, layout structure, key elements, interactions)
- ASCII wireframe (60–80 chars wide, using standard symbol set)
- Component list (ShadCN + custom + Tanstack if table present)
- Responsive behavior (desktop, tablet, mobile)
- AC Mapping table (every AC from the USD accounted for)
- YAML frontmatter

After all wireframes are written, show a summary:
```
Wireframes created: WF-001 (Login Screen), WF-002 (Dashboard), WF-003 (Shipment List)
```

Pause and ask: "Wireframes look good? Proceed to component specs?"

### Step 2 — Component Specs (`design-component-spec`)

For each WF-XXX artifact:

1. Read `features/{feature-name}/design/WF-XXX.md`
2. Read the corresponding USD for AC traceability
3. Activate `design-component-spec` skill
4. Identify logical component groupings from the wireframe (one COMP-XXX per form / table / modal / card group)
5. Assign sequential COMP-XXX IDs across all wireframes in this feature
6. Generate `features/{feature-name}/design/COMP-XXX.md` for each component

Each COMP-XXX file must include:
- Metadata header (ID, name, type, WF reference, story, ACs)
- Component overview (purpose, context, user interaction)
- ShadCN component mapping with element IDs (`COMP-XXX-EL-YYY`), variants, sizes, states
- Tanstack Table full config (if table present in wireframe)
- Layout structure with responsive behavior
- Accessibility (ARIA, keyboard nav, touch targets)
- Design tokens (colors, spacing, typography — no hardcoded values)
- Traceability table (WF elements → element IDs → ACs)
- YAML frontmatter

---

## Completion Output

After all stages complete, print:

```
## Design Pipeline Complete — {feature-name}

Artifacts created:
- features/{feature-name}/design/WF-001.md   (Login Screen → ST-001: AC-001–AC-005)
- features/{feature-name}/design/WF-002.md   (Dashboard → ST-002: AC-006–AC-012)
- features/{feature-name}/design/COMP-001.md (Login Form → WF-001)
- features/{feature-name}/design/COMP-002.md (Dashboard Header → WF-002)
- features/{feature-name}/design/COMP-003.md (Activity Table → WF-002)

Next steps:
- Run /validate-artifacts to check design quality gates
- Hand COMP-XXX files to engineers for implementation
- Reference design-framework/stage3-interactions/ for interaction flows
```

---

## Rules

- All artifacts must include YAML frontmatter
- WF-XXX and COMP-XXX IDs are sequential per feature, zero-padded
- Every AC from the USD must appear in the WF AC Mapping table and the COMP traceability table
- Do not produce COMP-XXX files without a completed WF-XXX reference
- If `ui-ux-pro-max` skill is available and the user wants design system guidance (color palette, typography), run it before generating wireframes
