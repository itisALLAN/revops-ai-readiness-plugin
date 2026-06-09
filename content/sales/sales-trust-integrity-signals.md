# Logic layer — Trust & Integrity Signals (readiness)

**Purpose.** Surface data patterns that *may* suggest reps are gaming or avoiding the
system, so leadership can investigate the *process and incentives* behind them. **Every
finding is a signal to investigate, never an accusation or a conclusion about any
individual.** If the data is gamed, an AI trained on it learns the gaming. **Assessment
only — changes nothing.**

**Framing rule (non-negotiable).** State in the narrative and in *every* finding that
these are signals to investigate, not conclusions. Never name-and-shame a rep. Patterns
have innocent explanations (territory mix, deal types, genuine timing).

**Minimum inputs.** Opportunities export (`opp_id`, `stage`, `amount`, `close_date`,
`owner`, `next_step`) and an activities export (`opp_id`, `date`, `logged`).

## Named checks
1. **SANDBAGGING_SIGNAL** — deals held at low stages despite strong activity, or close
   dates pushed conservatively far out relative to stage. Severity **medium**. A signal
   to investigate, not proof. May reflect pipeline pull-forward incentives.
2. **EOQ_CLIFF_SIGNAL** — close dates clustering on quarter/month ends, or amount/stage
   changes spiking near period close. Severity **medium**. A signal of period-driven
   behaviour worth a conversation, not a finding of wrongdoing.
3. **FORCED_FIELD_COMPLETION_SIGNAL** — fields populated only where required and left
   blank everywhere optional (e.g. next_step blank wherever not enforced), suggesting
   reps fill the minimum to advance. Severity **medium**.
4. **INCENTIVE_ALIGNMENT** (always include) — a recommendation, not a defect: review
   whether comp/forecast incentives reward the behaviour the patterns hint at, and fix
   the incentive before policing the data. Severity **low**.

## Disclaimers emitted
- A `disclaimers[]` entry: *"These are signals to investigate, not conclusions about
  any individual. Patterns can have legitimate explanations; confirm with the team
  before acting."*

## Fix patterns
- Investigate root cause with the team, not the rep, before any system change.
- Align incentives so accurate data is the path of least resistance.
- Re-baseline stage/close-date definitions so the patterns become measurable honestly.
- Never feed un-investigated patterns to an AI as ground truth.
