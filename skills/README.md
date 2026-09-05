# ai-ready-workflow

[![npm version](https://img.shields.io/npm/v/ai-ready-workflow)](https://www.npmjs.com/package/ai-ready-workflow)
[![license](https://img.shields.io/npm/l/ai-ready-workflow)](https://github.com/karlng279/ai-ready-product-workflow-v2/blob/main/LICENSE)
[![node](https://img.shields.io/node/v/ai-ready-workflow)](https://www.npmjs.com/package/ai-ready-workflow)

Agent-agnostic skill library for AI-assisted product development. One install command gives your AI agent structured methodology across PM strategy, PO pipeline, design, validation, and artifact sync.

**What you get:**
- 17 skills across 4 frameworks (PM, PO, Design, UI/UX) + artifact sync
- 6 pipeline slash commands (Claude Code)
- Entry point files for all 4 major AI agents
- Per-agent onboarding guide

Skills are pure markdown — any AI agent that can read a file can use them.

---

## Claude Desktop

Add all 17 skills to Claude Desktop — no cloning required.

**1. Edit your Claude Desktop config:**

`~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)
`%APPDATA%\Claude\claude_desktop_config.json` (Windows)

```json
{
  "mcpServers": {
    "ai-ready-workflow": {
      "command": "npx",
      "args": ["-y", "ai-ready-workflow", "mcp"]
    }
  }
}
```

**2. Fully quit and reopen Claude Desktop** (Cmd+Q on Mac, then reopen).

**3. Type `/` in any conversation** — all 17 skills appear as selectable prompt templates.

Each skill loads its full methodology into the conversation. Optionally add your own brief or context when selecting a prompt.

---

## Install (Claude Code / other AI agents)

### Option A — npx (no clone required)

```bash
npx ai-ready-workflow install
```

Installs all 17 skills into `.agent/skills/` in the current directory and appends the skill registry to `CLAUDE.md` (if it exists).

To install into a specific project:

```bash
npx ai-ready-workflow install /path/to/your/project
```

### Option B — From a clone

```bash
git clone https://github.com/karlng279/ai-ready-product-workflow-v2
cd ai-ready-product-workflow-v2
./skills/install.sh                        # Mac/Linux
.\skills\install.ps1                       # Windows (PowerShell)
```

### What the installer does

1. Creates `.agent/skills/` in the target directory
2. Copies each skill folder (any directory containing a `SKILL.md`) to `.agent/skills/`
3. Appends the skill registry table to `CLAUDE.md` (if present and not already patched)

Skills already present are skipped — re-running is safe.

---

## After Install

The installer copies the following into your project root:

| File | Agent | How skills activate |
|---|---|---|
| `.agent/skills/*/SKILL.md` | Claude Code | Auto-loaded on keyword match |
| `AGENTS.md` | OpenAI Codex | "Read AGENTS.md then help me write a PRD" |
| `GEMINI.md` | Gemini Code Assist | "Read GEMINI.md then help me write a PRD" |
| `.cursorrules` | Cursor | Auto-loaded on project open |
| `GETTING_STARTED.md` | All agents | Per-agent setup and first prompt examples |

See `GETTING_STARTED.md` in your project root for agent-specific setup and example prompts.

---

## Skill Catalogue

### UI/UX

| Skill | Trigger Keywords | What It Does |
|-------|-----------------|--------------|
| `ui-ux-pro-max` | UI design, color palette, typography, chart type, design system, wireframe style | Design intelligence — palette selection, typography rules, chart type guidance via Python + CSV databases |

**ui-ux-pro-max requires Python 3.** Run a database search before generating UI:

```bash
python3 .agent/skills/ui-ux-pro-max/scripts/search.py "your query"
```

---

### PO Pipeline (run in order)

| Skill | Trigger Keywords | Input → Output |
|-------|-----------------|----------------|
| `po-brief-to-prd` | feature brief, PRD, product requirements, create PRD | Brief → `prd.md` (PRD-XXX) |
| `po-prd-to-usm` | user story map, USM, story mapping from PRD | `prd.md` → `usm.md` |
| `po-usm-to-usl` | user story list, USL, MoSCoW prioritization, story list | `usm.md` → `usl.md` (ST-XXX) |
| `po-usl-to-usd` | user story details, acceptance criteria, AC-XXX, USD | `usl.md` → `usd/ST-XXX.md` |
| `po-usd-to-uat` | UAT, test cases, BDD, given-when-then, test scenarios | `usd/ST-XXX.md` → `uat/ST-XXX.md` (TC-XXX) |

Full pipeline: `/po-pipeline` slash command chains all 5 stages automatically.

---

### Validation & Sync

| Skill | Trigger Keywords | What It Does |
|-------|-----------------|--------------|
| `validate-prd` | validate PRD, PRD quality gate, PRD completeness check | PRD sections, measurable goals, personas, no placeholder text |
| `validate-usd` | validate USD, acceptance criteria check, AC completeness | Atomic ACs, observable outcomes, NFR metrics, empty/error state coverage |
| `artifact-sync` | sync check, stale artifacts, ripple impact, upstream changed, downstream stale, artifact drift, propagate changes | Detects stale artifacts when an upstream changes; produces Stale Impact Report with surgical per-artifact patches |

Full validation: `/validate-artifacts` slash command runs all quality gates.
Sync check: `/sync-check {feature-name} {changed-artifact-path}` detects and patches stale artifacts after any pipeline change.

---

### Design

| Skill | Trigger Keywords | Input → Output |
|-------|-----------------|----------------|
| `design-wireframe` | wireframe, WF-XXX, ASCII wireframe, screen layout, create wireframe, wireframe for story | `usd/ST-XXX.md` → `design/wireframes.md` (one `## WF-XXX` section per screen) |
| `design-component-spec` | component spec, COMP-XXX, ShadCN component, design to code, component handoff | `design/wireframes.md` → `design/COMP-XXX.md` |

Full design pipeline: `/design-pipeline` slash command chains both stages.

> **Note:** `design-wireframe` and `design-component-spec` enforce format and traceability. They are not design intelligence — use `ui-ux-pro-max` for palette, typography, and UX reasoning.

---

### PM Framework

| Skill | Trigger Keywords | Frameworks |
|-------|-----------------|------------|
| `pm-product-strategy` | product strategy, vision, OKRs, SWOT, competitive analysis, positioning | Product Strategy Canvas, OKR hierarchy, SWOT, Ansoff Matrix, JTBD strategic lens |
| `pm-product-discovery` | customer discovery, Jobs-to-be-Done, opportunity tree, assumption mapping, experiment | Opportunity Solution Tree (Teresa Torres), Assumption Mapping, JTBD interview scripts |
| `pm-market-research` | market research, persona, TAM SAM SOM, journey map, segmentation, ICP | Jobs-aware personas, TAM/SAM/SOM sizing, Customer Journey Map, competitive matrix |
| `pm-data-analytics` | metrics, KPIs, A/B test, North Star, funnel analysis, cohort, HEART | North Star Metric, HEART, AARRR/RARRA, A/B test design, cohort analysis, SQL generation |
| `pm-marketing-growth` | growth, value proposition, growth loop, PLG, activation, retention, monetization | Value Proposition Canvas, positioning statement, growth loop design, PLG flywheel |
| `pm-go-to-market` | go-to-market, GTM, launch plan, ICP, pricing, battlecard, sales enablement | ICP, beachhead market, GTM motion selection, launch plan, pricing strategy, battlecard |

---

## Artifact ID System

| Artifact | ID Format | File Location |
|----------|-----------|---------------|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story (List) | `ST-XXX` | `features/{name}/po/usl.md` |
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
│   ├── usd/               # One file per story: ST-XXX.md
│   └── uat/               # One file per story: ST-XXX.md
├── design/
│   ├── wireframes.md      # ALL WF-XXX sections for the feature
│   ├── COMP-XXX.md        # One file per component
│   └── interactions.md    # ALL interaction flows for the feature
└── code/
```

---

## Multi-Agent Compatibility

Skills are in `skills/*/SKILL.md` — the agent-agnostic source of truth. Each AI agent has its own entry point:

| Agent | Entry Point |
|-------|-------------|
| Claude Desktop | MCP server via `npx ai-ready-workflow mcp` (see above) |
| Claude Code | `.agent/skills/*/SKILL.md` (auto-loaded on skill match) |
| OpenAI Codex | `AGENTS.md` (skill index at repo root) |
| Gemini Code Assist | `GEMINI.md` (skill index at repo root) |
| Cursor | `.cursorrules` (rules file at repo root) |
| Any agent | `skills/*/SKILL.md` (read directly) |

---

## Slash Commands (Claude Code only)

Available in `.claude/commands/`:

| Command | Purpose |
|---------|---------|
| `/po-pipeline` | Run full PO pipeline: Brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Generate wireframes and component specs from USD |
| `/validate-artifacts` | Quality gate check on all feature artifacts |
| `/sync-check` | Detect stale artifacts after a change; generate surgical sync patches |
| `/pm-strategy` | Start a product strategy session |
| `/pm-discovery` | Start a discovery sprint session |

---

## Traceability Frontmatter

All generated artifacts must include YAML frontmatter:

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
[the artifact-sync plan](https://github.com/karlng279/ai-ready-product-workflow-v2/blob/main/docs/history/artifact-sync-plan.md) but are **not yet applied to any
artifact on disk** — treat them as the target state, not an existing convention:

```yaml
last_modified: 2026-05-22
change_summary: "One-sentence description of what changed"
change_type: additive        # additive | reductive | interface | structural
sync_status: in_sync         # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1
```

When an artifact is modified mid-pipeline, run `/sync-check` to detect all stale downstream and upstream artifacts and apply surgical patches.
