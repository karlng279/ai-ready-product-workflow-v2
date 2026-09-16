# ARCHITECTURE

**How this repository is built.** Authoritative on *mechanism*. For what artifacts and terms *mean*, see `PRD`.

Cite sections of this file as `ARCHITECTURE <n.n>` — e.g. `ARCHITECTURE 4.5`. Section numbers are load-bearing:
`tests/test_docs.py` resolves every citation, and renumbering is a breaking change.

---

## 1. What this repository is

Two products in one tree.

| | Purpose | Lives in |
|---|---|---|
| **Knowledge base** | Methodology an AI agent reads while producing product artifacts | `pm-framework/`, `po-framework/`, `design-framework/`, `codebase-framework/` |
| **npm package `ai-ready-workflow`** | Installs the skills into other people's projects | `skills/` — the whole directory is the package root |

There is no application code and no runtime. The only executable code is the `ui-ux-pro-max` Python search
scripts, the npm CLI, the MCP server, the two installers, and this repo's own test suite (`ARCHITECTURE 7`).

Because `skills/` is simultaneously the skill source of truth and the npm payload, **every change under
`skills/` is outward-facing** — it ships to installed projects on the next publish.

### 1.1 Directory map

```
├── CLAUDE.md                  # always-on rules (rules, not knowledge)
├── PRD.md                     # specification: meaning
├── ARCHITECTURE.md            # specification: mechanism (this file)
├── README.md                  # front door — a sweep site, see 1.2
├── AGENTS.md GEMINI.md .cursorrules   # per-agent skill indexes; twins of skills/ copies (2.2)
├── GETTING_STARTED.md         # onboarding for humans using the frameworks
├── docs/
│   ├── INDEX.md               # task → the exact sections it needs
│   ├── STATE.md               # status board; includes Waiting on owner
│   ├── decisions/             # NNNN-*.md, one per decision, + README index
│   ├── diagrams/              # Archify JSON + HTML, a dated as-is snapshot — not specification
│   ├── history/               # superseded plans, kept as record — not specifications
│   └── multi-session-repo-playbook.md   # the methodology this repo follows
├── tasks/
│   ├── BACKLOG.md             # the full plan, one row per unit of work
│   ├── cards/                 # one file per unit, authored just-in-time
│   └── lessons.md             # corrections, so they are not repeated
├── tests/                     # test_docs.py, test_prohibitions.py
├── skills/                    # 17 skills + the npm package (4)
├── .agent/skills/             # 17 symlinks into skills/ (2.1)
├── .claude/commands/          # 6 slash commands (5.1)
├── pm-framework/ po-framework/ design-framework/ codebase-framework/
├── features/                  # generated artifacts (PRD 7)
└── landing-page/              # marketing site, auto-deployed (6.2)
```

### 1.2 Sweep sites

`README.md` and `landing-page/index.html` summarise figures they do not own — skill counts, command counts,
framework names. This duplication is deliberate: a front door has to orient a reader. **Both are sweep
sites — change the source, change them.** `tests/test_docs.py` asserts the READMEs' skill sets in both directions (`check_readme_skill_set`) and sweeps
`landing-page/index.html` for banned strings, but nothing ties the landing page's skill grid to the real set
(`ARCHITECTURE 6.2`).

There is no `.env.example` and no `src/`. This repo has no environment variables of its own; the only secret is
the GitHub Actions `NPM_TOKEN` (`ARCHITECTURE 6.1`). Creating an empty `.env.example` would claim a mechanism
that does not exist.

---

## 2. Repository topology

### 2.1 Source of truth

```
skills/{name}/SKILL.md      ← CANONICAL. Every skill is authored here.
.agent/skills/{name}        → symlink to ../../skills/{name}
```

The `.agent/skills/` entries are **relative symlinks**, so editing either path edits the same inode. Claude Code
loads skills from `.agent/skills/`; everything else reads `skills/` directly. A new skill needs both
(`ARCHITECTURE 3.3`).

This is true *in this repository only*. In an installed project the same directory holds detached copies
(`ARCHITECTURE 4.5`).

### 2.2 The twin files

Three files exist twice, and the copies must stay **byte-identical**:

| Root | Twin | Why two |
|---|---|---|
| `AGENTS.md` | `skills/AGENTS.md` | root serves this repo; `skills/` copy is what npm ships and the installer drops into a user's project |
| `GEMINI.md` | `skills/GEMINI.md` | same |
| `.cursorrules` | `skills/.cursorrules` | same |

`tests/test_docs.py` asserts byte equality. They drifted once already — the `skills/` copies gained
`artifact-sync` and `/sync-check` while the root copies did not, and the root copies were stale for months.

Two further files exist twice but **intentionally differ**: `README.md` and `GETTING_STARTED.md`. The root pair
describes the *repository*; the `skills/` pair describes the *installed package*. Do not sync these.

### 2.3 Directories that look like skills but are not

`skills/documentation/` and `skills/skills/` contain nothing but a claude-mem stub. They have no `SKILL.md`, so
every enumerator (`ARCHITECTURE 3.1`) correctly ignores them. Do not treat them as skills; do not add a
`SKILL.md` to them.

---

## 3. The skill mechanism

### 3.1 How a skill is discovered

Discovery is **dynamic everywhere it matters** — a directory is a skill if and only if it contains `SKILL.md`:

- `skills/install.sh` and `skills/install.ps1` — `if [ ! -f "$skill_dir/SKILL.md" ]; then continue; fi`
- `skills/mcp-server.js` — `fs.readdirSync(SKILLS_DIR).filter(...)` on `SKILL.md` presence

Two places are **hand-maintained** and will silently go stale:

1. The `## Skills Registry` table inside `install.sh` and `install.ps1`, appended to a user's `CLAUDE.md`.
2. The skill count in the `skills/cli.js` help banner.

`tests/test_docs.py` asserts both: `check_skill_set_across_surfaces` for the registry tables and
`check_cli_banner` for the banner, each derived from the real skill set on disk.

### 3.2 Per-agent loading

| Agent | Entry point | Activation |
|---|---|---|
| Claude Code | `.agent/skills/*/SKILL.md` | auto-loaded when a trigger keyword in the skill's `description` matches |
| OpenAI Codex | `AGENTS.md` | user says "Read AGENTS.md then …" |
| Gemini Code Assist | `GEMINI.md` | user says "Read GEMINI.md then …" |
| Cursor | `.cursorrules` | auto-loaded on project open |
| Claude Desktop chat | `skills/mcp-server.js` via `npx ai-ready-workflow mcp` | MCP resources + `/` prompt picker |
| Any agent | `skills/*/SKILL.md` | read directly |

A skill's `description:` frontmatter is the trigger text. Trigger keywords belong in it, not in the body.

### 3.3 Adding or renaming a skill

Eleven surfaces. Miss one and the skill either fails to load or is invisible to three of the four agents.
`CLAUDE.md` is deliberately **not** one of them — it holds rules, not the registry.

**Items 7, 10 and 11 are asserted by nothing — they are on discipline.** Item 1 is asserted by
`tests/test_prohibitions.py` (`check_skill_frontmatter`); items 2–6, 8 and 9 by `tests/test_docs.py`.
Item 11 is partially covered: the banned-string sweep reads `landing-page/index.html`, but nothing ties its
skill grid to the real set.

1. `skills/{name}/SKILL.md` with `name:` and `description:` frontmatter
2. `ln -s ../../skills/{name} .agent/skills/{name}` — relative symlink, not a copy
3. `AGENTS.md` **and** `skills/AGENTS.md`
4. `GEMINI.md` **and** `skills/GEMINI.md`
5. `.cursorrules` **and** `skills/.cursorrules`
6. `README.md` **and** `skills/README.md`
7. `GETTING_STARTED.md` **and** `skills/GETTING_STARTED.md`
8. The registry tables in `skills/install.sh` **and** `skills/install.ps1`
9. The `skills/cli.js` help banner
10. `skills/package.json` `files` — `*/SKILL.md` ships automatically, but any **non-SKILL.md asset** needs an
    explicit entry, as `ui-ux-pro-max/scripts/` and `ui-ux-pro-max/data/` have
11. `landing-page/index.html` counts

---

## 4. The npm package

### 4.1 Identity and contents

`skills/package.json` — name `ai-ready-workflow`, bin `ai-ready-workflow` → `cli.js`, one **declared** dependency
(`@modelcontextprotocol/sdk`), Node >= 18. `mcp-server.js` also does `require('zod')`, which is undeclared —
it resolves today only as a transitive dependency of the SDK. A hoisting change would break `npx … mcp`.

The `files` array ships: `cli.js`, `mcp-server.js`, `smithery.yaml`, `install.sh`, `install.ps1`, `AGENTS.md`,
`GEMINI.md`, `.cursorrules`, `GETTING_STARTED.md`, `*/SKILL.md`, `ui-ux-pro-max/scripts/`,
`ui-ux-pro-max/data/`.

### 4.2 The CLI

Three commands, dispatched in `skills/cli.js`:

| Command | Effect |
|---|---|
| `install` | copies skills to `<target>/.agent/skills/`, entry-point files to the target root, appends a registry to an existing `CLAUDE.md` (`ARCHITECTURE 4.4`) |
| `install-cowork` | copies skills into Claude Desktop's Local Agent skills folder. **macOS only** — hard-exits on any other platform |
| `mcp` | starts the MCP stdio server (`ARCHITECTURE 4.3`) |

### 4.3 The MCP server

`skills/mcp-server.js` enumerates skills at startup and exposes each as an MCP **resource** (`skill://<name>`)
and as a prompt, plus **three** tools: `list_skills`, `get_skill` and `search_ui_ux`. The last spawns
`python3 ui-ux-pro-max/scripts/search.py`, so **Python 3 is a runtime requirement of the MCP server**, not
only of the skill. Consumed by Claude Desktop's regular chat via a `claude_desktop_config.json` entry running
`npx -y ai-ready-workflow mcp`.

Its server banner hardcodes a version (`mcp-server.js:35`) — the third place a version lives
(`ARCHITECTURE 6.4`).

### 4.4 The installers

`install.sh` (Mac/Linux) and `install.ps1` (Windows) do the same four things:

1. Copy every directory containing `SKILL.md` to `<target>/.agent/skills/`, **skipping any that already exist**
2. Copy `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `GETTING_STARTED.md` to the target root, skipping existing
3. **Append** a `## Skills Registry` table to `<target>/CLAUDE.md` — only if that file already exists, and only
   if it does not already contain the string `Skills Registry`. The installer never creates a `CLAUDE.md`
4. Print per-agent next steps

Because step 1 skips existing directories, **re-running the installer does not upgrade skills**. There is no
upgrade path; a user must delete a skill folder to get a newer copy.

### 4.5 Repo vs installed project

| | This repo | Installed project |
|---|---|---|
| `.agent/skills/{name}` | symlink into `skills/` | detached copy, never refreshed (`ARCHITECTURE 4.4`) |
| `pm-framework/` `po-framework/` `design-framework/` `codebase-framework/` | present | **absent** — not in `files` |
| `.claude/commands/` | 6 commands | **absent** — not in `files` |

**This is a live functional gap.** Every `SKILL.md` opens with a Knowledge Base pointer such as
`po-framework/stage1-prd/rules.md`, and `skills/po-brief-to-prd/SKILL.md` states *"Always read
`po-framework/stage1-prd/rules.md` before producing a PRD."* In an installed project that path does not exist,
so the skill runs on its `SKILL.md` body alone. Either ship the framework directories or make each `SKILL.md`
degrade gracefully. Tracked in `docs/STATE.md` under Known broken; not yet decided.

---

## 5. Pipelines as mechanism

### 5.1 Slash commands

Six files in `.claude/commands/`. Claude Code only — they are not shipped (`ARCHITECTURE 4.5`).

| Command | Chains | Writes |
|---|---|---|
| `/po-pipeline` | 5 PO skills in order | `features/{name}/po/**` |
| `/design-pipeline` | `design-wireframe` → `design-component-spec` | `features/{name}/design/**` |
| `/validate-artifacts` | `validate-prd`, `validate-usd`, plus inline gate checks | nothing — reports only |
| `/sync-check` | `artifact-sync` | patches, after confirmation |
| `/pm-strategy` | `pm-product-strategy` | `features/{name}/pm/strategy.md` |
| `/pm-discovery` | `pm-product-discovery` | `features/{name}/pm/discovery.md` |

`.claude/commands/CLAUDE.md` is a claude-mem stub, not a command. The count is six.

### 5.2 Stage folder layout

Layout differs by pipeline. Check before assuming a file exists.

| Pipeline | Per-stage files |
|---|---|
| PO (`stage1-prd` … `stage5-uat`) | `rules.md`, `quality-gate.md`, `template.md`, `prompts.md`, `example.md` (singular) |
| Design (`stage1-wireframes` … `stage3-interactions`) | `rules.md`, `quality-gate.md`, `prompts.md`, `examples.md` (plural), plus purpose-named templates |
| PM (6 pillars) | `rules.md`, `templates/` (3 each), `examples/` (1 each) |

`po-framework/stage2-usm/template.md` does not exist; that stage works from `rules.md` + `example.md`.

---

## 6. Continuous integration

### 6.1 npm publish

`.github/workflows/npm-publish.yml` fires **only on `v*` tags**, runs with `working-directory: skills`, and
runs `npm publish --access public` with the `NPM_TOKEN` secret. Nothing publishes on a push to `main`.

### 6.2 Landing page

`.github/workflows/deploy-landing.yml` fires on **every push to `main`**, with no paths filter, and uploads all
of `landing-page/`. Any commit to main republishes the site, so stale figures there go live immediately.

### 6.3 Documentation checks

`.github/workflows/tests.yml` runs both test files on every push to any branch and on every pull request.
`npm-publish.yml` will not publish unless they pass. Nothing else gates on them.

### 6.4 Release contract

1. Bump the version in **three** places: `skills/package.json`, `skills/package-lock.json`, and the
   hardcoded banner at `skills/mcp-server.js:35`
2. Sweep `landing-page/index.html` and `README.md` (`ARCHITECTURE 1.2`)
3. Commit, `git tag v<version>`, push the tag

---

## 7. The test suite

Two dependency-free Python files. No pytest — run them directly:

```bash
python3 tests/test_docs.py
python3 tests/test_prohibitions.py
```

Both exit non-zero on failure and print every violation with a path. They are also importable by pytest if it
is ever added.

### 7.1 `tests/test_docs.py` — documentation freshness

One `check_*` function per rule:

| Check | Asserts |
|---|---|
| `check_twins_byte_identical` | the three agent indexes equal their `skills/` copies |
| `check_readme_pair_differs` | `README.md` / `GETTING_STARTED.md` are **not** synced with their twins |
| `check_symlinks_match_skills` | one relative symlink per skill, both directions |
| `check_skill_set_across_surfaces` | the skill **set** in six indexes and both installer tables, both directions |
| `check_readme_skill_set` | the skill set in both READMEs, both directions |
| `check_cli_banner` | the `cli.js` count, derived from disk |
| `check_command_set` | the command set across ten surfaces |
| `check_citations_resolve` | every `PRD n.n` / `ARCHITECTURE n.n` names a real section |
| `check_links_resolve` | every relative link, minus the allowlist |
| `check_backlog_and_state_cards` | card IDs and statuses agree across BACKLOG, STATE and card files |
| `check_claimable_cards_are_unblocked` | nothing under STATE 'Next up' is blocked in BACKLOG |
| `check_decision_index` | `docs/decisions/` and its README index match |
| `check_banned_strings` | banned strings stay banned, across `.md`, `.cursorrules` and the landing page |
| `check_state_freshness` | `docs/STATE.md` carries a Last-updated date |
| `check_claude_md_is_rules_only` | `CLAUDE.md` stays under 150 lines |

Citation checking skips `docs/history/`, `features/` and the playbook itself — history must be allowed to
cite sections that have since been renumbered.

Links already dead when the checker was introduced are listed in `tests/known_dead_links.txt`, one row per
link with a reason. The allowlist is asserted **both ways**: an entry that starts resolving fails, so the
list cannot rot. Never add a row without tracking the fix.

### 7.2 `tests/test_prohibitions.py` — content rules

One `check_*` function per rule:

| Check | Asserts |
|---|---|
| `check_artifact_frontmatter` | all seven fields present **and non-empty** (`PRD 5.1`) |
| `check_artifact_values` | `artifact:` is in the `PRD 5.2` set |
| `check_status_values` | `status:` is `draft`, `review` or `approved` (`PRD 5.3`) |
| `check_generated_by_names_a_skill` | `generated-by:` is a real skill, or one of two declared exceptions |
| `check_feature_matches_folder` | `feature:` mirrors the folder name exactly |
| `check_no_per_id_design_files` | no `WF-*.md` or `INT-*.md` under any `design/` (`PRD 3.2`) |
| `check_skill_frontmatter` | every `SKILL.md` has `name:` and `description:`, and `name` matches its directory |

The two declared `generated-by` exceptions are `design-interactions` and `pm-to-po-handoff`; both are listed
in `docs/STATE.md` under Known broken.

### 7.3 Detectors must bite

Each file ends with a self-probe. It exercises the **pattern-matching** detectors — the banned-string regexes
and the `WF-*`/`INT-*` filename matcher — against known-bad and known-good inputs, checks that the frontmatter
parser accepts a valid block and rejects a missing one, and asserts that the skill, command, section and file
enumerators return something rather than silently nothing.

It does **not** prove every `check_*` function would fail on a real defect. That is what the mutation pass in
the M9-01 card log did, and it is worth repeating when a detector changes.
