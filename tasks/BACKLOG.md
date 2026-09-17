# BACKLOG

The full plan, one row per unit of work. **Card files are authored just-in-time** — a card written before its
dependencies land encodes guesses. When you claim a row with no card file, write the card first from this row
plus the sections it cites, using `tasks/cards/TEMPLATE.md`.

Card IDs encode the milestone: `M8-*` was artifact-sync and the doc reconciliation, `M9-*` is playbook
adoption and the cleanup it surfaced. The milestone is an ID range; there is no separate phase structure.

Status: `todo` · `in-flight` · `done` · `blocked`
Claim a card in `docs/STATE.md` and commit that line **before** starting.

Phases 0–7 are complete; their detail is in [`docs/history/phases-0-7.md`](../docs/history/phases-0-7.md).

---

## M8 — Artifact sync and agent-doc reconciliation

| ID | Title | Status | Blocked by | File set |
|---|---|---|---|---|
| M8-01 | `skills/artifact-sync/SKILL.md` — staleness detection and surgical patches | done | — | `skills/artifact-sync/` |
| M8-02 | `.agent/skills/artifact-sync` symlink | done | M8-01 | `.agent/skills/` |
| M8-03 | `.claude/commands/sync-check.md` — 6th slash command | done | M8-01 | `.claude/commands/sync-check.md` |
| M8-04 | Add artifact-sync + `/sync-check` to the `skills/` agent indexes | done | M8-01 | `skills/{AGENTS.md,GEMINI.md,.cursorrules}` |
| M8-05 | Sync the root agent indexes with their `skills/` twins | done | M8-04 | `AGENTS.md`, `GEMINI.md`, `.cursorrules` |
| M8-06 | Correct the wireframe output path everywhere (see decision 0001) | done | — | 11 docs + 2 commands |
| M8-07 | Correct "TanStack Query" → TanStack Table in 9 documents | done | — | agent indexes, `README.md`, `GETTING_STARTED.md` |
| M8-08 | Correct PM `artifact:` values (see decision 0002) | done | — | `.claude/commands/pm-*.md` |
| M8-09 | Add artifact-sync to the installer registry tables | done | M8-01 | `skills/install.{sh,ps1}` |
| M8-10 | `skills/cli.js` help banner 16 → 17 | done | — | `skills/cli.js` |
| M8-11 | Correct stale `ui-ux-pro-max` frontmatter counts | done | — | `skills/ui-ux-pro-max/SKILL.md` |

---

## M9 — Playbook adoption and the cleanup it surfaced

| ID | Title | Status | Blocked by | File set |
|---|---|---|---|---|
| M9-01 | Adopt the playbook layout: `PRD`/`ARCHITECTURE` split, `docs/`, `tasks/`, `tests/` | done | — | `CLAUDE.md`, `PRD.md`, `ARCHITECTURE.md`, `docs/**`, `tasks/**`, `tests/**` |
| M9-02 | Landing page figures corrected (counts, TanStack Table, artifact-sync card) — unpublished until merged to `main` | done | — | `landing-page/index.html` |
| M9-03 | Remove the claude-mem stubs: disable the plugin, delete every nested `CLAUDE.md`, gitignore them | done | — | `**/CLAUDE.md` except the root, `.claude/settings.json`, `.gitignore`, `ARCHITECTURE.md`, `tests/test_docs.py`, `docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/lessons.md`, `docs/decisions/0007-*`, `docs/decisions/README.md`, `tasks/cards/M9-03-*` |
| M9-04 | Fix the 6 references to `design-framework-uiux-promax-integration-plan.md`, which never existed | blocked | owner Q8 | `design-framework/design-rules/README.md`, `design-framework/themes/README.md`, `design-framework/themes/{corporate,ecommerce,erp,mds}.md` |
| M9-05 | Write `po-framework/stage2-usm/template.md` | todo | — | `po-framework/stage2-usm/template.md` |
| M9-06 | Resolve `WF-XXX` placeholders in 12 USD Design Reference tables | blocked | owner Q4 | `features/Export Customs Clearances/po/usd/*.md` |
| M9-07 | Publish `0.2.0` — bump `package-lock.json`, sweep sites, tag `v0.2.0` | blocked | owner Q2 | `skills/package{.json,-lock.json}`, `README.md`, `landing-page/` |
| M9-08 | Decide the npm knowledge-base gap: ship framework dirs, or degrade gracefully | blocked | owner Q1 | `skills/package.json` or all 17 `SKILL.md` |
| M9-09 | Build a `design-interactions` skill, or document stage 3 as permanently manual | blocked | owner Q6 | `skills/design-interactions/` or `ARCHITECTURE 5.2` |
| M9-10 | Apply the five `artifact-sync` sync fields to artifacts, or drop them from the spec | blocked | owner Q7 | `PRD 5.4`, `features/**` |
| M9-11 | Clear the rotted links allowlisted in `tests/known_dead_links.txt`, **excluding the 5 owned by M9-04** | todo | — | `design-framework/patterns/**`, `design-framework/templates/**`, `design-framework/design-rules/{naming-conventions,responsive}.md`, `design-framework/QUICK_START.md`, `po-framework/README.md`, `codebase-framework/component-patterns/animations.md` |
| M9-12 | Correct the enforcement claims and detector gaps found by the fresh-context audit | done | — | `ARCHITECTURE.md`, `CLAUDE.md`, `docs/INDEX.md`, `docs/decisions/0001-wireframes-single-file.md`, `tests/**` |
| M9-13 | Rewrite the shipped agent indexes and `ui-ux-pro-max` paths to be installed-project-agnostic | blocked | owner Q1 | `skills/AGENTS.md`, `skills/GEMINI.md`, `skills/.cursorrules`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `skills/ui-ux-pro-max/SKILL.md`, `skills/README.md`, `skills/GETTING_STARTED.md` |
| M9-14 | Draw the as-is Archify diagrams: agent collaboration, end-user adoption, framework internals | done | — | `docs/diagrams/**`, `docs/decisions/0006-diagrams-are-snapshots.md`, `docs/decisions/README.md`, `docs/INDEX.md`, `ARCHITECTURE.md` (1.1 map), `README.md` (tree), `docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/cards/M9-14-as-is-diagrams.md` |
| M9-15 | Add a browsable hub page for the diagrams (`docs/diagrams/index.html`) | done | M9-14 | `docs/diagrams/index.html`, `docs/diagrams/README.md`, `README.md` (tree), `docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/cards/M9-15-diagram-hub.md`, temporary uncommitted `.claude/launch.json` |
| M9-16 | Branch model: `develop` integrates, `main` needs owner confirmation — rules in every agent entry point | done | — | `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `skills/AGENTS.md`, `skills/GEMINI.md`, `skills/.cursorrules`, `ARCHITECTURE.md`, `docs/INDEX.md`, `docs/STATE.md`, `tasks/BACKLOG.md`, `tests/test_docs.py`, `docs/decisions/0008-*`, `docs/decisions/README.md`, `tasks/cards/M9-16-*` |

Owner questions Q1–Q9 are in [`docs/STATE.md`](../docs/STATE.md) → Waiting on owner.
