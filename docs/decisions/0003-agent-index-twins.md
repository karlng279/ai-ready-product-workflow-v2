# 0003 — Agent index files are byte-identical twins; the README pair deliberately is not

**Date:** 2026-09-04 · **Status:** accepted

## Context

Six files hold per-agent guidance: `AGENTS.md`, `GEMINI.md`, `.cursorrules` at the root, and copies of each
under `skills/`. The `skills/` copies are what npm ships and what the installer drops into a user's project.

They drifted. The `skills/` copies gained `artifact-sync` and `/sync-check` in commit `e498c31`; the root
copies did not, and were stale for months. A session reading the root `AGENTS.md` would not have known the
17th skill existed.

`README.md` and `GETTING_STARTED.md` also exist in both places, but differ substantively — the root pair
describes the repository, the `skills/` pair describes the installed package.

**Rejected: symlink the twins.** It removes drift by construction, but npm does not follow symlinks reliably
when packing, and Windows checkouts without developer mode get a text file containing a path.

**Rejected: generate them at publish time.** A build step for three markdown files, in a repo whose whole
premise is that everything is readable markdown with no build.

## Decision

The three agent index files and their `skills/` twins are **byte-identical**, asserted by
`tests/test_docs.py`. `README.md` and `GETTING_STARTED.md` and their twins **intentionally differ** and must
never be synced.

## Consequences

- Editing an agent index means editing two files. The test catches you if you forget.
- Adding a skill touches eleven surfaces (`ARCHITECTURE 3.3`); six of them are these files.
