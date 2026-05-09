# PM Workflow — How Skills Chain Together

This document describes the recommended order of PM activities and how each skill's output feeds into the next.

---

## Full PM Lifecycle

```
1. pm-product-strategy     → Define vision, mission, OKRs, competitive position
         ↓
2. pm-product-discovery    → Identify opportunities, run discovery, map assumptions
         ↓
3. pm-market-research      → Validate personas, size market, map customer journey
         ↓
4. pm-data-analytics       → Define success metrics, instrument tracking
         ↓
5. pm-marketing-growth     → Design growth model, value proposition, activation
         ↓
6. pm-go-to-market         → Plan launch, define ICP, price, create battlecards
         ↓
   → PO Framework: Feature brief → PRD → USM → USL → USD → UAT
```

---

## When to Use Each Skill

### Starting a new product or major initiative
Run all 6 skills in sequence. Start with strategy to establish direction before running discovery.

### Adding a new feature to an existing product
Start at step 2 (discovery) if strategy is already established. Use market-research to validate the segment. Jump to go-to-market for the feature launch plan.

### Improving an underperforming feature
Start at step 4 (data-analytics) to diagnose the problem. Use discovery to understand root causes. Use growth to design retention improvements.

### Entering a new market
Start at step 3 (market-research) to understand the new segment. Run strategy to update positioning. Go-to-market to plan the beachhead.

---

## Output Artifacts

| Step | Skill | Artifacts |
|------|-------|-----------|
| 1 | pm-product-strategy | Strategy canvas, OKR hierarchy, competitive map |
| 2 | pm-product-discovery | Opportunity Solution Tree, assumption map, interview guide |
| 3 | pm-market-research | Persona profiles, TAM/SAM/SOM sizing, journey map |
| 4 | pm-data-analytics | North Star metric, HEART dashboard, A/B test plan |
| 5 | pm-marketing-growth | Value proposition canvas, growth loop diagram, positioning statement |
| 6 | pm-go-to-market | ICP definition, launch plan, pricing model, battlecards |

---

## Integration with PO Framework

Once PM discovery surfaces a validated opportunity, it feeds into the PO pipeline:

```
Opportunity Solution Tree (Discovery)
         ↓
Feature brief (PM → PO handoff)
         ↓
PRD (po-brief-to-prd skill)
         ↓
USM → USL → USD → UAT
```

Store PM artifacts in `features/{feature-name}/pm/`:
- `features/{name}/pm/strategy.md`
- `features/{name}/pm/discovery.md`
- `features/{name}/pm/gtm.md`
