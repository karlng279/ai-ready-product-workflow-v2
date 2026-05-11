# /po-pipeline

Run the full PO pipeline for a feature: Brief → PRD → USM → USL → USD → UAT.

## Usage

```
/po-pipeline [feature-name] [brief or description]
```

If `feature-name` is omitted, ask for it before starting. If a brief is provided inline, use it directly. If not, ask the user to paste or describe the feature.

---

## What This Command Does

Executes the 5-stage PO artifact pipeline in sequence for a single feature. Each stage produces a traceable artifact stored in `features/{feature-name}/po/`.

| Stage | Skill | Input | Output |
|-------|-------|-------|--------|
| 1 | `po-brief-to-prd` | Feature brief | `prd.md` |
| 2 | `po-prd-to-usm` | `prd.md` | `usm.md` |
| 3 | `po-usm-to-usl` | `usm.md` | `usl.md` |
| 4 | `po-usl-to-usd` | `usl.md` | `usd/ST-XXX.md` per story |
| 5 | `po-usd-to-uat` | `usd/ST-XXX.md` | `uat/ST-XXX.md` per story |

---

## Execution Steps

### Step 0 — Setup

1. Confirm the feature name (use `$ARGUMENTS` if provided, otherwise ask)
2. Create the feature folder structure:
   ```
   features/{feature-name}/
   ├── po/
   │   ├── usd/
   │   └── uat/
   ├── design/
   ├── pm/
   └── code/
   ```
3. If a brief already exists at `features/{feature-name}/brief.md`, read it. Otherwise use the brief from `$ARGUMENTS` or ask the user.

### Step 1 — PRD (`po-brief-to-prd`)

- Read the brief
- Activate `po-brief-to-prd` skill
- Generate `features/{feature-name}/po/prd.md`
- Pause and show the PRD to the user
- Ask: "PRD looks good? Proceed to User Story Map, or revise first?"

### Step 2 — USM (`po-prd-to-usm`)

- Read `prd.md`
- Activate `po-prd-to-usm` skill
- Generate `features/{feature-name}/po/usm.md`
- Show the user story map to the user
- Proceed automatically to Step 3 (unless user says stop)

### Step 3 — USL (`po-usm-to-usl`)

- Read `usm.md`
- Activate `po-usm-to-usl` skill
- Generate `features/{feature-name}/po/usl.md` with MoSCoW prioritization
- Show the story list (count of Must/Should/Could/Won't)
- Ask: "Proceed to write acceptance criteria for all Must-Have stories?"

### Step 4 — USD (`po-usl-to-usd`)

- Read `usl.md`; filter to **Must Have** stories only (unless user requests others)
- Activate `po-usl-to-usd` skill
- Generate one `features/{feature-name}/po/usd/ST-XXX.md` per Must Have story
- After all USD files are written, show a summary: "Created USD for ST-001 through ST-00N"
- Proceed automatically to Step 5

### Step 5 — UAT (`po-usd-to-uat`)

- Read each `usd/ST-XXX.md`
- Activate `po-usd-to-uat` skill
- Generate one `features/{feature-name}/po/uat/ST-XXX.md` per story
- After all UAT files are written, show the completion summary

---

## Completion Output

After all stages complete, print:

```
## PO Pipeline Complete — {feature-name}

Artifacts created:
- features/{feature-name}/po/prd.md          (PRD-001)
- features/{feature-name}/po/usm.md          (USM-001)
- features/{feature-name}/po/usl.md          (N stories: X Must / Y Should / Z Could)
- features/{feature-name}/po/usd/ST-001.md   (acceptance criteria)
- ...
- features/{feature-name}/po/uat/ST-001.md   (UAT test cases)
- ...

Next steps:
- Run /design-pipeline to generate wireframes and component specs
- Run /validate-artifacts to run quality gates
```

---

## Pause Points

The pipeline pauses for user review at two points:
1. **After PRD** — user must confirm before USM is generated
2. **After USL** — user must confirm which stories to include in USD/UAT

All other transitions happen automatically.

---

## Rules

- All artifacts must include YAML frontmatter (`artifact`, `feature`, `version`, `status`, `generated-by`, `upstream`, `downstream`)
- Use the ID system: `PRD-XXX`, `USM-XXX`, `ST-XXX`, `AC-XXX`, `TC-XXX`
- Never skip stages — each stage's output is the next stage's input
- If the user stops mid-pipeline, they can resume by re-running `/po-pipeline {feature-name}` — the command will detect which stages already have artifacts and skip them
