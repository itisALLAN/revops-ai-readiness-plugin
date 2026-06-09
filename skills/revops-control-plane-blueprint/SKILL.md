---
name: revops-control-plane-blueprint
description: RevOps synthesis tool. Use when an operator wants one central control-plane blueprint synthesized from the three teams' deployment-guardrails packs — a least-privilege identity model, a unified audit-trail spec, context/data governance (PII, retention, privacy), and a central guardrail catalog. Triggers on "control plane blueprint", "unify our guardrails", "central identity and audit model for AI", "least-privilege model for agents", "governance blueprint", "/blueprint control-plane". Blueprint only — deploys nothing.
---

# Control Plane Blueprint (RevOps synthesis)

Synthesizes the three teams' deployment-guardrails packs into ONE central control-plane
blueprint: a least-privilege identity model, a unified audit-trail spec, context/data
governance (PII, retention, privacy), and a single central guardrail catalog.
**Blueprint only — this tool deploys, configures, and provisions nothing. A human builds it.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this tool's
logic layer at `${CLAUDE_PLUGIN_ROOT}/content/revops/revops-control-plane-blueprint.md`. Then:

1. **Ingest.** Read `readiness-output/index.json` and the three deployment-guardrails packs:
   `cs-deployment-guardrails`, `sales-deployment-guardrails`, `mkt-deployment-guardrails`.
   Record each in `consumed_artifacts[]`. If any of the three is missing, proceed with what
   is present but explicitly name the missing pack(s) in `summary.narrative` (no silent gaps)
   — a blueprint built on a partial input set must say so. If the index is empty, tell the
   operator to run the team guardrails tools first and stop.
2. **Synthesize** per the logic layer into four blueprint elements: least-privilege identity
   model, unified audit-trail spec, context/data governance (PII, retention, privacy), and a
   central guardrail catalog (the union/reconciliation of the three packs' guardrails).
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"revops-control-plane-blueprint", name:"Control Plane Blueprint", team:"revops", kind:"synthesis"}`
   - `findings[]`: one per blueprint element, each with concrete `the_fix` build steps.
   - `consumed_artifacts[]`: the three guardrail packs (those present).
   - `disclaimers[]`: include "Guidance, not legal advice."
   - `summary.headline` + `summary.stats` (packs ingested, guardrails catalogued, gaps).
   - Standard `cta`.
   Write to `/tmp/revops-control-plane-blueprint.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/revops-control-plane-blueprint.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the four blueprint elements at a glance, note any missing pack,
   and the artifact paths under `readiness-output/revops/`.

This tool produces a blueprint a human implements — it never configures or deploys a control plane.
