# install.ps1 — AI-Ready Product Workflow skill installer (Windows)
# Copies all skills to .agent\skills\ in the target project and optionally patches CLAUDE.md.
#
# Usage:
#   .\skills\install.ps1                        # installs into current directory
#   .\skills\install.ps1 C:\path\to\project     # installs into specified directory
#   npx ai-ready-workflow install               # same via npx (calls this script on Windows)

param(
    [string]$TargetDir = (Get-Location).Path
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$AgentSkillsDir = Join-Path $TargetDir ".agent\skills"

# ── Banner ─────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════╗"
Write-Host "║   AI-Ready Product Workflow — Skill Installer    ║"
Write-Host "╚══════════════════════════════════════════════════╝"
Write-Host ""
Write-Host "  Source : $ScriptDir"
Write-Host "  Target : $AgentSkillsDir"
Write-Host ""

# ── Create destination directory ───────────────────────────────────────────────
if (-not (Test-Path $AgentSkillsDir)) {
    New-Item -ItemType Directory -Path $AgentSkillsDir -Force | Out-Null
}

# ── Copy skill folders ─────────────────────────────────────────────────────────
$skillsCopied = 0
$skillsSkipped = 0

Get-ChildItem -Path $ScriptDir -Directory | ForEach-Object {
    $skillName = $_.Name
    $skillMd = Join-Path $_.FullName "SKILL.md"

    # Only process directories that contain a SKILL.md
    if (-not (Test-Path $skillMd)) {
        return
    }

    $dest = Join-Path $AgentSkillsDir $skillName

    if (Test-Path $dest) {
        Write-Host "  ↻  $skillName (already installed — skipping)"
        $skillsSkipped++
    } else {
        Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
        Write-Host "  ✓  $skillName"
        $skillsCopied++
    }
}

Write-Host ""
Write-Host "  Installed : $skillsCopied skill(s)"
if ($skillsSkipped -gt 0) {
    Write-Host "  Skipped   : $skillsSkipped already present"
}

# ── Patch CLAUDE.md ────────────────────────────────────────────────────────────
$claudeMd = Join-Path $TargetDir "CLAUDE.md"
$registryBlock = @"

---

## Skills Registry (added by ai-ready-workflow)

Skills are auto-loaded from `.agent/skills/*/SKILL.md`. Activate by using a trigger keyword.

| Skill | Triggers |
|---|---|
| ``ui-ux-pro-max`` | UI design, color palette, typography, chart type, design system |
| ``po-brief-to-prd`` | feature brief, PRD, product requirements, create PRD |
| ``po-prd-to-usm`` | user story map, USM, story mapping |
| ``po-usm-to-usl`` | user story list, USL, MoSCoW prioritization |
| ``po-usl-to-usd`` | user story details, acceptance criteria, AC-XXX, USD |
| ``po-usd-to-uat`` | UAT, test cases, BDD, given-when-then, test scenarios |
| ``validate-prd`` | validate PRD, PRD quality gate, PRD completeness |
| ``validate-usd`` | validate USD, acceptance criteria check, AC completeness |
| ``design-wireframe`` | wireframe, WF-XXX, ASCII wireframe, screen layout |
| ``design-component-spec`` | component spec, COMP-XXX, ShadCN component, design to code |
| ``pm-product-strategy`` | product strategy, vision, OKRs, SWOT, competitive analysis |
| ``pm-product-discovery`` | customer discovery, Jobs-to-be-Done, opportunity tree, assumption mapping |
| ``pm-market-research`` | market research, persona, TAM SAM SOM, journey map, segmentation |
| ``pm-data-analytics`` | metrics, KPIs, A/B test, North Star, funnel analysis, cohort, HEART |
| ``pm-marketing-growth`` | growth, value proposition, growth loop, PLG, activation, retention |
| ``pm-go-to-market`` | go-to-market, GTM, launch plan, ICP, pricing, battlecard |
"@

Write-Host ""
if (Test-Path $claudeMd) {
    $content = Get-Content $claudeMd -Raw
    if ($content -match "Skills Registry") {
        Write-Host "  CLAUDE.md already contains a Skills Registry — skipping patch."
    } else {
        Add-Content -Path $claudeMd -Value $registryBlock
        Write-Host "  Appended Skills Registry to CLAUDE.md"
    }
} else {
    Write-Host "  No CLAUDE.md found — skipping patch."
    Write-Host "  Tip: create CLAUDE.md in your project root and re-run to add the skill registry."
}

# ── Done ───────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "  Done! Skills are ready in $AgentSkillsDir"
Write-Host ""
Write-Host "  Next steps:"
Write-Host "    • In Claude Code, type a trigger keyword to activate a skill"
Write-Host "    • For UI/UX queries: python3 $AgentSkillsDir\ui-ux-pro-max\scripts\search.py `"<query>`""
Write-Host ""
