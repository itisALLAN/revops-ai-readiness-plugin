---
name: revops-semantic-reconciler
description: RevOps synthesis tool. Use when an operator wants one governed glossary across teams plus a list of cross-team definition conflicts (e.g. marketing vs sales on "qualified"/"MQL") that would cause an AI router to mis-route. Triggers on "reconcile our definitions", "governed glossary", "do our teams define terms the same way", "where do marketing and sales disagree", "semantic layer", "definition conflicts", "/reconcile".
---

# Semantic Reconciler (RevOps synthesis)

Ingests every team tool's `definitions[]` (plus any reporting CSVs the operator supplies)
and produces ONE governed glossary, alongside a list of cross-team definition CONFLICTS an
AI would trip over. Surfaces the conflict — recommends a canonical definition; a human ratifies it.
**Synthesis only — it governs nothing automatically and changes no system.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this tool's
logic layer at `${CLAUDE_PLUGIN_ROOT}/content/revops/revops-semantic-reconciler.md`. Then:

1. **Ingest.** Read `readiness-output/index.json` and every artifact it lists; collect each
   artifact's `definitions[]`. Web-fetch or read any reporting CSVs the operator supplies to
   infer how terms are operationalized. Record each ingested file in `consumed_artifacts[]`.
   At minimum look for `mkt-audience-consent-readiness` and `sales-stage-qualification-readiness`
   — name any expected input that produced nothing (no silent gaps). If the index is empty,
   tell the operator which team tools to run first and stop.
2. **Run the named checks** from the logic layer: cluster definitions by term, detect
   divergence, and assess router impact. For every term where two teams disagree, emit a
   `conflicts[]` entry with ≥2 `positions` (team + definition), an `impact` (what breaks for
   an AI router), and a `recommended_canonical`. You MUST surface the "Qualified"/"MQL"
   conflict between marketing and sales.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"revops-semantic-reconciler", name:"Semantic Reconciler", team:"revops", kind:"synthesis"}`
   - `conflicts[]`: ≥1 entry; the "Qualified"/"MQL" conflict is mandatory.
   - `definitions[]`: the governed glossary (MQL, Qualified, Customer, Pipeline, Churn, ARR),
     each with the recommended canonical definition and `source_team:"revops"`.
   - `consumed_artifacts[]`: every upstream artifact read.
   - `summary.headline`: name the conflict found; `summary.stats`: definitions reconciled,
     conflicts found, teams covered.
   - Standard `cta`.
   Write to `/tmp/revops-semantic-reconciler.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-semantic-reconciler.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline, the top conflict and its recommended canonical, and the artifact
   paths under `readiness-output/revops/`.

Never rewrite a system of record here — this tool reconciles and recommends; a human ratifies the glossary.
