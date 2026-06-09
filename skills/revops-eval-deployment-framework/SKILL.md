---
name: revops-eval-deployment-framework
description: RevOps readiness tool. Use when an operator wants a framework for evaluating and operating an AI agent safely — an eval harness design (historical-case test sets, cold-start vs accumulated-context, regression testing), versioned/rollback-able config discipline, a dev/test/prod model, and a live-fleet ops runbook (monitoring, tuning, incident response, lifecycle). Triggers on "how do we test our AI agent", "eval harness", "eval framework", "agent regression testing", "dev test prod for agents", "ops runbook for AI", "config versioning for agents", "/framework eval-deployment". Framework only — deploys nothing.
---

# Eval & Deployment Framework (RevOps readiness)

Produces the framework an org needs to evaluate, deploy, and operate an AI agent safely:
an eval harness design, config-versioning discipline, a dev/test/prod model, and a
live-fleet ops runbook. **Framework and documentation only — it deploys and runs nothing.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this tool's
logic layer at `${CLAUDE_PLUGIN_ROOT}/content/revops/revops-eval-deployment-framework.md`.
Then:

1. **Inputs.** No client data is required — this tool generates a framework. Optionally ask
   the operator for the agent's intended job and any historical case/transcript samples so
   the eval test-set guidance can be made concrete. No credentials, ever.
2. **Assemble the framework** per the logic layer's named components: eval harness design,
   versioned/rollback-able config discipline, dev/test/prod model, and live-fleet ops runbook.
   Each component becomes a finding with concrete `the_fix` steps a human follows to build it.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"revops-eval-deployment-framework", name:"Eval & Deployment Framework", team:"revops", kind:"readiness"}`
   - `findings[]`: one per framework component; each `the_fix` is the build recipe.
   - `summary.headline` + `summary.stats` (components, gates, environments).
   - Standard `cta`.
   Write to `/tmp/revops-eval-deployment-framework.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-eval-deployment-framework.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the four framework components at a glance, and the artifact paths
   under `readiness-output/revops/`.

This tool authors a framework a human implements — it never builds, runs, or deploys an eval harness or agent.
