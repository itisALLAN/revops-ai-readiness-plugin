---
name: sales-pipeline-reality-check
description: Sales readiness tool. Use when an operator wants to know whether the open pipeline reflects reality — stale close dates, blank next steps, stage-vs-activity mismatches, amount anomalies. Triggers on "is our pipeline real", "check pipeline hygiene", "are our close dates stale", "pipeline reality check", "is the forecast trustworthy", "/readiness pipeline-reality".
---

# Pipeline Reality Check (Sales)

Tests whether the open pipeline reflects what is actually happening — the precondition
for an AI ever trusting it. **Assessment only — changes nothing in any CRM.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-pipeline-reality-check.md`. Then:

1. **Inputs.** Ask for an opportunities export **and** an activities export, or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/opportunities.csv` and
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/activities.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: stale close dates, blank next
   steps, stage-vs-activity mismatches, amount anomalies. Use today's date as the
   reference point for "past due."
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-pipeline-reality-check", name:"Pipeline Reality Check", team:"sales", kind:"readiness"}`
   - `findings[]` for each named check that fires.
   - `summary.stats`: open opps, % past-due close, % blank next step. Standard `cta`.
   Write to `/tmp/sales-pipeline-reality-check.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-pipeline-reality-check.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
