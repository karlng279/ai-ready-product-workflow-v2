# AI-Ready Product Workflow v2

> From Idea to Implementation. A structured, AI-optimized knowledge base for building software products end-to-end.

[![npm version](https://img.shields.io/npm/v/ai-ready-workflow)](https://www.npmjs.com/package/ai-ready-workflow)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-17-blue)]()
[![Agents](https://img.shields.io/badge/agents-Claude%20%7C%20Codex%20%7C%20Gemini%20%7C%20Cursor-purple)]()

---

## What This Is

A multi-framework knowledge base that gives AI agents (Claude Code, Codex, Gemini, Cursor) structured methodology for every stage of product development — from strategy to code-ready specs.

**4 frameworks. 17 skills. 6 pipeline commands. One traceable artifact chain.**

---

## Frameworks

| Framework | Directory | Purpose | Stages |
|---|---|---|---|
| **PM Framework** | `pm-framework/` | Strategy, discovery, research, analytics, growth, GTM | Strategy → Discovery → Research → Analytics → Growth → GTM |
| **PO Framework** | `po-framework/` | Product requirements to testable specs | PRD → USM → USL → USD → UAT |
| **Design Framework** | `design-framework/` | Text-based UI/UX design | Wireframes → Component Specs → Interactions |
| **Codebase Framework** | `codebase-framework/` | Next.js 15 implementation patterns | Next.js 15 App Router + ShadCN UI + TanStack Table + React Hook Form + Zod |

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
| `.agent/skills/` (one folder per skill) | Claude Code (auto-loaded) |
| `AGENTS.md` | OpenAI Codex |
| `GEMINI.md` | Gemini Code Assist |
| `.cursorrules` | Cursor (auto-loaded on project open) |
| `GETTING_STARTED.md` | All agents — per-agent setup guide |
| `CLAUDE.md` | Claude Code — a Skills Registry table is **appended** to an existing `CLAUDE.md`; the installer never creates one |

Safe to re-run — existing skills and files are skipped, and the registry is not appended twice.

→ See [`skills/README.md`](skills/README.md) for the full skill catalogue and [`GETTING_STARTED.md`](GETTING_STARTED.md) for per-agent setup.

---

## Skills

### PM Framework
| Skill | Triggers |
|---|---|
| `pm-product-strategy` | product strategy, vision, OKRs, SWOT, competitive analysis |
| `pm-product-discovery` | customer discovery, Jobs-to-be-Done, opportunity tree |
| `pm-market-research` | market research, persona, TAM SAM SOM, journey map |
| `pm-data-analytics` | metrics, KPIs, A/B test, North Star, funnel analysis |
| `pm-marketing-growth` | growth, value proposition, growth loop, PLG, retention |
| `pm-go-to-market` | go-to-market, GTM, launch plan, ICP, pricing, battlecard |

### PO Pipeline
| Skill | Triggers |
|---|---|
| `po-brief-to-prd` | feature brief, PRD, product requirements |
| `po-prd-to-usm` | user story map, USM, story mapping |
| `po-usm-to-usl` | user story list, USL, MoSCoW prioritization |
| `po-usl-to-usd` | user story details, acceptance criteria, AC-XXX |
| `po-usd-to-uat` | UAT, test cases, BDD, given-when-then |

### Design
| Skill | Triggers |
|---|---|
| `design-wireframe` | wireframe, WF-XXX, ASCII wireframe, screen layout |
| `design-component-spec` | component spec, COMP-XXX, ShadCN component, design to code |
| `ui-ux-pro-max` | UI design, color palette, typography, chart type, design system — forked from [uupm.cc](https://www.uupm.cc/) |

### Validation & Sync
| Skill | Triggers |
|---|---|
| `validate-prd` | validate PRD, PRD quality gate |
| `validate-usd` | validate USD, acceptance criteria check |
| `artifact-sync` | sync check, stale artifacts, ripple impact, upstream changed, downstream stale, artifact drift, propagate changes |

---

## Slash Commands (Claude Code)

| Command | Purpose |
|---|---|
| `/po-pipeline` | Full PO pipeline: Brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Wireframes + component specs from USD |
| `/validate-artifacts` | Quality gate check on all feature artifacts |
| `/sync-check` | Detect stale artifacts after a change; generate surgical sync patches |
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
| Wireframe | `WF-XXX` | `features/{name}/design/wireframes.md` (all wireframes in one file) |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` |
| Interaction Flow | `INT-XXX` | `features/{name}/design/interactions.md` (all flows in one file; `artifact: INT`) |
| PM Strategy | `artifact: STRATEGY` | `features/{name}/pm/strategy.md` |
| PM Discovery | `artifact: OST` | `features/{name}/pm/discovery.md` |
| PM Market Research | `artifact: MARKET-RESEARCH` | `features/{name}/pm/market-research.md` |
| PM Analytics | `artifact: NSM` | `features/{name}/pm/analytics.md` |
| PM Growth | `artifact: GROWTH-LOOP` | `features/{name}/pm/growth.md` |
| PM GTM | `artifact: GTM-PLAN` | `features/{name}/pm/gtm.md` |

---

## Feature Folder Structure

```
features/{feature-name}/
├── pm/                    # PM artifacts (six)
│   ├── strategy.md
│   ├── discovery.md
│   ├── market-research.md
│   ├── analytics.md
│   ├── growth.md
│   └── gtm.md
├── po/
│   ├── brief.md           # human-written pipeline input
│   ├── prd.md
│   ├── usm.md
│   ├── usl.md
│   ├── usd/               # ST-XXX.md per story
│   └── uat/               # ST-XXX.md per story
├── design/
│   ├── wireframes.md      # ALL WF-XXX sections for the feature
│   ├── COMP-XXX.md        # one file per component
│   └── interactions.md    # ALL interaction flows for the feature
└── code/
```

---

## Repository Structure

This repo follows [`docs/multi-session-repo-playbook.md`](docs/multi-session-repo-playbook.md): rules in
`CLAUDE.md`, specification split into `PRD.md` (meaning) and `ARCHITECTURE.md` (mechanism), status on a board,
and both asserted by tests.

`skills/` is both the skill source of truth and the npm package root. `.agent/skills/` holds symlinks into it.
Root `AGENTS.md` / `GEMINI.md` / `.cursorrules` and their `skills/` twins are kept byte-identical.

```
ai-ready-product-workflow-v2/
├── CLAUDE.md                   # always-on rules (rules, not knowledge)
├── PRD.md                      # specification: what artifacts MEAN
├── ARCHITECTURE.md             # specification: how the repo WORKS
├── AGENTS.md GEMINI.md .cursorrules   # per-agent skill indexes
│
├── docs/
│   ├── INDEX.md                # task → the exact sections it needs
│   ├── STATE.md                # done · in flight · next · blocked · waiting on owner
│   ├── decisions/              # NNNN-*.md, one per decision
│   ├── diagrams/               # as-is diagrams (open the .html files)
│   ├── history/                # superseded plans, kept as record
│   └── multi-session-repo-playbook.md
├── tasks/
│   ├── BACKLOG.md              # the plan, one row per unit of work
│   ├── cards/                  # one file per unit, authored just-in-time
│   └── lessons.md              # corrections, so they are not repeated
├── tests/                      # test_docs.py · test_prohibitions.py
│
├── skills/                     # skill source of truth + npm package (17 skills)
│   ├── install.sh install.ps1  # installers
│   ├── cli.js mcp-server.js    # npx ai-ready-workflow
│   └── {skill-name}/SKILL.md
├── .agent/skills/              # Claude Code entry point (symlinks → skills/)
├── .claude/commands/           # 6 pipeline slash commands
│
├── pm-framework/               # PM methodology knowledge base
├── po-framework/               # PO pipeline knowledge base
├── design-framework/           # design system knowledge base
├── codebase-framework/         # Next.js 15 implementation patterns
└── features/                   # generated feature artifacts
```

Run the checks before and after any change:

```bash
python3 tests/test_docs.py && python3 tests/test_prohibitions.py
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

The `artifact-sync` skill additionally defines five **sync fields**. They are specified in
[`docs/history/artifact-sync-plan.md`](docs/history/artifact-sync-plan.md) but are **not yet applied to any
artifact on disk** — treat them as the target state, not an existing convention:

```yaml
last_modified: 2026-05-22
change_summary: "One-sentence description of what changed"
change_type: additive        # additive | reductive | interface | structural
sync_status: in_sync         # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1
```

---

## License

**MIT License**

Copyright © 2026 Karl Nguyen. Licensed under the MIT License. See [LICENSE](LICENSE) for details.
