#!/usr/bin/env python3
"""Documentation freshness checks.

Dependency-free. Run directly:  python3 tests/test_docs.py
Also importable by pytest if it is ever added — every check is a `check_*` function.

Every check asserts a SET, never a count. A count outlives its truth (tasks/lessons.md).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def fail(check, msg):
    FAILURES.append(f"{check}: {msg}")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def exists(rel):
    return os.path.exists(os.path.join(ROOT, rel))


def skill_set():
    """The real skills: directories under skills/ containing SKILL.md."""
    d = os.path.join(ROOT, "skills")
    return {n for n in os.listdir(d)
            if os.path.isfile(os.path.join(d, n, "SKILL.md"))}


def command_set():
    """The real slash commands. A CLAUDE.md here would be claude-mem output, not a command (decision 0007)."""
    d = os.path.join(ROOT, ".claude", "commands")
    return {n[:-3] for n in os.listdir(d) if n.endswith(".md") and n != "CLAUDE.md"}


# Files that are not .md but are still agent-facing surfaces.
EXTRA_SURFACES = [".cursorrules", "skills/.cursorrules", "landing-page/index.html"]


def markdown_files(skip=("/.git/", "/node_modules/", "/__pycache__/")):
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for fn in filenames:
            if fn.endswith(".md"):
                p = os.path.join(dirpath, fn)
                if not any(s in p for s in skip):
                    out.append(os.path.relpath(p, ROOT))
    return sorted(out)


# ---------------------------------------------------------------- checks

def check_twins_byte_identical():
    """ARCHITECTURE 2.2 — these three must be byte-identical to their skills/ copies."""
    for name in ("AGENTS.md", "GEMINI.md", ".cursorrules"):
        twin = os.path.join("skills", name)
        if not exists(name) or not exists(twin):
            fail("twins", f"missing {name} or {twin}")
            continue
        if read(name) != read(twin):
            fail("twins", f"{name} and {twin} differ — they must be byte-identical")


def check_readme_pair_differs():
    """ARCHITECTURE 2.2 — these two pairs must NOT be synced."""
    for name in ("README.md", "GETTING_STARTED.md"):
        twin = os.path.join("skills", name)
        if exists(name) and exists(twin) and read(name) == read(twin):
            fail("readme-pair", f"{name} and {twin} are identical; they describe different things")


def check_symlinks_match_skills():
    """ARCHITECTURE 2.1 — one symlink per skill, both directions."""
    skills = skill_set()
    agent_dir = os.path.join(ROOT, ".agent", "skills")
    links = {n for n in os.listdir(agent_dir)
             if os.path.islink(os.path.join(agent_dir, n))}
    for missing in sorted(skills - links):
        fail("symlinks", f"skills/{missing} has no .agent/skills symlink")
    for orphan in sorted(links - skills):
        fail("symlinks", f".agent/skills/{orphan} points at a non-skill")
    for n in sorted(skills & links):
        target = os.readlink(os.path.join(agent_dir, n))
        if target != f"../../skills/{n}":
            fail("symlinks", f".agent/skills/{n} -> {target}, expected ../../skills/{n}")


def check_skill_set_across_surfaces():
    """ARCHITECTURE 3.3 — every surface must name exactly the real skill set."""
    skills = skill_set()
    surfaces = {
        "AGENTS.md":        (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        "GEMINI.md":        (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        ".cursorrules":     (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        "skills/AGENTS.md": (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        "skills/GEMINI.md": (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        "skills/.cursorrules": (r"^- `skills/([a-z0-9-]+)/SKILL\.md`", None),
        "skills/install.sh":  (r"^\| `([a-z0-9-]+)` \|", "## Skills Registry"),
        "skills/install.ps1": (r"^\| ``([a-z0-9-]+)`` \|", "## Skills Registry"),
    }
    for rel, (pattern, after) in surfaces.items():
        if not exists(rel):
            fail("skill-set", f"{rel} missing")
            continue
        text = read(rel)
        if after:
            idx = text.find(after)
            if idx < 0:
                fail("skill-set", f"{rel} has no '{after}' block")
                continue
            text = text[idx:]
        found = set(re.findall(pattern, text, re.M))
        for missing in sorted(skills - found):
            fail("skill-set", f"{rel} does not list skill '{missing}'")
        for extra in sorted(found - skills):
            fail("skill-set", f"{rel} lists '{extra}', which is not a skill on disk")


def check_readme_skill_set():
    """ARCHITECTURE 1.2 — README is a sweep site; its skill table must match reality."""
    skills = skill_set()
    for rel in ("README.md", "skills/README.md"):
        found = set(re.findall(r"^\| `([a-z0-9-]+)` \|", read(rel), re.M))
        for missing in sorted(skills - found):
            fail("readme-skills", f"{rel} does not list skill '{missing}'")
        # the READMEs also table non-skills (commands, artifacts); only flag rows that
        # look like a skill name but are not one
        for extra in sorted(found - skills):
            if re.match(r"^(pm|po|design|validate|artifact|ui)-", extra):
                fail("readme-skills", f"{rel} lists '{extra}', which is not a skill on disk")


def check_command_set():
    """ARCHITECTURE 5.1 — documented commands must match .claude/commands/."""
    commands = command_set()
    for rel in ("CLAUDE.md", "AGENTS.md", "GEMINI.md", ".cursorrules", "README.md",
                "skills/AGENTS.md", "skills/GEMINI.md", "skills/.cursorrules",
                "skills/README.md", "skills/GETTING_STARTED.md"):
        found = set(re.findall(r"`/([a-z-]+)`", read(rel)))
        found = {c for c in found if c in commands or c.startswith(("po-", "pm-", "design-", "validate-", "sync-"))}
        for missing in sorted(commands - found):
            fail("commands", f"{rel} does not mention /{missing}")
        for extra in sorted(found - commands):
            fail("commands", f"{rel} mentions /{extra}, which has no command file")


def _section_numbers(rel):
    """Collect '4' and '4.5' style section numbers from a spec document's headings."""
    nums = set()
    for line in read(rel).splitlines():
        m = re.match(r"^#{2,4}\s+(\d+(?:\.\d+)?)[.\s]", line)
        if m:
            nums.add(m.group(1))
            nums.add(m.group(1).split(".")[0])
    return nums


def check_citations_resolve():
    """Every `PRD n.n` / `ARCHITECTURE n.n` must resolve to a real section."""
    available = {"PRD": _section_numbers("PRD.md"),
                 "ARCHITECTURE": _section_numbers("ARCHITECTURE.md")}
    for rel in markdown_files():
        if (rel.startswith("docs/history/") or rel.startswith("features/")
                or rel == "docs/multi-session-repo-playbook.md"):
            continue
        for doc, num in re.findall(r"\b(PRD|ARCHITECTURE)\s+(\d+(?:\.\d+)?)\b", read(rel)):
            if num not in available[doc]:
                fail("citations", f"{rel} cites '{doc} {num}', which is not a section")


def _known_dead_links():
    """Allowlist of links already dead when the checker was introduced.

    Each row carries a reason. The list is asserted both ways: an entry that
    starts resolving is a stale allowlist row and fails, so it cannot rot.
    """
    out = set()
    path = os.path.join(ROOT, "tests", "known_dead_links.txt")
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        if line.lstrip().startswith("#"):
            continue
        # comments are separated by two spaces + '#', so a '#anchor' in a link survives
        line = line.split("  #")[0].strip()
        if " -> " in line:
            src, tgt = line.split(" -> ", 1)
            out.add((src.strip(), tgt.strip()))
    return out


def check_links_resolve():
    """Every relative markdown link must resolve, unless explicitly allowlisted."""
    known = _known_dead_links()
    still_dead = set()
    for rel in markdown_files():
        base = os.path.dirname(os.path.join(ROOT, rel))
        for target in re.findall(r"\]\(([^)#][^)]*)\)", read(rel)):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = os.path.normpath(os.path.join(base, target.split("#")[0]))
            if not os.path.exists(path):
                if (rel, target) in known:
                    still_dead.add((rel, target))
                else:
                    fail("links", f"{rel} -> {target} does not exist")
    for stale in sorted(known - still_dead):
        fail("links", f"tests/known_dead_links.txt lists '{stale[0]} -> {stale[1]}', "
                      f"which now resolves or is gone — remove the allowlist row")


def check_backlog_and_state_cards():
    """Card IDs must agree across BACKLOG, STATE and any card files."""
    backlog = read("tasks/BACKLOG.md")
    backlog_ids = set(re.findall(r"^\| (M\d+-\d+) \|", backlog, re.M))
    if not backlog_ids:
        fail("cards", "tasks/BACKLOG.md has no card rows")
    for card_id in sorted(set(re.findall(r"\b(M\d+-\d+)\b", read("docs/STATE.md")))):
        if card_id not in backlog_ids:
            fail("cards", f"docs/STATE.md names {card_id}, which has no BACKLOG row")
    card_dir = os.path.join(ROOT, "tasks", "cards")
    for fn in os.listdir(card_dir):
        if fn == "TEMPLATE.md" or not fn.endswith(".md"):
            continue
        cid = fn.split("-")[0] + "-" + fn.split("-")[1]
        if cid not in backlog_ids:
            fail("cards", f"tasks/cards/{fn} has no BACKLOG row")
        row = re.search(rf"^\| {re.escape(cid)} \| [^|]* \| (\S+) \|", backlog, re.M)
        card = re.search(r"\*\*Status:\*\* (\S+)", read(f"tasks/cards/{fn}"))
        if row is None:
            fail("cards", f"{cid}: could not parse a status from its BACKLOG row")
        elif card is None:
            fail("cards", f"tasks/cards/{fn}: could not parse '**Status:** <value>'")
        elif row.group(1) != card.group(1):
            fail("cards", f"{cid}: BACKLOG says '{row.group(1)}', card says '{card.group(1)}'")


def check_decision_index():
    """Every decision file must be in the index, and vice versa."""
    d = os.path.join(ROOT, "docs", "decisions")
    files = {n for n in os.listdir(d) if n.endswith(".md") and n != "README.md"}
    listed = set(re.findall(r"\]\((\d{4}-[a-z0-9-]+\.md)\)", read("docs/decisions/README.md")))
    for missing in sorted(files - listed):
        fail("decisions", f"{missing} is not in docs/decisions/README.md")
    for ghost in sorted(listed - files):
        fail("decisions", f"docs/decisions/README.md lists {ghost}, which does not exist")


BANNED = [
    (r"design/WF-XXX\.md", "wireframes are sections in design/wireframes.md (PRD 3.2)"),
    (r"TanStack Query", "the stack uses TanStack Table (PRD 2.4)"),
    (r"artifact: PM-(?:STRATEGY|DISCOVERY)", "PM artifacts use framework codes (PRD 5.2)"),
    (r"\b16 skills\b", "there are 17; assert the set, not a count"),
]
# Operational surfaces only — an agent acts on these. The meta-documents
# (CLAUDE.md, PRD, ARCHITECTURE, docs/, tasks/) discuss the bans by name.
BANNED_SCOPE = ("AGENTS.md", "GEMINI.md", ".cursorrules", "README.md", "GETTING_STARTED.md",
                "landing-page/index.html")


def _in_banned_scope(rel):
    if rel in BANNED_SCOPE:
        return True
    if rel.startswith("skills/") and not rel.startswith("skills/ui-ux-pro-max/data"):
        return True
    return rel.startswith(".claude/commands/")


def check_banned_strings():
    scanned = 0
    for rel in markdown_files() + [f for f in EXTRA_SURFACES if exists(f)]:
        if not _in_banned_scope(rel):
            continue
        scanned += 1
        text = read(rel)
        for pattern, why in BANNED:
            for m in re.finditer(pattern, text):
                line = text[:m.start()].count("\n") + 1
                # allow explicit negations, e.g. "no TanStack Query"
                ctx = text[max(0, m.start() - 30):m.start()].lower()
                # a negation must be an adjacent word, not merely somewhere nearby
                if re.search(r"\b(no|not|never|instead of)\b[^.]{0,12}$", ctx):
                    continue
                fail("banned", f"{rel}:{line} '{m.group(0)}' — {why}")
    if scanned == 0:
        fail("banned", "check_banned_strings scanned no files — the sweep is blind")


def check_cli_banner():
    """ARCHITECTURE 3.3 item 9 — the cli.js help banner states a skill count."""
    text = read("skills/cli.js")
    real = len(skill_set())
    claimed = set(int(n) for n in re.findall(r"copies (\d+) skills", text))
    if not claimed:
        fail("cli-banner", "skills/cli.js has no 'copies N skills' banner line to check")
    for n in sorted(claimed - {real}):
        fail("cli-banner", f"skills/cli.js says 'copies {n} skills'; there are {real}")


def check_claimable_cards_are_unblocked():
    """docs/STATE.md 'Next up' must not list a card the BACKLOG says is blocked."""
    state = read("docs/STATE.md")
    m = re.search(r"## Next up[^\n]*\n(.*?)(?=\n## |\n---)", state, re.S)
    if not m:
        fail("state", "docs/STATE.md has no 'Next up' section")
        return
    backlog = read("tasks/BACKLOG.md")
    for cid in re.findall(r"^\| (M\d+-\d+) \|", m.group(1), re.M):
        row = re.search(rf"^\| {re.escape(cid)} \| [^|]* \| (\S+) \|", backlog, re.M)
        if row and row.group(1) == "blocked":
            fail("state", f"docs/STATE.md lists {cid} as claimable, but BACKLOG says blocked")


# Decision 0008 — the branching rules every agent entry point must state, word for word.
# CLAUDE.md is read by Claude Code, AGENTS.md by Codex, GEMINI.md by Gemini, .cursorrules by Cursor.
# The skills/ twins of the last three are covered by check_twins_byte_identical.
BRANCH_RULES = (
    "Start every development branch from `develop` and merge it back into `develop`.",
    "Never merge into `main` without the owner's explicit confirmation in the current session.",
)
AGENT_ENTRY_POINTS = ("CLAUDE.md", "AGENTS.md", "GEMINI.md", ".cursorrules")


def _squash(text):
    """Collapse whitespace so a rule wrapped across lines still matches."""
    return " ".join(text.split())


def check_branch_rules_in_entry_points():
    """Decision 0008 — every agent reads the same branching rules.

    This asserts the rules are STATED. It cannot stop a merge; that restriction is on
    discipline until GitHub branch protection exists (ARCHITECTURE 6.5).
    """
    for rel in AGENT_ENTRY_POINTS:
        text = _squash(read(rel))
        for rule in BRANCH_RULES:
            if _squash(rule) not in text:
                fail("branch-rules", f"{rel} does not state: {rule}")


def check_state_card_rows_unique():
    """A card is in exactly one row of the board: in flight, done, next up, or blocked.

    A duplicate means a move was half-done or an edit left an orphan table behind —
    a stale fragment once sat under 'Blocked on owner' for twelve days, contradicting
    the live rows above it.
    """
    seen = {}
    for n, line in enumerate(read("docs/STATE.md").splitlines(), 1):
        m = re.match(r"^\| (M\d+-\d+) \|", line)
        if m:
            seen.setdefault(m.group(1), []).append(n)
    for cid, lines in sorted(seen.items()):
        if len(lines) > 1:
            fail("state", f"docs/STATE.md has {cid} in {len(lines)} rows (lines {lines}); a card belongs in one")


def check_state_freshness():
    """docs/STATE.md must declare a Last updated date."""
    if not re.search(r"\*\*Last updated:\*\* \d{4}-\d{2}-\d{2}", read("docs/STATE.md")):
        fail("state", "docs/STATE.md has no '**Last updated:** YYYY-MM-DD' line")


def check_claude_md_is_rules_only():
    """The playbook caps the always-on file at ~150 lines."""
    n = len(read("CLAUDE.md").splitlines())
    if n > 150:
        fail("claude-md", f"CLAUDE.md is {n} lines; the cap is 150 (playbook layer 1)")


# ---------------------------------------------------------------- self-probe

def self_probe():
    """Verify the detectors bite. A vacuous test is worse than no test."""
    probes = []
    for pattern, _ in BANNED:
        bad = {"design/WF-XXX\\.md": "see design/WF-XXX.md for the screen",
               "TanStack Query": "built with TanStack Query today",
               "artifact: PM-(?:STRATEGY|DISCOVERY)": "artifact: PM-STRATEGY",
               "\\b16 skills\\b": "all 16 skills are installed"}[pattern]
        probes.append((pattern, bad, True))
        probes.append((pattern, "a wholly unrelated sentence", False))
    for pattern, sample, should_match in probes:
        if bool(re.search(pattern, sample)) != should_match:
            fail("self-probe", f"detector {pattern!r} did not behave on {sample!r}")
    if not skill_set():
        fail("self-probe", "skill_set() found nothing — the detector is blind")
    if not command_set():
        fail("self-probe", "command_set() found nothing — the detector is blind")
    if not _section_numbers("PRD.md"):
        fail("self-probe", "section parser found no PRD sections")


def main():
    self_probe()
    for name, fn in sorted(globals().items()):
        if name.startswith("check_") and callable(fn):
            fn()
    if FAILURES:
        print(f"FAIL — {len(FAILURES)} problem(s):\n")
        for f in FAILURES:
            print("  " + f)
        return 1
    print("ok — documentation is consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
