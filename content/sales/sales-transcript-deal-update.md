# Logic layer — Transcript → Deal Update Draft (★ flagship, activation)

**Purpose.** Turn a call transcript into drafted CRM-update text a rep pastes: next
steps, stage rationale, and extracted qualification signals. **Assist only — writes
nothing to any CRM.**

**Minimum inputs.** One call transcript (text/upload). Optional: the current stage and
the team's qualification framework (default to MEDDIC-style signals below).

## What to extract
1. **Next steps** — concrete, owned, dated where the transcript supports it. No invented
   commitments.
2. **Stage rationale** — what in the call justifies the current/proposed stage. If the
   transcript implies a stage change, propose it as a suggestion, not a fact.
3. **Qualification signals** — extract only what was actually said. Map to:
   - **Metrics / pain** (the quantified problem)
   - **Economic buyer / decision process** (who signs, approval thresholds)
   - **Budget** (stated number or range)
   - **Timeline / compelling event**
   - **Competition**
   - **Champion**
   Mark any signal **not** discussed as a gap to capture next — this is where the AI
   (and the rep) would otherwise be blind.
4. **Never fabricate.** If budget/authority/timeline weren't mentioned, say "not
   discussed" — do not infer a number.

## Output
`kind: "activation"`, one `drafts[]` entry: `kind:"crm-deal-update"`, `content` = the
paste-ready update (Next steps / Stage rationale / Qualification signals / Gaps to
capture), `grounded_on` = the transcript reference, `flags` = anything inferred or any
missing signal. `summary.headline` = the deal's readiness in one line. Standard CTA.
No `findings`.
