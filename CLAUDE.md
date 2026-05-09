# AI-Ready Product Workflow v2

A structured, multi-framework knowledge base for AI-assisted product development. Contains 4 frameworks, 16+ skills, and 5 pipeline slash commands.

---

## Frameworks

| Framework | Directory | Stages |
|---|---|---|
| **PO Framework** | `po-framework/` | PRD → USM → USL → USD → UAT |
| **Design Framework** | `design-framework/` | Wireframes → Component Specs → Interactions |
| **Codebase Framework** | `codebase-framework/` | Next.js 15 + ShadCN + TanStack Query |
| **PM Framework** | `pm-framework/` | Strategy → Discovery → Research → Analytics → Growth → GTM |

---

## Skills Registry

Skills live in `skills/*/SKILL.md` (agent-agnostic source of truth). Claude Code loads them via `.agent/skills/*/SKILL.md`.

### UI/UX
| Skill | Triggers |
|---|---|
| `ui-ux-pro-max` | UI design, color palette, typography, chart type, design system, wireframe style |

### PO Pipeline
| Skill | Triggers |
|---|---|
| `po-brief-to-prd` | feature brief, PRD, product requirements, create PRD |
| `po-prd-to-usm` | user story map, USM, story mapping from PRD |
| `po-usm-to-usl` | user story list, USL, MoSCoW prioritization, story list |
| `po-usl-to-usd` | user story details, acceptance criteria, AC-XXX, USD |
| `po-usd-to-uat` | UAT, test cases, BDD, given-when-then, test scenarios |

### Validation
| Skill | Triggers |
|---|---|
| `validate-prd` | validate PRD, PRD quality gate, PRD completeness check |
| `validate-usd` | validate USD, acceptance criteria check, AC completeness |

### Design
| Skill | Triggers |
|---|---|
| `design-wireframe` | wireframe, WF-XXX, ASCII wireframe, screen layout |
| `design-component-spec` | component spec, COMP-XXX, ShadCN component, design to code |

### PM Framework
| Skill | Triggers |
|---|---|
| `pm-product-strategy` | product strategy, vision, OKRs, SWOT, competitive analysis, positioning |
| `pm-product-discovery` | customer discovery, Jobs-to-be-Done, opportunity tree, assumption mapping |
| `pm-market-research` | market research, persona, TAM SAM SOM, journey map, segmentation |
| `pm-data-analytics` | metrics, KPIs, A/B test, North Star, funnel analysis, cohort, HEART |
| `pm-marketing-growth` | growth, value proposition, growth loop, PLG, activation, retention |
| `pm-go-to-market` | go-to-market, GTM, launch plan, ICP, pricing, battlecard |

---

## Slash Commands

| Command | Purpose |
|---|---|
| `/po-pipeline` | Run full PO pipeline: brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Generate wireframes and component specs from USD |
| `/validate-artifacts` | Quality gate check on current feature artifacts |
| `/pm-strategy` | Start a product strategy session |
| `/pm-discovery` | Start a discovery sprint session |

---

## Artifact ID System

| Artifact | ID Format | Location |
|---|---|---|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story (List) | `ST-XXX` | `features/{name}/po/usl.md` |
| Acceptance Criteria | `AC-XXX` | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | `TC-XXX` | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | `WF-XXX` | `features/{name}/design/WF-XXX.md` |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` |

---

## Traceability Frontmatter

All generated artifacts must include YAML frontmatter for traceability:

```yaml
---
artifact: PRD          # artifact type (PRD, USM, USL, USD, UAT, WF, COMP)
feature: feature-name  # feature folder name
version: 0.1
status: draft          # draft | review | approved
generated-by: po-brief-to-prd  # skill that produced this
upstream: brief.md     # input artifact
downstream: usm.md     # next artifact in pipeline
---
```

---

## Feature Folder Structure

```
features/{feature-name}/
├── pm/           # PM artifacts (strategy, discovery, GTM)
├── po/
│   ├── prd.md
│   ├── usm.md
│   ├── usl.md
│   ├── usd/      # One file per story: ST-XXX.md
│   └── uat/      # One file per story: ST-XXX.md
├── design/
│   ├── WF-XXX.md
│   └── COMP-XXX.md
└── code/
```

---

## ui-ux-pro-max Usage

The `ui-ux-pro-max` skill requires Python 3. Run the search script before generating UI:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "your query"
```

---

## Multi-Agent Compatibility

| Agent | Entry Point |
|---|---|
| Claude Code | `.agent/skills/*/SKILL.md` (auto-loaded) |
| OpenAI Codex | `AGENTS.md` (skill index) |
| Gemini Code Assist | `GEMINI.md` (skill index) |
| Cursor | `.cursorrules` |
| Any agent | `skills/*/SKILL.md` (read directly) |
