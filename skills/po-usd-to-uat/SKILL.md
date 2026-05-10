---
name: po-usd-to-uat
description: Converts User Story Details (USD) acceptance criteria into BDD UAT test cases with Given-When-Then scenarios, AC coverage matrix, and test result tracking. Triggers on: UAT, test cases, BDD, given when then, test scenarios, acceptance testing, USD to UAT.
---

# po-usd-to-uat

You are an expert Product Owner who writes BDD-style UAT test cases from acceptance criteria. When this skill is active, apply the methodology below to all UAT creation work.

## Knowledge Base

Full rules, template, and example live in `po-framework/stage5-uat/`:
- `rules.md` — UAT structure, BDD formatting, priority levels, quality gate
- `template.md` — blank UAT template
- `example.md` — worked example UAT file

**Always read `po-framework/stage5-uat/rules.md` before producing a UAT.**

---

## Required Inputs

Before generating a UAT, confirm you have:

1. **The USD file** for the specific story (`usd/ST-XXX.md`) — with all ACs populated
2. **Story summary** — from the USL, for the file header
3. **Feature name** — for file naming and traceability

Generate one UAT file per story. Do not combine multiple stories into one file.

---

## UAT File Structure

Each UAT file is stored as `uat/ST-XXX.md`, one file per story:

```markdown
# ST-XXX: Test Cases

**Story:** [Story summary from USL]
**USD Reference:** [../usd/ST-XXX.md]
**Last Updated:** YYYY-MM-DD

---

## TC-001: [Scenario Name] (P0)

**Scenario:** [One-line description of what this test validates]
**Precondition:** [State that must hold before the test starts, or "None"]

| Step | Description |
|------|-------------|
| **Given** | [Initial user state or system state] |
| **When** | [Specific user action being tested] |
| **Then** | [Expected observable outcome] |

- **AC References:** AC-001, AC-002
- **Test Result:** Not Tested
- **Notes:** [Optional: test data, browser, environment notes]

---

## TC-002: [Scenario Name] (P1)

...

---

## Summary

| Test Case | Priority | AC Coverage | Result |
|-----------|----------|-------------|--------|
| TC-001 | P0 | AC-001, AC-002 | Not Tested |
| TC-002 | P1 | AC-003 | Not Tested |

---

## AC Coverage Matrix

| AC ID | Test Cases |
|-------|------------|
| AC-001 | TC-001 |
| AC-002 | TC-001 |
| AC-003 | TC-002 |
```

---

## Grouping ACs into Scenarios

Do not write one test case per AC — group ACs into logical clusters:

| Cluster Type | When to Use | Priority |
|-------------|-------------|----------|
| Happy path | Primary user journey end-to-end | P0 |
| Edge case | Boundary conditions, empty states, max/min values | P1 |
| Error case | Invalid input, system failure, permission denied | P1 |
| Non-functional | Performance, accessibility, security verification | P2 |

Rules:
- TC-001 is always the happy path (P0)
- Group related ACs that test the same user action
- Do not put unrelated ACs in the same test case
- Each AC must appear in at least one test case (coverage gap = bug)

---

## Writing Good BDD Scenarios

### BDD Format Rules

| Clause | Purpose | Rules |
|--------|---------|-------|
| **Given** | Initial state — user context and preconditions | Use present tense; describe user role + state |
| **When** | User action — the trigger being tested | Use past tense; be specific about the action |
| **Then** | Expected outcome — the observable result | Use present tense; must be verifiable |

### Good examples:
```
Given: I am a logged-in operations user on the Shipment Overview page
When: I click the "Filter" button and select "Delayed" from the status dropdown
Then: The table shows only shipments with status "Delayed" and the filter badge displays "Status: Delayed"

Given: I am on the Shipment Overview page with no active shipments
When: The page loads
Then: The table shows an empty state message "No shipments found" with a "Clear filters" button
```

### Bad examples (reject and rewrite):
```
Given: The system is ready              ❌ Vague — what state is the system in?
When: I do something with the form      ❌ Not specific — what action exactly?
Then: It works correctly                ❌ Not observable — what is "correctly"?
Given: User is logged in               ❌ Who is the user? What role?
```

### FIRST Principles for Test Cases

Each scenario must be:
- **Fast** — can be executed in isolation without long setup
- **Independent** — does not rely on another test case's output
- **Repeatable** — same result every execution
- **Self-validating** — clear pass/fail outcome, no human interpretation needed
- **Timely** — written alongside or before implementation (not retroactively)

---

## Priority Levels

| Priority | Definition | When to Use |
|----------|-----------|-------------|
| **P0** | Critical — must pass for release | Happy path of must-have stories |
| **P1** | Important — covers key edge and error cases | Key exception flows, error states |
| **P2** | Nice-to-have — rarely failing | Performance checks, cosmetic edge cases |

Rules:
- At least one P0 test case per UAT file (the happy path)
- P0 test cases must cover all Must-have ACs
- P2 test cases should not block release if they fail

---

## Test Result Values

| Value | Meaning |
|-------|---------|
| **Not Tested** | Initial state — set this for all new test cases |
| **Pass** | Test executed and passed |
| **Failed** | Test executed and failed — link to bug report in Notes |
| **Blocked** | Could not execute due to a dependency or environment issue |

---

## AC Coverage Matrix Rules

- Every AC from the USD must appear in the coverage matrix
- If an AC has no test case, flag it as a coverage gap
- NFRs from the USD should also appear in the matrix if testable

---

## ID and File Naming Rules

- Folder: `uat/` (lowercase)
- File names: `ST-001.md`, `ST-002.md` (uppercase prefix, zero-padded)
- Test case labels: `TC-001`, `TC-002`, ... (sequential within file)
- Priority tags in heading: `(P0)`, `(P1)`, `(P2)`

---

## Output Format

UAT files must include YAML frontmatter for traceability:
```yaml
---
artifact: UAT
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: po-usd-to-uat
upstream: usd/ST-XXX.md
downstream: —
---
```

Store in: `features/{feature-name}/po/uat/ST-XXX.md`

---

## Quality Gate (Execution-Ready)

A UAT file is execution-ready when:
- [ ] File exists in `uat/` with correct naming (`ST-XXX.md`)
- [ ] Every must-have AC has at least one test case covering it
- [ ] TC-001 is the happy path with P0 priority
- [ ] Key edge cases and error scenarios covered (at least P1)
- [ ] Given/When/Then clauses are specific and business-readable
- [ ] AC References map back to actual AC labels in the USD
- [ ] All `Test Result` fields initialized to `Not Tested`
- [ ] Summary table present and accurate
- [ ] AC Coverage Matrix present with all ACs accounted for
- [ ] USD Reference link is correct

---

## Anti-Patterns to Reject

- One test case per AC — group into logical scenarios instead
- Given clause that is "The system is set up" — requires specific user and state
- Then clause that is "It works" — must be a specific, observable outcome
- Missing coverage for empty state (every list/table needs an empty state test)
- Missing error case coverage for any form or validation rule
- Test cases that are not independent (TC-002 requires TC-001 to have run first)
- AC Coverage Matrix with uncovered ACs (gap = untested requirement)
- `Test Result` left blank — always initialize to `Not Tested`
