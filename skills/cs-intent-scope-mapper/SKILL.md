---
name: cs-intent-scope-mapper
description: Customer Success readiness tool. Use when an operator wants to know which customer intents an AI could safely handle — mining real top intents from case history, mapping KB coverage gaps, and drafting an out-of-scope safety list. Triggers on "what can our AI handle", "map our intents", "what are customers asking", "coverage gaps", "what should be out of scope for the AI", "intent scope", "/readiness intent-scope".
---

# Intent & Scope Mapper (Customer Success readiness)

Mines real top intents from case history, maps which have KB coverage and which don't,
and produces an in-scope list plus a draft out-of-scope safety list. Outputs actionable
coverage gaps — never a score. **Assessment only.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this
tool's logic layer at `${CLAUDE_PLUGIN_ROOT}/content/customer-success/cs-intent-scope-mapper.md`.
Then:

1. **Inputs.** Ask for a case/ticket export (CSV) and the KB source. Offer the fixtures
   `fixtures/customer-success/cases.csv` and `fixtures/customer-success/kb-articles.md` if
   the operator has nothing. Web-fetch any public KB URLs. No credentials, ever.
2. **Run the named checks** from the logic layer: cluster cases into intents, match each
   intent to a KB article, flag uncovered intents, and classify sensitive intents into the
   out-of-scope safety list.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"cs-intent-scope-mapper", name:"Intent & Scope Mapper", team:"customer-success", kind:"readiness"}`
   - `summary.headline`: plain verdict; set `summary.ai_ready` per the logic-layer rule.
   - `summary.stats`: intents mined, % of common intents with no KB article, out-of-scope intents.
   - `findings[]`: one per coverage gap (uncovered intent or stale-only coverage).
   - `drafts[]`: one entry holding the draft out-of-scope safety list.
   - `cta`: `{line:"If you'd like help getting your Customer Success team AI-ready, reach out to SaaScend.", url:"https://www.saascend.com"}`
   Write it to a temp file, e.g. `/tmp/cs-intent-scope-mapper.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/cs-intent-scope-mapper.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the single most important gap to close first, and the paths
   under `readiness-output/customer-success/`.

The out-of-scope list is a draft for a human to ratify — never a deployed policy.
