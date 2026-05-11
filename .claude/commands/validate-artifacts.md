# /validate-artifacts

Run quality gate checks on all PO and design artifacts for a feature.

## Usage

```
/validate-artifacts [feature-name]
```

If `feature-name` is omitted, ask for it. If run from within a feature's folder, infer the feature name from the path.

---

## What This Command Does

Reads all existing artifacts for a feature and runs the quality gate checks defined in the PO and design frameworks. Reports pass/fail per artifact with specific gaps called out.

---

## Artifacts Checked

| Artifact | Quality Gate Source | Skill |
|----------|--------------------|----|
| `po/prd.md` | `po-framework/stage1-prd/rules.md` | `validate-prd` |
| `po/usm.md` | `po-framework/stage2-usm/rules.md` | — |
| `po/usl.md` | `po-framework/stage3-usl/rules.md` | — |
| `po/usd/ST-XXX.md` (each) | `po-framework/stage4-usd/rules.md` | `validate-usd` |
| `po/uat/ST-XXX.md` (each) | `po-framework/stage5-uat/rules.md` | — |
| `design/WF-XXX.md` (each) | `design-framework/stage1-wireframes/quality-gate.md` | `design-wireframe` |
| `design/COMP-XXX.md` (each) | `design-framework/stage2-component-specs/quality-gate.md` | `design-component-spec` |

---

## Execution Steps

### Step 1 — Inventory

List all artifact files found in `features/{feature-name}/`:

```
PRD:  po/prd.md                    ✅ found
USM:  po/usm.md                    ✅ found
USL:  po/usl.md                    ✅ found
USD:  po/usd/ST-001.md             ✅ found
      po/usd/ST-002.md             ✅ found
UAT:  po/uat/ST-001.md             ⚠️  missing
      po/uat/ST-002.md             ⚠️  missing
WF:   design/WF-001.md             ✅ found
COMP: design/COMP-001.md           ✅ found
```

### Step 2 — PRD Validation (`validate-prd` skill)

Activate `validate-prd` skill. Check `po/prd.md` for:

- [ ] YAML frontmatter present and complete
- [ ] Problem Statement section — specific, not generic
- [ ] Goals section — measurable outcomes
- [ ] User Personas section — at least one named persona
- [ ] User Stories Overview — stories listed
- [ ] Success Metrics — quantified KPIs
- [ ] Out of Scope section — explicit exclusions
- [ ] No placeholder text (no "TBD", "TODO", "[Add here]")

### Step 3 — USD Validation (`validate-usd` skill)

For each `usd/ST-XXX.md`, activate `validate-usd` skill. Check:

- [ ] YAML frontmatter present
- [ ] Every AC is atomic (one behavior per item)
- [ ] Every AC is observable (verifiable through UI or system behavior)
- [ ] Every AC is binary (clear pass/fail, no partial states)
- [ ] NFRs include specific metrics (no "fast", "secure" without numbers)
- [ ] Empty state AC present for every list or table screen
- [ ] Error state AC present where user input or network calls occur
- [ ] Story points estimated or marked `TBD`
- [ ] Traceability table present

### Step 4 — Wireframe Validation

For each `design/WF-XXX.md`, check:

- [ ] WF-XXX ID assigned and in header
- [ ] Story and AC IDs referenced in header
- [ ] ASCII wireframe present and uses standard symbols
- [ ] Component list provided
- [ ] Responsive behavior described (all 3 breakpoints)
- [ ] AC Mapping table present — every AC from the linked USD accounted for
- [ ] YAML frontmatter present with upstream/downstream

### Step 5 — Component Spec Validation

For each `design/COMP-XXX.md`, check:

- [ ] COMP-XXX and COMP-XXX-EL-YYY IDs assigned
- [ ] Upstream WF-XXX referenced in metadata
- [ ] All wireframe elements mapped to element IDs
- [ ] All ShadCN component names are valid (not invented)
- [ ] All elements have states defined (default, hover, focus, error, disabled)
- [ ] Tanstack Table fully configured if table present
- [ ] Accessibility section present (ARIA, keyboard nav, touch targets)
- [ ] Design tokens used (no hardcoded hex colors)
- [ ] Traceability table present — all ACs covered

### Step 6 — Traceability Check

Verify the chain is unbroken:

```
PRD → USM → USL → USD (ACs) → UAT (test cases) → WF (AC mapping) → COMP (element IDs)
```

Flag any break in the chain:
- USD ACs not covered in UAT
- USD ACs not appearing in any WF AC Mapping table
- WF elements not mapped in any COMP

---

## Report Format

Print a consolidated report after all checks:

```
## Validation Report — {feature-name}

### Summary
| Artifact | Status | Issues |
|----------|--------|--------|
| PRD      | ✅ Pass | — |
| USM      | ✅ Pass | — |
| USL      | ✅ Pass | — |
| USD ST-001 | ⚠️ Warn | AC-004 missing metric in NFR-001 |
| USD ST-002 | ✅ Pass | — |
| UAT ST-001 | ❌ Missing | File not found |
| WF-001   | ✅ Pass | — |
| COMP-001 | ⚠️ Warn | COMP-001-EL-003 missing error state |

### Issues to Fix

1. **po/usd/ST-001.md — NFR-001:** "Performance must be good" → add specific metric (e.g., "< 2s for 1,000 rows")
2. **po/uat/ST-001.md:** Missing — run /po-pipeline or generate UAT for ST-001
3. **design/COMP-001.md — COMP-001-EL-003:** Define error state (message text, placement, trigger condition)

### Traceability
- PRD → USM → USL: ✅ Chain intact
- USL → USD: ✅ All Must Have stories have USD files
- USD → UAT: ⚠️ ST-001 UAT missing
- USD ACs → WF coverage: ✅ All ACs mapped
- WF → COMP coverage: ✅ All wireframe elements have COMP entries
```

---

## Rules

- Read quality gate definitions from `po-framework/` and `design-framework/` before running checks — do not rely on memory alone
- Report specific failures with file path + section + issue — never say "something is wrong"
- A ✅ Pass means all checklist items for that artifact are green
- A ⚠️ Warn means the artifact exists but has specific fixable gaps
- A ❌ Missing means the file doesn't exist yet
