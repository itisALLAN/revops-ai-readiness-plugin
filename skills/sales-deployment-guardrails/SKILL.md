---
name: sales-deployment-guardrails
description: Sales readiness tool. Use when an operator wants a blueprint for what an AI may do in Sales and under what controls — assist vs act tiering, with customer-facing sends behind approval and forecast-affecting writes behind auditability and human-in-the-loop. Triggers on "what can the AI do safely", "AI guardrails", "assist vs act", "deployment guardrails", "what controls do we need", "tiering for our sales AI", "/readiness deployment-guardrails".
---

# Deployment Guardrails (Sales)

Produces a generated blueprint of what an AI may do in the Sales motion and under what
controls — an assist/act tiering with both act sub-tiers. **This suite never provisions
or deploys an AI agent; this is a blueprint a human implements. Guidance, not legal advice.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-deployment-guardrails.md`. Then:

1. **Inputs.** None required — this tool is **generated** from the logic layer. Optionally
   take prior sales readiness artifacts to tailor the tiers; otherwise produce the
   standard blueprint. No credentials, ever.
2. **Apply the logic layer** to build the tiering: Assist; Act tier (i) customer-facing
   sends behind approval; Act tier (ii) forecast-affecting writes needing auditability +
   human-in-the-loop.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-deployment-guardrails", name:"Deployment Guardrails", team:"sales", kind:"readiness"}`
   - `findings[]` one per tier, each stating the allowed scope and the required control.
   - a `disclaimers[]` entry: `"Guidance, not legal advice."` Standard `cta`.
   Write to `/tmp/sales-deployment-guardrails.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-deployment-guardrails.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important guardrail.
