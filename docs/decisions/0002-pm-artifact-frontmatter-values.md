# 0002 — PM artifacts use framework codes in `artifact:`, not `PM-*` labels

**Date:** 2026-09-04 · **Status:** accepted · **Amends:** `/pm-strategy`, `/pm-discovery`

## Context

`.claude/commands/pm-strategy.md` and `pm-discovery.md` instructed agents to write `artifact: PM-STRATEGY` and
`artifact: PM-DISCOVERY`. Every artifact on disk and both PM skills use `STRATEGY` and `OST`. The literal
strings `PM-STRATEGY` and `PM-DISCOVERY` appear in zero artifacts.

**Rejected: standardise on `PM-*` and migrate the artifacts.** It reads more consistently, but `OST` is a
meaningful term (Opportunity Solution Tree) that `PM-DISCOVERY` erases, the other four PM artifacts already use
descriptive codes (`NSM`, `GTM-PLAN`, `GROWTH-LOOP`, `MARKET-RESEARCH`), and migrating would have rewritten
seven files to make two commands right.

## Decision

The `artifact:` value is the framework's own code for the artifact type. `PRD 5.2` holds the complete set and
is the reference. `PM-STRATEGY` / `PM-DISCOVERY` remain valid as *conceptual names* in prose, never as
frontmatter values.

## Consequences

- The `artifact:` value is not derivable from the ID prefix. It must be looked up.
- Enforced by `tests/test_prohibitions.py` against the `PRD 5.2` set.
