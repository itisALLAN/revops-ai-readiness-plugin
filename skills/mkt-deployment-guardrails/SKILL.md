---
name: mkt-deployment-guardrails
description: Marketing readiness tool. Use when an operator wants a blueprint for how an AI marketing capability should be governed — the assist-vs-act boundary, approval-gate tiers, sign-off requirements, and an audit-trail spec — before anything is turned on. Triggers on "how should we govern AI marketing", "assist vs act", "approval gates for AI content", "deployment guardrails", "AI publishing controls", "what sign-off do we need", "/readiness deployment-guardrails".
---

# Deployment Guardrails (Marketing)

Produces a governance blueprint for an AI marketing capability: the **assist-vs-act**
boundary (act = publish), **approval-gate tiers** (auto-publish almost nothing early),
**sign-off requirements**, and an **audit-trail spec**. **Blueprint and guidance only —
it provisions nothing, publishes nothing, and is not legal advice.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-deployment-guardrails.md`. Then:

1. **Inputs.** None required — this tool generates the blueprint. Optionally ask which AI
   marketing use cases the operator is considering to tailor the tiers. No credentials, ever.
2. **Apply the named checks** from the logic layer: ASSIST_VS_ACT_UNDEFINED,
   APPROVAL_TIER_MISSING, SIGNOFF_UNDEFINED, NO_AUDIT_TRAIL. Emit one finding per tier/gate.
3. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-deployment-guardrails", name:"Deployment Guardrails", team:"marketing", kind:"readiness"}`
   - `findings[]` per approval-gate tier and the audit-trail spec.
   - `summary.headline` + `summary.stats`. Standard `cta`.
   - a `disclaimers[]` entry: **"Guidance, not legal advice."**
   Write to `/tmp/mkt-deployment-guardrails.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-deployment-guardrails.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important gate.
