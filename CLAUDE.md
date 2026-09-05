# AI-Ready Product Workflow v2

A structured, multi-framework knowledge base for AI-assisted product development.
**4 frameworks · 17 skills · 6 pipeline slash commands · one traceable artifact chain.**

---

## Orientation — read this first

This repo has **two jobs**. Know which one you are touching before you edit anything.

| Job | What it means | Lives in |
|---|---|---|
| **1. Knowledge base** | Methodology an AI agent reads while producing product artifacts. Not code. | `pm-framework/`, `po-framework/`, `design-framework/`, `codebase-framework/` |
| **2. Published npm package** | `ai-ready-workflow` — installs the skills into *other* people's projects. | `skills/` (the whole directory is the package root) |

`skills/` is therefore both the skill source of truth **and** the npm package payload. A change there ships to users.

There is no application code and no test suite. "Correct" here means *internally consistent and matching what the pipeline actually writes to disk* — verify claims against `features/` and against `skills/*/SKILL.md`, not against memory.

---

## Repo topology — source of truth

```
skills/{skill-name}/SKILL.md        ← CANONICAL. Every skill is authored here.
.agent/skills/{skill-name}          ← symlink → ../../skills/{skill-name}   (Claude Code auto-loads from here)
skills/AGENTS.md                    ← published twin of root AGENTS.md  (shipped by npm)
skills/GEMINI.md                    ← published twin of root GEMINI.md
skills/.cursorrules                 ← published twin of root .cursorrules
skills/README.md                    ← npm-facing readme (differs from root README.md by design)
skills/GETTING_STARTED.md           ← npm-facing onboarding (differs from root by design)
```

**Rule:** root `AGENTS.md` / `GEMINI.md` / `.cursorrules` and their `skills/` twins must stay byte-identical.
Root `README.md` and `GETTING_STARTED.md` intentionally differ from their `skills/` twins — root describes the *repo*, `skills/` describes the *installed package*.

Installers and the MCP server enumerate skills **dynamically** by looking for a `SKILL.md`, so a directory without one is silently ignored — but the hardcoded registry tables inside `install.sh` / `install.ps1` are manual and must be kept in sync by hand.

---

## Frameworks

| Framework | Directory | Stages |
|---|---|---|
| **PM Framework** | `pm-framework/` | Strategy → Discovery → Research → Analytics → Growth → GTM |
| **PO Framework** | `po-framework/` | PRD → USM → USL → USD → UAT |
| **Design Framework** | `design-framework/` | Wireframes → Component Specs → Interactions |
| **Codebase Framework** | `codebase-framework/` | Next.js 15 App Router + ShadCN UI + TanStack Table + React Hook Form + Zod |

Stage folder layout differs slightly between the two pipelines — check before assuming a file exists:

- **PO stages** (`po-framework/stage1-prd` … `stage5-uat`): `rules.md`, `quality-gate.md`, `template.md`, `prompts.md`, `example.md` (singular).
  `stage2-usm` has **no** `template.md`.
- **Design stages** (`design-framework/stage1-wireframes` … `stage3-interactions`): `rules.md`, `quality-gate.md`, `prompts.md`, `examples.md` (plural), plus one or two purpose-named templates
  (e.g. `template-ascii-wireframe.md`, `template-component-spec.md`, `template-interaction-flow.md`).
- **PM pillars** (6 of them): `rules.md`, `templates/` (3 each), `examples/` (1 each).

Framework dirs are **reference material** an agent reads. Skill dirs are **executable instructions** an agent follows. Do not confuse them.

---

## Skills Registry — 17 skills

Skills live in `skills/*/SKILL.md`. Claude Code loads them via the `.agent/skills/*` symlinks.

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

### Validation & Sync
| Skill | Triggers |
|---|---|
| `validate-prd` | validate PRD, PRD quality gate, PRD completeness check |
| `validate-usd` | validate USD, acceptance criteria check, AC completeness |
| `artifact-sync` | sync check, artifact sync, stale artifacts, ripple impact, upstream changed, downstream stale, artifact drift, check dependencies, propagate changes |

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

## Slash Commands — 6 commands

Defined in `.claude/commands/*.md`.

| Command | Purpose |
|---|---|
| `/po-pipeline` | Run full PO pipeline: brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | Generate wireframes and component specs from USD |
| `/validate-artifacts` | Quality gate check on current feature artifacts |
| `/sync-check` | Detect stale artifacts after a change and generate surgical sync patches |
| `/pm-strategy` | Start a product strategy session |
| `/pm-discovery` | Start a discovery sprint session |

---

## Artifact ID System

`WF-XXX` and `INT-XXX` are **section headings inside a single shared file**, not one file each. Everything else is one file per ID.

| Artifact | ID Format | Written to |
|---|---|---|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story (List) | `ST-XXX` | `features/{name}/po/usl.md` |
| Acceptance Criteria | `AC-XXX` | `features/{name}/po/usd/ST-XXX.md` (one file per story) |
| UAT Test Case | `TC-XXX` | `features/{name}/po/uat/ST-XXX.md` (one file per story) |
| Wireframe | `WF-XXX` | `features/{name}/design/wireframes.md` (**all wireframes in one file**, `## WF-XXX: Name` per screen) |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` (one file per component) |
| Component Element | `COMP-XXX-EL-YYY` | inside the parent `COMP-XXX.md` |
| Feature Brief | `artifact: BRIEF` | `features/{name}/po/brief.md` (human-written pipeline input) |
| Interaction Flow | `INT-XXX` | `features/{name}/design/interactions.md` (**one file per feature**; `## INT-001` per flow, state IDs `INT-XXX-ST-YYY`) |
| PM Strategy | `artifact: STRATEGY` | `features/{name}/pm/strategy.md` |
| PM Discovery | `artifact: OST` | `features/{name}/pm/discovery.md` |
| PM Market Research | `artifact: MARKET-RESEARCH` | `features/{name}/pm/market-research.md` |
| PM Analytics | `artifact: NSM` | `features/{name}/pm/analytics.md` |
| PM Growth | `artifact: GROWTH-LOOP` | `features/{name}/pm/growth.md` |
| PM GTM | `artifact: GTM-PLAN` | `features/{name}/pm/gtm.md` |

Authority for the single-file wireframe rule: `design-framework/stage1-wireframes/rules.md` ("One `wireframes.md` file per feature"), `skills/design-wireframe/SKILL.md`, and the reference implementation on disk.

---

## Feature Folder Structure

```
features/{feature-name}/
├── pm/                  # strategy.md, discovery.md, market-research.md,
│                        # analytics.md, growth.md, gtm.md
├── po/
│   ├── brief.md         # human-written input to the pipeline
│   ├── prd.md
│   ├── usm.md
│   ├── usl.md
│   ├── usd/             # ST-XXX.md — one file per story
│   └── uat/             # ST-XXX.md — one file per story
├── design/
│   ├── wireframes.md    # ALL WF-XXX sections for the feature
│   ├── COMP-XXX.md      # one file per component
│   └── interactions.md  # ALL interaction flows for the feature
└── code/                # optional; implementation
```

**Reference implementation:** `features/Export Customs Clearances/` is the one fully-worked feature — PM (6 artifacts) → PO (brief, PRD, USM, USL, 12 USD, 12 UAT) → Design (wireframes, 6 COMP, interactions). Read it before generating a new feature; it shows the conventions as actually applied. Note the folder name contains spaces — quote paths.

`features/Container-retail-vn/` contains only `pm/strategy.md` (a PM-only spike).

---

## Traceability Frontmatter

Every generated artifact opens with YAML frontmatter. These 7 fields are **required** and are present on all 43 artifacts on disk:

```yaml
---
artifact: PRD              # see the artifact: values table below — NOT always the same string as the ID prefix
feature: feature-name      # must match the features/ folder name exactly
version: 0.1
status: draft              # draft | review | approved
generated-by: po-brief-to-prd   # the skill that produced this file
upstream: brief.md         # input artifact (path relative to the feature folder)
downstream: usm.md         # next artifact in the chain
---
```

The `artifact-sync` skill additionally defines 5 **sync fields**. They are specified in `documentation/artifact-sync-plan.md` and advertised in `README.md`, but **no artifact on disk carries them yet** — adding them to newly generated artifacts is outstanding work, not an established convention:

```yaml
last_modified: 2026-05-21
change_summary: "One-sentence description of what changed"
change_type: additive              # additive | reductive | interface | structural
sync_status: in_sync               # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1
```

Propagation rule: `additive` → forward impacts only. `reductive` / `interface` / `structural` → forward **and** backward impacts.

### `artifact:` values actually in use

The `artifact:` value is **not** always the ID prefix — PM artifacts in particular use framework-specific codes. These are the values observed across all 43 artifacts on disk:

| File | `artifact:` |
|---|---|
| `po/brief.md` | `BRIEF` |
| `po/prd.md` | `PRD` |
| `po/usm.md` | `USM` |
| `po/usl.md` | `USL` |
| `po/usd/ST-XXX.md` | `USD` |
| `po/uat/ST-XXX.md` | `UAT` |
| `design/wireframes.md` | `WF` |
| `design/COMP-XXX.md` | `COMP` |
| `design/interactions.md` | `INT` |
| `pm/strategy.md` | `STRATEGY` |
| `pm/discovery.md` | `OST` (Opportunity Solution Tree) |
| `pm/market-research.md` | `MARKET-RESEARCH` |
| `pm/analytics.md` | `NSM` (North Star Metric) |
| `pm/growth.md` | `GROWTH-LOOP` |
| `pm/gtm.md` | `GTM-PLAN` |

The `PM-STRATEGY` / `PM-DISCOVERY` labels in the ID table are conceptual artifact names, not frontmatter values. Follow this table when writing frontmatter.

---

## Adding or renaming a skill — the full checklist

A skill is not "added" until every one of these is done. Miss one and the skill either fails to load or is invisible to three of the four supported agents.

1. `skills/{name}/SKILL.md` — with `name:` and `description:` frontmatter. The `description` is what triggers the skill; put the trigger keywords in it.
2. `ln -s ../../skills/{name} .agent/skills/{name}` — relative symlink, not a copy.
3. `CLAUDE.md` — this file: add to the Skills Registry table and bump the count in the header.
4. `AGENTS.md` **and** `skills/AGENTS.md` — keep identical.
5. `GEMINI.md` **and** `skills/GEMINI.md` — keep identical.
6. `.cursorrules` **and** `skills/.cursorrules` — keep identical.
7. `README.md` + `skills/README.md` + `GETTING_STARTED.md` + `skills/GETTING_STARTED.md` — counts and skill tables.
8. `skills/install.sh` **and** `skills/install.ps1` — the hardcoded "Skills Registry" block appended to a user's `CLAUDE.md`. This is manual; the file-copy loop is dynamic but this table is not.
9. `skills/cli.js` — the help banner states the skill count.
10. `skills/package.json` — the `files` array uses the `*/SKILL.md` glob, so a new skill's `SKILL.md` ships automatically; **any non-`SKILL.md` asset (scripts, data) needs an explicit entry**, as `ui-ux-pro-max/scripts/` and `ui-ux-pro-max/data/` have.
11. `landing-page/index.html` — user-facing counts (deployed to GitHub Pages on every push to `main`).

---

## Repo vs installed project — they are not the same

A skill behaves differently here than it does in a project someone installed the package into. Know which you are in.

| | This repo | An installed project |
|---|---|---|
| `.agent/skills/{name}` | **symlink** into `skills/{name}` — editing either path edits the same file | a **detached copy**; the installer never refreshes it, so re-running `install` skips existing skills |
| `pm-framework/`, `po-framework/`, `design-framework/`, `codebase-framework/` | present | **absent — they are not in `package.json` `files`** |
| `.claude/commands/` (6 slash commands) | present | **absent — not shipped** |

**This is a live functional gap.** Every `SKILL.md` opens with a Knowledge Base pointer such as
`po-framework/stage1-prd/rules.md`, and `skills/po-brief-to-prd/SKILL.md` goes as far as
*"Always read `po-framework/stage1-prd/rules.md` before producing a PRD."* In an installed project that path
does not exist. Skills there run on the SKILL.md body alone. Either ship the framework dirs, or make each
SKILL.md degrade gracefully when its knowledge base is missing — tracked as a known gap, not yet decided.

---

## Release contract

Publishing is tag-driven. Nothing publishes on a normal push to `main`.

1. Bump the version in **`skills/package.json` and `skills/package-lock.json`** — both, they currently disagree.
2. Commit, then `git tag v<version>` and push the tag.
3. `.github/workflows/npm-publish.yml` fires on `v*` tags only, runs with `working-directory: skills`, and
   executes `npm publish --access public` using the `NPM_TOKEN` secret.

Separately, **`.github/workflows/deploy-landing.yml` redeploys `landing-page/` to GitHub Pages on *every* push
to `main`, with no paths filter.** Any commit to main republishes the site, so stale counts there go live
immediately. `landing-page/index.html` currently still advertises "16 skills / 5 slash commands".

---

## Traps that will bite in the first ten minutes

- **Feature folder names are not slugs.** The docs write `features/{feature-name}/`, but the real folders are
  `Export Customs Clearances` (spaces, Title Case) and `Container-retail-vn`. The `feature:` frontmatter value
  mirrors the raw folder name exactly. Always quote these paths.
- **`upstream:` / `downstream:` rooting is inconsistent.** `po/` artifacts use bare filenames (`usm.md`);
  `design/` and `pm/` artifacts use feature-root-relative paths (`po/usd/`, `design/COMP-001.md`). Match the
  neighbouring artifacts rather than inventing a scheme.
- **The USD → wireframe traceability link is dead.** All 12 files in
  `features/Export Customs Clearances/po/usd/` still carry the literal placeholder `WF-XXX` in their
  Design Reference column — no real WF ID was ever written back after the wireframes were generated. Do not
  read those tables as resolved traceability.
- **`code/` has never existed.** No feature has one and no skill writes into it. It appears in the folder
  diagrams as an intended slot only.
- **No wireframe or component-spec validator skill exists.** `/validate-artifacts` runs those two stages from
  the framework `quality-gate.md` files inline; only `validate-prd` and `validate-usd` are real skills.
- **`npx ai-ready-workflow install-cowork` is macOS-only** — `skills/cli.js` hard-exits on any other platform.

---

## Working rules

- **Verify before you assert.** This repo's docs have drifted from disk before. Check `skills/*/SKILL.md` and `features/` rather than trusting a table in a README.
- **Never regenerate an artifact wholesale to fix a small change** — that is what `artifact-sync` / `/sync-check` exist for.
- **Never invent a ShadCN component name.** Check `design-framework/stage2-component-specs/shadcn-component-catalog.md`.
- **Quote paths under `features/`** — the reference feature folder name contains spaces.
- **Do not commit or push unless asked.**
- Changing anything under `skills/` changes the published npm package. Treat it as outward-facing.

---

## Known state and gotchas

Current as of the last audit. Verify before relying on any of it.

| Item | State |
|---|---|
| Version, in **three** places | `skills/package.json` = `0.2.0` (bumped in `e498c31`), but `skills/package-lock.json` still says `0.1.2`. **No `v0.2.0` git tag exists, so 0.2.0 is unpublished** — `.github/workflows/npm-publish.yml` fires only on `v*` tags. npm still serves `0.1.2`. Bump package.json **and** package-lock.json, then tag. |
| `documentation/backlog.md` | Phases 0–7e ✅. **Phase 8** (artifact-sync, `/sync-check`, agent-doc refresh) is tracked there with items 8.12–8.14 still open, plus a Known Gaps table G.1–G.5. This is the open-work index — read it first. |
| claude-mem stub files | 65 of the 66 tracked `CLAUDE.md` files are 169-byte stubs containing only a `<claude-mem-context>` block, scattered through nearly every directory. They are noise, are **not** gitignored, and are not this rulebook. **Only the root `CLAUDE.md` is real.** |
| Junk directories | `skills/documentation/`, `skills/skills/`, `.agent/skills/documentation/`, `.agent/skills/.agent/skills/`, `design-framework/design-framework/design-rules/` each contain nothing but a claude-mem stub. `skills/documentation/` and `skills/skills/` look like skills but have no `SKILL.md`, so tooling correctly ignores them. |
| `po-framework/stage2-usm/template.md` | **Missing.** Every other PO stage has one. `po-prd-to-usm` works from `rules.md` + `example.md`. |
| `design-interactions` skill | **Does not exist.** `features/.../design/interactions.md` is stamped `generated-by: design-interactions` and `design-framework/stage3-interactions/` has full rules and templates, but no skill wraps it. Stage 3 is manual. |
| `pm-to-po-handoff` | Appears as a `generated-by` value on disk; no such skill exists. |
| `ui-ux-pro-max` counts | Corrected to the real database: **67 styles, 96 palettes, 57 font pairings, 25 charts, 99 UX guidelines, 13 stacks**. Note this session's environment may also expose a *different* global `ui-ux-pro-max` plugin skill with other numbers — the repo's copy is the one under `skills/`. |
| `codebase-framework/templates/`, `codebase-framework/testing-patterns/` | Empty (`.gitkeep` only). |
| `.claude/commands/CLAUDE.md` | A claude-mem stub, not a command. There are 6 real commands. |

---

## ui-ux-pro-max Usage

Requires Python 3. Run the search script before generating UI:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "your query"
```

Domains (`--domain`, from `CSV_CONFIG` in `scripts/core.py`): `style`, `color`, `chart`, `landing`, `product`, `ux`, `typography`, `icons`, `react`, `web`. (The docstring at the top of `search.py` is out of date — it lists a nonexistent `prompt` domain and omits `icons`/`react`/`web`.)
Stack-scoped lookups: `--stack <name>` over the 13 stacks in `skills/ui-ux-pro-max/data/stacks/`.
Design-system generation: `--design-system [--persist] [-p "Project"] [--page "dashboard"]`.

---

## Multi-Agent Compatibility

| Agent | Entry Point | Activation |
|---|---|---|
| Claude Code | `.agent/skills/*/SKILL.md` | auto-loaded on trigger keyword |
| OpenAI Codex | `AGENTS.md` | "Read AGENTS.md then …" |
| Gemini Code Assist | `GEMINI.md` | "Read GEMINI.md then …" |
| Cursor | `.cursorrules` | auto-loaded on project open |
| Claude Desktop (chat) | `skills/mcp-server.js` via `npx ai-ready-workflow mcp` | MCP resources + `/` prompt picker |
| Any agent | `skills/*/SKILL.md` | read directly |

---

## Install into Another Project

```bash
# Option A — npx (no clone needed)
npx ai-ready-workflow install

# Option B — from this repo (Mac/Linux)
./skills/install.sh

# Option C — from this repo (Windows)
.\skills\install.ps1

# Option D — Claude Desktop Cowork / Local Agent mode (macOS only)
npx ai-ready-workflow install-cowork
```

The installer copies every directory containing a `SKILL.md` into the target's `.agent/skills/`, copies `AGENTS.md` / `GEMINI.md` / `.cursorrules` / `GETTING_STARTED.md` to the target root, and appends a Skills Registry section to an existing `CLAUDE.md`. It detects already-installed skills and skips them — safe to re-run.
