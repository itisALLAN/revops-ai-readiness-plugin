---
name: sales-trust-integrity-signals
description: Sales readiness tool. Use when an operator wants to surface data patterns that suggest reps may be gaming or avoiding the CRM — sandbagging, end-of-quarter cliffs, forced-only field completion. Surfaces SIGNALS TO INVESTIGATE, never accusations. Triggers on "are reps gaming the CRM", "check for sandbagging", "data integrity signals", "is the data being gamed", "EOQ cliffs", "trust signals", "/readiness trust-integrity".
---

# Trust & Integrity Signals (Sales)

Surfaces data patterns that *may* indicate reps gaming or avoiding the system. **These
are signals to investigate with curiosity — never accusations or conclusions.**
**Assessment only — changes nothing in any CRM.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-trust-integrity-signals.md`. Then:

1. **Inputs.** Ask for an opportunities export **and** an activities export, or use
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/opportunities.csv` and
   `${CLAUDE_PLUGIN_ROOT}/fixtures/sales/activities.csv`. No credentials, ever.
2. **Apply the named checks** from the logic layer: sandbagging, EOQ cliffs,
   forced-only field completion. **Frame every finding as a signal to investigate, not
   a conclusion** — say so in the narrative and in each finding.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-trust-integrity-signals", name:"Trust & Integrity Signals", team:"sales", kind:"readiness"}`
   - `findings[]` per signal, each explicitly framed as a signal to investigate.
   - include at least one **incentive-alignment** recommendation among the findings.
   - a `disclaimers[]` note stating these are signals, not conclusions. Standard `cta`.
   Write to `/tmp/sales-trust-integrity-signals.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-trust-integrity-signals.json --validate`
5. Hand back the artifact paths, read back the headline and the single most important next step.
