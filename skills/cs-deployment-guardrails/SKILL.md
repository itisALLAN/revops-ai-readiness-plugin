---
name: cs-deployment-guardrails
description: Customer Success readiness tool. Use when an operator wants the guardrails to put in place before a support AI goes live — escalation/handoff triggers, a context-handoff template, a read-only-first permission posture, and a retrieval-plumbing checklist. Needs no client data. Triggers on "what guardrails do we need", "how do we deploy a support AI safely", "escalation design", "handoff template", "permission posture for AI", "retrieval plumbing checklist", "/readiness deployment-guardrails".
---

# Deployment Guardrails (Customer Success readiness)

Generates the safety guardrails a Customer Success AI needs before going live:
escalation/handoff trigger design, a context-handoff template, a read-only-first
permission recommendation, and a retrieval-plumbing checklist. Generated from best
practice — needs no client data. **Recommendations only — the suite never deploys an AI.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this
tool's logic layer at `${CLAUDE_PLUGIN_ROOT}/content/customer-success/cs-deployment-guardrails.md`.
Then:

1. **Inputs.** None required — this tool is generated. Optionally accept the operator's
   stack notes (CRM, KB platform) to tailor wording, but never ask for credentials or
   live access.
2. **Generate the guardrails** from the logic layer: one finding per guardrail area
   (escalation triggers, read-only-first permissions, retrieval plumbing), and a
   context-handoff template as a draft.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"cs-deployment-guardrails", name:"Deployment Guardrails", team:"customer-success", kind:"readiness"}`
   - `summary.headline`: plain verdict on what must be in place; `summary.ai_ready` per the rule.
   - `findings[]`: one per guardrail (escalation/handoff design, read-only-first permissions,
     retrieval-plumbing checklist).
   - `drafts[]`: one entry holding the context-handoff template.
   - `disclaimers[]`: include "Guidance, not legal advice."
   - `cta`: `{line:"If you'd like help getting your Customer Success team AI-ready, reach out to SaaScend.", url:"https://www.saascend.com"}`
   Write it to a temp file, e.g. `/tmp/cs-deployment-guardrails.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/cs-deployment-guardrails.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the single highest-priority guardrail, and the paths under
   `readiness-output/customer-success/`.

This tool designs guardrails; it does not provision, configure, or deploy anything.
