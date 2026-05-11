# Getting Started

Choose your entry point based on where you are in the product lifecycle.

---

## Quick Install

If you want to use these skills in your own project:

```bash
npx ai-ready-workflow install
```

This copies all 16 skills to `.agent/skills/` and patches your `CLAUDE.md`. Then jump to whichever path below fits your current stage.

---

## Learning Paths

### Path 1 — PM Strategy (Start here for a new product)

Use when: You have an idea or opportunity but need to define strategy before writing requirements.

```
/pm-strategy → pm-framework/product-strategy/
/pm-discovery → pm-framework/product-discovery/
```

1. Read [`pm-framework/README.md`](pm-framework/README.md)
2. Read [`pm-framework/pm-workflow.md`](pm-framework/pm-workflow.md)
3. Run `/pm-strategy` — produces `features/{name}/pm/strategy.md`
4. Run `/pm-discovery` — produces `features/{name}/pm/discovery.md` with OST, assumptions, interview guide
5. When assumptions are validated, move to Path 2

**Relevant skills:** `pm-product-strategy`, `pm-product-discovery`, `pm-market-research`

---

### Path 2 — PO Pipeline (Feature requirements)

Use when: You have a validated idea or feature brief and need to write specs.

```
/po-pipeline → Brief → PRD → USM → USL → USD → UAT
```

1. Read [`po-framework/README.md`](po-framework/README.md)
2. Write a brief in `features/{name}/brief.md` (or have it ready in your message)
3. Run `/po-pipeline {feature-name}` — runs all 5 stages automatically
4. Review at the two pause points (after PRD, after USL)
5. When UAT files are written, move to Path 3

**Relevant skills:** `po-brief-to-prd`, `po-prd-to-usm`, `po-usm-to-usl`, `po-usl-to-usd`, `po-usd-to-uat`

---

### Path 3 — Design Pipeline (Wireframes + component specs)

Use when: USD acceptance criteria files exist and you need design artifacts for implementation.

```
/design-pipeline → WF-XXX wireframes → COMP-XXX component specs
```

1. Read [`design-framework/README.md`](design-framework/README.md)
2. Choose a theme from [`design-framework/themes/`](design-framework/themes/) (mds, corporate, ecommerce, erp)
3. Run `/design-pipeline {feature-name}` — generates wireframes then component specs
4. Review wireframes at the pause point before component specs are generated
5. Hand `COMP-XXX.md` files to engineers for implementation

**Relevant skills:** `ui-ux-pro-max` (design intelligence), `design-wireframe` (WF-XXX format), `design-component-spec` (COMP-XXX format)

---

### Path 4 — Code Implementation

Use when: Design artifacts (COMP-XXX) exist and you are ready to implement.

1. Read [`codebase-framework/README.md`](codebase-framework/README.md) for Next.js 15 patterns
2. Reference `features/{name}/design/COMP-XXX.md` for component definitions
3. Reference `features/{name}/po/uat/ST-XXX.md` for acceptance criteria to validate against

**Stack:** Next.js 15 App Router + ShadCN UI + TanStack Query + React Hook Form + Zod

---

### Path 5 — Validation

Use when: Artifacts exist and you want to run a quality check before progressing.

```
/validate-artifacts {feature-name}
```

Runs quality gates on all artifacts — PRD, USD, wireframes, component specs — and reports pass/warn/missing per file with specific issues called out.

**Relevant skills:** `validate-prd`, `validate-usd`

---

### Path 6 — Analytics & Growth (Post-launch PM work)

Use when: The product is live and you are working on metrics, growth, or GTM.

1. Read the relevant `pm-framework/` sub-area
2. Trigger the relevant skill by keyword in conversation

| Need | Skill |
|------|-------|
| Define metrics and KPIs | `pm-data-analytics` |
| Design growth loops | `pm-marketing-growth` |
| Plan a launch | `pm-go-to-market` |
| Research the market | `pm-market-research` |

---

## Full End-to-End Flow

```
PM Strategy (/pm-strategy)
    ↓
PM Discovery (/pm-discovery)
    ↓
PO Pipeline (/po-pipeline): Brief → PRD → USM → USL → USD → UAT
    ↓
Design Pipeline (/design-pipeline): USD → WF-XXX → COMP-XXX
    ↓
Code Implementation (codebase-framework)
    ↓
Validation (/validate-artifacts)
    ↓
Analytics & Growth (pm-data-analytics, pm-marketing-growth)
    ↓
Go-to-Market (pm-go-to-market)
```

---

## Traceability Chain

Every artifact links to the next via YAML frontmatter (`upstream` / `downstream`):

```
PM-STRATEGY → PM-DISCOVERY → PRD → USM → USL → USD (AC-XXX) → UAT (TC-XXX)
                                                    ↓
                                              WF-XXX → COMP-XXX → code/
```

---

## Artifact Locations

| Artifact | Where |
|----------|-------|
| PM artifacts | `features/{name}/pm/` |
| PO artifacts | `features/{name}/po/` |
| Design artifacts | `features/{name}/design/` |
| Code | `features/{name}/code/` |

---

## Multi-Agent Usage

| Agent | How to use this repo |
|-------|---------------------|
| Claude Code | Skills auto-load via `.agent/skills/`; use slash commands in `.claude/commands/` |
| OpenAI Codex | Read `AGENTS.md`, then read the relevant `skills/*/SKILL.md` |
| Gemini Code Assist | Read `GEMINI.md`, then read the relevant `skills/*/SKILL.md` |
| Cursor | Read `.cursorrules` for active context |
| Any agent | Read `skills/*/SKILL.md` directly |
