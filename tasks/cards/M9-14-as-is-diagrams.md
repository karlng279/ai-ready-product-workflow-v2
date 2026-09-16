# M9-14 — Draw the as-is diagrams: agent collaboration, end-user adoption, framework internals

**Milestone:** M9 · **Status:** in-flight · **Blocked by:** —

## Goal

`docs/diagrams/` holds a set of Archify diagrams (JSON source + generated standalone HTML) that show the repo
**as it is at `d04f47d`**: how agent sessions collaborate on this repo, how an end user adopts the framework
with their own agent, and how the framework works inside. Where a doc and disk disagree, the diagram shows
what is on disk and draws the documented-but-broken path as broken. The diagrams are a dated snapshot, not
specification. Enhancement ("to-be") diagrams are a separate, later card.

## Read first

- `docs/multi-session-repo-playbook.md` — the collaboration model the group A diagrams draw
- `ARCHITECTURE 3.2` — per-agent loading, checked against the agent tools
- `ARCHITECTURE 4.4` — the installers, checked against `skills/install.sh` and `skills/cli.js`

The other facts come from file:line evidence cited in each diagram's evidence card.

## Files I may touch

`docs/diagrams/**`, `docs/decisions/0006-diagrams-are-snapshots.md`, `docs/decisions/README.md`,
`docs/INDEX.md`, `ARCHITECTURE.md` (the 1.1 directory map only), `README.md` (the repository tree only),
`docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/cards/M9-14-as-is-diagrams.md`

## Acceptance

- [ ] `python3 tests/test_docs.py`
- [ ] `python3 tests/test_prohibitions.py`
- [ ] Every diagram passes `archify validate <type> <json> --quality showcase` with 0 errors and 0 warnings,
      and `archify deliver` exits 0
- [ ] Every HTML in `docs/diagrams/` matches its delivery receipt SHA-256
- [ ] `docs/diagrams/README.md` names the snapshot commit and says the cited section wins

## Out of scope

- To-be diagrams: a later card, after the owner reviews these
- Fixing anything the diagrams expose — M9-03 (claude-mem stubs), M9-06 (`WF-XXX`), M9-07 (version split),
  M9-08 / M9-13 (knowledge-base gap and shipped paths), M9-10 (sync fields)
- The owner's uncommitted work in the tree (64 staged `CLAUDE.md` deletions, `.claude/settings.json`) —
  both commits for this card are path-limited so that work stays staged and untouched

## Log
