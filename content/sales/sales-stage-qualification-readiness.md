# Logic layer — Stage & Qualification Readiness (readiness)

**Purpose.** Determine whether pipeline stages are differentiated in the data and
whether qualification signals are captured **as fields** an AI could score against.
A stage the rep can't be distinguished from another stage by any field value is a
stage "the AI has nothing to score against." **Assessment only — changes nothing.**

**Minimum inputs.** One opportunities export with at least: `opp_id`, `stage`,
`amount`, `close_date`, and ideally any qualification-bearing columns (budget
confirmed, economic buyer, next step, decision process). The fixture has stage,
amount, close_date, next_step, lead_source, competitor — but **no** explicit
qualification fields, which is itself the headline finding.

## Named checks
1. **MISSING_QUALIFICATION_FIELDS** — no columns capture the qualification signals an
   AI would score (budget confirmed, economic buyer identified, decision process,
   compelling event, metrics/pain). Severity **critical** if none exist; **high** if
   only one or two exist. Qualification lives in rep memory and call notes, not fields.
2. **UNDIFFERENTIATED_STAGES** — two or more stages cannot be told apart by any field
   value (e.g. Discovery vs Qualification rows look identical except the stage label
   itself). Severity **high**. The stage picklist carries meaning no data backs up.
3. **STAGE_WITHOUT_SCORABLE_SIGNAL** — a stage exists in the pipeline that has no field
   that would let an AI judge whether a deal belongs there (e.g. "Qualification" with
   no budget/authority fields). Severity **high**. List the affected stage names.
4. **FREEFORM_NEXT_STEP_ONLY** — qualification intent is only inferable from a freeform
   `next_step` string, not a structured field. Severity **medium**.

## Definitions emitted
- term **"Qualified"**, `source_team:"sales"`, definition e.g. *"Qualified = budget
  confirmed AND economic buyer identified on the opportunity record"*. Emit so the
  semantic-reconciler can surface the conflict with marketing's MQL-based definition.

## Fix patterns
- Add structured qualification fields (Budget Confirmed checkbox, Economic Buyer
  lookup, Decision Process picklist, Compelling Event date) so signals become scorable.
- Write stage entry/exit criteria tied to those fields, then validate stages are
  differentiated by data, not just by a label.
- Govern one canonical "Qualified" definition jointly with marketing before any AI
  scores or routes a deal.
