---
name: sales-account-icp-readiness
description: Sales readiness tool. Use when an operator wants to know whether account data, buying-committee/hierarchy, and ICP/MQL-SQL definitions are solid enough for an AI to route or prioritise accounts. Triggers on "is our account data AI-ready", "check ICP", "do we have buying committee data", "account hygiene", "is our ICP defined", "account ICP readiness", "/readiness account-icp".
---

# Account & ICP Readiness (Sales)

Assesses account data hygiene, buying-committee/hierarchy presence, and whether ICP
and MQL/SQL are defined well enough for an AI to route or prioritise. **Assessment only.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-account-icp-readiness.md`. Then:

1. **Inputs.** Ask for an accounts export (CSV/upload) or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/accounts.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: missing buying-committee contacts,
   hierarchy gaps, data hygiene, missing/implicit ICP definition.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-account-icp-readiness", name:"Account & ICP Readiness", team:"sales", kind:"readiness"}`
   - `findings[]` per check.
   - one `definitions[]` entry: term `"ICP"`, `source_team:"sales"`.
   - `summary.stats` + standard `cta`.
   Write to `/tmp/sales-account-icp-readiness.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-account-icp-readiness.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
