---
name: revops-practitioner-maturity
description: RevOps readiness tool. Use when an operator wants the RevOps practice to get its own house in order before it governs others' AI — a self-assessment of version control, reproducible deployment, and environment hygiene. Triggers on "is our RevOps practice ready", "RevOps maturity", "do we have our own house in order", "version control for our metadata", "reproducible deployment", "environment hygiene", "practitioner maturity", "/readiness practitioner-maturity". Self-assessment only — changes nothing.
---

# Practitioner Maturity (RevOps readiness)

A self-assessment of the RevOps practice's own engineering discipline — version control,
reproducible deployment, environment hygiene — because before RevOps governs other teams'
AI, its own practice has to meet the bar it sets. Outputs actionable fixes — never a score.
**Self-assessment only — it changes nothing.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this tool's
logic layer at `${CLAUDE_PLUGIN_ROOT}/content/revops/revops-practitioner-maturity.md`. Then:

1. **Inputs.** No client data required — this is a self-assessment of the RevOps practice.
   Optionally ask the operator how their team handles metadata version control, deployments,
   and environments so findings can be made concrete. No credentials, ever.
2. **Apply the named checks** from the logic layer: version control, reproducible deployment,
   and environment hygiene. Produce one finding per gap, each framed as "before you govern
   others' AI, your own practice needs this," with a concrete `the_fix`.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"revops-practitioner-maturity", name:"Practitioner Maturity", team:"revops", kind:"readiness"}`
   - `findings[]`: one per discipline gap; each with an actionable `the_fix`.
   - `summary.headline` + `summary.stats` (disciplines assessed, gaps, blocking gaps).
   - Standard `cta`.
   Write to `/tmp/revops-practitioner-maturity.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-practitioner-maturity.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the single most important discipline to fix first, and the
   artifact paths under `readiness-output/revops/`.

This tool assesses the RevOps practice's own discipline — it changes no system and deploys nothing.
