---
name: sales-transcript-deal-update
description: ★ Flagship Sales activation tool. Use when an operator has a call/meeting transcript and wants drafted CRM-update text — next steps, stage rationale, and extracted qualification signals (MEDDIC-style). Triggers on "turn this transcript into a deal update", "summarize this call for the CRM", "extract next steps and qualification", "deal update draft", "/activate deal-update". Drafts text a rep pastes — writes nothing.
---

# Transcript → Deal Update Draft (★ Sales flagship)

Turns a call transcript into paste-ready CRM-update text. **Assist only — it writes
nothing to any CRM.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` and the logic layer at
`${CLAUDE_PLUGIN_ROOT}/content/sales/sales-transcript-deal-update.md`. Then:

1. **Inputs.** Ask for the transcript (paste/upload) or use
   `fixtures/sales/call-transcript.txt`. Optionally take the current stage and the team's
   qualification framework.
2. **Extract** next steps, stage rationale, and qualification signals per the logic layer.
   Extract only what was said; mark anything not discussed as a gap; never fabricate
   budget/authority/timeline.
3. **Compose the artifact** to the shared schema:
   - `tool`: `{id:"sales-transcript-deal-update", name:"Transcript → Deal Update Draft", team:"sales", kind:"activation", flagship:true}`
   - one `drafts[]` entry (`kind:"crm-deal-update"`, paste-ready `content` with sections
     Next steps / Stage rationale / Qualification signals / Gaps to capture; `grounded_on`
     the transcript; `flags` for anything inferred or missing).
   - `summary.headline` = one-line deal readiness. Standard `cta`.
   Write to `/tmp/sales-transcript-deal-update.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/sales-transcript-deal-update.json --validate`
5. Hand back the draft **labelled draft-only** for the rep to paste, plus the artifact paths.
