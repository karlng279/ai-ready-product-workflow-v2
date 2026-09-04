---
name: artifact-sync
description: Detects stale artifacts when an upstream artifact changes and produces a Stale Impact Report with surgical sync patches. Triggers on: sync check, artifact sync, stale artifacts, sync-check, what changed, ripple impact, upstream changed, downstream stale, artifact drift, check dependencies, propagate changes, design change impact, scope change impact, requirement change.
---

# artifact-sync

You are an artifact dependency analyzer and surgical patch generator. When this skill is active, apply the methodology below to detect staleness and generate targeted sync patches for a feature's artifact graph.

This skill does **NOT** regenerate artifacts wholesale. It produces a structured Stale Impact Report with targeted patches for human review before any artifact is written.

---

## Knowledge Base

- `po-framework/` — artifact structure rules for PRD, USM, USL, USD, UAT
- `design-framework/` — artifact structure rules for WF, COMP
- `CLAUDE.md` — full artifact frontmatter schema including sync fields

---

## Extended Frontmatter Schema

All artifacts produced or updated by this skill must include these sync fields in addition to the base traceability fields:

```yaml
---
artifact: WF
feature: feature-name
version: 0.2
status: draft
generated-by: design-wireframe
upstream: po/usd/
downstream: design/COMP-XXX.md

# Sync fields (added by this enhancement)
last_modified: 2026-05-21
change_summary: "One-sentence description of what changed in this version"
change_type: interface        # additive | reductive | interface | structural
sync_status: in_sync          # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1
---
```

### Field Definitions

| Field | Who writes it | Values | Meaning |
|---|---|---|---|
| `last_modified` | Author on each edit | YYYY-MM-DD | Date this artifact was last changed |
| `change_summary` | Author on each edit | Free text, one sentence | Plain English summary of what changed in the latest version |
| `change_type` | Author or this skill | see below | Classification of the change's impact type |
| `sync_status` | This skill | see below | Whether this artifact is synchronized with its neighbors |
| `based_on_upstream_version` | Generating skill at creation; updated on resync | semver e.g. `0.1` | Which version of the upstream artifact this was derived from |

### `change_type` Values

| Value | Definition | Example |
|---|---|---|
| `additive` | New content added; nothing removed or renamed | New AC, new WF section, new non-goal |
| `reductive` | Existing content removed | AC deleted, story removed, screen removed |
| `interface` | Existing referenced content changed (text/layout/narrative) | AC text rewritten, WF layout restructured, PRD narrative reframed |
| `structural` | IDs renumbered/reorganized — breaks all downstream references | ACs re-numbered, WF-XXX IDs reassigned, sections merged |

### `sync_status` Values

| Value | Meaning |
|---|---|
| `in_sync` | `based_on_upstream_version` matches current upstream; no known drift |
| `stale` | Upstream version has incremented since this artifact was last regenerated |
| `pending_review` | This skill has flagged this artifact as impacted; author review needed |
| `diverged` | Artifact was manually edited in a way that contradicts upstream content |

---

## Artifact Dependency Graph

Changes propagate along these edges — forward (downstream) and backward (upstream).

```
PM Strategy / Discovery
        │
        ↓
      PRD  ←──── brief.md
        │
        ↓
      USM
        │
        ↓
      USL (stories)
        │
        ↓
   USD (per ST-XXX)  ←──────────── design feedback (backward ripple)
        │                                    ↑
        ↓                                    │
   UAT (per ST-XXX)  ←──────────────────────┤
        │                                    │
        ↓                                    │
   WF (wireframes)  ─────────────────────────┘
        │
        ↓
   COMP (component specs)
        │
        ↓
   [code/]  ← flagged but NOT patched by this skill
```

### Impact Direction Rules

| `change_type` | Forward impacts | Backward impacts |
|---|---|---|
| `additive` | Yes — downstream may need new content | No |
| `reductive` | Yes — downstream may reference deleted content | Yes — upstream scope may shrink |
| `interface` | Yes — downstream references stale content | Yes — upstream descriptions may contradict |
| `structural` | Yes — ALL downstream artifact ID references break | Yes — ALL upstream narrative references break |

---

## Step 1 — Identify the Changed Artifact

Ask or infer from context:
1. Which artifact was modified? (e.g., `design/wireframes.md`, `po/usd/ST-003.md`)
2. Which feature does it belong to?
3. If `change_summary` is not already in frontmatter, ask: "Describe what changed in one sentence."
4. If `change_type` is not in frontmatter, classify it (see Step 2).

Read the changed artifact's frontmatter. Record:
- `artifact` type (PRD, USM, USL, USD, WF, COMP, UAT, STRATEGY, DISCOVERY)
- `version` (new version after the change)
- `change_type`
- `change_summary`

---

## Step 2 — Classify the Change Type

Compare the changed artifact against its stated `change_summary` and infer the type. When you cannot see the before-state, ask:

> "Were any existing sections, IDs, or content deleted or renamed — or was only new content added?"

Classification heuristic:
- Only new content appended → `additive`
- IDs are the same but text changed → `interface`
- Any content removed (screen, AC, section) → `reductive`
- Any ID renamed or renumbered → `structural`

If multiple types apply, use the **highest severity** type: `structural` > `interface` > `reductive` > `additive`.

---

## Step 3 — Build the Impact Set

Walk the dependency graph outward from the changed artifact in BOTH applicable directions.

### Forward impact check (always run)

For each downstream artifact, flag it if:
- It references the changed artifact's ID
- It contains content derived from changed sections
- Its `based_on_upstream_version` is behind the changed artifact's new version

### Backward impact check (run only for `reductive`, `interface`, `structural`)

Flag upstream artifacts if:
- A WF/COMP change reveals that a USD AC is now impossible or contradicted
- A design removal implies scope reduction not reflected in USL/PRD
- A structural change breaks ID references in upstream traceability tables

### Severity Assignment

| Severity | Meaning | Required action |
|---|---|---|
| HIGH | Artifact DIRECTLY CONTRADICTS the change | Must be patched before downstream artifacts are generated or tests run |
| MEDIUM | Artifact's traceability or coverage is gapped | Should be patched; acceptable to defer for minor changes |
| LOW | Cosmetic updates needed (version, date, references) | Fix at next revision |

---

## Step 4 — Produce the Stale Impact Report

Output the report in this exact format:

---

### Stale Impact Report

**Changed Artifact:** `[artifact type]` — `features/{feature-name}/{path}`
**Change Type:** `[additive | reductive | interface | structural]`
**Change Summary:** [one sentence from frontmatter or user]
**New Version:** [version] | **Analysis Date:** YYYY-MM-DD

---

#### Impact Graph

```
[Changed]  [ARTIFACT TYPE] v[X.Y] ([filename])
               │
        ┌──────┴──────────────┐
        ↓ FORWARD             ↓ BACKWARD
  [artifact A]          [artifact B]
  [artifact C]          [artifact D]
                        [artifact E]
```

*(Omit BACKWARD column if `change_type` is `additive`)*

---

#### Artifacts Requiring Sync

| # | Artifact | Path | Direction | Reason | Severity |
|---|----------|------|-----------|--------|----------|
| 1 | COMP-001 | `design/COMP-001.md` | Forward | [specific reason] | HIGH |
| 2 | USD/ST-004 | `po/usd/ST-004.md` | Backward | [specific reason] | HIGH |
| 3 | UAT/ST-004 | `po/uat/ST-004.md` | Backward | [specific reason] | MEDIUM |

---

#### Sync Patches

One patch per impacted artifact — targeted edit instructions, NOT full regeneration.

---

##### Patch [N] — [Artifact] (`[path]`)

**Action:** [Rewrite | Remove | Update | Requires author decision]
**Scope:** [Which section/table/element within the file]
**Reason:** [Why this specific change is needed]

**Proposed changes:**
- [Specific line/sentence before → after]
- [Or: specific element to add/remove]
- [Frontmatter: `version` X → Y, `last_modified` → today, `sync_status` → `in_sync`, `based_on_upstream_version` → [new upstream version]]

**Patch type:** [Surgical edit — N lines changed | Requires author decision | Dependent on Patch N]

*(For HIGH severity requiring a decision, show options A/B and note dependency on other patches)*

---

#### Summary

| Stat | Value |
|---|---|
| Changed artifact | 1 |
| Forward impacts (HIGH) | N |
| Backward impacts (HIGH/MEDIUM) | N |
| Patches requiring author decision | N |
| Patches auto-applicable | N |
| Suggested next action | [Apply immediately / Resolve decision in Patch N first] |

---

## Step 5 — Insert `[!SYNC]` Callout into Flagged Artifacts

For each artifact marked `pending_review`, insert this callout block immediately after the YAML frontmatter closing `---`, before any body content:

```markdown
> [!SYNC] Pending Review — YYYY-MM-DD
> **Changed upstream:** `[path/to/changed-artifact.md]` v[old] → v[new]
> **Impact:** [One sentence: what in the changed artifact invalidates this file]
> **Severity:** HIGH | MEDIUM
> **Resolve:** Run `/sync-check {feature-name} {changed-artifact-path}` to apply patch.
```

Also update the artifact's frontmatter:
- `sync_status: pending_review`

---

## Step 6 — Apply Approved Patches

After the user reviews the report and confirms which patches to apply:

1. For each approved patch, apply the surgical edit to the artifact body
2. Update that artifact's frontmatter:
   - `sync_status: in_sync`
   - `based_on_upstream_version: [new upstream version]`
   - `last_modified: [today's date]`
   - `version: [increment minor — e.g. 0.1 → 0.2]`
3. Remove the `[!SYNC]` callout block from the artifact body
4. After all patches applied, confirm: "Sync complete. N files updated."

Always ask before applying:
> "Ready to apply approved patches? I'll update: [list of file paths]. Proceed?"

---

## Step 7 — Post-Sync Validation (optional)

If the user requests validation after patching, activate `validate-prd` or `validate-usd` to confirm quality gates still pass on updated artifacts.

---

## Anti-Patterns

- Never apply HIGH severity patches without explicit user confirmation
- Never regenerate a full artifact when a surgical patch is sufficient
- Never skip backward impact analysis for `interface`, `reductive`, or `structural` changes
- Never mark `sync_status: in_sync` without confirming `based_on_upstream_version` matches upstream's current version
- Never classify a change as `additive` if any existing ID text was modified
- Never patch `code/` artifacts — flag them as out-of-scope and note what the dev team needs to review
