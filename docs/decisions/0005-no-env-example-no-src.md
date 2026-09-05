# 0005 — No `.env.example` and no `src/`: declared absences, not omissions

**Date:** 2026-09-05 · **Status:** accepted

## Context

The playbook's layout lists `.env.example` ("every variable; nothing hardcoded in source") and `src/` or
language directories. Neither fits this repository.

There are no runtime environment variables. The only secret is the GitHub Actions `NPM_TOKEN`, which is a
repository secret consumed by `.github/workflows/npm-publish.yml` and never read by any code in the tree.

There is no application source. The executable code is the `ui-ux-pro-max` Python search scripts, the npm CLI,
the MCP server, two installers and this repo's own tests — each already living where it belongs.

**Rejected: create an empty `.env.example` for conformance.** The playbook's own anti-pattern list warns
against claiming a mechanism you have not written. An empty example file implies configuration that does not
exist and invites a session to look for it.

## Decision

Neither file nor directory is created. `ARCHITECTURE 1.2` states the absence and the reason, so a session that
looks for them finds an answer instead of a gap.

## Consequences

- A future session adding real configuration must create `.env.example` **and** amend `ARCHITECTURE 1.2`.
- No test enforces this; it is a documented absence, on discipline.
