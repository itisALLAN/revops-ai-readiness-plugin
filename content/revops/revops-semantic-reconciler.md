# Logic layer — Semantic Reconciler (RevOps synthesis)

**Purpose.** Build ONE governed glossary across the four teams and surface every place where
two teams define the same term differently. A definition conflict is the single most
dangerous gap for an AI router: if "qualified" means two things, the agent hands off, routes,
or scores against the wrong rule half the time. This tool makes the conflict visible and
recommends a canonical definition — a human ratifies it.

**Inputs (minimum).**
- `readiness-output/index.json` and the artifacts it references — specifically each
  artifact's `definitions[]` array. Marketing and sales tools both emit a definition for
  "Qualified"/"MQL"; those are the primary raw material.
- Optionally, reporting CSVs (e.g. an MQL report, a pipeline-by-stage report) the operator
  supplies, used to infer how a term is *operationalized* versus how it is *documented*.

No new client system access. No credentials. Synthesizes existing outputs + optional CSVs.

## Named checks
- **DEF-CLUSTER** — Group every `definitions[]` entry across all consumed artifacts by
  normalized term (case/stem-insensitive: "MQL" ≈ "Marketing Qualified Lead"). Triggers
  nothing on its own; produces the candidate set for the conflict scan.
- **DEF-DIVERGENCE** — For each clustered term, compare definitions across `source_team`.
  A finding (a `conflicts[]` entry) triggers when two teams' definitions are not logically
  equivalent — different gating criteria, different thresholds, or one includes a condition
  the other omits. Severity by blast radius: a term that gates a handoff or routing decision
  (Qualified, MQL) is the highest priority.
- **DEF-OPERATIONAL-DRIFT** — Where a reporting CSV is supplied, check whether the term is
  *used* the way it is *defined* (e.g. the MQL report fires on content-download alone while
  the documented definition also requires a score threshold). Drift reinforces a conflict
  entry or raises one on its own.
- **DEF-ORPHAN** — A core shared term (Customer, Pipeline, Churn, ARR) that no team defines
  at all. Not a conflict, but it must still be governed: emit a canonical definition in the
  glossary and note in the narrative that no team currently owns it.

## What it emits
- `conflicts[]` — one per diverging term, each with ≥2 `positions` (team + that team's
  definition), an `impact` (the concrete AI-router failure), and a `recommended_canonical`.
  **Mandatory entry:** term "Qualified"/"MQL", with the marketing position
  ("MQL = lead score above threshold OR content download, regardless of budget/authority")
  and the sales position ("Qualified = budget confirmed AND economic buyer identified").
- `definitions[]` — the governed glossary, `source_team:"revops"`, covering at minimum:
  **MQL, Qualified, Customer, Pipeline, Churn, ARR**. Each is the recommended canonical text,
  with `derived_from` naming the upstream source(s) it reconciles.
- `consumed_artifacts[]` — every upstream artifact ingested.
- `summary` — `headline` names the headline conflict; `stats` = definitions reconciled,
  conflicts found, teams covered.

## Recommendation patterns
- For Qualified/MQL: separate the two concepts explicitly. Keep "MQL" as a marketing-stage
  signal (interest), and reserve "Qualified" for a sales-accepted state with budget +
  economic buyer. The canonical should make the *transition rule* between them unambiguous so
  an AI router has a single gate.
- For a term with no owner (orphan), propose the most operationally common definition and
  flag that ownership must be assigned before any AI consumes it.
- Always frame the canonical as a *recommendation a human ratifies* — never assert it is now
  the governed truth.

**Acceptance:** must flag ≥1 cross-team definition conflict (the Qualified/MQL conflict
satisfies this) and emit a governed glossary covering the six core terms.
