# AI-Ready Product Workflow v2 — always-on rules

Rules only. Knowledge lives in `PRD.md` (meaning) and `ARCHITECTURE.md` (mechanism). **Do not read either end
to end** — use `docs/INDEX.md` to find the sections you need.

This repo follows `docs/multi-session-repo-playbook.md`. Sessions do not share memory; the repository is the
only channel between them. **A stale document is worse than a missing one.**

---

## Session protocol

1. Read `docs/STATE.md` — what is claimable, what is blocked, what is waiting on the owner.
2. Pick **one** card from `tasks/BACKLOG.md`. Read that card file only. If the row has no card file, write it
   first from the row plus the sections it cites.
3. Read only the sections the card names. Use `docs/INDEX.md`.
4. **Run both test files before touching anything** — an already-red suite is not yours to inherit silently.
5. Claim: add the card ID to the in-flight table in `docs/STATE.md` and **commit that line before starting**.
   That commit is the lock. Verify your file set is disjoint from everything else in flight.

```bash
python3 tests/test_docs.py && python3 tests/test_prohibitions.py
```

---

## Prohibitions

Each is something a context-free session does by default because it is locally the obvious move.

| Never | Why |
|---|---|
| Write `features/*/design/WF-XXX.md` | Wireframes are `## WF-XXX` sections inside one `design/wireframes.md` (`PRD 3.2`) |
| Write `artifact: PM-STRATEGY` or `PM-DISCOVERY` | Those are conceptual names. Real values are in `PRD 5.2` |
| Write a count of skills or commands as a number in a test or assertion | Assert the **set**. Counts outlive their truth (`ARCHITECTURE 7.1`) |
| Edit `AGENTS.md`, `GEMINI.md` or `.cursorrules` without editing its `skills/` twin | They must stay byte-identical (`ARCHITECTURE 2.2`) |
| Sync `README.md` or `GETTING_STARTED.md` with its `skills/` twin | These two pairs differ **by design** (`ARCHITECTURE 2.2`) |
| Add a skill without walking all 11 surfaces | `ARCHITECTURE 3.3`. Items 7, 10 and 11 are caught by **no test** |
| Say the stack uses TanStack Query | It uses TanStack **Table** + native fetch (`PRD 2.4`) |
| Invent a ShadCN component name | Check `design-framework/stage2-component-specs/shadcn-component-catalog.md` |
| Regenerate an artifact wholesale to fix a small change | That is what `artifact-sync` / `/sync-check` are for |
| Renumber a `PRD`/`ARCHITECTURE` section, or an artifact ID | Breaking change. Every citation and downstream reference dies |
| Claim an enforcement mechanism you have not written | Ship the test with the rule, or say plainly it is on discipline |
| Trust a count, table or path in a doc without checking disk | This repo's docs have drifted before. Verify, then assert |

---

## Rituals — keyed to what you touched

| If you touched | Then also |
|---|---|
| `skills/**` | You changed the **published npm package**. Treat as outward-facing (`ARCHITECTURE 1`) |
| A `SKILL.md` name or description | Walk `ARCHITECTURE 3.3` |
| A section number in `PRD.md` / `ARCHITECTURE.md` | Run `test_docs.py`; it lists every citation you broke |
| Anything under `features/` | Re-run `test_prohibitions.py` |
| A version number | Bump all **three**: `skills/package.json`, `skills/package-lock.json`, `skills/mcp-server.js` (`ARCHITECTURE 6.4`) |
| A skill or command count | Sweep `README.md` and `landing-page/index.html` (`ARCHITECTURE 1.2`) |
| Anything, after a correction from the owner | Append to `tasks/lessons.md` |
| Anything decided in conversation | Write it to `docs/decisions/` — a decision not written there did not happen |

---

## Conventions

**Citations.** Name the document: `PRD 5.2`, `ARCHITECTURE 4.5`. Never a bare number, never a symbol. A
citation that does not name its source cannot be machine-checked.

**Paths under `features/`.** Always quote them — folder names contain spaces (`PRD 7.1`).

**Card IDs.** `M<phase>-<nn>`, e.g. `M8-03`. The phase is an ID range; there is no separate phase structure.

**Commits.** Card ID in the subject. One card, one commit, clean tree.
**Never leave a dirty tree for the next session to find.**

**Commits.** Two commits are part of the protocol and need no permission: the claim line (step 5) and the
single card commit at Definition of done. **Anything else — and every push — needs the owner to ask.**

**Branch.** Work on a branch named for the milestone (`docs/multi-session-playbook`), not on `main`. A push to
`main` republishes the landing page immediately (`ARCHITECTURE 6.2`), so merging is the owner's call.

**This repo supersedes the global `tasks/todo.md` instruction.** Plans live in `tasks/BACKLOG.md` and
`tasks/cards/`; a shared todo file conflicts the moment two sessions run. Pending owner confirmation (STATE Q9).

---

## Commands

Six slash commands in `.claude/commands/` (Claude Code only; not shipped to installed projects).

| Command | Does |
|---|---|
| `/po-pipeline` | brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | USD → wireframes → component specs |
| `/validate-artifacts` | quality gates on a feature's artifacts |
| `/sync-check` | find stale artifacts after a change; generate surgical patches |
| `/pm-strategy` · `/pm-discovery` | PM sessions |

**Not built:** no `design-interactions` skill (stage 3 is manual), no wireframe or component-spec validator
skill. `/validate-artifacts` runs those gates inline.

---

## Working on X → read Y

| Working on | Read |
|---|---|
| Anything, first | `docs/STATE.md`, then `docs/INDEX.md` |
| A skill's behaviour | `skills/{name}/SKILL.md`, then the framework it cites |
| The artifact chain or frontmatter | `PRD 3`, `PRD 5` |
| Repo layout, twins, symlinks | `ARCHITECTURE 2` |
| The npm package or installers | `ARCHITECTURE 4` |
| Releasing | `ARCHITECTURE 6.4` |
| Why something is the way it is | `docs/decisions/`, then `docs/history/` |
| A new feature's artifacts | `features/Export Customs Clearances/` (`PRD 7.2`) |

---

## Definition of done

Paste this list into your final message with each item's **actual result**, not a claim that you did it.

- [ ] `python3 tests/test_docs.py` passes — output pasted
- [ ] `python3 tests/test_prohibitions.py` passes — output pasted
- [ ] The card's file set matches what you actually touched; if it grew, update the card **and** the
      `tasks/BACKLOG.md` row — an understated file set breaks the concurrency mechanism
- [ ] The card's Log records what you decided, what surprised you, and what you deliberately did not do
- [ ] Card status updated, and the BACKLOG row matches
- [ ] `docs/STATE.md`: in-flight row removed, Done row added, Next up re-derived, any new question added to
      Waiting on owner
- [ ] Every decision made in conversation written to `docs/decisions/`
- [ ] `tasks/lessons.md` appended if you were corrected
- [ ] Committed with the card ID in the subject, clean tree
