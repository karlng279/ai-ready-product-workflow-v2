# Getting Started — AI-Ready Product Workflow

You just installed **16 skills** across 4 frameworks for AI-assisted product development.

**What was installed:**
- `.agent/skills/` — 16 skill folders in your project root (Claude Code auto-loads from here)
- `AGENTS.md` — skill index for OpenAI Codex / ChatGPT
- `GEMINI.md` — skill index for Gemini Code Assist
- `.cursorrules` — rules file auto-loaded by Cursor

---

## Agent Setup

### Claude Desktop — Cowork / Local Agent Mode

Skills must be installed into Claude Desktop's skill folder:

```bash
npx ai-ready-workflow install-cowork
```

Then **restart Claude Desktop**. All 16 skills will appear under `/mnt/skills/user/` in Local Agent sessions and activate automatically on trigger keywords.

---

### Claude Desktop — Regular Chat (MCP)

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ai-ready-workflow": {
      "command": "npx",
      "args": ["-y", "ai-ready-workflow", "mcp"]
    }
  }
}
```

Restart Claude Desktop. Skills are available as MCP prompts (click `+` in chat input) and tools (`list_skills`, `get_skill`).

---

### Claude Code

Skills activate automatically — no setup needed.

When you mention a trigger keyword in conversation, Claude Code loads the matching skill and applies its methodology.

**Example prompts:**
- "Create a PRD for a user authentication feature"
- "Build a user story map from this PRD"
- "Write UAT test cases for ST-001"
- "Help me run a product strategy session"

**Pipeline slash commands** (chain multiple stages automatically):

| Command | What it does |
|---|---|
| `/po-pipeline` | Brief → PRD → USM → USL → USD → UAT |
| `/design-pipeline` | USD → Wireframes → Component Specs |
| `/validate-artifacts` | Quality gate check on all feature artifacts |
| `/pm-strategy` | Product strategy session |
| `/pm-discovery` | Discovery sprint session |

---

### OpenAI Codex / ChatGPT

Point Codex to `AGENTS.md` at your project root before starting work.

**Setup prompt:**
```
Read AGENTS.md at the project root to understand the skill library and frameworks available.
```

**Example prompts:**
- "Read AGENTS.md, then help me create a PRD for a user authentication feature"
- "Using the po-brief-to-prd skill in AGENTS.md, convert this brief into a PRD"
- "Check AGENTS.md for the validate-prd skill, then validate this PRD"

---

### Cursor

`.cursorrules` is auto-loaded by Cursor when you open the project — no setup needed.

Cursor reads the rules file on project open and applies the skill registry and framework conventions automatically.

**Example prompts:**
- "Create a PRD for a user authentication feature"
- "Generate a user story map from this PRD using the PO pipeline"
- "Validate this PRD against the quality gate"

---

### Gemini Code Assist

Point Gemini to `GEMINI.md` at your project root before starting work.

**Setup prompt:**
```
Read GEMINI.md at the project root to understand the skill library and frameworks available.
```

**Example prompts:**
- "Read GEMINI.md, then help me create a PRD for a user authentication feature"
- "Using the pm-product-strategy skill from GEMINI.md, run a product strategy session"
- "Check GEMINI.md for the po-usd-to-uat skill, then generate test cases for this story"

---

## Key Concepts

### Artifact IDs

Every generated artifact gets a unique ID for traceability:

| Artifact | ID | File |
|---|---|---|
| Product Requirements Doc | `PRD-XXX` | `features/{name}/po/prd.md` |
| User Story Map | `USM-XXX` | `features/{name}/po/usm.md` |
| User Story | `ST-XXX` | `features/{name}/po/usl.md` |
| Acceptance Criteria | `AC-XXX` | `features/{name}/po/usd/ST-XXX.md` |
| UAT Test Case | `TC-XXX` | `features/{name}/po/uat/ST-XXX.md` |
| Wireframe | `WF-XXX` | `features/{name}/design/WF-XXX.md` |
| Component Spec | `COMP-XXX` | `features/{name}/design/COMP-XXX.md` |
| PM Strategy | `PM-STRATEGY` | `features/{name}/pm/strategy.md` |
| PM Discovery | `PM-DISCOVERY` | `features/{name}/pm/discovery.md` |

### Feature Folder Structure

All artifacts for a feature live under `features/{feature-name}/`:

```
features/{feature-name}/
├── pm/           # PM artifacts (strategy, discovery, GTM)
├── po/
│   ├── prd.md
│   ├── usm.md
│   ├── usl.md
│   ├── usd/      # One file per story: ST-XXX.md
│   └── uat/      # One file per story: ST-XXX.md
├── design/
│   ├── WF-XXX.md
│   └── COMP-XXX.md
└── code/
```

### Traceability Chain

The full pipeline from idea to implementation:

```
Brief → PRD → USM → USL → USD → UAT → Wireframe → Component Spec
```

Each artifact references its upstream and downstream in YAML frontmatter, keeping the chain intact as work evolves.

---

## Go Deeper

Full framework documentation is in the source repository:

- **PO Framework** — `po-framework/` (5-stage pipeline rules, templates, examples)
- **PM Framework** — `pm-framework/` (6 PM areas: strategy, discovery, research, analytics, growth, GTM)
- **Design Framework** — `design-framework/` (wireframe conventions, component spec format)
- **Codebase Framework** — `codebase-framework/` (Next.js 15 + ShadCN + TanStack Query)

Repository: [https://github.com/karlng279/ai-ready-product-workflow-v2](https://github.com/karlng279/ai-ready-product-workflow-v2)
