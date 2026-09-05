# M9-12 — Correct the enforcement claims and detector gaps found by the fresh-context audit

**Milestone:** M9 · **Status:** done · **Blocked by:** —

## Goal

The enforcement claims in `CLAUDE.md`, `ARCHITECTURE.md` and the decision records describe what the tests
actually assert, and the detectors catch the defect classes they claim to catch.

## Read first

- `ARCHITECTURE 3.3` — the eleven surfaces and which are asserted
- `ARCHITECTURE 7.1`, `7.2`, `7.3` — what each check does
- `PRD 3.2` — the one-file rule the design-file detector enforces

## Files I may touch

`CLAUDE.md`, `ARCHITECTURE.md`, `docs/INDEX.md`, `docs/STATE.md`, `tasks/BACKLOG.md`, `tasks/lessons.md`,
`docs/decisions/0001-wireframes-single-file.md`, `tests/test_docs.py`, `tests/test_prohibitions.py`,
`.claude/commands/{validate-artifacts,sync-check}.md`, `skills/artifact-sync/SKILL.md`,
`.github/workflows/{tests.yml,npm-publish.yml}`, `landing-page/index.html`

## Acceptance

- [x] `python3 tests/test_docs.py` — `ok — documentation is consistent`
- [x] `python3 tests/test_prohibitions.py` — `ok — 43 artifacts and 17 skills satisfy the content rules`
- [x] The four defect classes the audit proved would slip past are now caught by mutation: `WF-XXX.md`,
      `WF-AUTH-001.md`, `INT-001.md`, empty frontmatter value — 4/4
- [x] No document claims a check that does not exist

## Out of scope

The shipped-package problems (M9-13) — the agent indexes and `ui-ux-pro-max` hardcode repo-relative paths that
break in an installed project. That is blocked on owner Q1, because the fix depends on whether the framework
directories get shipped.

## Log

**The audit caught me violating the prohibition I had just written.** `ARCHITECTURE 3.3` claimed
`test_docs.py` covered surfaces 1–9 and `CLAUDE.md` said "nine are asserted". Six were: the `cli.js` banner
and both `GETTING_STARTED` files were asserted by nothing, and surface 1 was asserted by the *other* test
file. Fixed both ways — wrote `check_cli_banner` (deriving the count from `skill_set()`, never a literal), and
rewrote the claims to **name the unasserted items** rather than count the asserted ones, so the sentence stays
true when a check is added.

**Four detectors were vacuous or too narrow.** `^WF-\d+\.md$` missed `WF-XXX.md` and `WF-AUTH-001.md`, and
there was no `INT-` detector at all despite `PRD 3.2` giving interactions the identical rule — now one
`PER_ID_FILE` pattern covers both. `.cursorrules` was in `BANNED_SCOPE` but `markdown_files()` only returns
`.md`, so it was never scanned; the landing page was not scanned either, which is why its "TanStack Query" and
six "16 skills" survived. The frontmatter check tested key *presence*, so an empty value passed. The
BACKLOG/card status comparison was guarded by `if row and card`, so a regex miss passed silently.

**Renumbering bit immediately.** Inserting `ARCHITECTURE 6.3` for CI pushed the release contract to 6.4, and
six citations kept pointing at 6.3 — which still resolved, so the suite stayed green while every one of them
was wrong. The citation checker proves a citation resolves, never that it resolves to what was meant. Recorded
in `tasks/lessons.md`.

**Landing page corrected but deliberately unpublished.** Owner question Q3 was about publishing, not about
whether the figures were right — they were plainly wrong (16 skills, 5 commands, TanStack Query, no
`artifact-sync` card). Corrected on this branch, where nothing deploys. `deploy-landing.yml` fires on push to
`main`, so merging remains the owner's decision.

**Deliberately not done:** the shipped agent indexes still describe this repository's layout to users who have
only `.agent/skills/` (M9-13), and `ui-ux-pro-max/SKILL.md` hardcodes `skills/ui-ux-pro-max/scripts/search.py`
in twelve places, which is wrong in every installed project. Both wait on Q1.
