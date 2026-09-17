# M9-03 — Remove the claude-mem stubs

**Milestone:** M9 · **Status:** done · **Blocked by:** —

## Goal

The root `CLAUDE.md` is the only `CLAUDE.md` in the repository, claude-mem cannot silently reintroduce stubs into
version control, and no document describes files that no longer exist.

## Read first

- `ARCHITECTURE 2.3` — nested `CLAUDE.md` files
- `ARCHITECTURE 5.1` — the slash-command set, which used to mention a stub

## Files I may touch

`**/CLAUDE.md` except the root, `.claude/settings.json`, `.gitignore`, `ARCHITECTURE.md`, `tests/test_docs.py`,
`docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/lessons.md`, `docs/decisions/0007-remove-claude-mem-stubs.md`,
`docs/decisions/README.md`, this card

## Acceptance

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] `git check-ignore` ignores `skills/po-brief-to-prd/CLAUDE.md` and `pm-framework/CLAUDE.md`, and does
      **not** ignore the root `CLAUDE.md`
- [x] Every `skills/*/` directory contains a `SKILL.md`
- [x] `check_state_card_rows_unique` fails on the re-inserted orphan fragment and on a card left in flight

## Out of scope

The branch model and the merge to `main` — card M9-16.

## Log

**The owner did the deletion; this card records it.** The 64 deletions and the `settings.json` change were
already staged, unclaimed, when this session started. They matched the M9-03 row exactly — every nested stub,
the root untouched, plugin disabled — so the owner answered Q5 by hand and confirmed committing it as M9-03. The
claim commit was path-limited to `docs/STATE.md` so the staged deletions did not ride along with it.

**Surprise: the board was corrupted, by an earlier session of mine.** The M9-12 edit that split "Next up" into
claimable and blocked sliced from a heading to the next `---`, which matched a table separator. It left an
orphan `---|---|---|` and seven stale rows — the old "65 claude-mem" and "4 dead links" wording — under "Blocked on
owner", listing M9-03, M9-05 and M9-11 a second time with contradicting status. Removed, and
`check_state_card_rows_unique` added. **Its first live catch was this card**: M9-03 sat in In flight and Done at
once until the in-flight row was cleared.

**Five empty directories removed with `rmdir`**, which refuses a non-empty directory. Git does not track empty
directories, so they were invisible to other clones but still showed up in a local listing of `skills/`.

**`ARCHITECTURE 2.3` kept its number and changed its subject.** Nothing cites it, and deleting the last
subsection of section 2 would not have shifted any other number — but reusing the slot for the nested
`CLAUDE.md` rule avoids a gap and keeps the mechanism next to the topology it belongs with.

**Deliberately not done:** `.claude/launch.json` is untracked and stays untracked — it is the M9-15 diagram-hub
preview helper, listed in that card's file set as temporary. The M9-14 diagrams still depict the stubs; they
are snapshots of `d04f47d` by design (decision 0006) and were not edited.
