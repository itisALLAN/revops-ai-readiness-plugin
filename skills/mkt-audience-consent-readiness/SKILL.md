---
name: mkt-audience-consent-readiness
description: Marketing readiness tool. Use when an operator wants to know whether their lead/audience data is clean and consented enough for an AI to segment, target, or message against — consent basis, subscription/suppression status, list hygiene, and MQL/lead-definition consistency with sales. Triggers on "is our audience data AI-ready", "check consent readiness", "audit our lead list", "can an AI target our leads", "consent and suppression check", "audience readiness", "/readiness audience-consent".
---

# Audience & Consent Readiness (Marketing)

Assesses whether lead/audience data is explicit, consented, and clean enough for an AI to
segment, target, or message against — consent basis, subscription/suppression status,
list and deliverability hygiene, and whether the MQL/lead definition is consistent with
sales. **Assessment only — it changes nothing in any CRM or ESP.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-audience-consent-readiness.md`. Then:

1. **Inputs.** Ask for a leads/contacts export (CSV/upload) or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/marketing/leads.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: CONSENT_BASIS_MISSING,
   SUPPRESSED_BUT_ACTIVE, COLD_LIST_NO_CONSENT, SEGMENT_NOT_EXPLICIT,
   MQL_DEFINITION_DRIFT. State the ~33% unknown/absent-consent figure explicitly and
   flag cold-list leads with no consent.
3. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-audience-consent-readiness", name:"Audience & Consent Readiness", team:"marketing", kind:"readiness"}`
   - `findings[]` for each consent/hygiene gap.
   - one `definitions[]` entry: term `"MQL"`, `source_team:"marketing"`, a **marketing**
     definition deliberately broader than sales' "Qualified" (so the semantic-reconciler
     surfaces the conflict).
   - `summary.headline` + `summary.stats` (leads, % MQLs without consent,
     suppressed-but-active count). Standard `cta`.
   Write to `/tmp/mkt-audience-consent-readiness.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-audience-consent-readiness.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
