---
name: mkt-claims-compliance-guardrails
description: Marketing readiness tool. Use when an operator wants to find risky marketing claims already live in their content before an AI is allowed to repurpose or generate copy — unsubstantiated superlatives, comparative claims, pricing/guarantee promises. Triggers on "check our claims", "are our marketing claims compliant", "scan content for risky claims", "claims guardrails", "compliance review of our content", "/readiness claims-compliance". Produces a substantiation standard, a banned-claims list, and a review path.
---

# Claims & Compliance Guardrails (Marketing)

Scans published marketing content for risky claims **already live** — unsubstantiated
superlatives, comparative claims, and pricing/guarantee promises — then produces a
substantiation standard, a banned-claims list, and a human review path. **Assessment
and guidance only — it changes nothing, sends nothing, and is not legal advice.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-claims-compliance-guardrails.md`. Then:

1. **Inputs.** Ask for content/blog URLs (web-fetch them) or an uploaded content corpus;
   or use `${CLAUDE_PLUGIN_ROOT}/fixtures/marketing/content-corpus.md`. No credentials, ever.
2. **Apply the named checks** from the logic layer: UNSUBSTANTIATED_SUPERLATIVE,
   COMPARATIVE_CLAIM, PRICING_GUARANTEE_PROMISE, NO_REVIEW_PATH. Cite the offending
   lines verbatim in `affected`/`evidence`.
3. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-claims-compliance-guardrails", name:"Claims & Compliance Guardrails", team:"marketing", kind:"readiness"}`
   - `findings[]` for each risky live claim, plus the substantiation standard and
     banned-claims list expressed in `the_fix`.
   - `summary.headline` + `summary.stats`. Standard `cta`.
   - a `disclaimers[]` entry: **"Guidance, not legal advice."**
   Write to `/tmp/mkt-claims-compliance-guardrails.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-claims-compliance-guardrails.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
