# The Multi-Session Repo Playbook

**How to structure a repository worked by several AI coding sessions that never talk to each other.**

Version 1.0 · Derived from a working project, August 2026

---

## 1. What this is, and when to use it

A repository layout plus a set of rituals for projects developed by **multiple AI agent sessions on
one machine**, in phases, over weeks. Copy this into a new repo and follow it from commit one.

Use it when **two or more of these** are true:

- More than one agent session works the repo, concurrently or in sequence
- The project runs long enough that you will forget your own decisions
- Correctness matters more than speed, so a silently wrong answer is worse than a slow one
- There is a Phase 2 whose adaptability you are protecting today

**Do not** use it for a weekend script or a single-session prototype. The overhead is roughly a day
of setup, and it earns that back only when sessions start losing context.

### The premise everything rests on

> Sessions do not share memory. The repository is the only channel between them.

Every rule below follows from that one sentence. A convention that lives in someone's head is a
convention that does not exist. An undocumented decision gets re-litigated, or worse, silently
reversed by a session that never knew it was made.

**The corollary that people miss: a stale document is worse than a missing one.** A missing document
makes a session ask. A stale one makes it act, confidently, on something untrue.

---

## 2. Repository layout

```
project/
├── README.md              # the front door — what this is, how to run it
├── CLAUDE.md              # always-on rules; loaded into every session
├── PRD.md                 # specification: what things MEAN
├── ARCHITECTURE.md        # specification: how the system WORKS
├── .env.example           # every variable; nothing hardcoded in source
├── docs/
│   ├── INDEX.md           # task → the exact sections it needs
│   ├── STATE.md           # done · in flight · next · blocked · waiting on owner
│   └── decisions/         # NNNN-*.md, one per decision made after the spec
│       └── README.md      # the decision index
├── tasks/
│   ├── BACKLOG.md         # the full plan, one row per unit of work
│   ├── cards/             # one file per unit; the detail
│   │   └── TEMPLATE.md
│   └── lessons.md         # corrections, so they are not repeated
├── src/ or <language dirs>
└── tests/
    ├── test_prohibitions.py   # architectural rules, asserted
    └── test_docs.py           # documentation freshness, asserted
```

Seven document surfaces, each with exactly one job. If you cannot say in one sentence what a
document is for and what it is *not* for, it will accumulate everything and be read by no one.

---

## 3. The document layers

### Layer 1 — `CLAUDE.md`: the always-on rules

Loaded into every session automatically, so it is the only place guaranteed to be read. **Cap it at
about 150 lines.** Everything in it competes for the same attention.

It holds **rules, not knowledge**:

| Include | Exclude |
|---|---|
| The prohibitions — things that must never happen | Architecture prose |
| Rituals keyed to what you touched | Rationale and history |
| How to cite, how to name, how to commit | Anything a session can look up when needed |
| The commands, marked for what is not built yet | Anything already in the specification |
| The session protocol and definition of done | |
| A pointer table: "working on X → read Y" | |

**The prohibitions are the highest-value content in the entire repository.** They are the things a
context-free session does by default because they are locally the obvious move — writing a file
directly instead of through the storage layer, hardcoding a path, duplicating a type by hand. State
them as hard rules with a one-line reason each, and enforce the machine-checkable ones with tests.

### Layer 2 — the specification: two documents, never three

Split on **meaning versus mechanism**:

- **`PRD.md`** — what every number, status and term *means*. Product decisions. Appendices carrying
  precise definitions.
- **`ARCHITECTURE.md`** — how the system is *built*. Components, data model, interfaces, testing,
  the change surface for later phases.

Where they overlap, declare one authoritative: **PRD on meaning, ARCHITECTURE on mechanism.**

**Never write a third document restating either.** A derived spec is a second hand-maintained copy
of one thing, and it drifts for exactly the reason you generate types from a schema instead of
hand-writing them twice. If you think you need one, name what it would contain that no existing
document contains. If the answer is "the same thing, organised differently", write an index instead.

**One exception, declared explicitly:** the README summarises figures it does not own, because a
front door has to orient a reader. Mark it in the README itself as a **sweep site** — change the
source, change the README.

### Layer 3 — `docs/INDEX.md`: the pointer map

Two specification documents run 1,000–1,500 lines. Reading both to orient costs a tenth of a context
window and still misses the detail that mattered.

INDEX contains **no specification content**, so it cannot contradict its sources. Three tables:

1. **By module** — "I am about to write code in X" → read these sections, then these, and these are
   the tests it must pass.
2. **By question** — "I need to know Y" → this exact section.
3. **Traps** — every defect the project has already paid for, with the section that explains it.

The traps table is the highest-value part and the one people skip. Each row is a bug someone already
shipped. A session that reads it does not ship that bug again.

### Layer 4 — `docs/STATE.md`: the status board

The second file a session reads, after the rules. **Cap it at about 70 lines** — it is a board, not
a history. History lives in git and in the cards.

Six sections:

| Section | Holds |
|---|---|
| **In flight** | The claim registry: card ID, who claimed it, when. This is the concurrency lock |
| **Done** | Card ID and one line on what landed |
| **Next up** | What is claimable *right now*, derived from real dependencies |
| **Known broken** | Current failures, and spec gaps deliberately left open |
| **Waiting on \<owner\>** | Every open input needed from the human, what it blocks, when asked |
| **Environment** | Toolchain versions, setup state, anything a fresh machine needs |

**"Waiting on \<owner\>" is the section everyone forgets and everyone needs.** Without it, the list
of things you owe the project exists only in chat, and a new session cannot tell you what to answer.

### Layer 5 — `docs/decisions/`: the decision log

One file per decision made *after* the specification was written: `NNNN-short-title.md`, containing
**Context → Decision → Consequences**. An index in `README.md`.

The rule that makes it work:

> A decision made in conversation and not written here did not happen.

Number sequentially. **Never renumber** — supersede, and say so in both files. Record the *reasoning*
including the options rejected, because the next session will otherwise rediscover the rejected
option and think it is new.

### Layer 6 — `tasks/`: one card per unit of work

**Not a shared `todo.md`.** A single todo file is a merge-conflict magnet the moment two sessions run
at once, and it grows until reading it costs more than the work.

- **`BACKLOG.md`** — the full plan. One row per unit: ID, title, status, blocked-by, **file set**.
- **`cards/<ID>-<slug>.md`** — the detail, one file per unit.
- **`lessons.md`** — corrections, so they are not repeated by a session that was not there.

**Card IDs encode the phase**: `M1-01` … `M7-04` for phase 1, `M8+` for phase 2. The phase is an ID
range, so you need no separate phase structure.

**Card format:**

```markdown
# <ID> — <title>

**Milestone:** M? · **Status:** todo · **Blocked by:** <IDs, or —>

## Goal
One paragraph. What exists after this card that did not before.

## Read first
Cite sections, not whole documents. More than three means the card is too big — split it.

## Files I may touch
The collision boundary. A concurrent session's card must not list any of these.

## Acceptance
Named tests, not prose. Done when these pass and you have pasted the output.

## Out of scope
What a session might reasonably drift into. Name the card that owns it instead.

## Log
Decisions, surprises, what the next session needs to know.
```

**Two mechanisms make this work:**

1. **"Files I may touch" is the concurrency primitive.** Two sessions may run at once only if their
   cards list disjoint file sets. No locks, no coordination, no shared state — just arithmetic on
   two lists. If the sets cannot be made disjoint, run one session.

2. **Cards are authored just-in-time.** The BACKLOG table is the full plan; card *files* exist only
   for work that is next up. Writing all thirty up front produces twenty-five stale files, because a
   card written before its dependencies land encodes guesses. When you claim a row with no card
   file, write the card first from the row plus the cited sections.

**Size a card to one session and one commit.** If it will not fit, it is two cards.

### Layer 7 — memory outside the repo

Agent-level memory (outside the repo, not versioned) holds only **how to work with this person**:
preferences, corrections, environment quirks. **Never project specs** — those must be versioned,
reviewable, and visible to every session and every human.

---

## 4. The session protocol

### Start

1. Read `docs/STATE.md` — what is claimable, what is blocked, what is waiting on the owner.
2. Pick **one** card. Read that card file only.
3. Read only the sections the card names. Use INDEX. **Do not read the specifications end to end.**
4. **Run the test suite before touching anything.** A suite that is already red is not yours to
   inherit silently — find out now, not after two hours of work.

### Claim

Add the card ID to the in-flight table in `STATE.md` **and commit that line before starting**. That
commit is the lock. Verify your file set is disjoint from anything else in flight.

### Finish — the definition of done

Do not report a card complete until every line holds. **Paste this list into the final message with
each item's actual result, not a claim that you did it.**

- [ ] Every acceptance test on the card passes, and you have pasted the output
- [ ] The whole suite is green, not just your file
- [ ] The linter is clean
- [ ] The card's file set matches what you actually touched — if it grew, update the card *and* the
      BACKLOG row, because an understated file set breaks the concurrency mechanism
- [ ] The card's Log records what you decided, what surprised you, and what you deliberately did not
      do
- [ ] Card status updated, and the BACKLOG row matches
- [ ] `STATE.md`: in-flight row removed, Done row added, "Next up" re-derived from real dependencies,
      any new question added to "Waiting on \<owner\>"
- [ ] Every decision made in conversation is written to `docs/decisions/`
- [ ] `lessons.md` appended if you were corrected
- [ ] Committed with the card ID in the subject, clean tree

**Never leave a dirty tree for the next session to find.**

---

## 5. Enforcement — the part that actually matters

Everything above is a convention, and conventions decay. The measured rate is not subtle: in one
project's first four commits, discipline-only rules produced a stale test name, wrong dates twice, a
wrong test count, a dead docstring, two stale layout blocks, a contradiction that hid claimable work,
and a decision record citing an enforcement mechanism that did not exist.

**So assert the documents the way you assert the code.** Two test files:

### `test_prohibitions.py` — the architectural rules

Scan the source tree and fail on violations. Typical checks:

- No filesystem access outside the designated storage module (with an explicit, commented allowlist)
- No hardcoded hosts, ports or paths — everything from configuration
- No use of the unsafe primitive your project bans (a float where you require exact decimals, a raw
  SQL string where you require the query builder)

**Verify your detectors bite.** Probe them against known-bad and known-good lines before trusting
them. A test that passes vacuously is worse than no test, because it buys false confidence.

### `test_docs.py` — documentation freshness

The seven checks that catch real drift:

| Check | Catches |
|---|---|
| Every citation resolves to a real section **or numbered list item** | Renumbering that silently invalidates references |
| Every markdown link resolves | Renamed or never-created files |
| BACKLOG status matches each card's status | Three surfaces disagreeing about what is done |
| STATE names only cards that exist | Drifted or invented IDs |
| Claimed test counts match the real count | "19 passed" outliving two commits |
| "Last updated" is not older than the file's last commit | Documents lying about their age |
| Banned characters and conventions stay banned | Style rules quietly eroding |

**Citation checking is the highest-value one.** Cite by naming the document — `ARCHITECTURE 14.4`,
never a bare number and never a special symbol. Two reasons: a citation that does not name its source
cannot be machine-checked, and sub-numbers often point at *list items* rather than headings, so
reordering a list silently invalidates every reference to it.

Declare renumbering a breaking change. The suite will list every citation you broke.

### What cannot be enforced

Whether prose still *describes* what the code does, and whether a card's acceptance criteria are the
*right* ones. For these, run a **fresh-context audit at each milestone boundary**: an agent that has
read only the repository, asked to report what is ambiguous, contradictory or missing, and explicitly
told that finding problems is the point.

> You cannot audit prose you just wrote. You cannot un-know what you meant.

In one project, a fresh-context audit found fifteen defects — including an enum that would have been
built with the wrong number of members — in documents that had been reviewed twice and called sound.

---

## 6. Bootstrapping a new repo

In order. Steps 1–3 before any application code.

1. **`git init`** plus `.gitignore` (secrets, private data, build artefacts) and `.env.example`.
   Commits are the checkpoint mechanism; without them a session that goes sideways cannot be rolled
   back and you cannot see what a parallel session did.
2. **Write the specification** — `PRD.md` and `ARCHITECTURE.md`. If you have one large document,
   split it on meaning versus mechanism now, while it is cheap.
3. **Write `CLAUDE.md`** — prohibitions, rituals, citation convention, session protocol, definition
   of done.
4. **Write `docs/INDEX.md`** — the pointer map. It will be wrong until the specs settle; write it
   anyway, because it is what stops sessions reading everything.
5. **Write `docs/STATE.md`** with all six sections, including "Waiting on \<owner\>" seeded with
   every open question you already have.
6. **Write `tasks/BACKLOG.md`** — the full plan as rows. Author card files only for what is next.
7. **Write the two test files** before the first feature card, so no code is ever written without
   them.
8. **Commit.** One commit, one card ID, clean tree. The habit starts here.

---

## 7. Anti-patterns

Each of these was a real failure, not a hypothetical.

**A derived spec document.** Someone proposes `docs/specs/` restating the PRD per module. It is a
second copy that drifts. Write an index instead.

**A shared `todo.md`.** Conflicts the moment two sessions run, and grows unbounded.

**Claiming an enforcement mechanism you have not written.** A decision record cited a "check" that
was a grep run once by hand. Ship the test with the rule, or say plainly that it is on discipline.

**Moving a dependency instead of removing it.** Configuration loading was moved out of the code to
kill a working-directory dependency — and the shipped example file then carried relative paths, so
the dependency simply moved somewhere nothing tested. *Moving a problem out of code moves it into
configuration, where nothing checks it.* After fixing a class of bug, re-read the artefacts the fix
produced, looking for the same bug.

**Checking only in the convenient context.** Configuration worked from an interactive shell and
would have failed under the scheduler, which is the only way it runs in production. Before finishing
anything that resolves a path or reads configuration, name every context it runs in — your shell,
the scheduler, the test runner, the deployment container — and check the *least* convenient one.

**Prose counting.** A specification said "six statuses" throughout. Six *categories*, but eight enum
members, because one category had three variants. A card's acceptance test was even named "a status
outside the six is rejected". Wherever a count appears, assert the **set**, never the number.

**Trusting your own review.** You reviewed it, so it is sound. It is not. Use a fresh context.

---

## 8. What this costs, honestly

**Setup:** most of a day, before any feature exists.

**Per card:** roughly ten minutes of bookkeeping — updating three surfaces and writing the log.

**Ongoing:** the test suite adds a second or two, and occasionally fails on a document rather than
code, which feels like friction until the first time it catches a contradiction that would have sent
a session down the wrong path for an afternoon.

**What you get:** a new session reaches full context in about 5,000 tokens instead of 25,000, can
name what to build next without guessing, cannot violate an architectural rule without a red test,
and cannot leave a document lying about its own state.

**The honest limit:** none of this makes prose correct. It makes prose *checkable*, keeps status
*consistent*, and makes violations *loud*. Whether the plan is any good is still a human judgement,
and the fresh-context audit at each milestone is the only real defence.

---

## Appendix — copy-paste starting points

### `.gitignore` essentials

```
# private data and secrets — never committed
data/
.env
*.session

# build and environment
.venv/
__pycache__/
node_modules/
dist/
```

### `docs/decisions/NNNN-title.md`

```markdown
# NNNN — <decision stated as a sentence>

**Date:** <date> · **Status:** accepted | superseded by NNNN · **Amends:** <card or decision>

## Context
What was true before, and what forced the choice. Name the options rejected and why —
otherwise the next session rediscovers a rejected option and thinks it is new.

## Decision
The decision, stated so it can be checked.

## Consequences
What gets easier, what gets harder, what must now be maintained.
Name the test that enforces it, if there is one. If there is not, say so.
```

### `tasks/lessons.md` entry

```markdown
## <short pattern name>

**What happened:** one or two sentences, concrete.
**Rule:** the imperative that prevents it.
```

### Session-start prompt for a new session

> Read `docs/STATE.md`, then the one card you are claiming in `tasks/cards/`, then only the document
> sections that card names. Do not read the specifications end to end. Run the test suite before
> touching anything. Claim the card in `STATE.md` and commit that line before starting work.
