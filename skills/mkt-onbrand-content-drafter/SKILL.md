---
name: mkt-onbrand-content-drafter
description: Marketing activation tool. Use when an operator wants a first SAFE market-facing draft grounded in their brand codex and auto-checked against the claims list and distinctiveness guard — to fill a content gap or repurpose an existing blog. Triggers on "draft on-brand content", "write a post in our voice", "repurpose this blog on-brand", "give me a safe first draft", "on-brand content drafter", "/activate onbrand-content". Loads the codex and runs the claims + distinctiveness checks before emitting. Drafts only — never sends or publishes.
---

# On-Brand Content Drafter (Marketing)

Produces the **first safe market-facing draft** — grounded in the brand codex and
auto-checked against the claims list and the distinctiveness guard before it emits.
**Drafts and proposes only — it never sends, schedules, or publishes anything. A human
owns every publish.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-onbrand-content-drafter.md`. Then:

1. **Load the codex.** Read the brand codex artifact at
   `${CLAUDE_PLUGIN_ROOT}/readiness-output/marketing/mkt-brand-codex-builder.json` — the
   draft is grounded on it. If absent, offer to run `mkt-brand-codex-builder` first.
2. **Inputs.** Ask for a content brief (gap to fill, or a blog to repurpose) — uploaded,
   pasted, or a URL to web-fetch; or use `${CLAUDE_PLUGIN_ROOT}/fixtures/marketing/content-corpus.md`.
   No credentials, ever.
3. **Draft, then auto-check before emitting.** Draft strictly in the codex voice, then run
   the **claims** checks (`mkt-claims-compliance-guardrails` logic) and the
   **distinctiveness** checks (`mkt-distinctiveness-guard` logic) against the draft. Strip
   or qualify any banned/risky claim and record what was deliberately avoided in `flags`.
4. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-onbrand-content-drafter", name:"On-Brand Content Drafter", team:"marketing", kind:"activation"}`
   - one `drafts[]` entry (`kind:"on-brand-content"`) with the on-brand draft, `grounded_on`
     citing the codex, and `flags` listing any claim deliberately avoided.
   - `summary.headline`; `summary.ai_ready` = `null`. Standard `cta`.
   Write to `/tmp/mkt-onbrand-content-drafter.json`.
5. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-onbrand-content-drafter.json --validate`
6. Hand back the artifact paths; remind the operator it is a draft for human review and publish.
