# Logic layer — Measurement & Attribution Readiness (readiness)

**Purpose.** Determine whether a **feedback loop** exists to catch AI-generated marketing
output tanking conversion or deliverability **before** the damage goes broad. The risk: an
AI can produce and distribute content far faster than a monthly report can reveal a
problem. Without consistent attribution, a closed loop, and leading-indicator alerting,
the team finds out a campaign is failing only after the quarter closes. **Assessment only.**

**Minimum inputs.** One campaign/marketing reporting export with at least: `campaign`,
`channel`, `month`, `spend`, `leads`, `mqls`, `opps`, `won`, `revenue`, and ideally an
`attribution_model` column. The fixture `fixtures/marketing/campaign-reporting.csv` has all
of these and deliberately mixes attribution models.

## Named checks
1. **INCONSISTENT_ATTRIBUTION** — the reporting mixes attribution models across rows
   (First-touch, Last-touch, Multi-touch) so the same revenue is credited differently
   depending on the row. Severity **high**. An AI optimizing spend against incomparable
   numbers will chase artifacts of the model, not real performance.
2. **NO_CLOSED_FEEDBACK_LOOP** — there is no evidence that downstream conversion/revenue is
   tied back to the originating content/campaign on a cadence fast enough to act on.
   Severity **high**. Without a closed loop, an AI's output cannot be evaluated and
   corrected; failures compound silently.
3. **NO_LEADING_INDICATOR_ALERT** — reporting is monthly/lagging with no leading-indicator
   alerting (reply/bounce/unsubscribe spikes, conversion-rate drop, deliverability dip)
   that would fire within hours. Severity **critical**. A leading-indicator alert is the
   circuit-breaker that lets a human pause an AI step before damage goes broad.

## Definitions emitted
None — this tool does not touch the shared semantic layer.

## Fix patterns
- Standardize on one attribution model (or report all models side-by-side, never mixed
  per-row) so performance is comparable before an AI optimizes against it.
- Close the loop: tie won revenue back to the originating campaign/content on a weekly or
  faster cadence, so AI output can be evaluated and corrected.
- Stand up leading-indicator alerting (bounce/unsubscribe spike, conversion drop,
  deliverability dip) with a named human owner and a documented pause/rollback action —
  the circuit-breaker for any AI content step.
