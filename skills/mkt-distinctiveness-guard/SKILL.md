---
name: mkt-distinctiveness-guard
description: Marketing readiness tool. Use when an operator wants to check whether their content is drifting toward generic LLM-voice / the mean, measured against their own brand codex. Triggers on "is our content drifting", "check distinctiveness", "is our content too generic", "are we sounding like everyone else", "distinctiveness guard", "voice drift check", "/readiness distinctiveness". Loads the brand codex as the yardstick; offers to build the codex first if it is absent.
---

# Distinctiveness Guard (Marketing)

Uses the **brand codex** as the yardstick to flag content drifting toward generic
LLM-voice or the mean. **Assessment only — it rewrites nothing automatically; it tells a
human what to fix.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/marketing/mkt-distinctiveness-guard.md`. Then:

1. **Load the codex.** Read the brand codex artifact at
   `${CLAUDE_PLUGIN_ROOT}/readiness-output/marketing/mkt-brand-codex-builder.json`. **If it
   is absent, offer to run `mkt-brand-codex-builder` first** — the guard needs the codex as
   its yardstick and cannot run meaningfully without it.
2. **Inputs.** Ask for content/blog URLs (web-fetch them) or an uploaded content corpus;
   or use `${CLAUDE_PLUGIN_ROOT}/fixtures/marketing/content-corpus.md`. No credentials, ever.
3. **Apply the named checks** from the logic layer against the codex: GENERIC_LLM_VOICE,
   MISSING_SIGNATURE_ELEMENTS, BANNED_FILLER_PRESENT, NO_CONCRETE_DELIVERABLE. Cite the
   drifting lines and give the fix (rewrite toward codex voice).
4. **Compose the artifact** to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"mkt-distinctiveness-guard", name:"Distinctiveness Guard", team:"marketing", kind:"readiness"}`
   - `findings[]` for each drifting piece, the fix being a rewrite toward the codex voice.
   - `summary.headline` + `summary.stats`. Standard `cta`.
   Write to `/tmp/mkt-distinctiveness-guard.json`.
5. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/mkt-distinctiveness-guard.json --validate`
6. Hand back the artifact paths, read back the headline and the single most important fix.
