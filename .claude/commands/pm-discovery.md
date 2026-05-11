# /pm-discovery

Start a product discovery sprint session. Maps opportunities, assumptions, and experiments using Teresa Torres' Continuous Discovery framework.

## Usage

```
/pm-discovery [product or feature name]
```

If a product/feature name is provided via `$ARGUMENTS`, use it. Otherwise ask: "What opportunity or problem are we discovering for?"

---

## What This Command Does

Activates the `pm-product-discovery` skill and guides a structured discovery session. The output is a discovery artifact stored in `features/{feature-name}/pm/discovery.md`.

This command is most useful:
- After `/pm-strategy` (to validate strategic assumptions)
- Before `/po-pipeline` (to ground requirements in validated user needs)
- When you have a hypothesis but need to structure what to test

---

## Session Flow

### Step 1 — Discovery Context

Ask the user (sequentially):

1. "What outcome are you trying to achieve? (business goal, not feature)"
2. "What do you currently know about users' pain in this area? Any existing research or data?"
3. "What are the key assumptions you're making that, if wrong, would invalidate this direction?"
4. "Have you talked to any users? If yes, what did you hear?"

Accept incomplete answers. The Opportunity Solution Tree will surface gaps.

### Step 2 — Opportunity Solution Tree (Teresa Torres)

Activate `pm-product-discovery` skill. Read `pm-framework/product-discovery/rules.md` before generating output.

Build the OST in this structure:

```
Desired Outcome (business metric)
└── Opportunity 1: [unmet user need / pain / job]
    ├── Opportunity 1a: [more specific need]
    │   ├── Solution A: [potential solution]
    │   └── Solution B: [potential solution]
    └── Opportunity 1b: [more specific need]
        └── Solution C: [potential solution]
└── Opportunity 2: [unmet user need]
    └── ...
```

Rules for the OST:
- Opportunities = user needs, pains, or desires (not solutions, not features)
- Solutions = concrete product ideas that address one or more opportunities
- Start broad, then drill down to specific sub-opportunities
- Aim for 2–4 top-level opportunities, 2–3 sub-opportunities each

### Step 3 — Assumption Mapping (Riskiest Assumption Test)

For the top 2–3 solutions identified, map assumptions:

| Assumption | Importance (High/Med/Low) | Evidence (Strong/Weak/None) | Risk Level | Test Method |
|-----------|--------------------------|----------------------------|-----------|-------------|
| [Users will X] | High | None | 🔴 Riskiest | Interview 5 users |
| [They currently use Y] | Med | Weak | 🟡 Medium | Survey / data pull |
| [Price point Z is acceptable] | High | Weak | 🔴 Riskiest | Willingness-to-pay test |

Risk Level = Importance × (1 / Evidence strength). Surface 2–3 riskiest assumptions.

### Step 4 — Customer Interview Guide

For the riskiest assumptions, generate a customer interview guide using the JTBD interview script:

```markdown
## Interview Guide — [opportunity area]

**Goal:** Understand [specific assumption to test]
**Target participant:** [description of who to interview]
**Duration:** 30–45 minutes

### Warm-up (5 min)
- Tell me about your role and how you typically do [related task]?
- Walk me through the last time you [relevant situation]?

### Core Questions (20 min)
- When you're trying to [job], what does that look like?
- What part of that process is most frustrating? Walk me through a specific example.
- What do you do today to solve this? What does that solution cost you?
- What would have to be true for you to switch to something new?

### Hypothesis Testing (10 min)
- [Specific question to test the riskiest assumption — open-ended, not leading]

### Wrap-up
- Is there anything I should have asked that I didn't?
- Who else should I talk to about this?
```

### Step 5 — Experiment Design

For each riskiest assumption, propose a lightweight experiment:

| Assumption | Experiment Type | Method | Success Criteria | Time |
|-----------|-----------------|--------|-----------------|------|
| [assumption] | Pretotype | Landing page with sign-up CTA | 20% click-through | 1 week |
| [assumption] | Prototype | Clickable mockup in 5 interviews | 3/5 users complete task without help | 2 weeks |
| [assumption] | Data analysis | Pull existing logs | X% of users already do Y | 2 days |

### Step 6 — Output

Save to `features/{feature-name}/pm/discovery.md` with frontmatter:

```yaml
---
artifact: PM-DISCOVERY
feature: [feature-name]
version: 0.1
status: draft
generated-by: pm-product-discovery
session-date: YYYY-MM-DD
upstream: pm/strategy.md
downstream: po/prd.md
---
```

Then print a session summary:

```
## Discovery Session Complete — {product/feature name}

Artifact: features/{feature-name}/pm/discovery.md

Deliverables:
- Opportunity Solution Tree: [N] opportunities, [M] solutions mapped
- Assumption Map: [K] assumptions identified, [2–3] riskiest flagged
- Customer Interview Guide: ready for [target participant type]
- Experiments: [N] tests designed for riskiest assumptions

Riskiest assumptions to test first:
1. [assumption 1]
2. [assumption 2]

Next steps:
- Run the customer interviews using the guide above
- After 5+ interviews, return and update this discovery artifact
- When assumptions are validated, run /po-pipeline to write the PRD
```

---

## Rules

- Activate `pm-product-discovery` skill before generating any discovery output
- Read `pm-framework/product-discovery/rules.md` for OST and assumption mapping rules
- Read `pm-framework/product-discovery/templates/opportunity-solution-tree.md` for OST structure
- Opportunities must be **user needs**, never features or solutions — reject and rewrite if the user frames opportunities as "we should build X"
- Riskiest assumptions drive the interview guide — do not write generic interview questions
- If the user hasn't spoken to any users yet, prioritize the interview guide above the experiment design
