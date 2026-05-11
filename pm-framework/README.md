# PM Framework

A structured knowledge base for Product Manager skills, covering the full PM lifecycle from strategy to go-to-market.

---

## Framework Structure

```
pm-framework/
├── pm-workflow.md              # How PM skills chain together
├── product-strategy/           # Vision, OKRs, competitive positioning
│   ├── rules.md
│   ├── templates/
│   └── examples/
├── product-discovery/          # Customer research, Opportunity Solution Tree
│   ├── rules.md
│   ├── templates/
│   └── examples/
├── market-research/            # Personas, TAM/SAM/SOM, journey maps
│   ├── rules.md
│   ├── templates/
│   └── examples/
├── data-analytics/             # Metrics, A/B testing, funnel analysis
│   ├── rules.md
│   ├── templates/
│   └── examples/
├── marketing-growth/           # Growth loops, PLG, value proposition
│   ├── rules.md
│   ├── templates/
│   └── examples/
└── go-to-market/               # GTM motion, launch plan, pricing, battlecards
    ├── rules.md
    ├── templates/
    └── examples/
```

---

## Skills

Each sub-framework has a corresponding skill in `skills/pm-*/SKILL.md` that Claude loads automatically when PM work is detected.

| Area | Skill | Key Frameworks |
|------|-------|----------------|
| Product Strategy | `pm-product-strategy` | Product Strategy Canvas, OKRs, Porter's Five Forces |
| Product Discovery | `pm-product-discovery` | Opportunity Solution Tree, JTBD, Assumption Mapping |
| Market Research | `pm-market-research` | Personas, TAM/SAM/SOM, Customer Journey Maps |
| Data & Analytics | `pm-data-analytics` | North Star Metric, HEART, AARRR, A/B Testing |
| Marketing & Growth | `pm-marketing-growth` | Value Proposition Canvas, Growth Loops, PLG |
| Go-to-Market | `pm-go-to-market` | ICP, GTM Motion, Launch Plan, Pricing, Battlecards |

---

## Automation with Slash Commands

Two slash commands are available in Claude Code for running PM sessions:

| Command | Purpose |
|---------|---------|
| `/pm-strategy` | Product strategy session — Vision, OKRs, SWOT, Strategic Bets. Saves to `features/{name}/pm/strategy.md` |
| `/pm-discovery` | Discovery sprint — Opportunity Solution Tree, Assumption Map, Interview Guide, Experiments. Saves to `features/{name}/pm/discovery.md` |

---

## Workflow

See [pm-workflow.md](pm-workflow.md) for how PM skills chain together in a typical product development cycle.

---

## Methodologies

This framework is grounded in:
- **Teresa Torres** — Continuous Discovery, Opportunity Solution Tree
- **Marty Cagan** — Empowered product teams, product discovery
- **Strategyzer** — Value Proposition Canvas, Business Model Canvas
- **Geoffrey Moore** — Crossing the Chasm, positioning, beachhead markets
- **Google Ventures** — HEART framework for UX metrics

---

## Integration with PO Framework

PM Framework → PO Framework: PM outputs feed into PO inputs.

| PM Output | PO Input |
|-----------|----------|
| Opportunity Solution Tree | Feature brief → PRD |
| Customer interview insights | PRD problem statement |
| ICP definition | User personas in PRD |
| North Star metric | PRD success metrics |
