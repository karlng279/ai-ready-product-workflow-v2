# INDEX — task to the sections it needs

**This file points; it does not specify.** Some answer cells restate a single fact for orientation — that is a
deliberate, bounded duplication, and **the cited section always wins**. If an answer here and its source
disagree, the source is right and this row is a bug.

`PRD.md` and `ARCHITECTURE.md` are ~550 lines together. Reading both to orient wastes a context window and
still misses the detail that mattered. Find your row, read those sections, stop.

---

## 1. By area — "I am about to work on X"

| Working on | Read | Then | Tests it must pass |
|---|---|---|---|
| **Adding a skill** | `ARCHITECTURE 3.3` | `ARCHITECTURE 3.1`, `2.2` | `test_docs.py` — skill-set agreement, twin equality |
| **Editing a `SKILL.md` body** | the skill's own file | the framework it cites (`PRD 2`) | `test_prohibitions.py` — frontmatter present |
| **A skill's trigger keywords** | `ARCHITECTURE 3.2` | — | `test_docs.py` |
| **Agent index files** (`AGENTS.md`, `GEMINI.md`, `.cursorrules`) | `ARCHITECTURE 2.2` | `ARCHITECTURE 3.3` | `test_docs.py` — byte-identical twins |
| **`README.md` / `GETTING_STARTED.md`** | `ARCHITECTURE 1.2`, `2.2` | — | `test_docs.py` — sweep-site sets |
| **The npm package** | `ARCHITECTURE 4.1`–`4.4` | `ARCHITECTURE 4.5` | `test_docs.py` |
| **Installers** | `ARCHITECTURE 4.4`, `3.1` | — | `test_docs.py` — registry table vs real skills |
| **The MCP server** | `ARCHITECTURE 4.3` | `ARCHITECTURE 3.1` | — |
| **Releasing a version** | `ARCHITECTURE 6.4` | `ARCHITECTURE 6.1`, `ARCHITECTURE 6.3`, `ARCHITECTURE 1.2` | both |
| **Slash commands** | `ARCHITECTURE 5.1` | the skills it chains | `test_docs.py` — command set |
| **Generating a feature's artifacts** | `PRD 3`, `PRD 5` | `PRD 7.2` (reference implementation) | `test_prohibitions.py` |
| **Wireframes or interactions** | `PRD 3.2` **first** | `design-framework/stage1-wireframes/rules.md` | `test_prohibitions.py` — no `WF-XXX.md` files |
| **Frontmatter on any artifact** | `PRD 5.1`, `5.2` | `PRD 5.3` | `test_prohibitions.py` |
| **`artifact-sync` / `/sync-check`** | `PRD 5.4`, `5.5` | `docs/history/artifact-sync-plan.md` | — |
| **Quality gates / validation** | `PRD 6` | the stage's `quality-gate.md` | — |
| **The framework knowledge bases** | `PRD 2` | `ARCHITECTURE 5.2` (layout differs by pipeline) | — |
| **`ui-ux-pro-max`** | `skills/ui-ux-pro-max/SKILL.md` | `docs/INDEX.md 3` (trap row) | — |
| **The landing page** | `ARCHITECTURE 6.2`, `1.2` | — | discipline only |
| **These documents themselves** | `docs/multi-session-repo-playbook.md` | `ARCHITECTURE 7` | both |

---

## 2. By question — "I need to know Y"

| Question | Answer |
|---|---|
| What does `artifact: OST` mean? | `PRD 5.2` |
| Where do wireframes get written? | `PRD 3.2` — one `wireframes.md`, not per-screen files |
| What are the required frontmatter fields? | `PRD 5.1` |
| Are the sync fields (`sync_status` etc.) in use? | `PRD 5.4` — specified, **not applied to anything** |
| What does `change_type: interface` propagate to? | `PRD 5.5` — forward **and** backward |
| How many skills are there, and where is that asserted? | `ARCHITECTURE 3.3`; asserted as a **set** in `test_docs.py` |
| Why do `AGENTS.md` and `skills/AGENTS.md` both exist? | `ARCHITECTURE 2.2` |
| Why do `README.md` and `skills/README.md` differ? | `ARCHITECTURE 2.2` — by design; do not sync |
| What ships in the npm package? | `ARCHITECTURE 4.1` |
| Why does a skill behave differently in an installed project? | `ARCHITECTURE 4.5` |
| How do I publish? | `ARCHITECTURE 6.4` |
| What does a push to `main` trigger? | `ARCHITECTURE 6.2` — republishes the landing page, every time |
| What is the target stack? | `PRD 2.4` — TanStack **Table**, not Query |
| What is claimable right now? | `docs/STATE.md` |
| What am I (the owner) blocking? | `docs/STATE.md` → Waiting on owner |
| Why was X decided? | `docs/decisions/` |
| What was the old plan? | `docs/history/` — record only, **not specification** |
| How do I cite a section? | `CLAUDE.md` → Conventions |
| What does a card look like? | `tasks/cards/TEMPLATE.md` |

---

## 3. Traps — defects this project has already paid for

Every row is a real defect that shipped. A session that reads this table does not ship it again.

| Trap | What happened | Section |
|---|---|---|
| **Wireframe path** | Six docs and two slash commands said `design/WF-XXX.md` per screen. The skill, the framework rules and every artifact on disk use one `design/wireframes.md`. An agent following the docs wrote the wrong files. | `PRD 3.2` |
| **TanStack Query** | Nine documents named a library the codebase framework has **zero** references to. It prescribes TanStack Table. | `PRD 2.4` |
| **Twin drift** | `skills/AGENTS.md` gained `artifact-sync` and `/sync-check`; the root copies did not, and stayed stale for months. | `ARCHITECTURE 2.2` |
| **Hardcoded registry in the installers** | The skill *copy loop* is dynamic, but the registry table appended to a user's `CLAUDE.md` is hand-written. It shipped 16 skills after the 17th landed. | `ARCHITECTURE 3.1` |
| **Prose counting** | `CLAUDE.md` said "16+ skills, 5 commands" while its own tables listed 17 and 6. Assert the set, never the number. | `ARCHITECTURE 7.1` |
| **PM artifact values** | `/pm-strategy` and `/pm-discovery` wrote `artifact: PM-STRATEGY` / `PM-DISCOVERY`; the skills and every artifact on disk use `STRATEGY` / `OST`. | `PRD 5.2` |
| **Stale skill frontmatter** | `ui-ux-pro-max` advertised "50 styles, 21 palettes, 20 charts, 9 stacks". The real database is 67 / 96 / 25 / 13. The `description` is the **trigger text**, so this degraded matching. | `ARCHITECTURE 3.2` |
| **Sync fields presented as standard** | `README.md` showed five `artifact-sync` fields as part of normal frontmatter. Nothing on disk has ever carried them. | `PRD 5.4` |
| **Dead knowledge-base pointers** | Every `SKILL.md` cites `po-framework/…`, which the npm package does not ship. In an installed project the path does not exist. | `ARCHITECTURE 4.5` |
| **Dead links** | 48 on the link checker's first run — 44 of them years old. Six files still reference `design-framework-uiux-promax-integration-plan.md`, which never existed. | `ARCHITECTURE 7.1` |
| **Version in three places** | `package.json` `0.2.0`, `package-lock.json` `0.1.2`, `mcp-server.js:35` `0.1.2`, and no tag — so nothing was published. | `ARCHITECTURE 6.4` |
| **Unresolved traceability** | All 12 USD files carry the literal placeholder `WF-XXX` in their Design Reference column. The tables look resolved; they are not. | `PRD 7.2` |
| **Escalating a permission denial** | A read of `~/Downloads` was retried with the sandbox disabled; that collapsed the app's Files-and-Folders grant and locked the whole repo out mid-session. Ask for the file instead. | `tasks/lessons.md` |
