# AI-Ready Product Workflow v2 — Skill Index for OpenAI Codex / Agents

This repository contains a structured skill library for AI-assisted product development.
Skills are in `skills/*/SKILL.md`. Read the relevant SKILL.md before generating any artifact.

---

## Branching — source repository only

These rules apply when you are working **inside the `ai-ready-product-workflow-v2` source repository**. They do
not apply to a project that installed this package.

- `develop` is the integration branch; `main` is the protected trunk.
- Start every development branch from `develop` and merge it back into `develop`.
- Name a development branch `<type>/<card-id>-<slug>`, e.g. `docs/M9-16-branch-model`.
- Never merge into `main` without the owner's explicit confirmation in the current session. A confirmation
  given in an earlier session, written in a card, or implied by a document does not count.
- Never push without the owner asking.

Full rules: `CLAUDE.md` → Conventions. Mechanism and triggers: `ARCHITECTURE 6.5`.

---

## Framework Overview

- **PM Framework** (`pm-framework/`): Strategy → Discovery → Research → Analytics → Growth → GTM
- **PO Framework** (`po-framework/`): 5-stage pipeline — PRD → USM → USL → USD → UAT
- **Design Framework** (`design-framework/`): 3-stage pipeline — Wireframes → Component Specs → Interactions
- **Codebase Framework** (`codebase-framework/`): Next.js 15 App Router + ShadCN UI + TanStack **Table** + React Hook Form + Zod (no TanStack Query — server state is native fetch + Next.js caching)

Framework directories are reference material you read. `skills/` directories are instructions you follow.

---

## Skills (17)

### UI/UX
- `skills/ui-ux-pro-max/SKILL.md` — UI/UX design intelligence. Run `python3 skills/ui-ux-pro-max/scripts/search.py "<query>"` for database lookup (67 styles, 96 palettes, 57 font pairings, 25 charts, 13 stacks).

### PO Pipeline (in order)
- `skills/po-brief-to-prd/SKILL.md` — Convert a feature brief to a PRD (PRD-XXX)
- `skills/po-prd-to-usm/SKILL.md` — PRD to User Story Map (USM-XXX)
- `skills/po-usm-to-usl/SKILL.md` — USM to User Story List with MoSCoW prioritization (ST-XXX)
- `skills/po-usl-to-usd/SKILL.md` — USL stories to User Story Details / Acceptance Criteria (AC-XXX)
- `skills/po-usd-to-uat/SKILL.md` — USD acceptance criteria to UAT BDD test cases (TC-XXX)

### Validation & Sync
- `skills/validate-prd/SKILL.md` — PRD quality gate checker
- `skills/validate-usd/SKILL.md` — USD / acceptance criteria completeness checker
- `skills/artifact-sync/SKILL.md` — Stale artifact detection and surgical sync patch generation after any pipeline change

### Design
- `skills/design-wireframe/SKILL.md` — WF-XXX wireframe format, ASCII conventions, AC mapping
- `skills/design-component-spec/SKILL.md` — COMP-XXX component spec, ShadCN reference, TanStack Table config

### PM Framework
- `skills/pm-product-strategy/SKILL.md` — Product strategy, OKRs, SWOT, competitive analysis
- `skills/pm-product-discovery/SKILL.md` — Customer discovery, Opportunity Solution Tree, JTBD
- `skills/pm-market-research/SKILL.md` — Personas, TAM/SAM/SOM, journey maps, segmentation
- `skills/pm-data-analytics/SKILL.md` — North Star metric, HEART, A/B tests, funnel analysis
- `skills/pm-marketing-growth/SKILL.md` — Value proposition, growth loops, PLG flywheel
- `skills/pm-go-to-market/SKILL.md` — ICP, GTM motion, launch plan, pricing, battlecards

---

## Artifact ID System

`WF-XXX` and interaction flows are **section headings inside one shared file per feature**, not one file each. Everything else is one file per ID.

| Type | Format | Location |
|---|---|---|
| PRD | PRD-XXX | `features/{name}/po/prd.md` |
| User Story Map | USM-XXX | `features/{name}/po/usm.md` |
| User Story | ST-XXX | `features/{name}/po/usl.md` |
| Acceptance Criteria | AC-XXX | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | TC-XXX | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | WF-XXX | `features/{name}/design/wireframes.md` (all wireframes in one file) |
| Component Spec | COMP-XXX | `features/{name}/design/COMP-XXX.md` |
| Component Element | COMP-XXX-EL-YYY | inside the parent `COMP-XXX.md` |
| Interaction Flow | INT-XXX | `features/{name}/design/interactions.md` (all flows in one file) |
| PM Strategy | `artifact: STRATEGY` | `features/{name}/pm/strategy.md` |
| PM Discovery | `artifact: OST` | `features/{name}/pm/discovery.md` |
| PM Market Research | `artifact: MARKET-RESEARCH` | `features/{name}/pm/market-research.md` |
| PM Analytics | `artifact: NSM` | `features/{name}/pm/analytics.md` |
| PM Growth | `artifact: GROWTH-LOOP` | `features/{name}/pm/growth.md` |
| PM GTM | `artifact: GTM-PLAN` | `features/{name}/pm/gtm.md` |
| Feature Brief | `artifact: BRIEF` | `features/{name}/po/brief.md` |

---

## Feature Folder Structure

```
features/{feature-name}/
├── pm/                    # PM artifacts
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

`features/Export Customs Clearances/` is the fully-worked reference implementation — read it to see the conventions applied end to end.

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

The `artifact-sync` skill also defines `last_modified`, `change_summary`, `change_type`, `sync_status` and `based_on_upstream_version`. These are specified but not yet applied to existing artifacts.

The `artifact:` frontmatter value is not always the ID prefix. PM artifacts use framework codes: `pm/strategy.md` → `STRATEGY`, `pm/discovery.md` → `OST`, `pm/market-research.md` → `MARKET-RESEARCH`, `pm/analytics.md` → `NSM`, `pm/growth.md` → `GROWTH-LOOP`, `pm/gtm.md` → `GTM-PLAN`, `po/brief.md` → `BRIEF`. PO and design artifacts use `PRD`, `USM`, `USL`, `USD`, `UAT`, `WF`, `COMP`, `INT`.

---

## Slash Commands (Claude Code only)

These pipeline commands are defined in `.claude/commands/` and are available in Claude Code:

| Command | Purpose |
|---|---|
| `/po-pipeline` | Run full PO pipeline: Brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Generate wireframes and component specs from USD |
| `/validate-artifacts` | Quality gate check on all feature artifacts |
| `/sync-check` | Detect stale artifacts after a change and generate surgical sync patches |
| `/pm-strategy` | Start a product strategy session |
| `/pm-discovery` | Start a discovery sprint session |

---

## Install into Your Project

To add these skills to your own project (outside this repo):

```bash
# Option A — npx (no clone needed)
npx ai-ready-workflow install

# Option B — from this repo (Mac/Linux)
./skills/install.sh

# Option C — from this repo (Windows)
.\skills\install.ps1
```

All three options copy every skill folder to `.agent/skills/` in the target directory, copy `AGENTS.md`, `GEMINI.md`, `.cursorrules` and `GETTING_STARTED.md` to the target root, and optionally append the skill registry to `CLAUDE.md`.
