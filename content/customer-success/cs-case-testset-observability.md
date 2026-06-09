# Logic layer — Case Test-Set & Observability (readiness)

**Purpose.** Turn resolved cases into a cold-start evaluation set (real customer questions
paired with known-good resolutions) and define the QA/observability plan — including a
named owner — needed to run an AI safely. You cannot trust an AI you cannot measure; this
produces the measuring stick before launch. **Builds the set and plan; runs no AI.**

**Minimum inputs.** A case/ticket export of resolved cases with at least a subject and a
resolution note (the fixture `cases.csv` has `subject`, `status`, `notes`). Use the fixture
if the operator has nothing.

## Named checks / build steps
1. **Resolved-case selection.** Use only cases with `status` Closed and a clear, correct
   resolution in the notes. Skip cases resolved ad hoc, escalated without a clean answer, or
   still open — they are not known-good.
2. **Question → known-good pairing.** For each selected case, write the customer question as
   asked and the verified known-good resolution from the notes. This becomes one test row.
   Prefer high-volume, in-scope intents (password reset, SSO, exports) — match the in-scope
   set from the Intent & Scope Mapper.
3. **Coverage balance.** The set should span the in-scope intents, not just the easiest one.
   Note any in-scope intent with no resolved case to draw from.
4. **Observability plan elements (each a finding).**
   - **Named owner.** A specific role/person owns AI quality monitoring. **Severity: high** —
     unowned monitoring does not happen.
   - **What to monitor.** Containment/handoff rate, retrieval-confidence distribution,
     escalation reasons, customer sentiment, and any answer that contradicts a known-good.
     **Severity: high.**
   - **Regression cadence.** Re-run the cold-start set on a fixed cadence (e.g. weekly and
     before every prompt/KB change) to catch regressions. **Severity: medium.**

## Test set (drafts[])
Emit one `drafts[]` entry (`kind:"cold-start-test-set"`) — a small markdown table of
question → known-good-resolution rows drawn from real resolved cases (e.g. CS-1001 password
reset, CS-1002 SSO, CS-1005 invite teammates, CS-1004/CS-1022 exports). Label it a starting
set in `flags`; note it must be human-reviewed.

## Definitions it may emit
None required.

## Fix patterns
- **Grow** the set over time; start with the highest-volume in-scope intents.
- **Gate** launch on a passing run of the cold-start set, not on intuition.
- **Re-run** the set on every KB or prompt change before shipping it.
- **Assign** a single accountable owner for monitoring before go-live.

## Severity / readiness signal
Set `summary.ai_ready` false until a named owner, a monitoring plan, and a regression cadence
are all defined and the cold-start set passes once. The headline names the monitoring owner
as the key dependency.
