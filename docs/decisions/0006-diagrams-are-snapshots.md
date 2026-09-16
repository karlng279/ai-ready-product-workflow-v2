# 0006 — Diagrams are dated as-is snapshots in `docs/diagrams/`, not specification

**Date:** 2026-09-16 · **Status:** accepted

## Context

The owner asked for diagrams of the repository as it is today — how agent sessions collaborate on it, how an end
user adopts the framework with their own agent, and the framework internals — with enhancement ("to-be")
diagrams to follow later. The diagrams are drawn with the Archify agent skill: a JSON source per diagram,
rendered to a self-contained HTML page of roughly 0.8 MB.

This repository's rule is that a stale document is worse than a missing one. An as-is diagram goes stale the
moment a card it depicts lands (M9-03, M9-07, M9-08 and M9-13 each change something drawn).

**Rejected: a sibling folder outside the repo.** Nothing would go stale in git, but no future session would
find the diagrams, and the owner chose the repo.

**Rejected: session scratchpad plus private share links.** The files would vanish with the session.

**Rejected: make the diagrams sweep sites (`ARCHITECTURE 1.2`).** Every card touching a depicted fact would
have to re-render a diagram, which is the whole-artifact regeneration this repo avoids.

## Decision

The diagrams live in `docs/diagrams/` as JSON source plus generated HTML, both committed, so the pages open
without Archify installed. `docs/diagrams/README.md` pins the snapshot commit and states that the cited
`PRD` / `ARCHITECTURE` section wins on any disagreement. The diagrams are a record, like `docs/history/`: a later
card regenerates the whole set with a new snapshot commit rather than patching individual facts.

## Consequences

- About 9 MB of generated HTML is in git; each regeneration adds a similar amount to history.
- Diagram text names sets instead of counting skills or commands, so fewer facts rot between regenerations.
- No test checks that a diagram matches disk. `test_docs.py` only checks that the README links resolve.
  Accuracy rests on the evidence card in each diagram and on discipline.
