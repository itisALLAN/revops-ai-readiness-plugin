---
name: revops-org-wide-roadmap
description: ★ Capstone RevOps synthesis tool. Use when an operator wants one prioritised org-wide AI-readiness roadmap synthesized from every team's tool outputs — tracing team-level symptoms to root RevOps causes. Triggers on "org-wide roadmap", "synthesize all the readiness results", "what should we fix first across teams", "the capstone", "/roadmap". Ingests readiness-output JSON; recommends only.
---

# Org-Wide AI-Readiness Roadmap (★ RevOps capstone)

Synthesizes every team's tool JSON into one prioritised roadmap that traces symptoms to
root RevOps causes. Recommends only — deploys nothing.

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/revops/revops-org-wide-roadmap.md`. Then:

1. **Ingest.** Read `readiness-output/index.json` and every artifact it lists. If empty,
   tell the operator which tools to run first and stop. Record each ingested file in
   `consumed_artifacts[]`; name any team/tool that produced nothing.
2. **Synthesize** per the logic layer: cluster cross-team symptoms by shared cause, trace
   each root cause to the symptoms it explains (cite source tool ids), then rank by
   leverage × severity and sequence now/next/later.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"revops-org-wide-roadmap", name:"Org-Wide AI-Readiness Roadmap", team:"revops", kind:"synthesis", flagship:true}`
   - `roadmap[]`, `consumed_artifacts[]`, `summary` (headline = highest-leverage move,
     narrative = correlated-failure story, stats = artifacts/teams/symptoms/root-causes).
   - Standard `cta`. Must trace ≥1 team symptom to a root RevOps cause.
   Write to `/tmp/revops-org-wide-roadmap.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-org-wide-roadmap.json --validate`
5. Read back the top 3 ranked actions with their root causes and the artifact paths.
