# AI-Ready Product Workflow v2 — Skill Index for OpenAI Codex / Agents

This repository contains a structured skill library for AI-assisted product development.
Skills are in `skills/*/SKILL.md`. Read the relevant SKILL.md before generating any artifact.

---

## Framework Overview

- **PO Framework** (`po-framework/`): 5-stage pipeline — PRD → USM → USL → USD → UAT
- **Design Framework** (`design-framework/`): 3-stage pipeline — Wireframes → Component Specs → Interactions
- **Codebase Framework** (`codebase-framework/`): Next.js 15 + ShadCN UI + TanStack Query
- **PM Framework** (`pm-framework/`): Strategy → Discovery → Research → Analytics → Growth → GTM

---

## Skills

### UI/UX
- `skills/ui-ux-pro-max/SKILL.md` — UI/UX design intelligence. Run `python3 skills/ui-ux-pro-max/scripts/search.py "<query>"` for database lookup.

### PO Pipeline (in order)
- `skills/po-brief-to-prd/SKILL.md` — Convert a feature brief to a PRD (PRD-XXX)
- `skills/po-prd-to-usm/SKILL.md` — PRD to User Story Map (USM)
- `skills/po-usm-to-usl/SKILL.md` — USM to User Story List with MoSCoW prioritization (ST-XXX)
- `skills/po-usl-to-usd/SKILL.md` — USL stories to User Story Details / Acceptance Criteria (AC-XXX)
- `skills/po-usd-to-uat/SKILL.md` — USD acceptance criteria to UAT BDD test cases (TC-XXX)

### Validation
- `skills/validate-prd/SKILL.md` — PRD quality gate checker
- `skills/validate-usd/SKILL.md` — USD / acceptance criteria completeness checker

### Design
- `skills/design-wireframe/SKILL.md` — WF-XXX wireframe format, ASCII conventions, AC mapping
- `skills/design-component-spec/SKILL.md` — COMP-XXX component spec, ShadCN reference

### PM Framework
- `skills/pm-product-strategy/SKILL.md` — Product strategy, OKRs, SWOT, competitive analysis
- `skills/pm-product-discovery/SKILL.md` — Customer discovery, Opportunity Solution Tree, JTBD
- `skills/pm-market-research/SKILL.md` — Personas, TAM/SAM/SOM, journey maps, segmentation
- `skills/pm-data-analytics/SKILL.md` — North Star metric, HEART, A/B tests, funnel analysis
- `skills/pm-marketing-growth/SKILL.md` — Value proposition, growth loops, PLG flywheel
- `skills/pm-go-to-market/SKILL.md` — ICP, GTM motion, launch plan, pricing, battlecards

---

## Artifact ID System

| Type | Format | Location |
|---|---|---|
| PRD | PRD-XXX | `features/{name}/po/prd.md` |
| User Story | ST-XXX | `features/{name}/po/usl.md` |
| Acceptance Criteria | AC-XXX | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | TC-XXX | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | WF-XXX | `features/{name}/design/WF-XXX.md` |
| Component Spec | COMP-XXX | `features/{name}/design/COMP-XXX.md` |

---

## Traceability Frontmatter

All generated artifacts must include:

```yaml
---
artifact: PRD
feature: feature-name
version: 0.1
status: draft
generated-by: po-brief-to-prd
upstream: brief.md
downstream: usm.md
---
```
