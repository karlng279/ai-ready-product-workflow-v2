# AI-Ready Product Workflow v2 — Full Audit & Restructure Plan

## Context

After a full read of 126 markdown files across all three frameworks, the three v2 planning documents, and research into the pm-skills reference repo, this plan addresses:

1. An honest assessment of what to keep vs. replace from the v2 plans
2. The PM framework addition (6 skills)
3. A complete restructuring roadmap to align with 2025–2026 Claude Code standards

---

## Part 1: Honest Assessment of v2 Plans

### What the v2 plans proposed

The three docs describe a **Node.js 20+ CLI application** with:
- A custom Skill Engine (TypeScript, Commander.js, Anthropic SDK, Zod)
- A custom Validation Engine
- A custom MCP Client (to call Figma)
- A custom Orchestrator that enforces workflow stages
- 16 skills defined as folders with `prompt.system.md`, `prompt.user.md`, `contract.input.json`, `contract.output.json`
- CLI commands: `workflow init`, `workflow run`, `workflow run-pipeline`, `workflow status`, `workflow validate`

### The verdict: The CLI approach is over-engineered and already obsolete

**The problem with the v2 plan:** It was designed to solve infrastructure gaps that Claude Code has since solved natively. Building a custom skill engine, orchestrator, and MCP client in Node.js duplicates what Claude Code already provides — and adds a maintenance burden without benefit.

#### What should be SCRAPPED from the v2 plans

| v2 Plan Component | Why Scrap It | Modern Replacement |
|---|---|---|
| Node.js CLI (`src/`, `workflow` commands) | Claude Code is already the CLI; a wrapper around a wrapper | Native Claude Code slash commands via `.claude/commands/` |
| Custom Skill Engine (TypeScript) | Claude Code natively loads `.agent/skills/` | Skills in `.agent/skills/` (markdown-only, no runtime) |
| Custom Orchestrator | Adds complexity; rigid stage-gating blocks creative AI use | CLAUDE.md + workflow commands chain steps naturally |
| Custom MCP Client | Figma MCP is already available as a native MCP tool | Use the Figma MCP tool directly in Claude Code |
| Custom Validation Engine (Zod + JSON schema) | Over-engineered for document validation | Validation as AI skills (validate-prd, validate-usd) |
| `contract.input.json` / `contract.output.json` | Strict JSON contracts fight LLM flexibility | Well-crafted prompt templates in skill markdown files |
| `workflow-stages.json`, `ai-models.json`, `mcp-servers.json` | Config for an engine that won't exist | `CLAUDE.md` holds all framework rules |

**What should be KEPT from the v2 plans:**

| Concept | Keep | How |
|---|---|---|
| Skill-based artifact generation (16 skills) | ✅ Keep the concept | Implement as `.agent/skills/` entries, not Node.js modules |
| Artifact traceability (YAML frontmatter) | ✅ Keep | Add to templates as markdown frontmatter |
| Figma integration | ❌ Out of scope | Removed from plan entirely |
| Quality gates per stage | ✅ Keep | Already exist in the knowledge base |
| Pipeline workflow idea | ✅ Keep | Implement as `.claude/commands/` slash commands |
| Skill categories (PO, validation, design, MCP) | ✅ Keep | Organize under `.agent/skills/` |

### What to keep from the existing v1 repo

| Component | Status | Action |
|---|---|---|
| `po-framework/` (5-stage artifact pipeline) | ✅ Excellent | Keep as-is; add frontmatter to templates |
| `design-framework/` (3-stage design pipeline) | ✅ Excellent | Keep as-is |
| `codebase-framework/` (Next.js patterns) | ✅ Solid | Keep; minor updates for Next.js 15 App Router |
| `design-framework/themes/` (4 themes) | ✅ Production-ready | Keep all 4 |
| `.agent/skills/ui-ux-pro-max/` | ✅ Working | Keep; register in CLAUDE.md |
| Artifact ID system (PRD-XXX, ST-XXX, etc.) | ✅ Clean | Keep as canonical |
| Quality gate checklists | ✅ Valuable | Keep; reference from new validation skills |
| `features/` output folder structure | ✅ Good | Keep; add `pm/` subfolder for PM artifacts |

### What to UPGRADE in the existing v1 repo

| Current Gap | Upgrade |
|---|---|
| CLAUDE.md is empty | Fill with full framework rules, skill registry, workflow overview |
| No slash commands | Add `.claude/commands/` for key pipelines |
| No PO automation skills | Add brief-to-prd, prd-to-usm, etc. as skills |
| No PM framework | Add pm-framework (this plan's main deliverable) |
| No validation skills | Add validate-prd, validate-usd, validate-traceability as skills |
| README.md is thin | Expand to include skill usage and slash command reference |

---

## Part 1b: Honest Assessment — Design Framework Skills

### Are `design-wireframe` and `design-component-spec` skills worth adding?

**Short answer: Yes, but understand what they are and aren't.**

The design-framework already has:
- `ui-ux-pro-max` — the design **intelligence** (styles, palettes, typography, UX guidelines via Python + CSV databases)
- `design-framework/stage1-wireframes/rules.md` — the wireframe **format spec** (WF-XXX ID, ASCII conventions, AC mapping, responsive sections)
- `design-framework/stage2-component-specs/rules.md` — the component spec **format** (COMP-XXX, ShadCN props, variants, states)

The gap the skills would fill: when Claude generates a wireframe, it currently needs to read `rules.md` + `examples.md` + know the theme constraints + know the AC mapping requirement. Without a skill, Claude does generic ASCII wireframes — not WF-003 with `AC-007, AC-008` mapping and the MDS theme constraints.

**Skills are not design intelligence — they are format convention enforcement.** They load the repo's specific ID system, section requirements, AC traceability rules, and ShadCN component catalogue reference into Claude's active context automatically.

**My judgment:**
- `design-wireframe/SKILL.md` — **Worth adding.** Encodes WF-XXX format, ASCII conventions, AC mapping, responsive sections, theme reference. Without it, Claude will produce non-standard wireframes that break traceability.
- `design-component-spec/SKILL.md` — **Worth adding, but scoped narrowly.** Encodes COMP-XXX format, ShadCN component reference, variant/prop/state specification. Does NOT replace `ui-ux-pro-max` (which handles design reasoning). These two skills work in sequence: `ui-ux-pro-max` → design system → `design-component-spec` → COMP-XXX artifact.

**What they are NOT:** They will not make Claude produce better-looking designs — that is `ui-ux-pro-max`'s job. These skills ensure the output is in the right format for downstream traceability.

**Figma is out of scope for this version.** No Figma integration, no design-figma-handoff skill. The design pipeline ends at COMP-XXX component specs.

---

## Part 2: PM Framework — `pm-framework`

### Design philosophy

Reference: `phuryn/pm-skills` (100+ skills across 8 plugins). The PM framework follows the same pattern as `ui-ux-pro-max`: a skill markdown file that teaches Claude both PM methodology (the why) and execution guidance (the how), grounded in proven frameworks (Teresa Torres, Marty Cagan, Strategyzer).

Each PM skill is a `.agent/skills/<skill-name>/SKILL.md` file. No Python, no CSV databases. Knowledge is embedded in the skill markdown itself — Claude's context window is the query engine.

### The 6 Skills

#### 1. `pm-product-strategy`
**Triggers:** product strategy, vision, mission, SWOT, competitive analysis, OKRs, positioning
**Frameworks covered:**
- Product Strategy Canvas (Strategyzer)
- OKR hierarchy (Objective → Key Results → Initiatives)
- SWOT + Porter's Five Forces + Ansoff Matrix
- Competitive positioning maps
- Vision/Mission statement templates
- Jobs-to-be-Done (JTBD) strategic lens

#### 2. `pm-product-discovery`
**Triggers:** customer discovery, user research, Jobs-to-be-Done, assumption mapping, opportunity tree, experiment
**Frameworks covered:**
- Opportunity Solution Tree (Teresa Torres)
- Assumption Mapping (Riskiest Assumption Tests)
- Customer Interview guide (JTBD interview script)
- Jobs-to-be-Done (main/micro jobs, desired outcomes)
- Continuous Discovery habits cadence
- Experiment design (pretotype → prototype → test)

#### 3. `pm-market-research`
**Triggers:** market research, persona, TAM, segmentation, journey map, competitive analysis, ICP
**Frameworks covered:**
- Persona creation (Jobs-aware personas with pain/gain/job)
- TAM / SAM / SOM sizing methodology
- Customer Segmentation (behavioral, psychographic, demographic)
- Customer Journey Map (stages, touchpoints, emotions, opportunities)
- Competitive analysis matrix (features, pricing, positioning)
- Market sizing via bottoms-up and tops-down

#### 4. `pm-data-analytics`
**Triggers:** metrics, KPIs, A/B test, cohort, SQL, funnel, analytics, North Star
**Frameworks covered:**
- North Star Metric framework (1 NSM + 5–7 input metrics)
- HEART framework (Google: Happiness, Engagement, Adoption, Retention, Task Success)
- Funnel analysis (acquisition → activation → retention → referral → revenue)
- A/B test design (hypothesis, sample size, duration, success criteria)
- Cohort analysis interpretation
- SQL query generation for product analytics (BigQuery / PostgreSQL dialect)
- AARRR (Pirate Metrics) vs. RARRA framework selection

#### 5. `pm-marketing-growth`
**Triggers:** growth, positioning, value proposition, North Star, growth loop, acquisition, retention, monetization
**Frameworks covered:**
- Value Proposition Canvas (Strategyzer)
- Positioning statement formula (Geoffrey Moore)
- Growth Loop design (viral, content, paid, product-led)
- PLG (Product-Led Growth) flywheel
- Activation optimization (aha moment identification)
- Retention mechanics (habit loops, notifications, re-engagement)
- North Star metric + growth model alignment

#### 6. `pm-go-to-market`
**Triggers:** go-to-market, GTM, launch, ICP, beachhead, pricing, battlecard, sales enablement
**Frameworks covered:**
- ICP (Ideal Customer Profile) definition
- Beachhead market selection (crossing the chasm)
- GTM motion selection (PLG, SLG, MLG, community-led)
- Launch plan (alpha → beta → GA)
- Pricing strategy (value-based, cost-plus, competitive, freemium)
- Battlecard template (vs. Competitor X: strengths, weaknesses, win stories, landmines)
- Sales enablement deck outline

---

## Part 2b: Multi-Agent Compatibility Strategy

### The problem with `.agent/skills/`

The `.agent/skills/` directory is **Claude Code-specific**. Other AI agents have their own context-loading conventions:

| Agent | Context File | Discovery Mechanism |
|---|---|---|
| Claude Code | `.agent/skills/*/SKILL.md` | Auto-loads on skill match |
| Codex (OpenAI) | `AGENTS.md` | Single context file |
| Cursor | `.cursorrules` | Single rules file |
| Gemini Code Assist | `GEMINI.md` | Single context file |
| Windsurf | `.windsurfrules` | Single rules file |
| Claude Desktop | `~/.claude/CLAUDE.md` | Global context |

### The strategy: Two-layer architecture

**Layer 1 — Agent-agnostic knowledge base (the source of truth)**
Move all skills from `.agent/skills/` to a top-level `skills/` directory. Skills are pure markdown — no Claude-specific syntax, no Python dependencies beyond the existing ui-ux-pro-max scripts. Any AI agent that can read a markdown file can use these skills.

**Layer 2 — Agent-specific entry points (thin wrappers)**
Each AI agent gets a config file that indexes the skills:
- `.agent/skills/*/SKILL.md` → symlinks or copies from `skills/*/SKILL.md` (Claude Code)
- `AGENTS.md` → imports or references the relevant skills (Codex)
- `.cursorrules` → imports skill content (Cursor)
- `GEMINI.md` → references skills (Gemini)

**Layer 3 (future) — MCP Server: the universal interface**
See Part 2c below. This is the real long-term answer.

### Practical implementation now

For the v2 restructure, the change is simple:

```
# Current (Claude-only)
.agent/skills/pm-product-strategy/SKILL.md

# New (agent-agnostic)
skills/pm-product-strategy/SKILL.md        ← source of truth
.agent/skills/pm-product-strategy/SKILL.md ← symlink (Claude Code)
AGENTS.md                                  ← lists all skills with descriptions (Codex)
GEMINI.md                                  ← same (Gemini)
```

The knowledge base in `skills/*.md` becomes the **portable artifact**. Each AI agent gets its own "door" into the same knowledge.

---

## Part 2c: Distributable via npm + Optional Local MCP (No Hosting Required)

### Clarifying MCP hosting — you are partially right

There are **two very different types of MCP servers:**

| Type | Transport | Hosting | Example |
|---|---|---|---|
| **Remote MCP** | HTTP/SSE | YES — needs a server URL you own | Figma MCP, Atlassian MCP |
| **Local MCP (stdio)** | stdin/stdout | NO — runs on the user's machine | filesystem MCP, sequential-thinking MCP |

You are correct that **remote MCP needs hosting** — that is a real cost and barrier. But **local MCP (stdio) is just an npm package** that runs as a local process. No server, no hosting, no infrastructure. Claude Desktop and Claude Code both support local MCP servers configured in `settings.json` pointing to a locally installed package.

This means: **npm IS the distribution format, and it can optionally also expose a local MCP interface**. The same npm package serves both:
- Pure file-copy install (simple, works everywhere)
- Local MCP server (advanced, enables Claude Desktop integration)

Neither requires you to host anything.

### The distribution plan (npm-first, no hosting)

#### Phase 1 — Now: Git + install script (zero infrastructure)
```
skills/
├── install.sh          # ./install.sh → copies skills to .agent/skills/ and appends CLAUDE.md
├── install.ps1         # Windows
└── package.json        # Makes it npx-runnable: npx ai-ready-workflow install
```

Install experience:
```bash
# Option A: npx (no clone needed)
npx ai-ready-workflow install

# Option B: manual
git clone <repo> && ./skills/install.sh
```

The script copies `skills/*/SKILL.md` to the user's `.agent/skills/` and patches their `CLAUDE.md` with the skill registry.

#### Phase 2 — Later: npm package with local MCP (no hosting)
The same npm package adds a `serve` command that starts a stdio MCP server locally:
```bash
npm install -g ai-ready-workflow-skills
# Then in Claude Desktop settings.json:
{
  "mcpServers": {
    "ai-ready-workflow": {
      "command": "ai-ready-workflow-skills",
      "args": ["serve"]
    }
  }
}
```

Skills become MCP `prompt` templates. Claude Desktop loads them via local process. No server, no URL, no hosting cost.

**Bottom line:** Your npm instinct is correct. npm IS the right distribution format. The local MCP interface is an optional enhancement on top of the same npm package — not a separate infrastructure concern.

### What NOT to do
- Do NOT build a custom CLI that wraps Claude or re-implements a workflow engine (this was the v2 plan's mistake)
- Do NOT host a remote MCP server (you are right, this has cost and complexity)
- Do NOT create separate npm packages per skill — one monorepo package with all skills is the right shape

---

## Part 3: Full Repo Restructure Plan

### New directory structure

```
ai-ready-product-workflow-v2/
│
├── CLAUDE.md                          # [REWRITE] Full framework rules, skill registry, workflow
├── AGENTS.md                          # [NEW] OpenAI Codex / OpenAI Agents index
├── GEMINI.md                          # [NEW] Gemini Code Assist index
├── README.md                          # [UPDATE] Add skill/command reference
├── GETTING_STARTED.md                 # [MINOR UPDATE] Add PM framework path
├── CONTRIBUTING.md                    # [KEEP AS-IS]
│
├── .claude/
│   ├── settings.json                  # [KEEP] claude-mem plugin enabled
│   └── commands/                      # [NEW] Slash commands (Claude Code only)
│       ├── po-pipeline.md             # /po-pipeline — brief → UAT
│       ├── design-pipeline.md         # /design-pipeline — USD → wireframes → component specs
│       ├── validate-artifacts.md      # /validate-artifacts — run all quality gates
│       ├── pm-strategy.md             # /pm-strategy — product strategy session
│       └── pm-discovery.md            # /pm-discovery — discovery sprint session
│
├── skills/                            # [NEW] Agent-agnostic skill source of truth
│   ├── install.sh                     # ./skills/install.sh → copies skills to local agent
│   ├── install.ps1                    # Windows version
│   ├── package.json                   # Enables: npx ai-ready-workflow install
│   │
│   ├── ui-ux-pro-max/                 # [MOVED FROM .agent/skills/]
│   │   ├── SKILL.md
│   │   └── scripts/ + data/           # Python scripts stay here
│   │
│   ├── po-brief-to-prd/               # [NEW] Converts feature brief to PRD
│   │   └── SKILL.md
│   ├── po-prd-to-usm/                 # [NEW] PRD → User Story Map
│   │   └── SKILL.md
│   ├── po-usm-to-usl/                 # [NEW] USM → User Story List (MoSCoW)
│   │   └── SKILL.md
│   ├── po-usl-to-usd/                 # [NEW] USL → User Story Details (AC-XXX)
│   │   └── SKILL.md
│   ├── po-usd-to-uat/                 # [NEW] USD → UAT BDD scenarios
│   │   └── SKILL.md
│   ├── validate-prd/                  # [NEW] PRD quality gate checker
│   │   └── SKILL.md
│   ├── validate-usd/                  # [NEW] USD/AC completeness checker
│   │   └── SKILL.md
│   ├── design-wireframe/              # [NEW] WF-XXX format enforcement + AC mapping
│   │   └── SKILL.md
│   ├── design-component-spec/         # [NEW] COMP-XXX format + ShadCN component reference
│   │   └── SKILL.md
│   │
│   ├── pm-product-strategy/           # [NEW] PM Framework
│   │   └── SKILL.md
│   ├── pm-product-discovery/          # [NEW] PM Framework
│   │   └── SKILL.md
│   ├── pm-market-research/            # [NEW] PM Framework
│   │   └── SKILL.md
│   ├── pm-data-analytics/             # [NEW] PM Framework
│   │   └── SKILL.md
│   ├── pm-marketing-growth/           # [NEW] PM Framework
│   │   └── SKILL.md
│   └── pm-go-to-market/               # [NEW] PM Framework
│       └── SKILL.md
│
├── .agent/
│   └── skills/                        # [Claude Code entry point — symlinks to skills/]
│       ├── ui-ux-pro-max → ../../skills/ui-ux-pro-max
│       ├── po-brief-to-prd → ../../skills/po-brief-to-prd
│       └── ... (all skills symlinked)
│
├── po-framework/                      # [KEEP] Update templates with frontmatter
├── design-framework/                  # [KEEP] No changes
├── codebase-framework/                # [KEEP] Minor Next.js 15 updates
│
├── pm-framework/                      # [NEW] PM methodology knowledge base
│   ├── README.md
│   ├── pm-workflow.md                 # How PM skills chain together
│   ├── product-strategy/
│   │   ├── rules.md
│   │   ├── templates/
│   │   │   ├── strategy-canvas.md
│   │   │   ├── okr-template.md
│   │   │   └── competitive-analysis.md
│   │   └── examples/
│   ├── product-discovery/
│   │   ├── rules.md
│   │   ├── templates/
│   │   │   ├── opportunity-solution-tree.md
│   │   │   ├── customer-interview-guide.md
│   │   │   └── assumption-map.md
│   │   └── examples/
│   ├── market-research/
│   │   ├── rules.md
│   │   ├── templates/
│   │   │   ├── persona-template.md
│   │   │   ├── tam-sam-som.md
│   │   │   └── journey-map.md
│   │   └── examples/
│   ├── data-analytics/
│   │   ├── rules.md
│   │   ├── templates/
│   │   │   ├── north-star-metric.md
│   │   │   ├── ab-test-design.md
│   │   │   └── funnel-analysis.md
│   │   └── examples/
│   ├── marketing-growth/
│   │   ├── rules.md
│   │   ├── templates/
│   │   │   ├── value-proposition-canvas.md
│   │   │   ├── positioning-statement.md
│   │   │   └── growth-loop-design.md
│   │   └── examples/
│   └── go-to-market/
│       ├── rules.md
│       ├── templates/
│       │   ├── icp-template.md
│       │   ├── launch-plan.md
│       │   └── battlecard.md
│       └── examples/
│
└── features/                          # [KEEP] Add pm/ subfolder to feature structure
    └── {feature-name}/
        ├── pm/                        # [NEW subfolder]
        │   ├── strategy.md
        │   ├── discovery.md
        │   └── gtm.md
        ├── po/
        ├── design/
        └── code/
```

### Key decisions explained

#### Why `.agent/skills/` over v2's Node.js approach
Claude Code natively discovers skills in `.agent/skills/` — no runtime to build, no CLI to install, no Anthropic SDK wrapper to maintain. A skill is just a markdown file with YAML frontmatter (`name`, `description`) that Claude reads and follows. Zero maintenance surface area.

#### Why `.claude/commands/` for pipelines
Slash commands (`.claude/commands/*.md`) are exactly what the v2 "orchestrator" tried to build: they chain steps into a workflow, enforce order, and can reference upstream artifacts. But they run in Claude Code natively with full context of the repo — no Node.js glue needed.

#### Why no custom MCP client
Figma integration is out of scope for this version. No MCP client is needed in the current plan.

#### Why pm-framework gets both a skills/ folder AND a knowledge base folder
- `.agent/skills/pm-*/` — gives Claude live, actionable guidance when the user triggers PM work
- `pm-framework/` — provides the human-readable knowledge base, templates, and examples (same pattern as po-framework, design-framework)

---

## Part 4: CLAUDE.md Rewrite (Key Contents)

The empty CLAUDE.md should become the **framework rulebook**:

```markdown
# AI-Ready Product Workflow v2

## Frameworks
- **PO Framework** (`po-framework/`): 5-stage: PRD → USM → USL → USD → UAT
- **Design Framework** (`design-framework/`): 3-stage: Wireframes → Component Specs → Interactions
- **Codebase Framework** (`codebase-framework/`): Next.js 15 + ShadCN + TanStack
- **PM Framework** (`pm-framework/`): Strategy → Discovery → Research → Analytics → Growth → GTM

## Skills Registry
- `ui-ux-pro-max` — UI/UX design (run python3 scripts/search.py)
- `po-brief-to-prd`, `po-prd-to-usm`, ... — PO artifact pipeline
- `pm-product-strategy`, `pm-product-discovery`, ... — PM skills

## Slash Commands
- `/po-pipeline` — Run the full PO pipeline for a feature brief
- `/design-pipeline` — Generate wireframes and component specs from USD
- `/validate-artifacts` — Quality gate check on current feature
- `/pm-strategy` — Start a product strategy session
- `/pm-discovery` — Start a discovery sprint

## Artifact ID System
| Type | Format | Location |
|---|---|---|
| PRD | PRD-XXX | `po/prd.md` |
| User Story | ST-XXX | `po/usl.md` |
| Acceptance Criteria | AC-XXX | `po/usd/ST-XXX.md` |
| Wireframe | WF-XXX | `design/WF-XXX.md` |
| Component | COMP-XXX | `design/COMP-XXX.md` |

## Traceability Frontmatter (required on all generated artifacts)
---
artifact: PRD
feature: [feature-name]
version: 0.1
status: draft
generated-by: po-brief-to-prd
upstream: brief.md
downstream: usm.md
---
```

---

## Implementation Sequence

### Phase 0 — Foundation (1–2 hours)
- [ ] Rewrite `CLAUDE.md` with full framework rulebook + skill registry
- [ ] Create top-level `skills/` directory; move `ui-ux-pro-max` from `.agent/skills/` to `skills/`
- [ ] Create `.agent/skills/` symlinks pointing to `skills/*/`
- [ ] Create `AGENTS.md` (Codex) and `GEMINI.md` (Gemini) with skill index
- [ ] Add frontmatter traceability headers to key po-framework templates (prd, usd, uat)
- [ ] Create `pm-framework/README.md` and folder structure

### Phase 1 — PM Framework Knowledge Base (4–6 hours)
- [ ] Write `pm-framework/product-strategy/` (rules + 3 templates + 1 example)
- [ ] Write `pm-framework/product-discovery/` (rules + 3 templates + 1 example)
- [ ] Write `pm-framework/market-research/` (rules + 3 templates + 1 example)
- [ ] Write `pm-framework/data-analytics/` (rules + 3 templates + 1 example)
- [ ] Write `pm-framework/marketing-growth/` (rules + 3 templates + 1 example)
- [ ] Write `pm-framework/go-to-market/` (rules + 3 templates + 1 example)

### Phase 2 — PM Skills (3–4 hours)
- [ ] Write `skills/pm-product-strategy/SKILL.md`
- [ ] Write `skills/pm-product-discovery/SKILL.md`
- [ ] Write `skills/pm-market-research/SKILL.md`
- [ ] Write `skills/pm-data-analytics/SKILL.md`
- [ ] Write `skills/pm-marketing-growth/SKILL.md`
- [ ] Write `skills/pm-go-to-market/SKILL.md`

### Phase 3 — PO Automation Skills (3–4 hours)
- [ ] Write `skills/po-brief-to-prd/SKILL.md`
- [ ] Write `skills/po-prd-to-usm/SKILL.md`
- [ ] Write `skills/po-usm-to-usl/SKILL.md`
- [ ] Write `skills/po-usl-to-usd/SKILL.md`
- [ ] Write `skills/po-usd-to-uat/SKILL.md`
- [ ] Write `skills/validate-prd/SKILL.md`
- [ ] Write `skills/validate-usd/SKILL.md`

### Phase 4 — Design Skills (1–2 hours)
- [ ] Write `skills/design-wireframe/SKILL.md` (WF-XXX format, AC mapping, ASCII conventions)
- [ ] Write `skills/design-component-spec/SKILL.md` (COMP-XXX format, ShadCN reference)

### Phase 5 — Slash Commands (2 hours)
- [ ] Write `.claude/commands/po-pipeline.md`
- [ ] Write `.claude/commands/design-pipeline.md`
- [ ] Write `.claude/commands/validate-artifacts.md`
- [ ] Write `.claude/commands/pm-strategy.md`
- [ ] Write `.claude/commands/pm-discovery.md`

### Phase 6 — Distribution Layer (1–2 hours)
- [ ] Write `skills/install.sh` (copies skills to `.agent/skills/` for Claude Code)
- [ ] Write `skills/package.json` (enables `npx ai-ready-workflow install`)
- [ ] Document MCP server as a future milestone in `docs/roadmap.md`

### Phase 7 — Cleanup: Remove Obsolete Docs (30 min)
Delete files that contain v1 assumptions or the now-scrapped v2 Node.js CLI plan:
- [ ] Delete `ai_ready_workflow_v2_prd.md`
- [ ] Delete `ai_ready_workflow_v2_implementation_plan.md`
- [ ] Delete `ai_ready_workflow_v2_technical_architecture.md`
- [ ] Delete `codebase-framework/FRAMEWORK_INTEGRATION.md` (v1 cross-framework mapping, now superseded by CLAUDE.md)

### Phase 8 — Update All README Files (1–2 hours)
Every framework directory has a README that must reflect the new structure:
- [ ] `README.md` (root) — full framework overview, skill/command reference, install instructions
- [ ] `GETTING_STARTED.md` (root) — add PM framework learning path (6th path)
- [ ] `po-framework/README.md` — add note that PO skills in `skills/po-*/` automate this workflow
- [ ] `design-framework/README.md` — add note that design skills enforce format; Figma section removed
- [ ] `codebase-framework/README.md` — update tech stack references (Next.js 15 App Router)
- [ ] `pm-framework/README.md` — write fresh (new framework, no existing README)
- [ ] `skills/README.md` — write: lists all skills, trigger keywords, install instructions

### Phase 9 — Record Plan in Documentation (15 min)
- [ ] Copy final plan to `documentation/restructure-plan-v2.md` for future reference

---

## Verification

After implementation, verify end-to-end:
1. `CLAUDE.md` loads and Claude can recite the framework structure from memory
2. Typing `pm-product-strategy` context triggers the skill (Claude references the skill's frameworks)
3. `/po-pipeline` slash command chains brief → PRD → USM correctly
4. `/pm-discovery` produces an Opportunity Solution Tree using Teresa Torres format
5. `design-component-spec` skill produces valid COMP-XXX artifacts with ShadCN references
6. A test feature in `features/test-feature/` has all subfolders: `pm/`, `po/`, `design/`, `code/`
7. All artifacts have proper YAML frontmatter traceability headers

---

## Summary of Recommendation

| Decision | Recommendation |
|---|---|
| v2 Node.js CLI | **Scrap entirely** — Claude Code is already the CLI |
| v2 custom Skill Engine | **Scrap** — use native skills in `skills/` directory |
| v2 Orchestrator | **Scrap** — use `.claude/commands/` slash commands |
| v2 custom MCP client | **Scrap** — Figma out of scope; no MCP client needed |
| v1 knowledge base (3 frameworks, 126 files) | **Keep** — core value, excellent quality |
| Artifact ID system + quality gates | **Keep** — add frontmatter traceability |
| ui-ux-pro-max skill | **Keep + Move** — to `skills/ui-ux-pro-max/` (agent-agnostic) |
| `.agent/skills/` (Claude-only path) | **Keep as symlink layer** — points to `skills/` source |
| PM Framework | **Add** — 6 skills + knowledge base |
| Design skills (wireframe, component-spec) | **Add** — format enforcement, not design intelligence; Figma out of scope |
| Multi-agent compatibility | **Add** — `AGENTS.md`, `GEMINI.md` as agent-specific indexes |
| CLI distribution | **Phase 1: `install.sh` + npx; Phase 2: local stdio MCP (no hosting)** |
| MCP hosting concern | **Not needed** — local stdio MCP = npm package, runs on user machine |
