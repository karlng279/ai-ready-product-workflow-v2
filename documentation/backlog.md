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
| 4.1 | `skills/design-wireframe/SKILL.md` (WF-XXX format, ASCII conventions, AC mapping) | ⬜ Not Started |
| 4.2 | `skills/design-component-spec/SKILL.md` (COMP-XXX format, ShadCN component reference) | ⬜ Not Started |
| 4.3 | Create `.agent/skills/` symlinks for both design skills | ⬜ Not Started |

---

## Phase 5 — Slash Commands

**Goal:** Write 5 `.claude/commands/*.md` files to replace the v2 Node.js CLI orchestrator.
**Commit:** `feat: phase 5 - slash commands (5 pipeline commands)`

| # | Task | Status |
|---|------|--------|
| 5.1 | `.claude/commands/po-pipeline.md` — brief → PRD → USM → USL → USD → UAT | ⬜ Not Started |
| 5.2 | `.claude/commands/design-pipeline.md` — USD → wireframes → component specs | ⬜ Not Started |
| 5.3 | `.claude/commands/validate-artifacts.md` — quality gate check | ⬜ Not Started |
| 5.4 | `.claude/commands/pm-strategy.md` — product strategy session | ⬜ Not Started |
| 5.5 | `.claude/commands/pm-discovery.md` — discovery sprint session | ⬜ Not Started |

---

## Phase 6 — Distribution Layer

**Goal:** Enable `npx ai-ready-workflow install` and `./install.sh` for local skill installation.
**Commit:** `feat: phase 6 - distribution layer (install.sh, install.ps1, package.json)`

| # | Task | Status |
|---|------|--------|
| 6.1 | `skills/install.sh` (copies skills to `.agent/skills/`, patches CLAUDE.md) | ⬜ Not Started |
| 6.2 | `skills/install.ps1` (Windows equivalent) | ⬜ Not Started |
| 6.3 | `skills/package.json` (enables `npx ai-ready-workflow install`) | ⬜ Not Started |
| 6.4 | `skills/README.md` (lists all skills, trigger keywords, install instructions) | ⬜ Not Started |

---

## Phase 7 — Update All README Files

**Goal:** Ensure all framework READMEs reflect the new structure and skill references.
**Commit:** `docs: phase 8 - update all README files`

| # | Task | Status |
|---|------|--------|
| 7.1 | Root `README.md` — full framework overview, skill/command reference, install instructions | ⬜ Not Started |
| 7.2 | `GETTING_STARTED.md` — add PM framework as 6th learning path | ⬜ Not Started |
| 7.3 | `po-framework/README.md` — note that PO skills in `skills/po-*/` automate this workflow | ⬜ Not Started |
| 7.4 | `design-framework/README.md` — note design skills enforce format; remove Figma section | ⬜ Not Started |
| 7.5 | `codebase-framework/README.md` — update tech stack (Next.js 15 App Router) | ⬜ Not Started |
| 7.6 | `pm-framework/README.md` — already written in Phase 0; review and finalize | ⬜ Not Started |
| 7.7 | `skills/README.md` — list all skills, triggers, install instructions | ⬜ Not Started |

---

## Summary

| Phase | Description | Status |
|-------|-------------|--------|
| 0 | Foundation (CLAUDE.md, skills/, agent indexes, pm-framework scaffold) | ✅ Done |
| 1 | PM Framework knowledge base (rules, templates, examples) | ✅ Done |
| 2 | PM Skills (6 SKILL.md files) | ✅ Done |
| 3 | PO Automation Skills (7 SKILL.md files) | ✅ Done |
| 4 | Design Skills (2 SKILL.md files) | ⬜ Not Started |
| 5 | Slash Commands (5 pipeline commands) | ⬜ Not Started |
| 6 | Distribution Layer (install.sh, package.json) | ⬜ Not Started |
| 7 | Update All README Files | ⬜ Not Started |
