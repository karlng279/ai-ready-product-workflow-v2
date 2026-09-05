# /sync-check

Run artifact synchronization analysis for a feature after an artifact has changed. Detects stale upstream and downstream artifacts and generates surgical sync patches.

## Usage

```
/sync-check [feature-name] [changed-artifact-path]
```

**Examples:**
```
/sync-check "Export Customs Clearances" design/wireframes.md
/sync-check my-feature po/usd/ST-003.md
/sync-check my-feature po/prd.md
/sync-check my-feature                   # will ask which artifact changed
```

If `feature-name` is omitted, ask for it.
If `changed-artifact-path` is omitted, ask which artifact was recently modified.

---

## Execution Steps

### Step 0 — Confirm Target

1. Parse `$ARGUMENTS` for `feature-name` and `changed-artifact-path`
2. Resolve the full path: `features/{feature-name}/{changed-artifact-path}`
3. Read the changed artifact
4. If `change_summary` is not present in its frontmatter, ask:
   > "What changed in this artifact? Describe in one sentence."
5. If `change_type` is not present, classify it using the `artifact-sync` skill methodology

### Step 1 — Activate `artifact-sync`

Read `skills/artifact-sync/SKILL.md` (or `.agent/skills/artifact-sync/SKILL.md` if installed).
Follow all steps defined in the skill:
- Classify the change type
- Build the impact set (forward and backward)
- Produce the Stale Impact Report
- Generate surgical patches

### Step 2 — Present the Report

Output the full Stale Impact Report as defined in the skill.
Wait for the user to review before proceeding.

### Step 3 — Apply Patches (with confirmation)

After presenting the report, ask:
> "Apply approved patches now, or review manually first?"

**If "apply now":**
- For MEDIUM and LOW severity patches: apply automatically, list files updated
- For HIGH severity patches: show each patch's before/after and ask "Apply this patch? (yes/no)" before writing

**If "review manually":**
- Print the list of files that need updates
- Stop — user can run `/sync-check` again when ready to apply

### Step 4 — Post-Sync Summary

After applying all approved patches, print:

```
Sync complete.
  [N] files updated
  [summary of changes: ACs removed/rewritten, test cases updated, elements removed]
  All patched artifacts: sync_status → in_sync
```

Optionally offer:
> "Run `/validate-artifacts {feature-name}` to confirm quality gates still pass?"

---

## Rules

- Read `skills/artifact-sync/SKILL.md` before doing any analysis
- Never apply patches silently — always list affected files before writing
- Never modify the changed artifact's BODY — only update its frontmatter sync fields after all downstream patches are applied
- If an artifact has no `sync_status` field, treat it as `stale` (it predates this enhancement)
- Never patch `code/` artifacts — flag them as requiring manual developer review
- Always confirm before writing multiple files
