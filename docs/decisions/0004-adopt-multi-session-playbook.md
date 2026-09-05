# 0004 — Adopt the Multi-Session Repo Playbook; split `CLAUDE.md` into `PRD` + `ARCHITECTURE`

**Date:** 2026-09-05 · **Status:** accepted

## Context

`CLAUDE.md` had grown to 370 lines mixing rules with reference tables, the artifact ID system, frontmatter
specifications, topology and a gotcha log. It is loaded into every session, so all of it competed for the same
attention, and a session needing one rule paid for all of it.

Work tracking lived in `documentation/backlog.md` as a flat phase list with no per-unit files, no claim
registry, and nowhere to record what was owed by the owner. Sessions had no way to see what another session
was touching.

The owner supplied `docs/multi-session-repo-playbook.md`, which prescribes seven document surfaces, a session
protocol, and asserting documents the way you assert code.

**Rejected: keep one large `CLAUDE.md`.** Simple, but the playbook's core claim — that a stale document is
worse than a missing one — had already been demonstrated in this repo eleven times over (`docs/INDEX.md` §3).

**Rejected: adopt the layout but skip the tests.** Conventions decay; this repo's had already decayed. Since
the repository *is* documentation, the playbook's document-freshness tests apply unusually directly here.

## Decision

Adopt the playbook, adapted to a repository that has no application code:

- `CLAUDE.md` → rules only, 125 lines
- `PRD.md` → meaning; `ARCHITECTURE.md` → mechanism; both with numbered, citable sections
- `docs/INDEX.md`, `docs/STATE.md`, `docs/decisions/`, `docs/history/`
- `documentation/backlog.md` → `tasks/BACKLOG.md`, plus `tasks/cards/` and `tasks/lessons.md`
- `tests/test_docs.py` and `tests/test_prohibitions.py`, dependency-free

Two departures from the playbook, taken deliberately: there is no `src/` or `tests/` for application code
because there is none, and `docs/STATE.md` runs to 83 lines rather than 70 because Known broken and Waiting on
owner are each nine rows and every row is load-bearing.

## Consequences

- Adding a skill, changing a count, or renumbering a section now fails a test rather than drifting silently.
- Section numbers in `PRD` and `ARCHITECTURE` are load-bearing; renumbering is a breaking change.
- Per-card bookkeeping costs roughly ten minutes: three surfaces plus a log.
- `docs/history/` holds superseded plans as record. They are **not** specifications and must not be cited as
  such.
