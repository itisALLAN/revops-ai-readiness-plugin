---
name: sales-capture-coverage
description: Sales readiness tool. Use when an operator wants to know how much deal reality is actually logged and where an AI would be blind — opps with zero activities, calls/meetings never captured, thin coverage on key deals. Triggers on "how much do we log", "is our activity capture good", "where is the AI blind", "capture coverage", "are calls logged", "/readiness capture-coverage".
---

# Capture Coverage (Sales)

Measures how much of the deal's real story is logged — and where an AI would be flying
blind because the conversation never made it into the system. **Assessment only.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-capture-coverage.md`. Then:

1. **Inputs.** Ask for an activities export **and** at least one transcript (to show a
   real conversation that may or may not be captured), or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/activities.csv` and
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/call-transcript.txt`. Optionally take the
   opportunities export to know which deals are open. No credentials, ever.
2. **Apply the named checks** from the logic layer: zero-activity opps, uncaptured
   calls/meetings, thin coverage on high-value deals.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-capture-coverage", name:"Capture Coverage", team:"sales", kind:"readiness"}`
   - `findings[]` per check. `summary.stats`: activities per open opp, opps with no
     activity. Standard `cta`.
   Write to `/tmp/sales-capture-coverage.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-capture-coverage.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important fix.
