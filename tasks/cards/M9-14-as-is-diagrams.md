# M9-14 — Draw the as-is diagrams: agent collaboration, end-user adoption, framework internals

**Milestone:** M9 · **Status:** done · **Blocked by:** —

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

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] Every diagram passes `archify validate <type> <json> --quality showcase` with 0 errors and 0 warnings,
      and `archify deliver` exits 0 — 11/11, each 9/9 artifact checks
- [x] Every HTML in `docs/diagrams/` matches its delivery receipt SHA-256 — 11/11, JSON sources too
- [x] `docs/diagrams/README.md` names the snapshot commit and says the cited section wins

## Out of scope

- To-be diagrams: a later card, after the owner reviews these
- Fixing anything the diagrams expose — M9-03 (claude-mem stubs), M9-06 (`WF-XXX`), M9-07 (version split),
  M9-08 / M9-13 (knowledge-base gap and shipped paths), M9-10 (sync fields)
- The owner's uncommitted work in the tree (64 staged `CLAUDE.md` deletions, `.claude/settings.json`) —
  both commits for this card are path-limited so that work stays staged and untouched

## Log

**Decided.** Eleven diagrams in three groups (agents maintaining the repo; end-user adoption; framework
internals), JSON source and HTML both committed, pinned to `d04f47d` — decision 0006. Research was split
across three read-only agents; every load-bearing fact was then re-checked on disk before it went into a
diagram. Both commits for this card are path-limited, so the owner's 64 staged claude-mem `CLAUDE.md` deletions
and the unstaged `.claude/settings.json` change were left exactly as found. The tree is therefore **not clean**
after this card, and that is not this card's work.

**Browser evidence.** `archify visual-check` passed 11/11 (containment at 1440×900 through 2048×1320, light
and dark). Perceptual review was mine, from the captured screenshots — no human has reviewed them yet.

**Surprised — true on disk, not yet in `docs/STATE.md`.** These are drawn in the diagrams and are the input
for the to-be card:

1. Only Claude Code sessions receive the maintainer protocol. `AGENTS.md`, `GEMINI.md` and `.cursorrules` are
   npm-shipped twins of `skills/` copies with no pointer to it, and decision 0003 means a pointer added there
   would ship to users. Diagram 01.
2. Before this card, no commit had ever added an In flight row: the claim lock was unused. There are no git or
   Claude hooks, and the branch has never been pushed, so a claim is invisible to another clone or a cloud
   agent. Diagrams 02, 03.
3. The local, gitignored `.claude/settings.local.json` pre-approves `git push *`, `git push origin main` and a
   `git merge`, which contradicts `CLAUDE.md` → Conventions (every push needs the owner).
4. The docs and the installer's registry text say Claude Code auto-loads `.agent/skills/`. This Claude Code
   session listed the `.claude/commands` but none of the `.agent/skills` skills; Claude Code discovers project
   skills under `.claude/skills/`. `ARCHITECTURE 3.2` needs re-verifying. Diagram 06.
5. `/po-pipeline` reads the brief from `features/{name}/brief.md`, while the docs and the reference feature use
   `po/brief.md`; it also creates the `code/` folder that `PRD 7.1` calls an unused slot. Diagram 07.
6. `docs/STATE.md` still carries a stale table fragment after "Blocked on owner" (M9-02 shown blocked though
   done, duplicate rows, old counts). No test catches it, because the Next-up check stops at that heading.

**Archify notes for whoever regenerates.** Workflow node `tag`s are not drawn on the canvas, so put conditions
in `sublabel`. The lifecycle renderer always draws an "Outcomes" band. Sequence and dataflow sublabels are 7px,
so the desktop readability gate caps the viewBox width near 1085; tall diagrams overflow 1440×900, so keep
the aspect wide.

**Deliberately not done.** No finding above was fixed, and none was added to `docs/STATE.md` Known broken — the
to-be card owns that. The STATE fragment was left alone. Nothing was pushed.
