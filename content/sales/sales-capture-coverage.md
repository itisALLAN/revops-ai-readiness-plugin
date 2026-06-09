# Logic layer — Capture Coverage (readiness)

**Purpose.** Measure how much deal reality is actually logged, and locate where an AI
would be blind because conversations never reached the system. An AI can only reason
over what is captured; uncaptured calls are invisible to it. **Assessment only.**

**Minimum inputs.** An activities export (`opp_id`, `type`, `date`, `logged`) and at
least one transcript showing a real conversation. Optional opportunities export to
scope to open deals only.

## Named checks
1. **ZERO_ACTIVITY_OPP** — an open opportunity with no logged activity at all. Severity
   **high**; **critical** if it is high-value or late-stage. The AI knows nothing about
   the deal beyond its static fields.
2. **UNCAPTURED_CONVERSATION** — a transcript (or known call/meeting) that has no
   matching logged activity. Severity **high**. The richest signal exists outside the
   system entirely.
3. **THIN_COVERAGE_KEY_DEAL** — a high-value open opportunity carrying only one or two
   logged activities relative to its stage. Severity **medium**. Coverage is too thin
   for an AI to summarise the deal reliably.
4. **EMAIL_ONLY_COVERAGE** — a deal whose only logged touches are emails, with no calls
   or meetings captured. Severity **low**. Conversational context is missing.

## Stats to emit
- Average logged activities per open opportunity.
- Count (and %) of open opportunities with zero logged activity.

## Fix patterns
- Auto-capture calls/meetings via the CRM's activity logging or a conversation-capture
  integration so transcripts land on the record.
- Set a minimum-activity expectation per stage and surface zero-activity open deals to
  managers.
- Backfill key open deals from calendars and inboxes before an AI summarises them.
