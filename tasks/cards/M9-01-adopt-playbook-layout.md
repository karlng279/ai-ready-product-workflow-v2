# M9-01 — Adopt the Multi-Session Repo Playbook layout

**Milestone:** M9 · **Status:** done · **Blocked by:** —

## Goal

The repository follows `docs/multi-session-repo-playbook.md`: rules separated from knowledge, a two-document
specification with citable sections, a status board carrying what the owner owes, a decision log, per-card work
tracking, and two test files that assert the documentation the way tests assert code.

## Read first

- `docs/multi-session-repo-playbook.md` — layers 1–7, the session protocol, enforcement
- `ARCHITECTURE 1.1` — the target directory map
- `PRD 5.2` — the artifact values the prohibitions test asserts

## Files I may touch

`CLAUDE.md`, `PRD.md`, `ARCHITECTURE.md`, `README.md`, `docs/**`, `tasks/**`, `tests/**`,
`skills/README.md` (one broken link), `.gitignore`

## Acceptance

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] Every detector proven to bite by mutation: 11/11 caught
- [x] `CLAUDE.md` under the 150-line cap — 125 lines, asserted by `check_claude_md_is_rules_only`

## Out of scope

Everything the restructure surfaced but did not fix: M9-02 through M9-11, and owner questions Q1–Q9 in
`docs/STATE.md`. Clearing the 38 rotted links is M9-11, not this card.

## Log

**The link checker was the highest-yield thing in this card.** It found 48 dead links on first run — 4 caused
by moving `documentation/` and 44 pre-existing. That ratio was the argument for the whole playbook: 44 broken
references had been sitting in `design-framework/` and `po-framework/` unnoticed.

**Allowlist rather than mass-fix.** Fixing 38 rotted links needs judgment about what each should point at, and
would have swallowed this card. They are allowlisted in `tests/known_dead_links.txt` with a reason each, and
the allowlist is asserted both ways — an entry that starts resolving fails, so it cannot rot. New dead links
still fail. Tracked as M9-11.

**Two departures from the playbook, both deliberate** (decision 0005 and 0004): no `.env.example` or `src/`,
because neither exists here and a hollow file would claim a mechanism that is not there; and `docs/STATE.md`
runs 83 lines against a ~70 cap, because Known broken and Waiting on owner are nine rows each and every row is
load-bearing.

**Surprise: `CLAUDE.md` stopped being a skill-registry surface.** Cutting it to rules removed the skill table,
so `ARCHITECTURE 3.3` went from listing it among the surfaces to eleven surfaces that exclude it. Missing that
would have left the test asserting a table that no longer exists.

**Banned-string scoping needed care.** `PRD`, `CLAUDE.md`, `docs/INDEX.md` and the decision records all discuss
the banned strings by name. The check runs only over operational surfaces — the agent indexes, the READMEs,
`skills/**` and `.claude/commands/**` — the files an agent acts on rather than reads about.

**Deliberately not done:** the 65 claude-mem stub `CLAUDE.md` files were left in place (owner Q5). Deleting
them changes how claude-mem behaves in this repo, which is the owner's tool, not mine to reconfigure.
