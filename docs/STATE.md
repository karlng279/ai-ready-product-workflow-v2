# STATE

**Board, not history.** History lives in git, in `tasks/cards/*` logs, and in `docs/history/`.
Read this first, every session. Cap: ~70 lines.

**Last updated:** 2026-09-16

---

## In flight — the claim registry

Add your card ID here and **commit that line before starting work**. That commit is the lock.
Your card's file set must be disjoint from every other row.

| Card | Claimed by | Since | File set |
|---|---|---|---|
| — | — | — | — |

---

## Done

| Card | Landed |
|---|---|
| M8-01…M8-11 | artifact-sync skill, `/sync-check`, and the agent-doc reconciliation (17 skills, 6 commands) |
| M9-01 | Playbook layout adopted: `PRD`/`ARCHITECTURE` split, `docs/`, `tasks/`, `tests/`, `CLAUDE.md` cut to rules |
| M9-02 | Landing page figures corrected — 17 skills, 6 commands, TanStack Table, artifact-sync card. **Unpublished until merged to `main`** |
| M9-12 | Fresh-context audit corrections: enforcement claims made true, 4 vacuous detectors fixed, CI added |
| M9-14 | As-is Archify diagrams in `docs/diagrams/`, snapshot of `d04f47d` (decision 0006). Its card Log lists six on-disk findings not yet on this board |
| M9-15 | `docs/diagrams/index.html` hub: every diagram by group, theme pass-through, deep links |

---

## Next up — claimable now

Nothing here is blocked. Claim one, add it to In flight, commit that line.

| Card | Title |
|---|---|
| M9-05 | Write `po-framework/stage2-usm/template.md` |
| M9-11 | Clear the rotted links allowlisted in `tests/known_dead_links.txt` |

## Blocked on owner

Not claimable until the linked question is answered.

| Card | Title | Blocked by |
|---|---|---|
| M9-03 | Delete the claude-mem stub `CLAUDE.md` files and gitignore them | Q5 |
| M9-04 | Fix the references to `design-framework-uiux-promax-integration-plan.md`, a plan file that never existed — 6 files | Q8 |
| M9-06 | Resolve the `WF-XXX` placeholders in the USD Design Reference tables | Q4 |
| M9-07 | Publish `0.2.0` — bump `package-lock.json`, tag `v0.2.0` | Q2 |
| M9-08 | Decide the npm knowledge-base gap | Q1 |
| M9-09 | `design-interactions` skill, or declare stage 3 manual | Q6 |
| M9-10 | Apply the sync fields, or drop them from the spec | Q7 |
| M9-13 | Rewrite the shipped agent indexes to be path-agnostic | Q1 |

---|---|---|
| M9-02 | Sweep `landing-page/index.html` — 16→17 skills, 5→6 commands (8 occurrences) | owner decision Q3 |
| M9-03 | Delete the 65 claude-mem stub `CLAUDE.md` files and gitignore them | owner decision Q5 |
| M9-04 | Fix 4 dead links to `documentation/design-framework-uiux-promax-integration-plan.md` | owner decision Q8 |
| M9-05 | Write `po-framework/stage2-usm/template.md` | — |
| M9-11 | Clear the 38 rotted links allowlisted in `tests/known_dead_links.txt` | — |
| M9-06 | Resolve the `WF-XXX` placeholders in all 12 USD Design Reference tables | owner decision Q4 |
| M9-07 | Publish `0.2.0` — bump `package-lock.json`, sweep sites, tag | owner decision Q2 |

---

## Known broken

| What | Detail |
|---|---|
| **npm package ships no knowledge base** | Every `SKILL.md` cites `po-framework/…` etc.; those dirs are not in `files`. In an installed project the path does not exist. `ARCHITECTURE 4.5`. Needs decision Q1 |
| **Version split three ways** | `package.json` `0.2.0`, `package-lock.json` `0.1.2`, and `mcp-server.js:35` `0.1.2`; no `v0.2.0` tag → 0.2.0 unpublished; npm serves `0.1.2`. `ARCHITECTURE 6.4` |
| **USD → wireframe traceability dead** | All 12 USD files carry the literal `WF-XXX` placeholder. `PRD 7.2` |
| **`design-interactions` skill does not exist** | Artifacts are stamped `generated-by: design-interactions`; stage 3 is manual. Allowlisted in `test_prohibitions.py` |
| **`pm-to-po-handoff` does not exist** | Appears as a `generated-by` value on disk. Allowlisted |
| **`po-framework/stage2-usm/template.md` missing** | Every other PO stage has one |
| **42 dead links** | Allowlisted in `tests/known_dead_links.txt` with a reason each: 38 rotted targets (card M9-11) and 4 illustrative template paths. The link checker guards against **new** ones |
| **Empty dirs** | `codebase-framework/templates/`, `codebase-framework/testing-patterns/` — `.gitkeep` only |
| **claude-mem stubs** | Every tracked `CLAUDE.md` except the root one is claude-mem output — 64 of 65, verifiable with `git ls-files \| grep 'CLAUDE.md$' \| xargs grep -l claude-mem-context`. Not gitignored |

---

## Waiting on owner

Every open input needed from the human, what it blocks, when asked.

| # | Question | Blocks | Asked |
|---|---|---|---|
| Q1 | Ship the four framework dirs in the npm package, **or** make each `SKILL.md` degrade gracefully without them? | The package's core promise | 2026-09-05 |
| Q2 | Publish `0.2.0` now? Requires bumping `package-lock.json` and pushing a `v0.2.0` tag. | M9-07 | 2026-09-05 |
| Q3 | The landing page figures are **already corrected on this branch**. Merging to `main` republishes the site immediately (`ARCHITECTURE 6.2`) — merge now, or hold? | publishing the fix | 2026-09-05 |
| Q4 | Resolve the `WF-XXX` placeholders in the 12 USD files, or leave the reference feature as-is? | M9-06 | 2026-09-05 |
| Q5 | Delete every tracked `CLAUDE.md` that is claude-mem output — 64 of 65, all but the root — and gitignore them? This changes how claude-mem behaves here, which is your tool. | M9-03 | 2026-09-05 |
| Q6 | Build a `design-interactions` skill, or document stage 3 as permanently manual? | Design stage 3 | 2026-09-05 |
| Q7 | Apply the five `artifact-sync` sync fields to artifacts, or drop them from the spec? (`PRD 5.4`) | `artifact-sync` usefulness | 2026-09-05 |
| Q8 | Six files reference `design-framework-uiux-promax-integration-plan.md`, which never existed. Delete the references, or write the document? | M9-04 | 2026-09-05 |
| Q9 | Your global `~/.claude/CLAUDE.md` says "write plans to `tasks/todo.md`"; the playbook forbids a shared todo. `CLAUDE.md` currently states the playbook wins here — confirm or reverse. | Session protocol | 2026-09-05 |
| Q10 | The shipped agent indexes and `ui-ux-pro-max/SKILL.md` hardcode repo-relative paths (`skills/...`) that are wrong in every installed project. Rewrite them path-agnostic? Depends on Q1. | M9-13 | 2026-09-05 |

---

## Environment

- **Python 3.11.1**, no pytest. Tests are dependency-free: `python3 tests/test_docs.py`.
- **Node >= 18** for the npm package. `npm` not required for doc work.
- `ui-ux-pro-max` needs Python 3 for `scripts/search.py`.
- Repo lives under `~/Documents`, a macOS TCC-protected path — a sandboxed agent may be denied access. See
  `tasks/lessons.md` → *Never escalate a permission denial*.
