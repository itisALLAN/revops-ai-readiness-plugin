---
name: revops-data-architecture-handoff
description: RevOps readiness tool. Use when an operator wants to know whether their object graph is trustworthy enough for an AI to route across — checking referential integrity, orphaned records, broken lead→opportunity→case handoff seams, and duplicate keys in multi-object CRM exports. Triggers on "check our data architecture", "are our objects connected", "referential integrity", "find orphaned records", "broken handoffs", "duplicate accounts", "data handoff readiness", "/readiness data-architecture".
---

# Data Architecture & Handoff Readiness (RevOps)

Cross-checks multi-object CRM exports for the integrity problems that break AI routing:
orphaned records, broken lead→opportunity→case seams, dangling foreign keys, and duplicate
keys. Outputs a per-defect fix — never a score. **Assessment only — it changes no records.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this tool's
logic layer at `${CLAUDE_PLUGIN_ROOT}/content/revops/revops-data-architecture-handoff.md`.
Then:

1. **Inputs.** Ask for multi-object exports (Accounts, Contacts, Leads, Opportunities, Cases
   as CSV/upload) or use `${CLAUDE_PLUGIN_ROOT}/fixtures/revops/multi-object-export.md`. The
   foreign keys must be present so seams can be traced. No credentials, ever.
2. **Run the named checks** from the logic layer across the objects: referential integrity
   (dangling FKs), orphaned records, broken lead→opp→case seams, and duplicate keys. Produce
   one finding per distinct defect, each with a concrete `the_fix` and the `affected` record ids.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"revops-data-architecture-handoff", name:"Data Architecture & Handoff Readiness", team:"revops", kind:"readiness"}`
   - `summary.headline`: plain verdict on whether the graph is trustworthy for AI routing;
     set `summary.ai_ready` (false if any critical/high integrity defect exists).
   - `summary.stats`: objects checked, broken FKs, orphans, duplicates.
   - `findings[]`: one per defect; include `affected` (record ids) and `evidence`.
   - Standard `cta`.
   Write to `/tmp/revops-data-architecture-handoff.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-data-architecture-handoff.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the single most important defect to fix first, and the paths
   under `readiness-output/revops/`.

Never modify or merge records here — this tool diagnoses; a human owns the cleanup.
