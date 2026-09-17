# 0007 — Remove the claude-mem stub `CLAUDE.md` files and ignore nested `CLAUDE.md`

**Date:** 2026-09-17 · **Status:** accepted · **Amends:** `ARCHITECTURE 2.3`; answers owner question Q5

## Context

The claude-mem plugin, enabled in `.claude/settings.json`, wrote a 169-byte `CLAUDE.md` containing only a
`<claude-mem-context>` block into every directory it visited. Sixty-four of the sixty-five tracked `CLAUDE.md`
files were these stubs; only the root file was a rulebook. Five directories — `skills/documentation/`,
`skills/skills/`, `.agent/skills/documentation/`, `.agent/skills/.agent/skills/` and
`design-framework/design-framework/design-rules/` — existed only to hold one.

The cost was not disk space. Claude Code loads nested `CLAUDE.md` files as instructions, so every stub was a
rules surface saying nothing, sitting beside the one that mattered. `skills/documentation/` and `skills/skills/`
looked like skills to anyone listing the directory.

Deleting them changes how claude-mem behaves here, which is the owner's tool, so it waited on the owner (Q5).
The owner answered by disabling the plugin in `.claude/settings.json` and deleting exactly the 64 stubs.

**Rejected: delete without ignoring.** If claude-mem is enabled again — at project or user level — the stubs
return, untracked, and a session could commit them wholesale.

**Rejected: ignore `CLAUDE.md` everywhere.** The root file is tracked and would survive, but the rule would read
as if the rulebook itself were disposable.

## Decision

- claude-mem is disabled in `.claude/settings.json`.
- The 64 stubs and the five stub-only directories are removed.
- `.gitignore` ignores `**/CLAUDE.md` and re-includes `/CLAUDE.md`.

## Consequences

- The root `CLAUDE.md` is the only `CLAUDE.md` in the repository.
- A deliberate nested `CLAUDE.md` now needs `git add -f`, and should come with a decision record — it adds a
  rules surface that no non-Claude agent reads.
- Every enumerator that skipped the stubs keeps its guard: `command_set()` still excludes a stray `CLAUDE.md` in
  `.claude/commands/`, because an ignored file still exists on disk.
- No test asserts the absence of nested `CLAUDE.md` files. The `.gitignore` rule is the mechanism; checked by
  hand with `git check-ignore`.
