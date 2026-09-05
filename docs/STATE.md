# STATE

**Board, not history.** History lives in git, in `tasks/cards/*` logs, and in `docs/history/`.
Read this first, every session. Cap: ~70 lines.

**Last updated:** 2026-09-05

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

---

## Next up — claimable now

| Card | Title | Blocked by |
|---|---|---|
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
| **Version split three ways** | `package.json` `0.2.0`, `package-lock.json` `0.1.2`, no `v0.2.0` tag → 0.2.0 unpublished; npm serves `0.1.2`. `ARCHITECTURE 6.3` |
| **USD → wireframe traceability dead** | All 12 USD files carry the literal `WF-XXX` placeholder. `PRD 7.2` |
| **`design-interactions` skill does not exist** | Artifacts are stamped `generated-by: design-interactions`; stage 3 is manual. Allowlisted in `test_prohibitions.py` |
| **`pm-to-po-handoff` does not exist** | Appears as a `generated-by` value on disk. Allowlisted |
| **`po-framework/stage2-usm/template.md` missing** | Every other PO stage has one |
| **42 dead links** | Allowlisted in `tests/known_dead_links.txt` with a reason each: 38 rotted targets (card M9-11) and 4 illustrative template paths. The link checker guards against **new** ones |
| **Empty dirs** | `codebase-framework/templates/`, `codebase-framework/testing-patterns/` — `.gitkeep` only |
| **65 claude-mem stubs** | 65 of 66 tracked `CLAUDE.md` files are 169-byte `<claude-mem-context>` noise, not gitignored |

---

## Waiting on owner

Every open input needed from the human, what it blocks, when asked.

| # | Question | Blocks | Asked |
|---|---|---|---|
| Q1 | Ship the four framework dirs in the npm package, **or** make each `SKILL.md` degrade gracefully without them? | The package's core promise | 2026-09-05 |
| Q2 | Publish `0.2.0` now? Requires bumping `package-lock.json` and pushing a `v0.2.0` tag. | M9-07 | 2026-09-05 |
| Q3 | Sweep `landing-page/index.html` to 17 skills / 6 commands? It redeploys on **every** push to `main`. | M9-02 | 2026-09-05 |
| Q4 | Resolve the `WF-XXX` placeholders in the 12 USD files, or leave the reference feature as-is? | M9-06 | 2026-09-05 |
| Q5 | Delete the 65 claude-mem stub `CLAUDE.md` files and gitignore them? This changes how claude-mem behaves in this repo. | M9-03 | 2026-09-05 |
| Q6 | Build a `design-interactions` skill, or document stage 3 as permanently manual? | Design stage 3 | 2026-09-05 |
| Q7 | Apply the five `artifact-sync` sync fields to artifacts, or drop them from the spec? (`PRD 5.4`) | `artifact-sync` usefulness | 2026-09-05 |
| Q8 | The 4 dead links point at a plan that never existed. Delete the links, or write the document? | M9-04 | 2026-09-05 |
| Q9 | Your global `~/.claude/CLAUDE.md` says "write plans to `tasks/todo.md`"; this playbook forbids a shared todo (`docs/multi-session-repo-playbook.md` §7). Which wins in this repo? | Session protocol | 2026-09-05 |

---

## Environment

- **Python 3.11.1**, no pytest. Tests are dependency-free: `python3 tests/test_docs.py`.
- **Node >= 18** for the npm package. `npm` not required for doc work.
- `ui-ux-pro-max` needs Python 3 for `scripts/search.py`.
- Repo lives under `~/Documents`, a macOS TCC-protected path — a sandboxed agent may be denied access. See
  `tasks/lessons.md` → *Never escalate a permission denial*.
