# Product Discovery — Rules

## What Product Discovery Is

Discovery answers the question: "What should we build, and why?" It runs continuously alongside delivery — not as a pre-phase, but as an ongoing habit. The goal is to reduce the risk of building the wrong thing by testing assumptions before committing to development.

Marty Cagan's definition: Discovery is about coming up with a product that is **valuable** (customers want it), **usable** (customers can figure out how to use it), **feasible** (engineers can build it), and **viable** (it works for the business).

---

## Required Components

### 1. Opportunity Framing (Opportunity Solution Tree)
Before running discovery, frame the opportunity using the OST (Teresa Torres):
- **Desired outcome:** The business metric you are trying to improve. Specific, measurable.
- **Opportunities:** Customer problems, pains, or desires that, if addressed, would improve the outcome.
- **Solutions:** Potential product changes that could address opportunities. Generate many before committing.
- **Experiments:** Tests that help you validate solutions before building.

Rule: Never jump from outcome to solution. Map the opportunity space first.

### 2. Assumption Mapping
For each candidate solution, surface and prioritize assumptions:
- **Desirability assumptions:** Will customers want this?
- **Usability assumptions:** Will customers understand how to use it?
- **Feasibility assumptions:** Can we build it?
- **Viability assumptions:** Is this sustainable for the business?

Prioritize by: **Risk × Uncertainty**. High risk + high uncertainty = test first. Known facts don't need testing.

### 3. Customer Interview Guide
Every discovery cycle must include customer interviews. Rules:
- Minimum 5 interviews before drawing conclusions.
- Interview the problem, not the solution. Never show a mockup in the first interview.
- Use the JTBD interview script: probe for past behaviour, not hypothetical future behaviour.
- Document: Jobs hired for, pains, gains, switching moments, emotional context.

### 4. Experiment Design
For riskiest assumptions, design a test before building:
- **Hypothesis:** "We believe [assumption]. If we [action], we expect [outcome]. We'll know we're right if [metric] changes by [amount] within [time]."
- **Pretotype:** Can you fake the solution to test demand before building?
- **Prototype:** Clickable mock to test usability. Not production code.
- **Test:** What is the smallest experiment that would invalidate or confirm this assumption?

---

## Frameworks to Apply

### Opportunity Solution Tree (Teresa Torres)
Use for: structuring the discovery process from outcome → opportunity → solution → experiment.
Prevents: jumping to solutions before understanding the problem space.
Rule: One tree per team per quarter. Updated weekly as you learn.

### Continuous Discovery Habits (Teresa Torres)
Core habit: interview at least one customer per week, every week.
Three types of work: weekly interviews → synthesize learnings → update the OST.

### Jobs-to-be-Done (JTBD)
Use for: understanding WHY customers buy and what progress they're trying to make.
Core types:
- **Functional job:** The practical task (e.g., "track where my shipment is")
- **Emotional job:** How the customer wants to feel (e.g., "feel in control")
- **Social job:** How they want to be perceived (e.g., "look competent to my team")
- **Switching moments:** What triggered the customer to look for a new solution?

### Assumption Mapping
Use for: prioritizing what to test during discovery.
Map assumptions on 2x2: Importance (how critical to success) vs. Evidence (how much do we know).
Focus experiments on High Importance + Low Evidence quadrant.

### Riskiest Assumption Test (RAT)
Use for: designing the smallest possible experiment to invalidate a risky assumption.
Faster than building an MVP — test the assumption, not the full product.

---

## Quality Checklist

Before moving from discovery to delivery:
- [ ] Opportunity Solution Tree has been updated with current learnings
- [ ] At least 5 customer interviews conducted this discovery cycle
- [ ] All major assumptions surfaced and prioritized
- [ ] Riskiest assumptions have been tested (or de-risked with existing evidence)
- [ ] At least 3 solution candidates considered before choosing one
- [ ] Usability tested with real users before committing to development

---

## Anti-Patterns to Avoid

- **Discovery as a pre-phase:** Discovery is not "requirements gathering done first." It runs continuously, in parallel with delivery.
- **Surveys as discovery:** Surveys tell you what people say, not what they do. Interviews and observation surface the real job.
- **Showing solutions in first interviews:** Customers will react to what you show, not to their actual needs. Start with their story, not your hypothesis.
- **Skipping assumption mapping:** Moving from idea to backlog without surfacing assumptions means you're doing fake discovery.
- **Stopping at 1–2 interviews:** Patterns emerge after 5+. One customer's experience is an anecdote, not insight.
