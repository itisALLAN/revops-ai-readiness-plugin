# Logic layer — Pipeline Reality Check (readiness)

**Purpose.** Test whether the open pipeline reflects reality. Stale close dates, blank
next steps, and stages that disagree with activity history mean an AI built on this
data would forecast and prioritise on fiction. **Assessment only — changes nothing.**

**Minimum inputs.** Opportunities export (`opp_id`, `stage`, `amount`, `close_date`,
`next_step`) and an activities export (`opp_id`, `type`, `date`). Use **today's date**
as the reference point for past-due detection.

## Named checks
1. **STALE_CLOSE_DATE** — an open opportunity (not Closed Won/Lost) whose `close_date`
   is in the past relative to today. Severity **high**; **critical** if the deal is in
   a late stage (Negotiation/Proposal). List the offending opp_ids.
2. **BLANK_NEXT_STEP** — an open opportunity with an empty `next_step`. Severity
   **medium**; **high** when it is also stale. An AI has no forward signal to act on.
3. **STAGE_ACTIVITY_MISMATCH** — a late-stage deal with no recent activity (e.g. in
   Negotiation but the most recent logged activity is weeks old, or none at all).
   Severity **high**. The stage claims momentum the activity log denies.
4. **AMOUNT_ANOMALY** — an amount that is zero, missing, or a clear outlier versus the
   account's profile. Severity **medium**. Flag for review, do not assume fraud.

## Stats to emit
- Open opportunities (count).
- % of open opps with a past-due close date.
- % of open opps with a blank next step.

## Fix patterns
- Enforce close-date re-baselining on stage change; require a future close_date to keep
  a deal open.
- Make next_step required to save an open opportunity.
- Add an activity-recency rule per stage (e.g. Negotiation requires activity in the
  last 14 days) and surface violators to the rep, not the AI.
- Review zero/blank amounts before any AI consumes pipeline value.
