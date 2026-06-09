---
name: sales-stage-qualification-readiness
description: Sales readiness tool. Use when an operator wants to know whether their pipeline stages are differentiated in the data and whether qualification signals are captured as fields an AI could score against. Triggers on "are our stages AI-ready", "do we capture qualification", "check stage hygiene", "can an AI score our deals", "stage qualification readiness", "/readiness stage-qualification".
---

# Stage & Qualification Readiness (Sales)

Assesses whether pipeline stages are differentiated in the data and whether
qualification signals exist **as fields** — the raw material an AI would need to
score a deal. **Assessment only — changes nothing in any CRM.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-stage-qualification-readiness.md`. Then:

1. **Inputs.** Ask for an opportunities export (CSV/upload) or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/opportunities.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: stage differentiation, missing
   qualification fields, stages the AI "has nothing to score against."
3. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"sales-stage-qualification-readiness", name:"Stage & Qualification Readiness", team:"sales", kind:"readiness"}`
   - `findings[]` for undifferentiated stages and absent qualification fields.
   - one `definitions[]` entry: term `"Qualified"`, `source_team:"sales"`, a
     sales-specific definition (this is reconciled later against marketing's).
   - `summary.headline` + `summary.stats`. Standard `cta`.
   Write to `/tmp/sales-stage-qualification-readiness.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-stage-qualification-readiness.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
