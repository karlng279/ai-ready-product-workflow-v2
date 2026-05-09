---
artifact: PRD
feature: feature-name
version: 0.1
status: draft
generated-by: po-brief-to-prd
upstream: brief.md
downstream: usm.md
---

# PRD: [Feature Name]

**ID:** PRD-XXX
**Version:** 0.1
**Owner:** [Name]
**Status:** draft
**Last Updated:** YYYY-MM-DD

---

## 1. Summary

[2–3 sentence executive summary: what is being built, for whom, and why now.]

---

## 2. Problem Statement

### 2.1 Pain Points

- [Describe a specific user or business pain]
- [Describe another pain]
- [Describe another pain]

### 2.2 Opportunities

- [What opportunity does this unlock?]
- [What becomes possible that wasn't before?]

---

## 3. Goals & Non-Goals

### 3.1 Business Goals

- [Measurable business outcome — be specific with metrics and timeframes]
- [Another business goal]

### 3.2 User Goals

- [What the user can do or accomplish that they couldn't before]
- [Another user goal]

### 3.3 Non-Goals

- [What is explicitly out of scope for this release]
- [Another non-goal]

---

## 4. User Personas

| Persona | Role | Key Need |
|---------|------|----------|
| [Name] | [Role] | [What they need from this feature] |

---

## 5. Requirements

### 5.1 Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-001 | [Describe requirement] | Must Have |
| FR-002 | [Describe requirement] | Should Have |

### 5.2 Non-Functional Requirements

| ID | Requirement | Metric |
|----|-------------|--------|
| NFR-001 | Performance | [e.g., page load < 2s at P95] |
| NFR-002 | Security | [e.g., data encrypted at rest] |

---

## 6. User Flows

[Describe the high-level user journeys. Reference USM when created.]

1. [Step 1]
2. [Step 2]
3. [Step 3]

---

## 7. Success Metrics

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| [Metric name] | [Current] | [Goal] | [How measured] |

---

## 8. Dependencies

| Type | Dependency | Status |
|------|-----------|--------|
| Technical | [API, service, or infrastructure dependency] | [pending/ready] |
| Product | [Other feature or team dependency] | [pending/ready] |

---

## 9. Open Questions

- [ ] [Unresolved question that needs an answer before development begins]
- [ ] [Another open question]

---

## 10. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | YYYY-MM-DD | [Author] | Initial draft |

---

<!--
TEMPLATE INSTRUCTIONS:

1. FILE LOCATION: features/{feature}/po/prd.md

2. FRONTMATTER: Update feature name before sharing. Keep version in sync with Revision History.

3. SECTIONS TO ALWAYS COMPLETE:
   - Summary (required)
   - Problem Statement (required)
   - Goals & Non-Goals (required)
   - Requirements — at minimum FR-001 through FR-005 (required)
   - Success Metrics (required)

4. QUALITY CHECKLIST:
   [ ] Summary is 2–3 sentences, no jargon
   [ ] Each goal has a measurable metric
   [ ] Non-goals are listed (at least 2)
   [ ] Functional requirements are atomic and verifiable
   [ ] NFRs have specific numeric metrics
   [ ] Success metrics have baselines and targets
   [ ] Open questions are listed or section is removed
-->
