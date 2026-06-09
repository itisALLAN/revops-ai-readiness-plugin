---
name: mkt-brand-codex-builder
description: ★ Flagship Marketing activation tool. Use when an operator wants to codify their brand voice into a machine-usable codex from content/blog URLs — voice, tone, positioning, messaging pillars, approved/banned language, visual notes. Triggers on "build a brand codex", "codify our voice", "extract our brand voice", "brand guidelines from our content", "/activate brand-codex". The codex JSON feeds the distinctiveness guard and content drafter.
---

# Codified Brand Builder (★ Marketing flagship)

Builds a machine-usable brand codex from a content corpus. The codex JSON is the
yardstick the Distinctiveness Guard and On-Brand Content Drafter consume.

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-brand-codex-builder.md`. Then:

1. **Inputs.** Ask for representative content/blog URLs (web-fetch them) or an uploaded
   corpus; or use `fixtures/marketing/content-corpus.md`. Take whatever volume is offered.
2. **Codify** voice, tone, positioning, pillars, approved + banned language, and visual
   notes per the logic layer, with verbatim exemplars. Flag any generic/off-voice samples
   as negative examples.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"mkt-brand-codex-builder", name:"Codified Brand Builder", team:"marketing", kind:"activation", flagship:true}`
   - top-level `codex` object with keys `voice, tone, positioning, pillars[], approved_language[], banned_language[], visual_notes, examples[]`.
   - one `drafts[]` entry (`kind:"brand-codex"`) rendering the codex human-readably.
   - `summary.headline` = the codified voice in a line. Standard `cta`.
   Write to `/tmp/mkt-brand-codex-builder.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-brand-codex-builder.json --validate`
5. Tell the operator the codex is saved at `readiness-output/marketing/mkt-brand-codex-builder.json`
   and that the distinctiveness guard and content drafter will use it.
