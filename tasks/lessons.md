# Lessons

Corrections, so they are not repeated by a session that was not there.
Append when the owner corrects you, or when a session pays for a mistake twice.

Format: what happened (concrete), then the rule (imperative).

---

## Never escalate a permission denial

**What happened:** A read of a file in `~/Downloads` returned `Operation not permitted`. The session retried
the same read with the sandbox disabled. That escalation collapsed the app's macOS Files-and-Folders grant,
and the entire repository under `~/Documents` became unreadable mid-task — `Desktop`, `Downloads` and
`Documents` all denied. Recovery needed the owner to restart the app.

**Rule:** When a path outside the repository is denied, ask the owner to move the file into the repo. Never
retry with the sandbox disabled. The escalation cannot widen a macOS TCC grant, and it can destroy one.

---

## Verify the authority, not the majority

**What happened:** Eleven documents said wireframes are written to `design/WF-XXX.md`; three said
`design/wireframes.md`. The three were right — they were the framework rules, the skill that does the writing,
and the artifact on disk. Counting documents would have produced the wrong answer and corrupted the pipeline.

**Rule:** When documents disagree, rank the sources: what the code or skill actually does > what the framework
rules state > what an index says. Check disk before deciding. Never resolve a conflict by majority.

---

## Assert the set, never the count

**What happened:** `CLAUDE.md` claimed "16+ skills, 5 pipeline slash commands" while its own tables listed 17
and 6. The installers shipped a hardcoded 16-row registry after the 17th skill landed. Every one of these was a
number that outlived its truth.

**Rule:** Wherever a count appears in a document or a test, assert the **set** it summarises. A test that
checks `len(skills) == 17` passes for the wrong seventeen.

---

## Re-audit the artifacts your own fix produced

**What happened:** After correcting the PM `artifact:` values across the agent docs, the same wrong values were
still sitting in the `/pm-strategy` and `/pm-discovery` output templates — the exact place an agent would copy
them from. The first sweep had covered documentation and missed the generators.

**Rule:** After fixing a class of error, re-run the detector over everything that *produces* the artifact, not
only everything that *describes* it.

---

## You cannot audit prose you just wrote

**What happened:** A self-reviewed documentation rewrite carried two invented facts — a `search.py` domain list
copied from a stale docstring, and a PM `artifact:` enum that contradicted disk. A fresh-context audit caught
both immediately.

**Rule:** Run a fresh-context audit at every milestone boundary: an agent that has read only the repository,
told explicitly that finding problems is the point. Do not skip it because the work was careful.

---

## Renumbering a section silently repoints every citation to it

**What happened:** Inserting a new `ARCHITECTURE 6.3` (CI checks) pushed the release contract to 6.4. Six
citations across `CLAUDE.md`, `docs/INDEX.md` and `docs/STATE.md` still said 6.3 — and the citation checker
passed, because 6.3 still *existed*. The references were not broken, they were silently pointing at the wrong
section, which is worse.

**Rule:** Renumbering is a breaking change even when the suite stays green. Before inserting or removing a
numbered section, grep for every citation of that number and each one after it. The test proves a citation
*resolves*, never that it resolves to what the author meant.

---

## Do not claim a test asserts something without opening the test

**What happened:** `ARCHITECTURE 3.3` claimed "`test_docs.py` covers items 1–9" and `CLAUDE.md` said "Nine are
asserted". Six were. The `cli.js` banner and both `GETTING_STARTED` files were asserted by nothing, and item 1
was asserted by the *other* test file. This was written in the same commit that added a prohibition against
claiming an enforcement mechanism you have not written.

**Rule:** When writing that something is enforced, open the test file and find the line. Then name the check
(`check_cli_banner`), not a count of checks — a named function can be verified, "nine" cannot.

---

## A count in prose is a bug waiting to happen — including in a card title

**What happened:** New documents written in the same session claimed "65 of 66 tracked `CLAUDE.md` files"
(really 64 of 65), "4 dead links" (really 6 files), and "8 occurrences" on the landing page (really 13). Each
was a number typed once and never re-derived.

**Rule:** In a document, prefer the predicate and the command that yields it — "every tracked `CLAUDE.md`
except the root, verifiable with `git ls-files | xargs grep -l claude-mem-context`" — over a number. If a
number must appear, it belongs in a test that derives it from disk.

---

## Slice on a heading, never on `---`

**What happened:** An edit replaced a section of `docs/STATE.md` by slicing from its heading to the next `---`.
The first `---` it found was inside a table separator (`|---|---|---|`), so it cut mid-table and left an orphan
separator plus seven stale rows under "Blocked on owner". The fragment contradicted the live rows above it for
twelve days, and the suite stayed green because no check looked for a card listed twice.

**Rule:** When replacing a markdown section programmatically, bound it by the next heading (`\n## `), and match
a horizontal rule only as a whole line (`\n---\n`). Then re-read the file. `check_state_card_rows_unique` now
catches the duplicate-row symptom.
