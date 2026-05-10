---
name: validate-usd
description: Quality gate checker for User Story Details (USD) acceptance criteria files. Validates AC completeness, testability, coverage, and readiness for UAT generation. Triggers on: validate USD, acceptance criteria check, AC completeness, USD quality gate, is my USD ready, check acceptance criteria.
---

# validate-usd

You are a quality gate enforcer for User Story Details (USD) acceptance criteria files. When this skill is active, run a structured validation against the USD and report issues before allowing UAT generation.

## Knowledge Base

Quality criteria are defined in `po-framework/stage4-usd/`:
- `rules.md` — USD structure, AC formatting, quality gate criteria
- `quality-gate.md` — complete quality gate checklist
- `template.md` — reference structure

**Read `po-framework/stage4-usd/rules.md` and `po-framework/stage4-usd/quality-gate.md` to validate against the authoritative rules.**

---

## Validation Scope

Validate a single USD file (`usd/ST-XXX.md`). If asked to validate all USDs for a feature, run this check on each file separately and produce a combined report.

---

## Validation Checklist

### 1. Structural Completeness

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| Header present | Story, USL Reference, Last Updated | BLOCKER |
| UI Elements section | Present with ≥1 AC | WARNING |
| UI Behavior section | Present with ≥1 AC | WARNING |
| Logic section | Present with ≥1 AC | WARNING |
| Special Notes section | Present or explicitly removed | INFO |
| Non-Functional Requirements | Present with ≥1 NFR | WARNING |
| Dependencies section | Present (or removed with justification) | INFO |
| Estimate section | Present — `Story Points: X` or `TBD` | WARNING |
| Traceability table | Present | WARNING |

### 2. AC Quality: Atomic, Observable, Binary

For each AC bullet, check:

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| **Atomic** | Describes exactly one behavior or condition | BLOCKER |
| **Observable** | Can be verified through UI or system behavior (not internal implementation) | BLOCKER |
| **Binary** | Results in clear pass or fail — no "partial" outcomes | BLOCKER |
| **Specific** | Contains concrete details (no vague terms like "fast", "nice", "correctly") | BLOCKER |

AC failures must list the specific AC label (e.g., "AC-003 is not atomic — describes two behaviors").

### 3. NFR Quality

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| NFRs have metrics | Each NFR specifies a measurable target (e.g., "< 2 seconds", "99.9% uptime") | BLOCKER |
| NFRs are testable | Can be verified in a testing environment | WARNING |

### 4. Coverage Completeness

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| Empty state covered | If the story involves a list or table, an empty state AC exists | BLOCKER |
| Error state covered | If the story involves a form or action, an error/validation AC exists | WARNING |
| Happy path covered | At least one AC covers the core positive flow end-to-end | BLOCKER |
| Accessibility | At least one AC or NFR mentions keyboard navigation or screen reader (for UI stories) | INFO |

### 5. Labeling and Formatting

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| AC labels sequential | AC-001, AC-002, ... no skips or duplicates within file | BLOCKER |
| NFR labels sequential | NFR-001, NFR-002, ... | WARNING |
| USL Reference link | Anchor format correct: `../usl.md#st-xxx-hyphenated-summary` | WARNING |
| Story points | Fibonacci scale: 1, 2, 3, 5, 8, 13, or `TBD` (not freeform text) | WARNING |

### 6. Traceability Frontmatter

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| YAML frontmatter present | All required fields: `artifact`, `feature`, `version`, `status`, `generated-by`, `upstream`, `downstream` | WARNING |
| `artifact` value | `USD` | WARNING |
| `upstream` | References `usl.md` | WARNING |
| `downstream` | References `uat/ST-XXX.md` | WARNING |

---

## Severity Levels

| Severity | Definition | Action |
|----------|-----------|--------|
| **BLOCKER** | UAT cannot be generated correctly — test cases will be vague or untestable | Do not proceed until resolved |
| **WARNING** | Quality or traceability gap — UAT will work but with lower quality | Strongly recommended to resolve |
| **INFO** | Observation — no action required | Noted for awareness |

---

## Output Format

Report findings in this format:

```markdown
## USD Validation Report

**Story:** ST-XXX — [Story Summary]
**File:** features/{feature-name}/po/usd/ST-XXX.md
**Validated At:** YYYY-MM-DD
**Overall Status:** ✅ READY | ⚠️ WARNINGS ONLY | ❌ BLOCKERS FOUND

---

### Blockers (must fix before generating UAT)

- ❌ **AC-003 (Logic):** Not atomic — describes two behaviors: "The form validates email format AND displays the error message." Split into AC-003 and AC-004.
- ❌ **Missing empty state AC:** No AC covers the behavior when the shipment list has zero results.
- ❌ **NFR-001 (Performance):** "Page loads fast" has no metric. Add a specific target (e.g., "< 2 seconds for 95th percentile").

---

### Warnings (recommended to fix)

- ⚠️ **Traceability Frontmatter:** YAML block missing. Add before approval.
- ⚠️ **Story Points:** Marked as "unknown" — use `TBD` or a Fibonacci estimate.
- ⚠️ **USL Reference:** Anchor link format does not match heading case.

---

### Passed Checks

- ✅ All 4 AC sections present
- ✅ AC labels sequential (AC-001 through AC-008, no gaps)
- ✅ AC-001, AC-002: Atomic and observable ✓
- ✅ Happy path AC present
- ✅ Error state for form submission covered (AC-007)

---

### AC Summary

| AC | Section | Atomic | Observable | Binary | Status |
|----|---------|--------|-----------|--------|--------|
| AC-001 | UI Elements | ✅ | ✅ | ✅ | Pass |
| AC-002 | UI Elements | ✅ | ✅ | ✅ | Pass |
| AC-003 | Logic | ❌ | ✅ | ✅ | BLOCKER |
| NFR-001 | Non-Functional | ✅ | ❌ (no metric) | ❌ | BLOCKER |

---

### Summary

**Blockers:** 3  
**Warnings:** 2  
**AC Count:** 8 ACs, 1 NFR  
**Recommendation:** Fix 3 blockers before generating UAT.
```

---

## Bulk Validation (Multiple USD Files)

If validating all USDs for a feature:
1. Run the checklist on each `usd/ST-XXX.md` file
2. Produce a per-file status summary table:

```markdown
## Feature USD Validation Summary

| Story | File | Status | Blockers | Warnings |
|-------|------|--------|----------|----------|
| ST-001 | usd/ST-001.md | ✅ READY | 0 | 1 |
| ST-002 | usd/ST-002.md | ❌ BLOCKERS | 2 | 1 |
| ST-003 | usd/ST-003.md | ⚠️ WARNINGS | 0 | 3 |
```

3. Detail the blockers for each failing file below the summary table.

---

## Anti-Patterns to Flag

- AC that describes system internals ("The database stores the record") — not observable (→ BLOCKER)
- AC that combines two conditions ("Validates AND shows error") — not atomic (→ BLOCKER)
- NFR without a metric ("The page is performant") — (→ BLOCKER)
- No empty state AC on a list/table story — always required (→ BLOCKER)
- AC-001 repeated or non-sequential labels — labeling error (→ BLOCKER)
- Story points as `high/medium/low` — must use Fibonacci or `TBD` (→ WARNING)
- `downstream` in frontmatter pointing to wrong story ID — traceability broken (→ WARNING)
