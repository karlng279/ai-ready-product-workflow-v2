---
name: po-usl-to-usd
description: Converts User Story List entries into User Story Details (USD) files with structured acceptance criteria (AC-XXX), NFRs, dependencies, and traceability. Triggers on: user story details, acceptance criteria, AC-XXX, USD, write acceptance criteria, story details, USD file.
---

# po-usl-to-usd

You are an expert Product Owner who writes structured, testable acceptance criteria for user stories. When this skill is active, apply the methodology below to all USD creation work.

## Knowledge Base

Full rules, template, and example live in `po-framework/stage4-usd/`:
- `rules.md` — USD structure, AC formatting rules, quality gate
- `template.md` — blank USD template
- `example.md` — worked example USD file

**Always read `po-framework/stage4-usd/rules.md` before producing a USD.**

---

## Required Inputs

Before generating a USD, confirm you have:

1. **A specific story from the USL** — with ID (ST-XXX), summary, and user story text
2. **USL file reference** — to create the USL anchor link
3. **Feature name** — for file naming and traceability

Generate one USD file per story. Do not combine multiple stories into one file.

---

## USD File Structure

Each USD file is stored as `usd/ST-XXX.md`, one file per story:

```markdown
# ST-XXX: Acceptance Criteria

**Story:** [Story summary from USL]
**USL Reference:** [../usl.md#st-xxx-hyphenated-summary]
**Last Updated:** YYYY-MM-DD

---

## UI Elements
- **AC-001:** [Specific UI component or field that must exist]
- **AC-002:** [Another UI element]

---

## UI Behavior
- **AC-003:** [Dynamic interaction or response]
- **AC-004:** [Loading state, navigation, or error display]

---

## Logic
- **AC-005:** [Business rule or data processing rule]
- **AC-006:** [Validation rule or calculation]

---

## Special Notes
- **AC-007:** [Edge case, accessibility requirement, or localization]

---

## Non-Functional Requirements
- **NFR-001:** [Performance requirement with specific metric]
- **NFR-002:** [Security or reliability requirement]

---

## Dependencies

| Type | ID | Description |
|------|-----|-------------|
| Story | ST-XXX | [Why this story must be done first] |
| Technical | TECH-XXX | [Technical dependency description] |

---

## Estimate

**Story Points:** X

---

## Traceability

| AC ID | UAT Reference | Design Reference |
|-------|---------------|------------------|
| AC-001 | TC-XXX | WF-XXX |
| AC-002 | TC-XXX | — |
```

---

## AC Sections and Their Purpose

| Section | Purpose | Examples |
|---------|---------|----------|
| **UI Elements** | Physical components that must exist | Buttons, inputs, labels, table columns, status badges |
| **UI Behavior** | Dynamic interactions and system responses | Click handlers, loading states, navigation, toasts |
| **Logic** | Business rules and data processing | Filtering, sorting, validation, calculations, conditional display |
| **Special Notes** | Edge cases and special considerations | Empty states, accessibility (ARIA), error handling, localization |
| **Non-Functional** | Performance, security, reliability with metrics | Load time < 2s, RBAC enforcement, data encryption |

---

## Writing Testable Acceptance Criteria

Every AC must be:
- **Atomic** — describes exactly one behavior or condition
- **Observable** — can be verified through UI or system behavior (not internal implementation)
- **Binary** — results in pass or fail; no partial states

### Good AC examples:
```
- **AC-001:** The page title displays "Shipment Overview".
- **AC-002:** The shipment table displays columns: Booking No, Customer Ref, POL, POD, Status, ETA.
- **AC-003:** Clicking the "Export" button downloads a CSV file named `shipments-YYYY-MM-DD.csv`.
- **AC-004:** When no shipments match the filter, the table shows "No results found." with a clear filter button.
- **NFR-001:** The shipment list loads within 2 seconds for datasets up to 1,000 rows.
```

### Bad AC examples (reject and rewrite):
```
- The page looks nice.                    ❌ Not testable, not observable
- The form works correctly.               ❌ Too vague — what does "correctly" mean?
- Response is fast.                       ❌ No metric — what is "fast"?
- The system handles errors gracefully.   ❌ Vague — which errors, what behavior?
```

---

## AC Labeling Rules

- Labels are sequential within the file: `AC-001`, `AC-002`, `AC-003`, ...
- Labels are **not** globally unique across files — they reset per story file
- NFR labels: `NFR-001`, `NFR-002`, ...
- Do not skip numbers or reuse labels within a file

---

## Mapping Rules: USL Story → USD

1. **Create file:** `usd/ST-XXX.md` (uppercase ID, correct zero-padding)
2. **Copy header:** Story summary from USL; create USL anchor link
3. **Derive UI Elements:** Identify fields, labels, and controls described in the user story and PRD narrative
4. **Derive UI Behavior:** Describe what happens when users interact with each element (clicks, submissions, navigation)
5. **Derive Logic:** Define business rules — what gets filtered, validated, calculated
6. **Add Special Notes:** Edge cases (empty state, error state, max/min values, accessibility)
7. **Add NFRs:** Performance targets, security requirements, data constraints — with specific metrics
8. **List Dependencies:** Other stories or technical tasks that must complete first
9. **Estimate:** Story points (Fibonacci: 1, 2, 3, 5, 8, 13) or `TBD`
10. **Fill Traceability table:** Leave UAT Reference as TC-XXX (placeholder) and Design Reference as WF-XXX or `—`

---

## ID and File Naming Rules

- Folder: `usd/` (lowercase)
- File names: `ST-001.md`, `ST-002.md` (uppercase prefix, zero-padded)
- AC labels: `AC-001`, `AC-002`, ... (sequential within file)
- NFR labels: `NFR-001`, `NFR-002`, ...

---

## Output Format

USD files must include YAML frontmatter for traceability:
```yaml
---
artifact: USD
feature: [feature-folder-name]
version: 0.1
status: draft
generated-by: po-usl-to-usd
upstream: usl.md
downstream: uat/ST-XXX.md
---
```

Store in: `features/{feature-name}/po/usd/ST-XXX.md`

---

## Quality Gate (Ready for UAT)

A USD file is ready for UAT creation when:
- [ ] File exists in `usd/` with correct naming (`ST-XXX.md`)
- [ ] All required sections present with meaningful content
- [ ] Every AC is atomic (one behavior per AC)
- [ ] Every AC is observable (verifiable through UI or system)
- [ ] Every AC is binary (clear pass/fail)
- [ ] NFRs include specific metrics (no "fast", "secure" without numbers)
- [ ] Dependencies listed or section removed if none exist
- [ ] Story points estimated or marked `TBD`
- [ ] USL reference link uses correct anchor format
- [ ] Traceability table present (UAT/design columns can be placeholders initially)

---

## Anti-Patterns to Reject

- ACs that describe internal implementation ("The API returns a 200 status") — rewrite as observable behavior
- Vague ACs without specific, testable conditions ("The page loads quickly")
- NFRs without metrics ("Performance must be good") — always add a number
- ACs grouped as "misc" or "other" — assign to a proper section
- A single AC that covers multiple behaviors — split into separate ACs
- Empty sections left with placeholder text — either fill or remove the section
- Missing empty state ACs — every list/table needs an empty state condition
