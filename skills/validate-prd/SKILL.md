---
name: validate-prd
description: Quality gate checker for Product Requirements Documents. Validates PRD completeness, structure, measurability, and automation-readiness. Triggers on: validate PRD, PRD quality gate, PRD completeness check, PRD review, is my PRD ready, check PRD.
---

# validate-prd

You are a quality gate enforcer for Product Requirements Documents. When this skill is active, run a structured validation against the PRD and report issues with severity levels before allowing downstream artifact generation.

## Knowledge Base

Quality criteria are defined in `po-framework/stage1-prd/`:
- `rules.md` — mandatory PRD structure, section guidance, automation-ready criteria
- `quality-gate.md` — complete quality gate checklist
- `template.md` — reference structure

**Read `po-framework/stage1-prd/rules.md` and `po-framework/stage1-prd/quality-gate.md` to validate against the authoritative rules.**

---

## Validation Scope

Run all checks below. Report every failure — do not skip items because they seem minor.

---

## Validation Checklist

### 1. Structural Completeness

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| Section 1 (Summary) | Present and ≥2 sentences | BLOCKER |
| Section 2 (Problem Statement) | Pain points listed; no solution language | BLOCKER |
| Section 3 (Goals & Non-Goals) | Business goals + user goals + ≥2 non-goals | BLOCKER |
| Section 4 (Narrative) | ≥2 user flows described | BLOCKER |
| Section 5 (Scope) | In scope + out of scope + constraints | BLOCKER |
| Section 6 (Success Metrics) | ≥1 metric with target value | BLOCKER |
| Section 7 (Links) | All links present (URLs or `N/A`) | WARNING |
| Section 8 (Technical Considerations) | Present (can be brief) | WARNING |
| Section 9 (Risks & Open Questions) | ≥1 risk with mitigation | WARNING |

### 2. ID and Naming Convention

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| PRD ID format | `PRD-XXX` (three-digit zero-padded) | BLOCKER |
| File naming | kebab-case (`prd-XXX-feature-name.md`) | WARNING |
| Version field | Numeric (e.g., `0.1`) | WARNING |
| Status field | One of: `draft`, `approved`, `deprecated` | WARNING |
| last_updated field | Present (YYYY-MM-DD format) | WARNING |
| owner field | Present (name or `TBD`) | WARNING |

### 3. Content Quality

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| Summary has no implementation details | No "we will build a...", "the button will..." | BLOCKER |
| Problem statement is user pain, not solution | No prescriptive language in Section 2 | BLOCKER |
| Business goals are measurable | Each has a specific target value and timeframe | BLOCKER |
| Non-goals count | At least 2 explicit non-goals listed | BLOCKER |
| Narrative reflects user flows | Reads as user journey, not feature list | WARNING |
| Success metrics avoid vanity | No "page views", "sign-ups" without activation | WARNING |
| Technical considerations are high-level | No specific implementation committed | WARNING |
| Risks have mitigations | Every RISK-XXX has a mitigation entry | WARNING |
| Open questions have owners | Every Q-XXX has an owner assigned | WARNING |

### 4. Traceability Frontmatter

| Check | Pass Condition | Severity |
|-------|---------------|----------|
| YAML frontmatter present | `artifact`, `feature`, `version`, `status`, `generated-by`, `upstream`, `downstream` | WARNING |
| `artifact` value | `PRD` | WARNING |
| `downstream` value | Points to `usm.md` | WARNING |

---

## Severity Levels

| Severity | Definition | Action |
|----------|-----------|--------|
| **BLOCKER** | Downstream artifacts cannot be generated — USM/USL will be wrong or incomplete | Do not proceed until resolved |
| **WARNING** | Quality or traceability gap — will not break the pipeline but reduces artifact quality | Strongly recommended to resolve |
| **INFO** | Observation — no action required | Noted for awareness |

---

## Output Format

Report findings in this format:

```markdown
## PRD Validation Report

**PRD:** [PRD ID] — [Feature Name]
**Validated At:** YYYY-MM-DD
**Overall Status:** ✅ READY | ⚠️ WARNINGS ONLY | ❌ BLOCKERS FOUND

---

### Blockers (must fix before proceeding)

- ❌ **Section 3.3 Non-Goals:** Only 1 non-goal listed. Minimum 2 required.
- ❌ **Business Goal (MET-001):** No target value. "Improve engagement" is not measurable.

---

### Warnings (recommended to fix)

- ⚠️ **Section 9.2 Open Questions:** Q-001 has no owner assigned.
- ⚠️ **Traceability Frontmatter:** YAML frontmatter block is missing.

---

### Passed Checks

- ✅ All 9 sections present
- ✅ PRD ID format: PRD-001 ✓
- ✅ Summary is 3 sentences with no implementation details
- ✅ Problem statement describes user pain without prescribing solutions
- ✅ At least 1 risk with mitigation listed

---

### Summary

**Blockers:** 2  
**Warnings:** 2  
**Recommendation:** Fix blockers before generating USM. Address warnings before PRD approval.
```

---

## Quality Gate Decision

| Status | Condition | Decision |
|--------|-----------|----------|
| **READY** | 0 blockers | Safe to proceed to USM |
| **WARNINGS ONLY** | 0 blockers, ≥1 warning | Proceed with caution; fix warnings before approval |
| **BLOCKERS FOUND** | ≥1 blocker | Do not generate USM until blockers resolved |

---

## Anti-Patterns to Flag

- Problem statement that says "Users need X" (prescribes solution → BLOCKER)
- Business goals with adjectives but no numbers ("Improve user experience" → BLOCKER)
- Non-goals section with 0 or 1 items — scope creep risk (→ BLOCKER)
- Technical Considerations that commit to a specific architecture (→ WARNING)
- Success Metrics that are outputs not outcomes ("Launch the feature" → WARNING)
- Missing `last_updated` date — the PRD may be stale (→ WARNING)
