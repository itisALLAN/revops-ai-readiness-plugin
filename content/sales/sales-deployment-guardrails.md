# Logic layer — Deployment Guardrails (readiness, generated)

**Purpose.** Give Sales leadership a blueprint for what an AI may do and under what
controls, tiered by risk. The suite **never provisions or deploys an AI agent** — this
is guidance a human implements. **Compliance content is guidance, not legal advice.**

**Minimum inputs.** None. The tool is generated from this logic layer. Optionally ingest
prior sales readiness artifacts to tailor the tiers to the org's gaps.

## The tiers (always emit one finding per tier)
1. **ASSIST_TIER** — read-only help: summarise deals, draft text for a human, surface
   risks, answer questions over CRM data. No writes, no sends. Severity **low**. This is
   the safe first step once the readiness gaps are closed.
2. **ACT_TIER_CUSTOMER_FACING** — anything that would reach a prospect/customer (emails,
   sequences, scheduling). **Behind explicit human approval before send.** Controls:
   consent / CAN-SPAM / GDPR considerations (lawful basis, unsubscribe, sender identity),
   and a hard rule that the AI **never commits price or contractual terms**. Severity
   **high**.
3. **ACT_TIER_FORECAST_AFFECTING** — writes that change reported numbers (stage, amount,
   close date, forecast category). Require **full auditability** (who/what/when/why,
   reversible) and **human-in-the-loop** sign-off before the write lands. Severity
   **high**.

## Disclaimers emitted
- A `disclaimers[]` entry exactly: *"Guidance, not legal advice."*

## Fix patterns
- Start at Assist only; graduate a capability to an Act tier only after its readiness
  prerequisites pass.
- For customer-facing acts: route every draft through human approval; log consent basis;
  forbid price/terms commitments in the AI's scope.
- For forecast-affecting acts: require an audit trail and human confirmation on every
  write; keep changes reversible.
- Never let the AI self-promote between tiers; tier changes are a human governance
  decision.
