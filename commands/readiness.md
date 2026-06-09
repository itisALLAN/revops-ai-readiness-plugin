---
description: Run a GTM team's AI-readiness tools (customer-success | sales | marketing | revops)
argument-hint: <team> [tool-id]
---

The operator wants to run AI-readiness assessments for a GTM team.

**Requested:** `$ARGUMENTS`

Do this:

1. Resolve the team from the first argument. Accept loose forms — "cs", "customer success", "success" → `customer-success`; "sales" → `sales`; "marketing", "mktg" → `marketing`; "revops", "ops" → `revops`. If no team is given, ask which of the four teams to run.
2. List that team's readiness tools (skills prefixed `cs-`, `sales-`, `mkt-`, `revops-`) and, in one line each, what input each needs. If a specific tool-id was given as the second argument, go straight to it.
3. Ask the operator which tool to run (or "all"), then for the inputs that tool needs — file uploads, Google Drive files, or public URLs. Never ask for credentials or live system access; this suite uses native connectors only.
4. Invoke the matching skill(s) by name. Each skill loads its content/logic layer, performs the analysis, emits a schema-valid JSON artifact, and renders the branded HTML via `shared/render.py`.
5. Report where the two artifacts landed under `readiness-output/<team>/` and surface the headline + blocking count.

Every output is an actionable list of changes — never a score or maturity grade. The suite never provisions, configures, or deploys an AI agent.
