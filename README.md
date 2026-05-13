# AI-Ready Product Workflow v2

> From Idea to Implementation. A structured, AI-optimized knowledge base for building software products end-to-end.

[![npm version](https://img.shields.io/npm/v/ai-ready-workflow)](https://www.npmjs.com/package/ai-ready-workflow)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-16-blue)]()
[![Agents](https://img.shields.io/badge/agents-Claude%20%7C%20Codex%20%7C%20Gemini%20%7C%20Cursor-purple)]()

---

## What This Is

A multi-framework knowledge base that gives AI agents (Claude Code, Codex, Gemini, Cursor) structured methodology for every stage of product development — from strategy to code-ready specs.

**4 frameworks. 16 skills. 5 pipeline commands. One traceable artifact chain.**

---

## Frameworks

| Framework | Directory | Purpose | Stages |
|---|---|---|---|
| **PM Framework** | `pm-framework/` | Strategy, discovery, research, analytics, growth, GTM | Strategy → Discovery → Research → Analytics → Growth → GTM |
| **PO Framework** | `po-framework/` | Product requirements to testable specs | PRD → USM → USL → USD → UAT |
| **Design Framework** | `design-framework/` | Text-based UI/UX design | Wireframes → Component Specs → Interactions |
| **Codebase Framework** | `codebase-framework/` | Next.js 15 implementation patterns | Next.js 15 + ShadCN UI + TanStack Query |

---

## Install Skills into Your Project

```bash
# Option A — npx (no clone needed, recommended)
npx ai-ready-workflow install

# Option B — from this repo (Mac/Linux)
./skills/install.sh

# Option C — from this repo (Windows)
.\skills\install.ps1
```

**What the installer copies to your project:**

| File / Folder | Used by |
|---|---|
| `.agent/skills/` (16 skill folders) | Claude Code (auto-loaded) |
| `AGENTS.md` | OpenAI Codex |
| `GEMINI.md` | Gemini Code Assist |
| `.cursorrules` | Cursor (auto-loaded on project open) |
| `GETTING_STARTED.md` | All agents — per-agent setup guide |

Safe to re-run — existing files are skipped.

→ See [`skills/README.md`](skills/README.md) for the full skill catalogue and [`GETTING_STARTED.md`](GETTING_STARTED.md) for per-agent setup.

---

## Skills

### UI/UX
| Skill | Triggers |
|---|---|
| `ui-ux-pro-max` | UI design, color palette, typography, chart type, design system |

### PO Pipeline
| Skill | Triggers |
|---|---|
| `po-brief-to-prd` | feature brief, PRD, product requirements |
| `po-prd-to-usm` | user story map, USM, story mapping |
| `po-usm-to-usl` | user story list, USL, MoSCoW prioritization |
| `po-usl-to-usd` | user story details, acceptance criteria, AC-XXX |
| `po-usd-to-uat` | UAT, test cases, BDD, given-when-then |

### Validation
| Skill | Triggers |
|---|---|
| `validate-prd` | validate PRD, PRD quality gate |
| `validate-usd` | validate USD, acceptance criteria check |

### Design
| Skill | Triggers |
|---|---|
| `design-wireframe` | wireframe, WF-XXX, ASCII wireframe, screen layout |
| `design-component-spec` | component spec, COMP-XXX, ShadCN component, design to code |

### PM Framework
| Skill | Triggers |
|---|---|
| `pm-product-strategy` | product strategy, vision, OKRs, SWOT, competitive analysis |
| `pm-product-discovery` | customer discovery, Jobs-to-be-Done, opportunity tree |
| `pm-market-research` | market research, persona, TAM SAM SOM, journey map |
| `pm-data-analytics` | metrics, KPIs, A/B test, North Star, funnel analysis |
| `pm-marketing-growth` | growth, value proposition, growth loop, PLG, retention |
| `pm-go-to-market` | go-to-market, GTM, launch plan, ICP, pricing, battlecard |

---

## Slash Commands (Claude Code)

| Command | Purpose |
|---|---|
| `/po-pipeline` | Full PO pipeline: Brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Wireframes + component specs from USD |
| `/validate-artifacts` | Quality gate check on all feature artifacts |
| `/pm-strategy` | Product strategy session |
| `/pm-discovery` | Discovery sprint session |

---

## Artifact ID System

| Artifact | ID | Location |
|---|---|---|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story | `ST-XXX` | `features/{name}/po/usl.md` |
| Acceptance Criteria | `AC-XXX` | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | `TC-XXX` | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | `WF-XXX` | `features/{name}/design/WF-XXX.md` |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` |
| PM Strategy | `PM-STRATEGY` | `features/{name}/pm/strategy.md` |
| PM Discovery | `PM-DISCOVERY` | `features/{name}/pm/discovery.md` |

---

## Feature Folder Structure

```
features/{feature-name}/
├── pm/                    # PM artifacts
│   ├── strategy.md
│   ├── discovery.md
│   └── gtm.md
├── po/
│   ├── prd.md
│   ├── usm.md
│   ├── usl.md
│   ├── usd/               # ST-XXX.md per story
│   └── uat/               # ST-XXX.md per story
├── design/
│   ├── WF-XXX.md          # per screen
│   └── COMP-XXX.md        # per component
└── code/
```

---

## Repository Structure

```
ai-ready-product-workflow-v2/
├── CLAUDE.md                   # Claude Code framework rulebook
├── AGENTS.md                   # OpenAI Codex / Agents skill index
├── GEMINI.md                   # Gemini Code Assist skill index
├── .cursorrules                # Cursor rules file
│
├── skills/                     # Agent-agnostic skill source of truth (16 skills)
│   ├── install.sh              # Mac/Linux installer
│   ├── install.ps1             # Windows installer
│   ├── cli.js + package.json   # npx ai-ready-workflow install
│   └── {skill-name}/SKILL.md
│
├── .agent/skills/              # Claude Code entry point (symlinks → skills/)
├── .claude/commands/           # Claude Code slash commands (5 pipeline commands)
│
├── pm-framework/               # PM methodology knowledge base
├── po-framework/               # PO pipeline knowledge base
├── design-framework/           # Design system knowledge base
├── codebase-framework/         # Next.js 15 implementation patterns
└── features/                   # Generated feature artifacts
```

---

## Multi-Agent Support

All 4 agents are supported. `npx ai-ready-workflow install` provisions each agent's entry point automatically.

| Agent | Entry Point | How skills activate |
|---|---|---|
| Claude Code | `.agent/skills/*/SKILL.md` | Auto-loaded on keyword match |
| OpenAI Codex | `AGENTS.md` | "Read AGENTS.md then help me write a PRD" |
| Gemini Code Assist | `GEMINI.md` | "Read GEMINI.md then help me write a PRD" |
| Cursor | `.cursorrules` | Auto-loaded on project open |
| Any agent | `skills/*/SKILL.md` | Read the relevant SKILL.md directly |

See [`GETTING_STARTED.md`](GETTING_STARTED.md) for per-agent first prompts and setup.

---

## Traceability Frontmatter

Every generated artifact includes YAML frontmatter:

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

---

## License

**Proprietary — All Rights Reserved**

Copyright © 2026 Karl Nguyen. Unauthorized copying, distribution, or modification is prohibited without explicit written permission.
