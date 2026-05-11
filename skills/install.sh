#!/usr/bin/env bash
# install.sh — AI-Ready Product Workflow skill installer
# Copies all skills to .agent/skills/ in the target project and optionally patches CLAUDE.md.
#
# Usage:
#   ./skills/install.sh                   # installs into current directory
#   ./skills/install.sh /path/to/project  # installs into specified directory
#   npx ai-ready-workflow install         # same via npx

set -euo pipefail

# ── Resolve paths ─────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$(pwd)}"
AGENT_SKILLS_DIR="$TARGET_DIR/.agent/skills"

# ── Banner ────────────────────────────────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║   AI-Ready Product Workflow — Skill Installer    ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""
echo "  Source : $SCRIPT_DIR"
echo "  Target : $AGENT_SKILLS_DIR"
echo ""

# ── Create destination directory ──────────────────────────────────────────────
mkdir -p "$AGENT_SKILLS_DIR"

# ── Copy skill folders ────────────────────────────────────────────────────────
SKILLS_COPIED=0
SKILLS_SKIPPED=0

for skill_dir in "$SCRIPT_DIR"/*/; do
  skill_name="$(basename "$skill_dir")"

  # Only process directories that contain a SKILL.md
  if [ ! -f "$skill_dir/SKILL.md" ]; then
    continue
  fi

  dest="$AGENT_SKILLS_DIR/$skill_name"

  if [ -d "$dest" ]; then
    echo "  ↻  $skill_name (already installed — skipping)"
    SKILLS_SKIPPED=$((SKILLS_SKIPPED + 1))
  else
    cp -r "$skill_dir" "$dest"
    echo "  ✓  $skill_name"
    SKILLS_COPIED=$((SKILLS_COPIED + 1))
  fi
done

echo ""
echo "  Installed : $SKILLS_COPIED skill(s)"
if [ "$SKILLS_SKIPPED" -gt 0 ]; then
  echo "  Skipped   : $SKILLS_SKIPPED already present"
fi

# ── Patch CLAUDE.md ───────────────────────────────────────────────────────────
CLAUDE_MD="$TARGET_DIR/CLAUDE.md"

echo ""
if [ -f "$CLAUDE_MD" ] && grep -q "Skills Registry" "$CLAUDE_MD" 2>/dev/null; then
  echo "  CLAUDE.md already contains a Skills Registry — skipping patch."
elif [ -f "$CLAUDE_MD" ]; then
  cat >> "$CLAUDE_MD" << 'REGISTRY'

---

## Skills Registry (added by ai-ready-workflow)

Skills are auto-loaded from `.agent/skills/*/SKILL.md`. Activate by using a trigger keyword.

| Skill | Triggers |
|---|---|
| `ui-ux-pro-max` | UI design, color palette, typography, chart type, design system |
| `po-brief-to-prd` | feature brief, PRD, product requirements, create PRD |
| `po-prd-to-usm` | user story map, USM, story mapping |
| `po-usm-to-usl` | user story list, USL, MoSCoW prioritization |
| `po-usl-to-usd` | user story details, acceptance criteria, AC-XXX, USD |
| `po-usd-to-uat` | UAT, test cases, BDD, given-when-then, test scenarios |
| `validate-prd` | validate PRD, PRD quality gate, PRD completeness |
| `validate-usd` | validate USD, acceptance criteria check, AC completeness |
| `design-wireframe` | wireframe, WF-XXX, ASCII wireframe, screen layout |
| `design-component-spec` | component spec, COMP-XXX, ShadCN component, design to code |
| `pm-product-strategy` | product strategy, vision, OKRs, SWOT, competitive analysis |
| `pm-product-discovery` | customer discovery, Jobs-to-be-Done, opportunity tree, assumption mapping |
| `pm-market-research` | market research, persona, TAM SAM SOM, journey map, segmentation |
| `pm-data-analytics` | metrics, KPIs, A/B test, North Star, funnel analysis, cohort, HEART |
| `pm-marketing-growth` | growth, value proposition, growth loop, PLG, activation, retention |
| `pm-go-to-market` | go-to-market, GTM, launch plan, ICP, pricing, battlecard |
REGISTRY
  echo "  Appended Skills Registry to CLAUDE.md"
else
  echo "  No CLAUDE.md found — skipping patch."
  echo "  Tip: create CLAUDE.md in your project root and re-run to add the skill registry."
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "  Done! Skills are ready in $AGENT_SKILLS_DIR"
echo ""
echo "  Next steps:"
echo "    • In Claude Code, type a trigger keyword to activate a skill"
echo "    • For UI/UX queries: python3 $AGENT_SKILLS_DIR/ui-ux-pro-max/scripts/search.py \"<query>\""
echo ""
