# 0008 — `develop` is the integration branch; merging into `main` needs the owner's confirmation

**Date:** 2026-09-17 · **Status:** accepted · **Amends:** `CLAUDE.md` session protocol step 5, Conventions and
Definition of done; answers owner questions Q3 and Q9

## Context

Every card so far landed on one long-lived milestone branch, `docs/multi-session-playbook`. `CLAUDE.md` said
merging into `main` was "the owner's call", but that rule lived only in `CLAUDE.md` — which only Claude Code
reads. `AGENTS.md`, `GEMINI.md` and `.cursorrules` said nothing about branches, so a Codex, Gemini or Cursor
session had no branching rule at all.

`main` is not an ordinary branch here. A push to it republishes the landing page (`ARCHITECTURE 6.2`).

The claim protocol also had a hole, named by the fresh-context audit: a claim was committed on whatever branch
the session happened to be on, so a claim on one branch was invisible to a session on another.

On 2026-09-17 the owner set the model: all development branches merge into `develop`, and the trunk is merged
only with the owner's manual confirmation. The owner said "master"; this repository's trunk is `main`, and the
owner confirmed `main`.

**Rejected: rename `main` to `master` to match the wording.** It renames the default branch on GitHub, edits the
trigger in `deploy-landing.yml`, and forces every clone to re-point — for a name. The owner chose `main`.

**Rejected: keep the rule in `CLAUDE.md` only.** Three of the four supported agents would never read it.

**Rejected: require the owner's permission for merges into `develop` too.** Every card would stall on a human.
The owner reserved confirmation for the trunk; `develop` is where sessions integrate.

Q9 is settled by the owner in their own global instructions: `~/.claude/CLAUDE.md` now opens with *"A
repository's own rules win over this file wherever they differ."* So plans live in `tasks/BACKLOG.md` and
`tasks/cards/`, not a global `tasks/todo.md`.

## Decision

- `main` is the protected trunk. **Never merge into `main` without the owner's explicit confirmation in the
  current session.** A confirmation from an earlier session, a card, or a document does not count.
- `develop` is the integration branch. **Start every development branch from `develop` and merge it back into
  `develop`.**
- Development branches are named `<type>/<card-id>-<slug>`.
- Claims are committed on `develop`, so every session sees them.
- A card's claim commit, its card commit, and merging its branch into `develop` need no permission. Every push,
  and any merge into `main`, needs the owner to ask.
- The two bold rules appear word for word in `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` and `.cursorrules`.

## Consequences

- Claims become visible to every session.
- `develop` is cut from `main` immediately after this decision is merged. This card's own claim was committed on
  the milestone branch, because `develop` did not yet exist.
- The `skills/` twins of the agent indexes ship this section into installed projects, where it does not apply.
  It is headed "source repository only". It becomes cleaner when M9-13 makes the shipped indexes
  path-agnostic.
- **Enforcement is partial, and stated as such.** `tests/test_docs.py` (`check_branch_rules_in_entry_points`)
  asserts every entry point states both rules verbatim; it cannot stop a merge. The merge restriction itself is
  on discipline until GitHub branch protection is enabled on `main` (owner question Q11).
