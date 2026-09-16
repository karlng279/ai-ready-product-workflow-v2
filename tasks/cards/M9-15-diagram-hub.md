# M9-15 — Add a browsable hub page for the diagrams

**Milestone:** M9 · **Status:** in-flight · **Blocked by:** —

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
`docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/cards/M9-15-diagram-hub.md`

## Acceptance

- [ ] `python3 tests/test_docs.py`
- [ ] `python3 tests/test_prohibitions.py`
- [ ] Every diagram HTML in `docs/diagrams/` has exactly one hub entry, and every hub entry names a file that exists
- [ ] Opened in a browser: each entry loads its diagram, the hash deep link works, and the theme switch reaches the frame

## Out of scope

- Redrawing or correcting any diagram — they stay the M9-14 snapshot
- The to-be (enhancement) diagrams — a later card

## Log
