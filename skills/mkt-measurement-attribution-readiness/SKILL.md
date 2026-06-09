---
name: mkt-measurement-attribution-readiness
description: Marketing readiness tool. Use when an operator wants to know whether they could detect AI-generated marketing output tanking conversion or deliverability before the damage spreads — consistent attribution, a closed feedback loop, and leading-indicator alerting. Triggers on "is our measurement AI-ready", "check our attribution", "do we have a feedback loop", "would we catch AI output going wrong", "measurement and attribution readiness", "/readiness measurement-attribution".
---

# Measurement & Attribution Readiness (Marketing)

Assesses whether a feedback loop exists to catch AI-generated marketing output tanking
conversion or deliverability **before** the damage goes broad — consistent attribution,
a closed measurement loop, and leading-indicator alerting. **Assessment only — it changes
nothing.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-measurement-attribution-readiness.md`. Then:

1. **Inputs.** Ask for a campaign/marketing reporting export (CSV/upload) or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/marketing/campaign-reporting.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: INCONSISTENT_ATTRIBUTION,
   NO_CLOSED_FEEDBACK_LOOP, NO_LEADING_INDICATOR_ALERT. Pull stats from the reporting fixture.
3. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-measurement-attribution-readiness", name:"Measurement & Attribution Readiness", team:"marketing", kind:"readiness"}`
   - `findings[]` for inconsistent attribution, the missing feedback loop, and missing
     leading-indicator alerting.
   - `summary.headline` + `summary.stats` from the reporting data. Standard `cta`.
   Write to `/tmp/mkt-measurement-attribution-readiness.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-measurement-attribution-readiness.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
