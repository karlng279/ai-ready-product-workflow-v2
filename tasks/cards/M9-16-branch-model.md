# M9-16 — Branch model: `develop` integrates, `main` needs the owner's confirmation

**Milestone:** M9 · **Status:** done · **Blocked by:** —

## Goal

Every agent — Claude Code, Codex, Gemini, Cursor — reads the same two branching rules: start every development
branch from `develop` and merge it back into `develop`, and never merge into `main` without the owner's explicit
confirmation in the current session. A test fails if any entry point stops stating them.

## Read first

- `ARCHITECTURE 6.2` — why a push to `main` is outward-facing
- `ARCHITECTURE 2.2` — the byte-identical twins the rules must also go into
- decision 0008

## Files I may touch

`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `skills/AGENTS.md`, `skills/GEMINI.md`,
`skills/.cursorrules`, `ARCHITECTURE.md`, `docs/INDEX.md`, `docs/STATE.md`, `tasks/BACKLOG.md`,
`tests/test_docs.py`, `docs/decisions/0008-develop-integration-branch.md`, `docs/decisions/README.md`, this card

## Acceptance

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] `check_branch_rules_in_entry_points` failed before the rules were written (8 failures), and passes after
- [x] Mutation: rule removed from `CLAUDE.md`; removed from `GEMINI.md` and its twin; reworded in `.cursorrules`
      and its twin — 3/3 caught by the branch-rules check itself, not masked by the twin check
- [x] Twins still byte-identical; `CLAUDE.md` at 138 lines, under the 150 cap

## Out of scope

- Merging into `main`, cutting `develop`, pushing — done by the same session after this card, on the owner's
  explicit confirmation, and not part of any card's file set.
- GitHub branch protection and the default branch — owner settings (Q11).

## Log

**The owner said "master"; the trunk is `main`.** There is no `master` branch locally or on the remote, and
`deploy-landing.yml` triggers on `main`. Asked rather than guessed: renaming the default branch is outward-facing
and repoints every clone. The owner chose `main`.

**The rule had to reach agents that never read `CLAUDE.md`.** Before this card, `AGENTS.md`, `GEMINI.md` and
`.cursorrules` said nothing about branches. The same two sentences now appear word for word in all four entry
points. The test compares with whitespace collapsed, so a rule wrapped differently still matches, but a single
changed word fails — the point is that every agent reads the *same* rule.

**Test first.** The check was written before the rules and failed with eight problems — two rules missing from
four files — which proved it could fail before it was trusted to pass.

**Enforcement is stated as partial, deliberately.** The test proves the rules are *written*; it cannot stop a
merge. Claiming otherwise would repeat the M9-12 mistake. The real mechanism is GitHub branch protection, which
agents cannot turn on — raised as Q11.

**A permission call made here, and flagged.** The owner reserved confirmation for merges into `main`. This card
lets a session merge its own finished card branch into `develop` without asking, since requiring the owner for
every card would stall all work on a human. Pushing still needs the owner. If that reading is wrong, it is one
paragraph in `CLAUDE.md` → Conventions and decision 0008.

**Two stale items resolved in passing.** `CLAUDE.md` had two separate **Commits.** paragraphs — one saying "one
card, one commit", one saying two commits — merged into one. Q9 left the board: the owner's global
`~/.claude/CLAUDE.md` now says repository rules win, which settles it.

**Surprise: the shipped twins carry the section into installed projects.** Byte-identity (decision 0003) means
`skills/AGENTS.md` gets it too, so a user's project will read a rule that does not apply to it. Headed "source
repository only" to contain the damage; the real fix belongs to M9-13.

**Deliberately not done:** `docs/STATE.md` is now 101 lines against the ~70 cap and the 83 accepted in decision
0004 — the Done table grows with every card. Not trimmed here; it needs a rule for when a Done row leaves the
board.
