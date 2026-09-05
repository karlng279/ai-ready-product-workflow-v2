# PRD

**What the artifacts, terms and values in this repository mean.** Authoritative on *meaning*. For how the
repository is built, see `ARCHITECTURE`.

Cite sections of this file as `PRD <n.n>` — e.g. `PRD 5.2`. Section numbers are load-bearing:
`tests/test_docs.py` resolves every citation, and renumbering is a breaking change.

---

## 1. Purpose and audience

This repository gives an AI agent a **structured methodology for product development** — from strategy through
requirements and design to code-ready specifications — expressed entirely as markdown that any agent can read.

Two audiences:

- **An agent working inside this repo**, generating artifacts for a feature under `features/`.
- **An agent in someone else's project** that installed the npm package, with skills but no framework
  directories (`ARCHITECTURE 4.5`).

The value proposition is **traceability**: every artifact declares what it came from and what it feeds, so a
change anywhere can be traced to everything it affects.

---

## 2. The four frameworks

A framework is **reference material an agent reads**. A skill is **executable instruction an agent follows**.
Skills cite frameworks; frameworks never cite skills.

### 2.1 PM Framework — `pm-framework/`

Six pillars, run in sequence or dipped into as needed: **Strategy → Discovery → Research → Analytics → Growth →
GTM**. Answers *should we build this, for whom, and how will we know it worked.* Outputs live in
`features/{name}/pm/`.

### 2.2 PO Framework — `po-framework/`

Five stages, strictly ordered: **PRD → USM → USL → USD → UAT**. Each consumes the previous.

| Stage | Produces | Means |
|---|---|---|
| 1 PRD | `po/prd.md` | The problem, goals, personas, success metrics and explicit non-goals |
| 2 USM | `po/usm.md` | The user journey decomposed into activities and steps, so stories have a shape |
| 3 USL | `po/usl.md` | Every story with MoSCoW priority and an estimate — the prioritised backlog |
| 4 USD | `po/usd/ST-XXX.md` | Per story: atomic, observable, binary acceptance criteria plus NFRs |
| 5 UAT | `po/uat/ST-XXX.md` | Per story: Given-When-Then test cases covering every AC |

### 2.3 Design Framework — `design-framework/`

Three stages: **Wireframes → Component Specs → Interactions**. Consumes USD acceptance criteria; produces
artifacts an engineer can implement without guessing.

Stage 3 has full rules and templates but **no skill wraps it** — it is performed manually.

### 2.4 Codebase Framework — `codebase-framework/`

Implementation patterns for the target stack: **Next.js 15 App Router, ShadCN UI, TanStack Table, React Hook
Form, Zod.** Server state is native `fetch` with Next.js caching — **there is no TanStack Query in this
framework**, and documents claiming otherwise are wrong.

---

## 3. The artifact chain

### 3.1 The chain

```
PM strategy → PM discovery → brief → PRD → USM → USL → USD → UAT
                                                      ↓
                                              wireframes → component specs → interactions
```

Each artifact names its `upstream` and `downstream` in frontmatter (`PRD 5.1`). The chain is the reason the
`artifact-sync` skill can compute what a change affects.

### 3.2 One file per ID, or sections in a shared file

This distinction is the single most misread convention in the repo. **Two artifact types are one file per
feature, with IDs as section headings inside it:**

| Type | File | IDs appear as |
|---|---|---|
| Wireframes | `design/wireframes.md` — **one file for the whole feature** | `## WF-001: Screen Name` |
| Interactions | `design/interactions.md` — **one file for the whole feature** | `## INT-001` |

Everything else is one file per ID. There is no `design/WF-XXX.md`; writing one is a defect.

Authority: `design-framework/stage1-wireframes/rules.md` ("One `wireframes.md` file per feature"),
`skills/design-wireframe/SKILL.md`, and the reference implementation (`PRD 7.2`).

---

## 4. Artifact ID system

| Artifact | ID format | Written to |
|---|---|---|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story | `ST-XXX` | `features/{name}/po/usl.md` |
| Acceptance Criterion | `AC-XXX` | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | `TC-XXX` | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | `WF-XXX` | `features/{name}/design/wireframes.md` (section — `PRD 3.2`) |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` |
| Component Element | `COMP-XXX-EL-YYY` | inside the parent `COMP-XXX.md` |
| Interaction Flow | `INT-XXX` | `features/{name}/design/interactions.md` (section — `PRD 3.2`) |
| Interaction State | `INT-XXX-ST-YYY` | inside `interactions.md` |

IDs are sequential per feature and zero-padded to three digits. **An ID is never reused or renumbered** — a
renumber invalidates every reference to it downstream.

---

## 5. Traceability frontmatter

### 5.1 Required fields

Seven fields, present on all 43 artifacts currently on disk. `tests/test_prohibitions.py` asserts them.

```yaml
---
artifact: PRD              # see PRD 5.2 — NOT always the ID prefix
feature: Export Customs Clearances   # must match the folder name exactly, spaces and all
version: 0.1
status: draft              # see PRD 5.3
generated-by: po-brief-to-prd        # the skill that produced this file
upstream: brief.md         # what this was derived from
downstream: usm.md         # what is derived from this
---
```

`upstream` / `downstream` rooting is **inconsistent on disk**: `po/` artifacts use bare filenames (`usm.md`);
`design/` and `pm/` artifacts use feature-root-relative paths (`po/usd/`, `design/COMP-001.md`). Match the
neighbouring artifacts rather than inventing a scheme.

### 5.2 `artifact:` values

The `artifact:` value is **not always the ID prefix**. PM artifacts use framework-specific codes. This is the
complete set in use:

| File | `artifact:` | Expands to |
|---|---|---|
| `po/brief.md` | `BRIEF` | Feature brief |
| `po/prd.md` | `PRD` | Product Requirements Document |
| `po/usm.md` | `USM` | User Story Map |
| `po/usl.md` | `USL` | User Story List |
| `po/usd/ST-XXX.md` | `USD` | User Story Details |
| `po/uat/ST-XXX.md` | `UAT` | User Acceptance Test |
| `design/wireframes.md` | `WF` | Wireframes |
| `design/COMP-XXX.md` | `COMP` | Component Specification |
| `design/interactions.md` | `INT` | Interaction flows |
| `pm/strategy.md` | `STRATEGY` | Product strategy |
| `pm/discovery.md` | `OST` | Opportunity Solution Tree |
| `pm/market-research.md` | `MARKET-RESEARCH` | Market research |
| `pm/analytics.md` | `NSM` | North Star Metric |
| `pm/growth.md` | `GROWTH-LOOP` | Growth loop |
| `pm/gtm.md` | `GTM-PLAN` | Go-to-market plan |

`PM-STRATEGY` and `PM-DISCOVERY` are **conceptual names, not frontmatter values**. Writing them into
`artifact:` is a defect.

### 5.3 `status`

`draft` → `review` → `approved`. A downstream artifact may be generated from a `draft` upstream, but the
generated artifact inherits that uncertainty and must not be marked `approved`.

### 5.4 Sync fields — specified, not yet applied

The `artifact-sync` skill defines five further fields. **No artifact on disk carries them.** They are the
target state, not an established convention; treat a document presenting them as standard as wrong.

```yaml
last_modified: 2026-05-21
change_summary: "One-sentence description of what changed"
change_type: additive              # PRD 5.5
sync_status: in_sync               # in_sync | stale | pending_review | diverged
based_on_upstream_version: 0.1
```

### 5.5 `change_type` and the propagation rule

| Value | Means |
|---|---|
| `additive` | New content only; nothing removed or renamed |
| `reductive` | Existing content removed |
| `interface` | Referenced content changed — AC text, wireframe layout, PRD narrative |
| `structural` | IDs renumbered or reorganised; breaks all downstream references |

**Propagation:** `additive` ripples forward only. `reductive`, `interface` and `structural` ripple **forward
and backward** — a design change can invalidate the acceptance criteria above it.

---

## 6. Quality gates

Each stage folder carries a `quality-gate.md` defining what "good enough to proceed" means. The recurring
criteria across stages:

- **Atomic** — one behaviour per item
- **Observable** — verifiable through UI or system behaviour
- **Binary** — clear pass/fail, no partial states
- **Quantified** — an NFR saying "fast" or "secure" without a number fails
- **Covered** — every AC appears in a UAT case and in a wireframe AC-mapping table
- **No placeholders** — `TBD`, `TODO`, `[Add here]` fail the gate

Only `validate-prd` and `validate-usd` exist as skills. Wireframe and component-spec gates are run inline by
`/validate-artifacts` from the framework files.

---

## 7. Feature folders

### 7.1 Layout

```
features/{feature-name}/
├── pm/         strategy.md  discovery.md  market-research.md
│               analytics.md  growth.md  gtm.md
├── po/         brief.md  prd.md  usm.md  usl.md
│               usd/ST-XXX.md     uat/ST-XXX.md
├── design/     wireframes.md  COMP-XXX.md  interactions.md
└── code/       optional implementation
```

**Feature folder names are not slugs.** The real folders are `Export Customs Clearances` (spaces, Title Case)
and `Container-retail-vn`. The `feature:` frontmatter value mirrors the folder name exactly. Always quote these
paths in shell commands.

`code/` has never existed in practice — no feature has one and no skill writes into it. It is an intended slot.

### 7.2 Reference implementation

`features/Export Customs Clearances/` is the one fully-worked feature: 6 PM artifacts, brief + PRD + USM + USL +
12 USD + 12 UAT, and wireframes + 6 component specs + interactions. **Read it before generating a new feature**
— it shows the conventions as actually applied.

Its USD files carry the literal placeholder `WF-XXX` in the Design Reference column: no real wireframe ID was
written back after the wireframes were generated. Do not read those tables as resolved traceability.

`features/Container-retail-vn/` holds only `pm/strategy.md` — a PM-only spike.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **AC** | Acceptance Criterion — one atomic, observable, binary condition |
| **BDD** | Given-When-Then test phrasing used in UAT |
| **JTBD** | Jobs-to-be-Done — framing a need as a job the user hires a product for |
| **MoSCoW** | Must / Should / Could / Won't — the USL prioritisation scheme |
| **NFR** | Non-Functional Requirement — performance, security, accessibility, with numbers |
| **NSM** | North Star Metric — the single measure of delivered value |
| **OST** | Opportunity Solution Tree — Teresa Torres' discovery structure |
| **Ripple / impact set** | The artifacts a change invalidates, computed by `artifact-sync` (`PRD 5.5`) |
| **Skill** | A `SKILL.md` an agent follows; distinct from a framework (`PRD 2`) |
| **Sweep site** | A document restating figures it does not own (`ARCHITECTURE 1.2`) |
| **USD / USL / USM** | User Story Details / List / Map (`PRD 2.2`) |
