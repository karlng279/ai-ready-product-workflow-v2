# npm Publish Plan — `ai-ready-workflow`

> **Status:** v0.1.0 is live on npm. This document now tracks the ongoing publish workflow and version history.

---

## Version History

| Version | What changed | Status |
|---|---|---|
| `0.1.0` | Initial publish — 16 skills, CLI, install scripts | ✅ Live |
| `0.1.1` | Multi-agent fix + documentation (Phase 7e) | ⬜ Pending |

---

## What Was Fixed to Get 0.1.0 Live

The original error:
```
npm error 404 Not Found - GET https://registry.npmjs.org/ai-ready-workflow - Not found
```

Root cause: `skills/package.json` existed locally but was never published. Two additional issues found during publish:
1. npm token was a **Publish** type — required 2FA OTP. Fixed by generating an **Automation** token.
2. `bin` entry used `"./cli.js"` — npm auto-corrected to `"cli.js"`. Fixed in package.json.
3. `cli.js` was not marked executable — fixed with `chmod +x`.

---

## Critical Finding (Phase 7e Audit)

**The installer only provisions Claude Code.** After `npx ai-ready-workflow install`:
- `AGENTS.md`, `GEMINI.md`, `.cursorrules` are **not** copied to the target project
- These files are **not** in the npm `files` array
- Non-Claude agents (Codex, Gemini, Cursor) get skills but no entry point index

Full fix scope is in [npm-docs-plan.md](npm-docs-plan.md).

**0.1.1 will fix this** — see Phase 7e in [backlog.md](backlog.md).

---

## Publish Workflow (all versions)

### Prerequisites
- npm Automation token stored in `~/.npmrc` (already configured)
- `NPM_TOKEN` secret set in GitHub repo (already configured for GitHub Actions)

### Manual publish
```bash
cd skills/
npm publish --access public
```

### Automated publish (via GitHub Actions)
Push a `v*` tag — the workflow in `.github/workflows/npm-publish.yml` handles the rest:
```bash
# 1. Bump version in skills/package.json
# 2. Commit the change
git tag v0.1.1
git push origin v0.1.1
```

### Verify after publish
```bash
npm info ai-ready-workflow          # check version, bin, files
```

---

## 0.1.1 Pre-Publish Checklist

Before publishing 0.1.1, confirm all 7e tasks are done:

- [ ] `skills/AGENTS.md` created (copied from repo root)
- [ ] `skills/GEMINI.md` created (copied from repo root)
- [ ] `skills/.cursorrules` created (copied from repo root)
- [ ] `skills/install.sh` updated — copies 3 entry point files to target root
- [ ] `skills/install.ps1` updated — same for Windows
- [ ] `skills/GETTING_STARTED.md` created — per-agent onboarding guide
- [ ] `skills/README.md` updated — badges, all-agent table, after-install section
- [ ] `skills/cli.js` updated — agent-aware post-install banner
- [ ] `skills/package.json` updated — 4 new files in array, version bumped to `0.1.1`
- [ ] `npm pack --dry-run` confirms all new files are included
- [ ] `npm publish --access public` runs clean

### End-to-End Test
```bash
mkdir /tmp/aiwf_test && cd /tmp/aiwf_test
npx ai-ready-workflow install
ls .agent/skills/           # 16 skill folders
ls AGENTS.md GEMINI.md .cursorrules GETTING_STARTED.md   # all 4 present
```

---

## Files Changed (cumulative)

| File | Version | Action |
|---|---|---|
| `documentation/npm-publish-plan.md` | — | Created and maintained (this file) |
| `documentation/backlog.md` | — | Tracks 7c, 7d, 7e progress |
| `.github/workflows/npm-publish.yml` | 0.1.0 | Created — auto-publish on `v*` tags |
| `skills/package.json` | 0.1.0 | `./cli.js` → `cli.js` in bin; version set |
| `skills/cli.js` | 0.1.0 | `chmod +x` applied |
| `skills/AGENTS.md` | 0.1.1 | To create |
| `skills/GEMINI.md` | 0.1.1 | To create |
| `skills/.cursorrules` | 0.1.1 | To create |
| `skills/install.sh` | 0.1.1 | To update — multi-agent entry point copy |
| `skills/install.ps1` | 0.1.1 | To update — multi-agent entry point copy |
| `skills/GETTING_STARTED.md` | 0.1.1 | To create |
| `skills/README.md` | 0.1.1 | To update |
| `skills/cli.js` | 0.1.1 | To update — post-install banner |
| `skills/package.json` | 0.1.1 | To update — files array + version bump |
