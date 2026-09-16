# Diagrams — as-is snapshot

**Snapshot of commit `d04f47d` · drawn 2026-09-16 by card M9-14 · record, not specification.**

These diagrams show the repository **as it was at that commit**, including what was broken. Where a doc and disk
disagreed, the diagram shows what is on disk and draws the documented-but-broken path as broken. Where a
diagram and `PRD.md` / `ARCHITECTURE.md` disagree, **the cited section wins** — see
[decision 0006](../decisions/0006-diagrams-are-snapshots.md). They are not sweep sites; a later card regenerates
them rather than patching them in place.

**Start at [index.html](index.html)** — one page that lists every diagram by group, previews the chosen one,
passes the System / Light / Dark theme through, and gives each diagram a deep link (`index.html#artifact-chain`).

Any diagram `.html` also opens on its own. Each one is self-contained: theme switch, pan and zoom, search, guided
views, and export. The `.json` next to it is the Archify source, and every diagram carries an evidence card
naming the files it was drawn from.

## A. Agents maintaining this repo

| # | Diagram | Question it answers | Source |
|---|---|---|---|
| 01 | [Which rules reach each maintainer agent](01-agent-entry-points.html) | When Claude Code, Codex, Gemini or Cursor opens this repo, which rules reach it? | [architecture](01-agent-entry-points.architecture.json) |
| 02 | [One maintainer session](02-maintainer-session.html) | What does one session do from start to card commit, and what is enforced by code? | [workflow](02-maintainer-session.workflow.json) |
| 03 | [Two sessions sharing one repo](03-parallel-sessions.html) | How do two concurrent sessions coordinate, and where does that break? | [sequence](03-parallel-sessions.sequence.json) |
| 04 | [Card lifecycle](04-card-lifecycle.html) | Which states does a card pass through, and where is status recorded? | [lifecycle](04-card-lifecycle.lifecycle.json) |

## B. An end user adopting the framework

| # | Diagram | Question it answers | Source |
|---|---|---|---|
| 05 | [How an end user installs](05-install-paths.html) | What do `npx … install`, a clone, `mcp` and `install-cowork` actually write? | [workflow](05-install-paths.workflow.json) |
| 06 | [What each agent picks up](06-installed-project-per-agent.html) | After install, what does each agent load, and what does a fork get that npm does not? | [architecture](06-installed-project-per-agent.architecture.json) |
| 07 | [A new user's first feature](07-first-feature-journey.html) | What does the first feature run look like on the clone route and on the npm route? | [sequence](07-first-feature-journey.sequence.json) |

## C. Framework internals

| # | Diagram | Question it answers | Source |
|---|---|---|---|
| 08 | [Artifact chain](08-artifact-chain.html) | How do artifacts flow from PM to design, by real frontmatter edges? | [dataflow](08-artifact-chain.dataflow.json) |
| 09 | [What `/sync-check` does](09-change-propagation.html) | How does a change propagate, and what gets patched with consent? | [workflow](09-change-propagation.workflow.json) |
| 10 | [Repository layout and what ships](10-repo-topology.html) | What lives where, which files are twins, and what reaches npm? | [architecture](10-repo-topology.architecture.json) |
| 11 | [How a change reaches users](11-release-pipeline.html) | Which Actions run on push, on `main`, and on a `v*` tag? | [workflow](11-release-pipeline.workflow.json) |

## Regenerating

Drawn with the Archify agent skill, version 2.17 (installed outside this repo). From the skill's directory:

```bash
node bin/archify.mjs validate <type> <name>.<type>.json --quality showcase --json
node bin/archify.mjs deliver <type> <name>.<type>.json <name>.html --quality showcase --json
node bin/archify.mjs visual-check <name>.html --json
```

Run `visual-check` against a copy outside the repo: it writes PNG and JSON evidence files beside the HTML.
When regenerating, update the snapshot commit above and in the `index.html` footer, re-verify each evidence card
against disk, and keep skill and command **counts** out of the diagram text — name the set instead. A diagram
added or renamed needs its `index.html` entry too; nothing tests that the two agree.
