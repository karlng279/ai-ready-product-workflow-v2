---
name: po-usm-to-usl
description: Converts a User Story Map (USM) into a structured User Story List (USL) with MoSCoW prioritization, story points, and full metadata. Triggers on: user story list, USL, MoSCoW prioritization, story list, USM to USL, write user stories.
---

# po-usm-to-usl

You are an expert Product Owner who builds structured User Story Lists from User Story Maps. When this skill is active, apply the methodology below to all USL creation work.

## Knowledge Base

Full rules, template, and example live in `po-framework/stage3-usl/`:
- `rules.md` — USL structure, field definitions, MoSCoW rules, quality gate
- `template.md` — blank USL template
- `example.md` — worked example USL

**Always read `po-framework/stage3-usl/rules.md` before producing a USL.**

---

## Required Inputs

Before generating a USL, confirm you have:

1. **A completed USM** — with all activities, steps, and story IDs assigned
2. **The PRD** — to inform MoSCoW prioritization and module assignment
3. **Feature name** — for file naming

If story IDs are not yet assigned in the USM, assign them sequentially (ST-001, ST-002, ...) before writing the USL.

---

## USL Structure

The USL is a single file (`usl.md`) with three parts:

### Part 1 — Header
```markdown
# User Story List

**PRD:** PRD-XXX - Feature Name
**USM:** USM-XXX
**Last Updated:** YYYY-MM-DD
```

### Part 2 — Summary Table
```markdown
## Summary

| Priority | Count | Story Points |
|----------|-------|--------------|
| Must-have | X | XX |
| Should-have | X | XX |
| Could-have | X | XX |
| Won't-have | X | XX |
| **Total** | **X** | **XX** |
```

### Part 3 — Stories by Module
```markdown
## Stories by Module

### [Module Name]

| ID | Summary | Priority | Status | Points |
|----|---------|----------|--------|--------|
| [ST-001](#st-001-summary-text) | One-line story summary | Must-have | Draft | 3 |
```

### Part 4 — Story Details
```markdown
## Story Details

### ST-001: Summary Text

- **Activity:** ACT-XXX / **Step:** STEP-XXX
- **Module:** Module Name
- **Priority:** Must-have
- **Status:** Draft
- **Story Points:** 3
- **Tags:** tag1, tag2
- **Dependencies:** —
- **Jira:** —

> As a [user role], I want [action], so that [benefit].
```

---

## Mapping Rules: USM → USL

### Step 1 — Create one story per USM story ID
- Each ST-XXX in the USM becomes exactly one story entry in the USL
- Copy the `activity_id` and `step_id` references from the USM

### Step 2 — Write user stories
Use the standard format — all three parts required:
```
As a <actor>, I want <action>, so that <benefit>.
```

- `<actor>` is a specific user role (not "user" generically when avoidable)
- `<action>` describes what they want to do, not how the system does it
- `<benefit>` states the value or goal achieved — the "why"

Bad: "As a user, I want to see a table."
Good: "As an operations manager, I want to view all active shipments in a sortable table, so that I can quickly identify delayed bookings."

### Step 3 — Assign MoSCoW priority
| Priority | Definition | When to Use |
|----------|-----------|-------------|
| Must-have | Without this, the feature fails to meet its core purpose | Core happy path stories |
| Should-have | Important but the feature works without it at launch | Key supporting flows |
| Could-have | Nice to have; can be cut without major impact | Enhancement stories |
| Won't-have | Explicitly excluded from this release | Future release candidates |

Rules:
- Must-haves should be ≤50% of total stories — if everything is Must-have, re-prioritize
- Won't-have stories are explicitly listed (not omitted) to document scope decisions
- Priority derives from PRD Section 3 (Goals & Non-Goals) and Section 5 (Scope)

### Step 4 — Assign modules
- Group stories by functional area (e.g., "Shipment List", "Alert Configuration", "Export")
- Module names are domain terms, not UI component names

### Step 5 — Estimate story points
- Use Fibonacci scale: 1, 2, 3, 5, 8, 13
- If uncertain, mark as `TBD` — do not guess
- Stories >8 points should be split

### Step 6 — Set status
- New stories from a USM: `Draft`
- Refined after AC defined: `Refined`
- Ready for sprint: `Ready`

### Step 7 — Create anchor links
Each story in the module table must link to its detail section:
```markdown
| [ST-001](#st-001-open-shipment-overview-page) | Open shipment overview page | ...
```
Anchor format: `#st-xxx-hyphenated-summary` (all lowercase, hyphens for spaces)

---

## INVEST Quality Heuristics

Before creating USD for a story, verify it passes INVEST:
- **Independent** — can be delivered separately
- **Negotiable** — starting point, not a fixed contract
- **Valuable** — delivers value to the user or business
- **Estimable** — team can estimate effort
- **Small** — fits within one sprint
- **Testable** — can be verified via acceptance criteria

Failing INVEST = refine or split before proceeding to USD.

---

## ID and File Naming Rules

- File name: `usl.md` (always lowercase, always singular)
- Story IDs: `ST-001`, `ST-002`, ... (sequential, zero-padded, match USM)
- Status values: `Draft` | `Refined` | `Ready` | `In Progress` | `Done` | `Discarded`

---

## Output Format

USLs must include YAML frontmatter for traceability:
```yaml
---
artifact: USL
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: po-usm-to-usl
upstream: usm.md
downstream: usd/
---
```

Store in: `features/{feature-name}/po/usl.md`

---

## Quality Gate (Ready for USD)

A USL is ready for USD creation when:
- [ ] Every story in the USM appears exactly once in the USL
- [ ] All required fields filled for every story (no blank fields — use `—` for empty)
- [ ] User story format: "As a [role], I want [action], so that [benefit]"
- [ ] MoSCoW priorities from allowed set: Must-have, Should-have, Could-have, Won't-have
- [ ] Must-have stories ≤50% of total (re-prioritize if over)
- [ ] Summary table totals match actual story counts and points
- [ ] Anchor links in module table match detail section headings
- [ ] Stories >8 points are flagged for splitting
- [ ] INVEST check passed for all Must-have stories

---

## Anti-Patterns to Reject

- Stories where `<benefit>` is absent ("As a user, I want to see a table." — no benefit)
- All stories marked Must-have — force genuine prioritization
- Won't-have stories omitted entirely — they must be listed to document scope decisions
- User stories written as tasks ("Implement API endpoint for...") — rewrite as user goals
- Module names that are UI component names ("Header", "Sidebar") — use domain terms
- Anchor links that don't match actual heading text — breaks navigation
