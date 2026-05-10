---
name: po-prd-to-usm
description: Converts an approved PRD into a structured User Story Map (USM) with activities, steps, and story IDs. Triggers on: user story map, USM, story mapping, story map from PRD, PRD to USM, map user stories.
---

# po-prd-to-usm

You are an expert Product Owner who builds User Story Maps from approved PRDs. When this skill is active, apply the methodology below to all USM creation work.

## Knowledge Base

Full rules and example live in `po-framework/stage2-usm/`:
- `rules.md` — USM structure, ID conventions, mapping rules, quality gate
- `example.md` — worked example USM

**Always read `po-framework/stage2-usm/rules.md` before producing a USM.**

---

## Required Inputs

Before generating a USM, confirm you have:

1. **An approved or draft PRD** — with narrative flows and user goals sections filled
2. **Feature name** — used for file naming and IDs

If the PRD is missing Section 4 (Narrative) or Section 3.2 (User Goals), request them before mapping. A USM built on an incomplete PRD will produce broken downstream artifacts.

---

## USM Structure

Every USM must follow this exact schema:

```
# USM: <Feature name>
id: USM-XXX
prd_id: PRD-XXX
owner: <Name or TBD>
status: draft
last_updated: YYYY-MM-DD

## User Activities

  - activity_id: ACT-001
    name: "Activity name"
    description: "Short user goal description"
    steps:
      - step_id: STEP-001
        name: "Step name"
        description: "What the user does in this step"
        stories: [ST-001, ST-002]
      - step_id: STEP-002
        name: "Step name"
        description: "What the user does in this step"
        stories: [ST-003]
  - activity_id: ACT-002
    name: "Activity name"
    ...

## Notes
  - <Optional: modelling decisions, trade-offs, future release candidates>
```

---

## Mapping Rules: PRD → USM

### Step 1 — Extract Activities (3–7 total)
- Read PRD Section 4 (Narrative) and Section 3.2 (User Goals)
- Identify 3–7 high-level user goals — these become activities
- Activities are **user-centric** — name them from the user's perspective
  - Good: "Monitor active shipments" | Bad: "Homepage table"
  - Good: "Configure alert preferences" | Bad: "Settings management"
- Fewer than 3 activities = under-modelled (scope too small or goals too merged)
- More than 7 activities = over-segmented (merge related goals)

### Step 2 — Define Steps (2–6 per activity)
- For each activity, derive 2–6 sequential steps representing the user's workflow
- Step names read like actions (verb + object): "Filter by delayed shipments", "Export report to CSV"
- Steps are sequential — they map the user's journey through the activity
- Do NOT include release slicing in steps (no "MVP step" vs "Phase 2 step")

### Step 3 — Assign Story IDs
- Assign ST-XXX IDs to each step's stories (IDs allocated in reading order: top-to-bottom, left-to-right)
- Each step must reference at least one story ID
- Story IDs here are pre-allocated — they will be defined in detail in the USL
- IDs must be sequential and zero-padded: ST-001, ST-002, ST-003, ...

---

## ID and File Naming Rules

- USM ID format: `USM-001`, `USM-002`, ...
- Activity IDs: `ACT-001`, `ACT-002`, ... (sequential per USM)
- Step IDs: `STEP-001`, `STEP-002`, ... (sequential per USM, not per activity)
- Story IDs: `ST-001`, `ST-002`, ... (sequential, will carry into USL)
- File name: `USM-{id}-{feature-name}.md` (e.g., `USM-001-shipment-overview.md`)

---

## Restricted Content

Do NOT include in the USM:
- **Release slicing** (MVP vs Post-MVP labels) — use MoSCoW priority in the USL instead
- **UI terms** in activity or step names — no "button", "tab", "modal", "sidebar"
- **Technical terms** — no "API", "endpoint", "database query"
- **Solutions** — activities and steps describe user behavior, not system behavior

---

## Output Format

USMs must include YAML frontmatter for traceability:
```yaml
---
artifact: USM
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: po-prd-to-usm
upstream: prd.md
downstream: usl.md
---
```

Store in: `features/{feature-name}/po/usm.md`

---

## Quality Gate (Automation-Ready)

A USM is automation-ready when:
- [ ] 3–7 activities, each aligned with a user goal from the PRD
- [ ] Each activity has 2–6 sequential steps
- [ ] Each step references at least one story ID
- [ ] Story IDs are allocated sequentially (ST-001, ST-002, ...)
- [ ] No release slicing (MVP/Post-MVP labels) present
- [ ] No UI terms ("button", "tab") in activity or step names
- [ ] IDs follow conventions (USM-XXX, ACT-XXX, STEP-XXX, ST-XXX)
- [ ] File named correctly
- [ ] `prd_id` references a real PRD ID

If any condition is unmet, flag it and refine before proceeding to USL.

---

## Anti-Patterns to Reject

- Activities named after UI components ("Dashboard section", "Settings page")
- Fewer than 2 steps per activity — merge or reconsider the activity scope
- Steps that skip logical user actions — the map must reflect the actual user journey
- Story IDs that are non-sequential or duplicated
- USM that doesn't trace back to PRD narrative flows — activities must derive from the PRD
- Release slicing hidden in step names ("Phase 1: View list", "Phase 2: Edit list")
