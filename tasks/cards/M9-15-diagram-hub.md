# M9-15 — Add a browsable hub page for the diagrams

**Milestone:** M9 · **Status:** done · **Blocked by:** —

## Goal

`docs/diagrams/index.html` is one page that lists every diagram M9-14 drew, grouped the way
`docs/diagrams/README.md` groups them, and previews the chosen one in a frame. It follows the hub the owner
uses in `kn-signal-log/docs/diagrams/index.html`: a sidebar list, System / Light / Dark theme passed to each
diagram as `?theme=`, a deep link per diagram in the address hash, and "Open in a new tab".

## Read first

- `docs/diagrams/README.md` — the diagram set, its grouping, and the snapshot caveat the hub must repeat
- decision 0006 — the diagrams are a record, not specification

## Files I may touch

`docs/diagrams/index.html`, `docs/diagrams/README.md`, `README.md` (the repository tree line only),
`docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/cards/M9-15-diagram-hub.md` — grew during the work: a temporary,
uncommitted `.claude/launch.json` (see Log)

## Acceptance

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] Every diagram HTML in `docs/diagrams/` has exactly one hub entry, and every hub entry names a file that exists
      — 11 entries, 11 files, ids unique
- [x] Opened in a browser: each entry loads its diagram, the hash deep link works, and the theme switch reaches the frame
      — headless Chrome at 1440×900: 11/11 entries load their page with an SVG; `#artifact-chain` opens diagram 08;
      Dark sends `?theme=dark` and the framed diagram reports `data-theme="dark"`; the choice survives a reload; a
      malformed hash falls back to the first entry; no horizontal overflow at 1440 or 375 wide

## Out of scope

- Redrawing or correcting any diagram — they stay the M9-14 snapshot
- The to-be (enhancement) diagrams — a later card

## Log

**Decided.** Same shell and behaviour as the owner's `kn-signal-log` hub (sidebar, System / Light / Dark saved in
`localStorage`, `?theme=` into the frame, frame replaced rather than re-pointed so Back is not doubled, hash deep
links), with three additions: entries are grouped under the README's three headings, the top bar shows the
question each diagram answers, and the current entry scrolls into view on a deep link. The styles are a small
hand-written sheet using the reference's colour tokens, not a copy of its compiled Tailwind bundle, most of
which styles that project's charts. The icon is a new neutral flow glyph; the KN mark belongs to the other
project.

**Surprised.** The built-in browser pane renders local files as a static snapshot, so the frame cannot load
there, and it refused `localhost`. The shell sandbox also cannot reach a local server. Verification ran through
headless Chrome over a DevTools pipe against `file://` URLs instead, with no sandbox change.

**Left behind.** A temporary `.claude/launch.json` was created to start a preview server; deleting it was
denied, so it is still in the working tree, untracked and not part of this commit. It is safe to delete.

**Not done.** The design hook flagged the type scale as flat (.6875 / .75 / .8 / .875rem). It is the reference
hub's scale, kept on purpose, and no ignore rule was added. No test checks that `index.html` and the diagram
files agree; the README now says so.
