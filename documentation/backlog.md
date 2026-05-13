# Restructure Backlog — AI-Ready Product Workflow v2

Tracks implementation progress of the restructure plan defined in [restructure-plan-v2.md](restructure-plan-v2.md).

**Legend:** ✅ Done | 🔄 In Progress | ⬜ Not Started

---

## Phase 0 — Foundation

**Goal:** Core infrastructure — CLAUDE.md, skills/ directory, agent indexes, pm-framework scaffold.
**Commit:** `feat: phase 0 - foundation (CLAUDE.md, skills/, AGENTS.md, GEMINI.md, pm-framework scaffold)`

| # | Task | Status |
|---|------|--------|
| 0.1 | Save restructure plan to `documentation/restructure-plan-v2.md` | ✅ Done |
| 0.2 | Rewrite root `CLAUDE.md` with full framework rulebook + skill registry | ✅ Done |
| 0.3 | Create `skills/` directory; move `ui-ux-pro-max` from `.agent/skills/` to `skills/` | ✅ Done |
| 0.4 | Update `.agent/skills/ui-ux-pro-max` → symlink to `skills/ui-ux-pro-max` | ✅ Done |
| 0.5 | Create `AGENTS.md` (OpenAI Codex / Agents skill index) | ✅ Done |
| 0.6 | Create `GEMINI.md` (Gemini Code Assist skill index) | ✅ Done |
| 0.7 | Add YAML frontmatter to `po-framework/stage4-usd/template.md` | ✅ Done |
| 0.8 | Add YAML frontmatter to `po-framework/stage5-uat/template.md` | ✅ Done |
| 0.9 | Create missing `po-framework/stage1-prd/template.md` | ✅ Done |
| 0.10 | Create `pm-framework/` directory structure (6 areas × rules + templates + examples) | ✅ Done |
| 0.11 | Write `pm-framework/README.md` and `pm-framework/pm-workflow.md` | ✅ Done |

---

## Phase 1 — PM Framework Knowledge Base

**Goal:** Write `rules.md`, 3 templates, and 1 example for each of the 6 PM areas.
**Commit:** `feat: phase 1 - pm-framework knowledge base (rules, templates, examples)`

| # | Task | Status |
|---|------|--------|
| 1.1 | `pm-framework/product-strategy/rules.md` | ✅ Done |
| 1.2 | `pm-framework/product-strategy/templates/` (strategy-canvas, okr-template, competitive-analysis) | ✅ Done |
| 1.3 | `pm-framework/product-strategy/examples/` (example-strategy-canvas) | ✅ Done |
| 1.4 | `pm-framework/product-discovery/rules.md` | ✅ Done |
| 1.5 | `pm-framework/product-discovery/templates/` (opportunity-solution-tree, customer-interview-guide, assumption-map) | ✅ Done |
| 1.6 | `pm-framework/product-discovery/examples/` (example-ost) | ✅ Done |
| 1.7 | `pm-framework/market-research/rules.md` | ✅ Done |
| 1.8 | `pm-framework/market-research/templates/` (persona-template, tam-sam-som, journey-map) | ✅ Done |
| 1.9 | `pm-framework/market-research/examples/` (example-persona) | ✅ Done |
| 1.10 | `pm-framework/data-analytics/rules.md` | ✅ Done |
| 1.11 | `pm-framework/data-analytics/templates/` (north-star-metric, ab-test-design, funnel-analysis) | ✅ Done |
| 1.12 | `pm-framework/data-analytics/examples/` (example-north-star) | ✅ Done |
| 1.13 | `pm-framework/marketing-growth/rules.md` | ✅ Done |
| 1.14 | `pm-framework/marketing-growth/templates/` (value-proposition-canvas, positioning-statement, growth-loop-design) | ✅ Done |
| 1.15 | `pm-framework/marketing-growth/examples/` (example-growth-loop) | ✅ Done |
| 1.16 | `pm-framework/go-to-market/rules.md` | ✅ Done |
| 1.17 | `pm-framework/go-to-market/templates/` (icp-template, launch-plan, battlecard) | ✅ Done |
| 1.18 | `pm-framework/go-to-market/examples/` (example-gtm-plan) | ✅ Done |

---

## Phase 2 — PM Skills

**Goal:** Write 6 SKILL.md files in `skills/pm-*/` so Claude auto-loads PM methodology on trigger.
**Commit:** `feat: phase 2 - pm skills (6 SKILL.md files)`

| # | Task | Status |
|---|------|--------|
| 2.1 | `skills/pm-product-strategy/SKILL.md` | ✅ Done |
| 2.2 | `skills/pm-product-discovery/SKILL.md` | ✅ Done |
| 2.3 | `skills/pm-market-research/SKILL.md` | ✅ Done |
| 2.4 | `skills/pm-data-analytics/SKILL.md` | ✅ Done |
| 2.5 | `skills/pm-marketing-growth/SKILL.md` | ✅ Done |
| 2.6 | `skills/pm-go-to-market/SKILL.md` | ✅ Done |
| 2.7 | Create `.agent/skills/` symlinks for all 6 PM skills | ✅ Done |

---

## Phase 3 — PO Automation Skills

**Goal:** Write 7 SKILL.md files (5 PO pipeline + 2 validation) in `skills/po-*/`.
**Commit:** `feat: phase 3 - po automation skills (7 SKILL.md files)`

| # | Task | Status |
|---|------|--------|
| 3.1 | `skills/po-brief-to-prd/SKILL.md` | ✅ Done |
| 3.2 | `skills/po-prd-to-usm/SKILL.md` | ✅ Done |
| 3.3 | `skills/po-usm-to-usl/SKILL.md` | ✅ Done |
| 3.4 | `skills/po-usl-to-usd/SKILL.md` | ✅ Done |
| 3.5 | `skills/po-usd-to-uat/SKILL.md` | ✅ Done |
| 3.6 | `skills/validate-prd/SKILL.md` | ✅ Done |
| 3.7 | `skills/validate-usd/SKILL.md` | ✅ Done |
| 3.8 | Create `.agent/skills/` symlinks for all 7 PO skills | ✅ Done |

---

## Phase 4 — Design Skills

**Goal:** Write 2 SKILL.md files for design format enforcement (not design intelligence).
**Commit:** `feat: phase 4 - design skills (design-wireframe, design-component-spec)`

| # | Task | Status |
|---|------|--------|
| 4.1 | `skills/design-wireframe/SKILL.md` (WF-XXX format, ASCII conventions, AC mapping) | ✅ Done |
| 4.2 | `skills/design-component-spec/SKILL.md` (COMP-XXX format, ShadCN component reference) | ✅ Done |
| 4.3 | Create `.agent/skills/` symlinks for both design skills | ✅ Done |

---

## Phase 5 — Slash Commands

**Goal:** Write 5 `.claude/commands/*.md` files to replace the v2 Node.js CLI orchestrator.
**Commit:** `feat: phase 5 - slash commands (5 pipeline commands)`

| # | Task | Status |
|---|------|--------|
| 5.1 | `.claude/commands/po-pipeline.md` — brief → PRD → USM → USL → USD → UAT | ✅ Done |
| 5.2 | `.claude/commands/design-pipeline.md` — USD → wireframes → component specs | ✅ Done |
| 5.3 | `.claude/commands/validate-artifacts.md` — quality gate check | ✅ Done |
| 5.4 | `.claude/commands/pm-strategy.md` — product strategy session | ✅ Done |
| 5.5 | `.claude/commands/pm-discovery.md` — discovery sprint session | ✅ Done |

---

## Phase 6 — Distribution Layer

**Goal:** Enable `npx ai-ready-workflow install` and `./install.sh` for local skill installation.
**Commit:** `feat: phase 6 - distribution layer (install.sh, install.ps1, package.json)`

| # | Task | Status |
|---|------|--------|
| 6.1 | `skills/install.sh` (copies skills to `.agent/skills/`, patches CLAUDE.md) | ✅ Done |
| 6.2 | `skills/install.ps1` (Windows equivalent) | ✅ Done |
| 6.3 | `skills/package.json` + `skills/cli.js` (enables `npx ai-ready-workflow install`) | ✅ Done |
| 6.4 | `skills/README.md` (lists all skills, trigger keywords, install instructions) | ✅ Done |

---

## Phase 7 — Documentation & Agent Index Updates

**Goal:** Ensure all framework READMEs, agent index files, and multi-agent entry points reflect the full capability set from phases 0–5 (16 skills, 5 slash commands, PM framework, design skills, pm/ artifact folder).
**Commit:** `docs: phase 7 - documentation and agent index updates`

### 7a — Framework READMEs

| # | Task | Status |
|---|------|--------|
| 7.1 | Root `README.md` — full framework overview, skill/command reference, install instructions | ✅ Done |
| 7.2 | `GETTING_STARTED.md` — create with all 4 frameworks + 6 learning paths | ✅ Done |
| 7.3 | `po-framework/README.md` — add PO skills + `/po-pipeline` automation section | ✅ Done |
| 7.4 | `design-framework/README.md` — add design skills automation section (no Figma to remove) | ✅ Done |
| 7.5 | `codebase-framework/README.md` — update tech stack to Next.js 15 | ✅ Done |
| 7.6 | `pm-framework/README.md` — add `/pm-strategy` + `/pm-discovery` slash commands section | ✅ Done |
| 7.7 | `skills/README.md` — list all 16 skills with triggers and install instructions | ✅ Done (Phase 6) |

### 7b — Agent Index Files (reflect phases 0–5)

> **What each file needs:** PM artifact IDs (PM-STRATEGY, PM-DISCOVERY), `pm/` subfolder in feature folder structure, full 16-skill registry, and (where appropriate) slash command references.

| # | Task | Status |
|---|------|--------|
| 7.8 | `CLAUDE.md` — add PM artifact IDs (PM-STRATEGY, PM-DISCOVERY); add Phase 6 install section (`npx ai-ready-workflow install`) | ✅ Done |
| 7.9 | `AGENTS.md` — add USM-XXX + PM artifact IDs; add Feature Folder Structure section; add Slash Commands reference; add Phase 6 install section | ✅ Done |
| 7.10 | `GEMINI.md` — same updates as 7.9 (PM artifact IDs, folder structure, slash commands reference, Phase 6 install section) | ✅ Done |
| 7.11 | `.cursorrules` — create Cursor-compatible rules file; mirror `AGENTS.md` structure with all 16 skills, artifact IDs, traceability frontmatter, feature folder structure, and install instructions | ✅ Done |

### 7c — npm Publish & Distribution Fix

**Goal:** Publish `skills/package.json` to npm so `npx ai-ready-workflow install` works. Add GitHub Actions workflow for automated publishing on git tags.
**Plan:** [npm-publish-plan.md](npm-publish-plan.md)

| # | Task | Status |
|---|------|--------|
| 7c.1 | Create `.github/workflows/npm-publish.yml` (auto-publish on `v*` tags) | ✅ Done |
| 7c.2 | Add `NPM_TOKEN` secret to GitHub repo settings | ✅ Done |
| 7c.3 | Run `npm login` + `npm publish --access public` from `skills/` | ✅ Done |
| 7c.4 | Verify: `npm info ai-ready-workflow` returns version 0.1.0 | ✅ Done |
| 7c.5 | End-to-end test: `npx ai-ready-workflow install` in a blank directory | ✅ Done |

### 7d — npm Package Documentation

> **Superseded by 7e.** All 7d tasks are covered in 7e with broader scope. No separate publish needed.

---

### 7e — Multi-Agent Fix + Documentation + Publish (0.1.1)

**Goal:** Fix the installer for all 4 agents, ship all entry point files in the npm package, add per-agent docs, then publish once as `0.1.1`. Single pass — no intermediate publish.
**Plan:** [npm-docs-plan.md](npm-docs-plan.md)

**Critical finding:** The package claims multi-agent support but the installer only provisions Claude Code. `AGENTS.md`, `GEMINI.md`, and `.cursorrules` are never copied to the target project and are not in the npm files array.

#### Step 1 — Code Fix

| # | Task | Status |
|---|------|--------|
| 7e.1 | Create `skills/AGENTS.md` — copy from repo root, maintained in `skills/` for packaging | ✅ Done |
| 7e.2 | Create `skills/GEMINI.md` — copy from repo root | ✅ Done |
| 7e.3 | Create `skills/.cursorrules` — copy from repo root | ✅ Done |
| 7e.4 | Update `skills/install.sh` — copy `AGENTS.md`, `GEMINI.md`, `.cursorrules` to target root (skip if exists) | ✅ Done |
| 7e.5 | Update `skills/install.ps1` — same for Windows | ✅ Done |

#### Step 2 — Documentation

| # | Task | Status |
|---|------|--------|
| 7e.6 | Create `skills/GETTING_STARTED.md` — 4 agent-specific sections (Claude Code, Codex, Cursor, Gemini) | ✅ Done |
| 7e.7 | Rework `skills/README.md` — npm badges, "what you get" box, "after install" section, all-agent entry point table | ✅ Done |
| 7e.8 | Update `skills/cli.js` — post-install banner with agent-aware next steps | ✅ Done |

#### Step 3 — Package & Publish

| # | Task | Status |
|---|------|--------|
| 7e.9 | Update `skills/package.json` — add `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `GETTING_STARTED.md` to files array; bump to `0.1.1` | ✅ Done |
| 7e.10 | `npm pack --dry-run` — confirm all new files are in the tarball | ✅ Done |
| 7e.11 | `npm publish --access public` from `skills/` | ✅ Done |
| 7e.12 | Verify: `npx ai-ready-workflow install` copies entry points for all 4 agents | ✅ Done |

---

## Summary

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Foundation (CLAUDE.md, skills/, agent indexes, pm-framework scaffold) | ✅ Done |
| 1 | PM Framework knowledge base (rules, templates, examples) | ✅ Done |
| 2 | PM Skills (6 SKILL.md files) | ✅ Done |
| 3 | PO Automation Skills (7 SKILL.md files) | ✅ Done |
| 4 | Design Skills (2 SKILL.md files) | ✅ Done |
| 5 | Slash Commands (5 pipeline commands) | ✅ Done |
| 6 | Distribution Layer (install.sh, package.json) | ✅ Done |
| 7 | Documentation & Agent Index Updates | ✅ Done |
