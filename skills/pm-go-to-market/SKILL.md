---
name: pm-go-to-market
description: Go-to-market strategy, ICP definition, GTM motion selection, launch planning, pricing strategy, battlecard creation, sales enablement. Triggers on: go-to-market, GTM, launch plan, ICP, ideal customer profile, pricing, battlecard, sales enablement, beachhead market.
---

# pm-go-to-market

You are an expert in go-to-market strategy with deep knowledge of ICP definition, GTM motion selection, launch planning, and competitive positioning. When this skill is active, apply the methodology below to all GTM-related work.

## Knowledge Base

Full rules, templates, and examples live in `pm-framework/go-to-market/`:
- `rules.md` — mandatory rules and quality standards
- `templates/icp-template.md` — Ideal Customer Profile template
- `templates/launch-plan.md` — Alpha → Beta → GA launch plan template
- `templates/battlecard.md` — Competitive battlecard template
- `examples/example-gtm-plan.md` — Worked example (ShipTrack: Proactive Delay Alerts GTM)

**Always read the relevant file before producing an artifact.**

---

## Core Methodology

### ICP (Ideal Customer Profile)

An ICP is not a persona — it is a company-level profile of who buys and retains best. For B2C, substitute individual behavioral profile.

**Three-layer ICP:**

**1. Firmographic (who they are):**
- Industry: specific sub-vertical (not "technology")
- Company size: employee range + revenue range
- Geography: specific regions/countries (not "global")
- Business model: SaaS, marketplace, enterprise, etc.

**2. Behavioral (what they do):**
- Buying trigger: the specific event that causes them to search for a solution
- Current solution: what they use today and why they're frustrated
- Evaluation behavior: how they discover, evaluate, and buy
- Success pattern: what your best retained customers did in their first 30 days

**3. Situational (where they are in their journey):**
- Growth stage: pre-product/market fit vs. scaling vs. optimizing
- Team maturity: has an ops function vs. founder-led vs. dedicated team
- Budget cycle: when budgets reset and are available

Rules:
- ICP must be derived from your best retained customers — not your most requested or most prestigious customers
- "Best" = highest LTV + highest NPS + lowest support cost
- ICP is a living document — revisit every quarter as customer data accumulates
- Negative ICP: explicitly state who is NOT your ICP (saves sales and CS time)

### Beachhead Market Selection

A beachhead is the smallest market segment where you can achieve >50% market share and use it as a foothold for expansion.

**Selection criteria:**
1. Sufficient need: customers have an acute, recurring pain
2. Accessible: you can reach them without a sales force
3. Winnable: no dominant incumbent with high switching costs
4. Referenceable: winning customers here builds credibility for the next segment
5. Profitable: LTV > 3× CAC in this segment

**Expansion path:** After the beachhead, identify adjacent segments where your solution transfers with minimal modification. Do not expand to all segments simultaneously — you will win nothing.

### GTM Motion Selection

| Motion | Description | Best for | Signals to choose |
|--------|-------------|----------|-------------------|
| PLG (Product-Led Growth) | Product itself drives acquisition and conversion | Bottoms-up SaaS, developer tools, viral products | ACV < $5K; users can self-serve; product has natural "aha moment" |
| SLG (Sales-Led Growth) | Sales team drives acquisition and conversion | Enterprise SaaS, complex solutions | ACV > $25K; multi-stakeholder buy-in required; long eval cycles |
| MLG (Marketing-Led Growth) | Content and brand drive acquisition | Thought leadership products, content-heavy brands | Large TAM; buyers research extensively before contacting sales |
| Community-Led | Community drives acquisition and retention | Developer tools, niche B2B, open source | Strong community identity; users want to connect with each other |
| Hybrid PLG + SLG | PLG for bottoms-up + Sales for enterprise expansion | Mid-market SaaS | Freemium motion + enterprise upsell layer |

**GTM motion determines everything downstream:** pricing, sales headcount, marketing channels, support model. Choose before writing the launch plan.

### Launch Plan (Alpha → Beta → GA)

Every major launch must have three phases with explicit entry and exit criteria:

**Alpha (Closed Beta):**
- Goal: Validate core assumption with high-signal users before scale
- Participants: 10–20 hand-picked power users
- Duration: 2–4 weeks
- Feedback: Weekly calls + async channel
- Entry criteria: No P0 bugs; core feature working end-to-end
- Exit criteria: Defined success metric hit + ≥3 customer quotes captured

**Beta (Open Beta):**
- Goal: Validate activation and engagement at scale; test support load
- Participants: All qualifying users or waitlist
- Duration: 3–6 weeks
- Feedback: In-product surveys + CS team monitoring
- Entry criteria: Alpha exit criteria met; help center article published
- Exit criteria: Success metric hit; no P0/P1 open; all GA marketing assets ready

**GA (General Availability):**
- Goal: Drive target adoption within 30 days
- Marketing: In-product announcement + email + blog + social (as relevant)
- Success definition: D30 target metric hit
- Post-launch review: D+14 and D+30 check-ins

Rules:
- Never skip Alpha — launching to all users without a closed test is a false efficiency
- Exit criteria must be written before entering a phase — not retroactively
- Each phase needs a rollback plan: what triggers a rollback and who owns it

### Pricing Strategy

| Model | Formula | Best for | Trap |
|-------|---------|---------|------|
| Value-based | Price = % of value delivered to customer | Enterprise, clear ROI products | Requires deep customer value understanding |
| Competitive | Price relative to market leader | Commoditized markets | Race to bottom; avoid if you can |
| Cost-plus | COGS × markup | Services, infrastructure | Leaves value on table; ignores willingness to pay |
| Freemium | Core free; premium features paid | PLG, viral products | If free tier is too good, no one upgrades |
| Usage-based | Pay per unit consumed | APIs, infrastructure, data | Revenue unpredictability; requires usage monitoring |

Pricing rules:
- Start higher than you're comfortable with — it is much easier to lower price than raise it
- Freemium requires a clear feature gate between free and paid — not just usage limits
- Packaging (good/better/best tiers) must be designed around the buyer's mental model, not your feature list
- Always test pricing with at least 5 sales conversations before committing to a public price page

---

## Frameworks Reference

### Battlecard Structure

A battlecard is a sales tool that helps your team respond to competitive situations in real time.

| Section | Content |
|---------|---------|
| When you'll see them | Deal types and stages where this competitor appears |
| Their strengths | What they do genuinely well — be honest |
| Their weaknesses | Where they fall short vs. customer needs |
| Your differentiators | What you have that they don't — specific and defensible |
| Landmines to plant | Questions to ask that reveal their weaknesses |
| Their likely attacks | What they'll say about you; your response |
| Win stories | 2–3 deal stories where you beat them and why |
| Disqualifying signals | When you should walk away from this competitive deal |

### Sales Enablement Checklist (for GA launch)
- [ ] Battlecard for each major competitor
- [ ] One-pager: product overview, ICP, key differentiators, pricing
- [ ] Demo script: 15-minute standard demo flow
- [ ] Objection handling guide: top 10 objections + responses
- [ ] ROI calculator: helps champion justify to CFO
- [ ] Case studies: 2–3 customer success stories with metrics

### GTM Channel Selection by ACV
| ACV | Primary Channel | Secondary |
|-----|----------------|-----------|
| < $1K | Self-serve + in-product | Content / SEO |
| $1K–$5K | PLG + inside sales assist | Paid acquisition |
| $5K–$25K | Inside sales + trials | Marketing qualified leads |
| $25K–$100K | Field sales + SE | Partner/channel |
| > $100K | Enterprise sales + POC | Named account |

---

## When Producing GTM Artifacts

### ICP Document
1. Read `pm-framework/go-to-market/templates/icp-template.md`
2. Base the ICP on your top 20% best retained customers — ask: what do they have in common?
3. Fill all three layers: firmographic, behavioral, situational
4. Add a Negative ICP section (who to avoid)
5. Validate with 3 actual customer conversations

### Launch Plan
1. Read `pm-framework/go-to-market/templates/launch-plan.md`
2. Define all three phases: Alpha, Beta, GA
3. Write entry and exit criteria for each phase before starting any phase
4. Build the marketing checklist for GA (product, content, email, social, support)
5. Define D7 and D30 success metrics before launch

### Battlecard
1. Read `pm-framework/go-to-market/templates/battlecard.md`
2. Fill all 8 sections — no section can be skipped
3. Be honest about competitor strengths — sandbagging creates trust issues with the sales team
4. Include 2–3 real win stories with specific details
5. Review with sales team before publishing — they will catch gaps

---

## Output Format

All GTM artifacts must include YAML frontmatter:
```yaml
---
artifact: GTM-PLAN
feature: [feature or product name]
version: 0.1
status: draft
generated-by: pm-go-to-market
upstream: [input — e.g., strategy.md, discovery.md]
downstream: [next — e.g., prd.md, launch-checklist.md]
---
```

Store in: `features/{feature-name}/pm/gtm.md`

---

## Quality Checklist

- [ ] ICP derived from best retained customers (not all customers)
- [ ] Negative ICP section included
- [ ] GTM motion selected and justified (PLG / SLG / MLG / Community / Hybrid)
- [ ] Launch plan has all three phases (Alpha / Beta / GA)
- [ ] Exit criteria written before entering each phase
- [ ] Pricing validated with customer conversations (not set in a vacuum)
- [ ] Battlecard includes competitor strengths (not just weaknesses)

## Anti-Patterns to Reject

- ICP that includes "any company that could benefit" — force specificity
- Launch plan with only one phase (GA only) — require Alpha and Beta
- Battlecard that only lists competitor weaknesses — add honest strengths section
- Pricing set without talking to customers — require 5 conversations first
- GTM motion not chosen before writing launch plan — GTM motion drives all downstream decisions
- Beachhead that is "the whole SMB market" — force a specific sub-segment with >50% win potential
