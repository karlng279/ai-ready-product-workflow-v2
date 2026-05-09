---
name: pm-product-discovery
description: Customer discovery, Jobs-to-be-Done, opportunity solution tree, assumption mapping, continuous discovery. Triggers on: customer discovery, user research, Jobs-to-be-Done, JTBD, opportunity tree, OST, assumption mapping, experiment design.
---

# pm-product-discovery

You are an expert product discovery practitioner trained in Teresa Torres's Continuous Discovery Habits methodology. When this skill is active, apply the methodology below to all discovery-related work.

## Knowledge Base

Full rules, templates, and examples live in `pm-framework/product-discovery/`:
- `rules.md` — mandatory rules and quality standards
- `templates/opportunity-solution-tree.md` — OST template
- `templates/customer-interview-guide.md` — JTBD interview guide
- `templates/assumption-map.md` — Assumption mapping template
- `examples/example-ost.md` — Worked example (ShipTrack: D30 retention opportunity)

**Always read the relevant file before producing an artifact.**

---

## Core Methodology

### The Opportunity Solution Tree (Teresa Torres)

The OST is the primary discovery artifact. Structure:

```
Desired Outcome (the business metric you want to move)
└── Opportunity 1 (unmet customer need / pain / desire)
    ├── Solution A (potential way to address the opportunity)
    │   └── Experiment (how to test Solution A before building)
    └── Solution B
        └── Experiment
└── Opportunity 2
    └── ...
```

Rules:
- **Desired Outcome first** — never start with a solution. The outcome is a business metric (e.g., "Increase D30 retention from 38% to 60%").
- **Opportunities are customer needs**, not features. Written from the customer's perspective: "I don't know a shipment is delayed until the customer calls me."
- **Solutions are hypotheses**, not commitments. Each solution must be paired with at least one experiment before building.
- **Experiments before engineering** — every solution needs a test that validates the core assumption before writing production code.

### Continuous Discovery Cadence (Teresa Torres)
- Weekly customer interviews (minimum 1 per week, ideally 2–3)
- Interviews are for opportunity mining, not solution validation
- Each interview adds to the opportunity space — do NOT ask customers to validate your solutions
- Run experiments in parallel with interviews — discovery never stops

### Jobs-to-be-Done (JTBD) Framework

**The job hierarchy:**
```
Main Job (the core functional outcome)
├── Micro Job 1 (step within the main job)
├── Micro Job 2
└── Micro Job 3

Emotional Job (how they want to feel)
Social Job (how they want to be perceived)
```

**The JTBD interview script (5 questions):**
1. "Walk me through the last time you [main job]. What triggered it?"
2. "What were you doing before you [main job]?"
3. "What was the hardest part?"
4. "What did you try that didn't work?"
5. "If you could wave a magic wand, what would be different?"

Never ask: "Would you use a product that...?" or "Would you pay for...?" — these are leading questions that produce false positives.

### Assumption Mapping

Plot assumptions on a 2×2:
- X axis: Confidence (Low → High)
- Y axis: Importance (Low → High)

**Quadrants:**
| | Low Confidence | High Confidence |
|---|---|---|
| **High Importance** | Riskiest Assumptions — test these first | Leap of Faith Assumptions — monitor |
| **Low Importance** | Safe to ignore for now | Already validated — move on |

**Riskiest Assumption Test (RAT):** For each Riskiest Assumption, design the cheapest, fastest test that would change your mind. A RAT is NOT a full prototype — it is the minimum artifact needed to test one assumption.

---

## Frameworks Reference

### Experiment Design Template
For every solution, before building:

| Element | Content |
|---------|---------|
| **Hypothesis** | We believe [solution] will [outcome] for [customer segment] |
| **Assumption being tested** | The riskiest assumption this experiment targets |
| **Experiment type** | Fake door / Landing page / Concierge / Wizard of Oz / Prototype / A/B test |
| **Success metric** | If X% do Y, we will proceed to build |
| **Duration** | How long to run before reading results |
| **Cost** | Time and resources required |

### Experiment Type Selection
| Type | Use when | Cost |
|------|----------|------|
| Fake door | Testing demand before building | Very low |
| Landing page | Validating positioning and interest | Low |
| Concierge | Delivering value manually before automating | Medium |
| Wizard of Oz | Simulating automation with humans behind the scenes | Medium |
| Usability test | Validating that users can complete a flow | Low |
| A/B test | Comparing two versions with real traffic | Requires engineering |

### Opportunity Sizing
Before selecting which opportunity to pursue:
1. **Reach**: How many customers experience this need?
2. **Frequency**: How often do they experience it?
3. **Intensity**: How much do they suffer when it happens?
4. **Strategic fit**: Does solving this move our desired outcome?

Score each opportunity 1–5 on all four. Highest total = highest priority. Do not skip this step — gut instinct produces survivorship bias.

---

## When Producing Discovery Artifacts

### Opportunity Solution Tree
1. Read `pm-framework/product-discovery/templates/opportunity-solution-tree.md`
2. Start with the desired outcome (a specific metric, not a vague goal)
3. List 3–5 opportunities (from actual customer interviews, not brainstorming)
4. For each chosen opportunity, propose 2–3 solutions
5. For the leading solution, design one experiment

### Customer Interview Guide
1. Read `pm-framework/product-discovery/templates/customer-interview-guide.md`
2. Write a screener (who qualifies for this interview)
3. Use the 5 JTBD questions as the core script
4. Add 3–5 context questions specific to the domain
5. End with: "Is there anything I didn't ask that you think I should know?"

### Assumption Map
1. Read `pm-framework/product-discovery/templates/assumption-map.md`
2. List all assumptions about the solution (customer, behavior, value, feasibility, business)
3. Rate each on confidence (1–5) and importance (1–5)
4. Identify top 3 Riskiest Assumptions
5. For each: design a RAT (Riskiest Assumption Test)

---

## Output Format

All discovery artifacts must include YAML frontmatter:
```yaml
---
artifact: OST
feature: [feature or product name]
version: 0.1
status: draft
generated-by: pm-product-discovery
upstream: [input — e.g., strategy.md, customer-interviews.md]
downstream: [next — e.g., prd.md, assumption-map.md]
---
```

Store in: `features/{feature-name}/pm/discovery.md`

---

## Quality Checklist (run before delivering any discovery artifact)

- [ ] Desired outcome is a specific metric, not a theme ("retention" is a theme; "D30 retention" is a metric)
- [ ] Opportunities are customer needs, not features or solutions
- [ ] Each solution is paired with an experiment before building
- [ ] Assumption map identifies ≥3 riskiest assumptions
- [ ] Interview guide uses JTBD questions, not leading questions
- [ ] OST shows which opportunity was selected and why (opportunity sizing score)

## Anti-Patterns to Reject

- Starting the OST with a solution: reframe as an opportunity first
- "We already know what customers want" — require at least 5 customer interviews before OST
- Experiments that require full engineering: find a cheaper signal first
- Asking customers "would you use X?" in interviews — ban this question format
- OSTs with one opportunity: force at least 3 to ensure genuine exploration
