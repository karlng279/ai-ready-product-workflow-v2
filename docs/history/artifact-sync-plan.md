# Plan: Artifact Synchronization Enhancement

## Context

The framework currently has declarative traceability (upstream/downstream frontmatter fields, ID references) but **no change propagation mechanism**. When a user modifies an artifact mid-pipeline — e.g., redesigns wireframes after USD/UAT are written — there is no way to know which other artifacts are now stale or what specifically needs to change. This creates silent inconsistencies across PM → PO → Design → Dev.

The goal is to add a **lightweight, AI-native sync system** that: captures what changed, identifies the impact radius (bidirectional), and generates surgical patches for affected artifacts — without requiring any external tooling (stays pure markdown + AI conventions).

---

## Architecture: 3 Layers

### Layer 1 — Change Capture (frontmatter extension)
Add 5 new fields to ALL artifact frontmatter:

```yaml
last_modified: 2026-05-21            # ISO date, updated on every meaningful edit
change_summary: "Removed filter panel from WF-002"  # One-sentence delta description
change_type: reductive               # additive | reductive | interface | structural
sync_status: in_sync                 # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1      # upstream version this was derived from
```

| `change_type` | Meaning |
|---|---|
| `additive` | New content only; nothing removed or renamed |
| `reductive` | Existing content removed |
| `interface` | Existing referenced content changed (AC text, WF layout, PRD narrative) |
| `structural` | IDs renumbered/reorganized — breaks all downstream references |

**Propagation rule:**
- `additive` → forward impacts only
- `reductive`, `interface`, `structural` → both forward AND backward impacts

### Layer 2 — Sync Detection (new `artifact-sync` skill)
A new skill that:
1. Identifies the changed artifact and classifies `change_type`
2. Walks the dependency graph (both directions) to build an impact set
3. Outputs a **Stale Impact Report** — table of affected artifacts with severity (HIGH/MEDIUM/LOW) and reason
4. Generates a **surgical patch per impacted artifact** — targeted diffs, not full regeneration
5. Adds a `> [!SYNC]` inline callout to flagged artifacts (human-readable alert in markdown body)
6. Applies approved patches after user confirmation

### Layer 3 — Sync Command (new `/sync-check` slash command)
`/sync-check [feature-name] [changed-artifact-path]` orchestrates the full flow:
- Activates `artifact-sync` skill
- Produces the Stale Impact Report
- Offers apply-all or per-patch confirmation
- Optionally runs `validate-artifacts` after patching

---

## Dependency Graph (for impact analysis)

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
   USD (per ST-XXX)  ←──── design feedback (backward ripple)
        │
        ↓
   UAT (per ST-XXX)  ←──── design feedback (backward ripple)
        │                    ↑
        ↓                    │
   WF (wireframes)  ─────────┘
        │
        ↓
   COMP (component specs)
        │
        ↓
   [code/]  (out of scope — flagged but not patched)
```

---

## Stale Impact Report Format

The skill produces this exact structure:

```
### Stale Impact Report

**Changed Artifact:** WF — features/my-feature/design/wireframes.md
**Change Type:** interface
**Change Summary:** Restructured WF-001 from 2-col to 3-col; removed filter panel from WF-002
**New Version:** 0.2   |   **Date:** 2026-05-21

#### Impact Graph
[ASCII graph showing changed artifact + forward/backward impacts]

#### Artifacts Requiring Sync
| # | Artifact | Path | Direction | Reason | Severity |
|---|...

#### Sync Patches
One patch per artifact — surgical edit instructions (NOT full regeneration)
With before/after diffs and "requires author decision" flags for HIGH items

#### Summary stats
```

---

## Files to Create / Modify

### New Files
| File | Purpose |
|---|---|
| `skills/artifact-sync/SKILL.md` | Core skill — full methodology, impact matrix, report template, patch protocol |
| `.claude/commands/sync-check.md` | Slash command — orchestrates skill, handles apply confirmation |

### Modified Files
| File | Change |
|---|---|
| `skills/package.json` | Version `0.1.2` → `0.2.0` |
| `CLAUDE.md` | Add `artifact-sync` to Skills Registry table; add `/sync-check` to Slash Commands table |
| `skills/AGENTS.md` | Add artifact-sync row + `/sync-check` to commands table |
| `skills/GEMINI.md` | Same as AGENTS.md |
| `skills/.cursorrules` | Same as AGENTS.md |

> `mcp-server.js` and `install.sh`/`install.ps1` need NO changes — the MCP server auto-discovers `*/SKILL.md` and the installers auto-copy any folder containing `SKILL.md`.

---

## Key Skill Design Decisions

**`based_on_upstream_version` (not a hash):** Human-readable, no tooling required. AI can compare version numbers from frontmatter directly.

**`change_type` on the artifact (not inferred):** The author knows what changed; the skill cannot infer `reductive` vs `interface` without the before-state (no git tooling). Author classifies; skill uses the signal.

**`sync_notes` in body (not frontmatter):** Frontmatter is consumed programmatically. The sync note is a human communication — rendered as a blockquote callout in markdown, visible in any editor.

**Separate from `validate-artifacts`:** Validate runs quality gates in isolation on demand. Sync checking requires a trigger (something changed) and is cross-artifact. They remain separate concerns.

---

## Concrete Example: Design Change Mid-Pipeline

**Scenario:** You've completed the full pipeline for an "Export Customs Clearances" feature — PRD → USM → USL → USD → UAT → WF → COMP. Then during design review, you decide the wireframe needs a significant change: the "bulk export" action moves from a floating action button to a top toolbar, and an "inline preview" panel is removed entirely.

---

### Step 1 — You update `design/wireframes.md` and bump its frontmatter

```yaml
---
artifact: WF
feature: export-customs-clearances
version: 0.2                          # bumped from 0.1
last_modified: 2026-05-21
change_summary: "Moved bulk export to top toolbar; removed inline preview panel"
change_type: interface                # existing content restructured (additive + reductive)
sync_status: in_sync
based_on_upstream_version: 0.1       # generated from USDs at version 0.1
---
```

---

### Step 2 — You run `/sync-check export-customs-clearances design/wireframes.md`

The `artifact-sync` skill reads the wireframe, classifies the change as `interface` (existing elements changed + removed), then walks the dependency graph.

**It produces this Stale Impact Report:**

```
### Stale Impact Report

Changed Artifact: WF — features/export-customs-clearances/design/wireframes.md
Change Type: interface
Change Summary: Moved bulk export to top toolbar; removed inline preview panel
New Version: 0.2  |  Date: 2026-05-21

#### Impact Graph

  [Changed] WF v0.2 (wireframes.md)
       │
  ┌────┴──────────────┐
  ↓ FORWARD           ↓ BACKWARD
  COMP-001            USD/ST-004  (AC-007: "User sees inline preview on hover")
  COMP-002            USD/ST-006  (AC-003: "Bulk export button floats bottom-right")
                      UAT/ST-004  (TC-005: tests the inline preview panel)
                      UAT/ST-006  (TC-002: tests floating button position)

#### Artifacts Requiring Sync

| # | Artifact   | Path                 | Direction | Reason                                                        | Severity |
|---|------------|----------------------|-----------|---------------------------------------------------------------|----------|
| 1 | COMP-001   | design/COMP-001.md   | Forward   | WF-003 element map references inline preview panel (now gone) | HIGH     |
| 2 | COMP-002   | design/COMP-002.md   | Forward   | WF-001 bulk export zone ID changed from FAB to toolbar slot   | HIGH     |
| 3 | USD/ST-004 | po/usd/ST-004.md     | Backward  | AC-007 describes inline preview on hover — screen removed     | HIGH     |
| 4 | USD/ST-006 | po/usd/ST-006.md     | Backward  | AC-003 specifies floating button position — now toolbar       | HIGH     |
| 5 | UAT/ST-004 | po/uat/ST-004.md     | Backward  | TC-005 tests the inline preview panel (AC-007) — now invalid  | MEDIUM   |
| 6 | UAT/ST-006 | po/uat/ST-006.md     | Backward  | TC-002 asserts FAB bottom-right position — now wrong          | MEDIUM   |
```

---

### Step 3 — Skill generates surgical patches (not full rewrites)

**Patch for USD/ST-004 (backward — HIGH):**
```
Action: Requires author decision on AC-007
Reason: AC-007 "User sees inline preview panel on hover" — screen no longer exists

Options:
  A) Remove AC-007 (inline preview is dropped from scope)
  B) Rewrite AC-007 to reflect a different preview mechanism (e.g., modal on click)

Also insert sync_notes callout at top of file:
> [!SYNC] Pending Review — 2026-05-21
> Upstream WF v0.2 removed the inline preview panel.
> AC-007 is now invalid. Decide: remove or rewrite?
```

**Patch for USD/ST-006 (backward — HIGH):**
```
Action: Rewrite AC-003 (surgical — one sentence change)
Before: "The bulk export button appears as a floating action button in the bottom-right corner"
After:  "The bulk export button appears in the top toolbar, first action on the left"

Update traceability table: AC-003 → Design Reference WF-001 (toolbar zone, not FAB zone)
```

**Patch for COMP-001 (forward — HIGH):**
```
Action: Remove EL-004 (inline preview panel element) from component mapping table
Remove States section row: "preview-open" state
Update Traceability: remove AC-007 → COMP-001-EL-004 row
```

**Patch for UAT/ST-004 (forward — MEDIUM, depends on USD/ST-004 decision):**
```
If AC-007 removed: remove TC-005 and update AC Coverage Matrix
If AC-007 rewritten: rewrite TC-005 Given/When/Then to match new preview mechanism
```

---

### Step 4 — You review and apply

You decide: **remove AC-007** (inline preview is out of scope). The skill applies 5 patches, updates each file's `sync_status: in_sync` and `based_on_upstream_version: 0.2`, removes all `[!SYNC]` callouts, and prints a final summary:

```
Sync complete.
  5 files updated  |  1 AC removed (AC-007)  |  1 test case removed (TC-005)
  All artifacts: sync_status → in_sync
```

**Total impact of one design change, fully traced and patched:**
- 2 COMP files updated (element maps corrected)
- 2 USD files updated (1 AC rewritten, 1 removed)
- 2 UAT files updated (test cases realigned)
- Zero full regenerations — all surgical edits

---

## Verification

1. Create a test feature with a WF artifact
2. Manually bump WF version and write a `change_summary`
3. Run `/sync-check [feature] design/wireframes.md`
4. Confirm: Stale Impact Report appears with correct forward/backward impacts
5. Confirm: Patch for a USD file is surgical (modifies only the stale AC, not the whole file)
6. Apply patches and confirm `sync_status: in_sync` on patched artifacts
7. Confirm npx install picks up the new `artifact-sync` skill folder
