---
name: cs-case-testset-observability
description: Customer Success readiness tool. Use when an operator wants a cold-start evaluation set and a monitoring plan before a support AI goes live — real questions with known-good resolutions drawn from resolved cases, plus a QA/observability plan with a named owner. Triggers on "build a test set for our AI", "how do we evaluate the AI", "cold-start eval", "what should we monitor", "QA plan for the support AI", "regression set from our cases", "/readiness testset-observability".
---

# Case Test-Set & Observability (Customer Success readiness)

Builds a cold-start evaluation set from resolved cases (real questions + known-good
resolutions) and a QA/monitoring plan with a named owner. Outputs an actionable test set
and observability plan — never a score. **Assessment only.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this
tool's logic layer at `${CLAUDE_PLUGIN_ROOT}/content/customer-success/cs-case-testset-observability.md`.
Then:

1. **Inputs.** Ask for a case/ticket export with resolved cases (subject + resolution
   notes). Offer the fixture `fixtures/customer-success/cases.csv` if the operator has
   nothing. No credentials, ever.
2. **Build the test set** from the logic layer: select resolved cases with a clear
   known-good resolution, turn each into a question → expected-resolution pair, and define
   the observability plan (named owner, what to monitor, regression cadence).
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"cs-case-testset-observability", name:"Case Test-Set & Observability", team:"customer-success", kind:"readiness"}`
   - `summary.headline`: plain verdict; `summary.ai_ready` per the rule.
   - `summary.stats`: resolved cases available, test cases built.
   - `findings[]`: the observability plan elements (named owner, what to monitor, regression cadence).
   - `drafts[]`: one entry holding the cold-start test set as a small question → known-good table.
   - `cta`: `{line:"If you'd like help getting your Customer Success team AI-ready, reach out to SaaScend.", url:"https://www.saascend.com"}`
   Write it to a temp file, e.g. `/tmp/cs-case-testset-observability.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/cs-case-testset-observability.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the named monitoring owner, and the paths under
   `readiness-output/customer-success/`.

The test set evaluates a future AI; this tool builds the set, it does not run an AI.
