# npm Documentation Plan — `ai-ready-workflow`

> **Updated after Phase 7e audit.** The original plan (7d) assumed docs were the only gap. The audit revealed a more critical issue: the installer only provisions Claude Code. This plan now covers both the code fix (7e code) and the documentation work (7e docs) as a single coordinated effort.

---

## Problem (Revised)

Two distinct gaps were found:

**Gap 1 — Installer is Claude-only (critical)**
After `npx ai-ready-workflow install`, non-Claude agents get nothing useful. `AGENTS.md`, `GEMINI.md`, and `.cursorrules` are never copied to the target project and are not in the npm `files` array. The package description says "for Claude Code and other AI agents" — but only Claude Code actually works.

**Gap 2 — No user-facing documentation (original 7d concern)**
`skills/README.md` is shipped but reads like an internal dev reference. No badges, no "what you get" summary, no post-install guidance. No `GETTING_STARTED.md` exists for any agent.

---

## Agent Support Matrix (current vs. target)

| Agent | Skills copied | Entry point provisioned | Current | Target |
|---|---|---|---|---|
| Claude Code | ✅ `.agent/skills/` | ✅ `CLAUDE.md` patched | Full support | Full support |
| OpenAI Codex | ✅ `.agent/skills/` | ❌ `AGENTS.md` not copied | Broken | Fixed in 7e |
| Gemini Code Assist | ✅ `.agent/skills/` | ❌ `GEMINI.md` not copied | Broken | Fixed in 7e |
| Cursor | ✅ `.agent/skills/` | ❌ `.cursorrules` not copied | Broken | Fixed in 7e |

---

## What Needs to Change

### Part A — Code Fix (must come first)

| Gap | Fix |
|---|---|
| Entry point files not in npm package | Create `skills/AGENTS.md`, `skills/GEMINI.md`, `skills/.cursorrules` — maintained in `skills/` for packaging |
| Installer skips non-Claude agents | Update `install.sh` + `install.ps1` — copy the 3 entry point files to target project root (skip if already exists) |
| `files` array incomplete | Add `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `GETTING_STARTED.md` to `skills/package.json` |

### Part B — Documentation

| Gap | Fix |
|---|---|
| No per-agent onboarding guide | Create `skills/GETTING_STARTED.md` with 4 agent-specific sections |
| README not optimized for npm | Rework `skills/README.md` — badges, "what you get", "after install", all-agent entry point table |
| CLI silent after install | Update `skills/cli.js` — print agent-aware post-install banner |

---

## File-by-File Plan

### 1. `skills/AGENTS.md` — New (copy from repo root)

Copied from `AGENTS.md` at repo root and maintained as the canonical version inside `skills/` for npm packaging. The installer copies this to the target project root.

Content covers: framework overview, full 16-skill registry with trigger keywords, artifact ID system, feature folder structure, traceability frontmatter.

---

### 2. `skills/GEMINI.md` — New (copy from repo root)

Same as above for Gemini Code Assist. Copied from `GEMINI.md` at repo root.

---

### 3. `skills/.cursorrules` — New (copy from repo root)

Same as above for Cursor. Copied from `.cursorrules` at repo root.

---

### 4. `skills/install.sh` + `skills/install.ps1` — Update

After the existing skill-copy loop, add logic to copy agent entry points to the target project root:

```bash
# Copy agent entry point files to target root (skip if already exists)
for f in AGENTS.md GEMINI.md .cursorrules; do
  src="$SCRIPT_DIR/$f"
  dst="$TARGET/$f"
  if [ -f "$src" ] && [ ! -f "$dst" ]; then
    cp "$src" "$dst"
    echo "  + $f"
  fi
done
```

Same logic for `install.ps1` in PowerShell.

---

### 5. `skills/package.json` — Update files array + bump version

```json
{
  "version": "0.1.1",
  "files": [
    "cli.js",
    "install.sh",
    "install.ps1",
    "AGENTS.md",
    "GEMINI.md",
    ".cursorrules",
    "GETTING_STARTED.md",
    "*/SKILL.md",
    "ui-ux-pro-max/scripts/",
    "ui-ux-pro-max/data/"
  ]
}
```

Note: `README.md` is auto-included by npm and does not need to be listed.

---

### 6. `skills/GETTING_STARTED.md` — New file

Onboarding guide for users across all 4 agents. Sections:

**Intro** — What was just installed, where it lives (`.agent/skills/`), what the entry point files are.

**Section 1 — Claude Code**
- How skills auto-load (keyword triggers in conversation)
- Available slash commands: `/po-pipeline`, `/design-pipeline`, `/validate-artifacts`, `/pm-strategy`, `/pm-discovery`
- First prompt example: "Create a PRD for a user authentication feature"

**Section 2 — OpenAI Codex / ChatGPT with code interpreter**
- Point Codex to `AGENTS.md` at project root
- How to reference skills: "Read `AGENTS.md` then help me write a PRD"
- First prompt example

**Section 3 — Cursor**
- `.cursorrules` is auto-loaded by Cursor on project open
- No extra setup needed — skills are referenced automatically
- First prompt example

**Section 4 — Gemini Code Assist**
- Point Gemini to `GEMINI.md` at project root
- How to reference skills in a prompt
- First prompt example

**Section 5 — Key concepts (all agents)**
- Artifact IDs (PRD-XXX, ST-XXX, AC-XXX, etc.)
- Feature folder structure
- Traceability chain: Brief → PRD → USM → USL → USD → UAT → Wireframe → Component

**Section 6 — Go deeper**
- Link to full repo for framework docs (`pm-framework/`, `po-framework/`, etc.)

---

### 7. `skills/README.md` — Rework for npm page

Add at the **top**:
- npm badges: version, license, node version
- One-line pitch
- "What you get" summary (16 skills, 4 frameworks, 5 pipeline commands, 4 agent support)

Add **"After install"** section:
- Files copied and where
- Agent entry point table (all 4 agents, their entry point file, how skills activate)
- Pointer to `GETTING_STARTED.md`

Keep existing: skill catalogue, artifact ID system, feature folder structure, multi-agent compatibility table, traceability frontmatter.

---

### 8. `skills/cli.js` — Post-install banner

After successful install, print an agent-aware banner:

```
  ✓ Installed 16 skill(s) to .agent/skills/
  ✓ Copied agent entry points: AGENTS.md, GEMINI.md, .cursorrules

  Next steps by agent:
    Claude Code   → mention a keyword: "create a PRD for..."
    Cursor        → .cursorrules auto-loaded on project open
    Codex/Gemini  → "Read AGENTS.md then help me write a PRD"

  Full guide:  GETTING_STARTED.md (in your project root)
  Docs:        https://github.com/karlng279/ai-ready-product-workflow-v2
```

---

## Files to Change

| File | Action |
|---|---|
| `skills/AGENTS.md` | Create — copied from repo root |
| `skills/GEMINI.md` | Create — copied from repo root |
| `skills/.cursorrules` | Create — copied from repo root |
| `skills/install.sh` | Edit — add entry point copy logic |
| `skills/install.ps1` | Edit — add entry point copy logic (PowerShell) |
| `skills/package.json` | Edit — add 4 files to array, bump to `0.1.1` |
| `skills/GETTING_STARTED.md` | Create — per-agent onboarding guide |
| `skills/README.md` | Edit — badges, "what you get", "after install" section |
| `skills/cli.js` | Edit — agent-aware post-install banner |

---

## Publish Step

```bash
cd skills/
npm publish --access public
```

---

## Verification Checklist

1. `npm info ai-ready-workflow` — version `0.1.1`
2. `npx ai-ready-workflow install` in a blank dir
3. Check `.agent/skills/` — 16 folders
4. Check project root — `AGENTS.md`, `GEMINI.md`, `.cursorrules`, `GETTING_STARTED.md` all present
5. CLI output — post-install banner lists all 4 agents
6. npmjs.com package page — updated README with badges and all-agent entry point table
