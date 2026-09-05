# 0001 — Wireframes live as sections in one `wireframes.md` per feature, not one file per screen

**Date:** 2026-09-04 · **Status:** accepted · **Amends:** the agent index files and two slash commands

## Context

Two conventions were in the repository at once.

- `design/WF-XXX.md`, one file per screen — stated in `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`,
  `README.md`, `skills/README.md`, `skills/GETTING_STARTED.md`, `design-framework/README.md`, and in the
  `/design-pipeline` and `/validate-artifacts` command definitions. Eleven places.
- `design/wireframes.md`, one file per feature with `## WF-XXX` sections — stated in
  `design-framework/stage1-wireframes/rules.md` ("One `wireframes.md` file per feature"),
  `skills/design-wireframe/SKILL.md`, and `skills/design-component-spec/SKILL.md`, which reads
  `upstream: design/wireframes.md`.

An agent following the first convention writes files nothing downstream reads.

**Rejected: make the docs win.** Eleven documents outnumber three, but the count is not the evidence. The
authorities are the framework rules and the skill that does the writing, and the reference implementation on
disk agrees with them: `features/Export Customs Clearances/design/` contains `wireframes.md`, not `WF-001.md`.
Changing the convention would also have orphaned the existing artifact and the `/sync-check` example that
cites `design/wireframes.md`.

## Decision

`features/{name}/design/wireframes.md` is the single wireframe file for a feature. `WF-XXX` is a section
heading inside it. The same shape applies to `interactions.md` and `INT-XXX`.

All eleven documents and both slash commands were corrected to match.

## Consequences

- The wireframe artifact cannot be split per screen without breaking `design-component-spec`'s upstream path.
- A wireframe has no frontmatter of its own; the file carries one block for all of them.
- Enforced by `tests/test_prohibitions.py` (`check_no_per_id_design_files`), which fails on any
  `features/*/design/WF-*.md` **or** `INT-*.md`. The first implementation matched only `WF-<digits>.md` and
  would have missed `WF-XXX.md`; a fresh-context audit caught the gap and the pattern was widened.
