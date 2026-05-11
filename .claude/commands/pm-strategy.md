# /pm-strategy

Start a product strategy session. Produces a structured strategy artifact using PM frameworks.

## Usage

```
/pm-strategy [product or feature name]
```

If a product/feature name is provided via `$ARGUMENTS`, use it. Otherwise ask: "What product or initiative are we building strategy for?"

---

## What This Command Does

Activates the `pm-product-strategy` skill and guides a focused strategy session. The output is a strategy artifact stored in `features/{feature-name}/pm/strategy.md` (or a standalone `pm/strategy.md` if this is a product-level strategy).

---

## Session Flow

### Step 1 — Context Gathering

Ask the user (sequentially, not all at once):

1. "What problem does this product/feature solve? Who has this problem?"
2. "What's your current thinking on the target market or user segment?"
3. "Do you have existing research, metrics, or competitor context to share?"
4. "What does success look like in 6–12 months?"

Accept whatever the user provides — incomplete answers are fine. The skill will surface gaps through the frameworks.

### Step 2 — Framework Selection

Based on what the user shares, activate `pm-product-strategy` skill and apply the most relevant frameworks:

| User Context | Primary Framework |
|--------------|-------------------|
| Early-stage, problem unclear | Jobs-to-be-Done strategic lens |
| Market positioning question | Product Strategy Canvas + Competitive Positioning Map |
| Goal-setting or planning cycle | OKR hierarchy (Objective → Key Results → Initiatives) |
| Competitive threat or expansion | SWOT + Ansoff Matrix |
| Full strategy session | All frameworks sequentially |

Always start with the Product Strategy Canvas as the primary structure.

### Step 3 — Strategy Generation

Activate `pm-product-strategy` skill. Read `pm-framework/product-strategy/rules.md` before generating output.

Produce the following sections based on what the user has shared:

**1. Product Vision & Mission**
- Vision statement (inspirational, long-term, customer-outcome focused)
- Mission statement (operational, what you do and for whom)

**2. Strategic Context**
- Jobs-to-be-Done: What job is the customer hiring this product to do?
- Problem statement: Specific, user-grounded, measurable pain

**3. Target Market**
- Primary segment (who feels the pain most acutely)
- Beachhead: Where to win first before expanding

**4. Competitive Landscape**
- 3–5 competitors or alternatives (including "do nothing")
- Differentiation: Where you win, where you don't compete

**5. OKR Framework**
- Objective: Qualitative north star (1 sentence)
- Key Results: 3–5 measurable outcomes (with specific numbers)
- Initiatives: Projects that drive the key results

**6. SWOT Summary**
- Strengths, Weaknesses, Opportunities, Threats (4 bullets each)

**7. Strategic Bets**
- 2–3 explicit strategic choices: "We will do X and NOT do Y because..."

### Step 4 — Output

Save to `features/{feature-name}/pm/strategy.md` (create folder if needed) with frontmatter:

```yaml
---
artifact: PM-STRATEGY
feature: [feature-name]
version: 0.1
status: draft
generated-by: pm-product-strategy
session-date: YYYY-MM-DD
---
```

Then print a session summary:

```
## Strategy Session Complete — {product/feature name}

Artifact: features/{feature-name}/pm/strategy.md

Frameworks applied:
- Product Strategy Canvas
- Jobs-to-be-Done
- OKR Hierarchy
- SWOT Analysis

Key outputs:
- Vision: [one-line summary]
- Primary OKR: [Objective in 10 words]
- Strategic bet: [top bet in 15 words]

Next steps:
- /pm-discovery — validate assumptions through customer discovery
- /po-pipeline — translate strategy into product requirements (PRD)
```

---

## Rules

- Activate `pm-product-strategy` skill before generating any strategy content — do not rely on general knowledge alone
- Read `pm-framework/product-strategy/rules.md` for framework details and templates
- Ask clarifying questions if context is too thin to produce meaningful strategy (e.g., no target user identified)
- Never produce generic strategy filler — if data is missing, mark sections as `[To be validated in discovery]`
- Strategic bets must be explicit tradeoffs: "We will X, not Y"
