# Logic layer — Practitioner Maturity (RevOps readiness)

**Purpose.** RevOps is the keystone of this suite — it governs identity, audit, glossary,
and guardrails for everyone else's AI. That authority is only credible if the RevOps practice
holds itself to the same engineering discipline it is about to demand of other teams. This
tool is a self-assessment: does RevOps have version control, reproducible deployment, and
environment hygiene for its own work? Frame every finding as: **before you govern others' AI,
your own practice needs this.** Self-assessment only — it changes nothing.

**Inputs.** None required. Optionally, the operator describing how the team currently handles
metadata version control, deployments, and environments — used to make findings concrete.

## Named checks (each becomes a finding when the discipline is absent or partial)
- **PM-VERSION-CONTROL** — Is all RevOps work product (CRM metadata, automation definitions,
  config, the glossary and guardrail catalog this suite produces) under version control with
  history and review? Triggers when work lives only in the live org or in untracked files,
  with no diff, history, or peer review.
- **PM-REPRODUCIBLE-DEPLOY** — Can a change be deployed the same way every time, from source,
  with the ability to roll back? Triggers when deployments are manual point-and-click in the
  org, undocumented, or not reproducible from a tracked source.
- **PM-ENVIRONMENT-HYGIENE** — Are there separate, clean environments (e.g. sandbox/test vs
  production), with changes validated outside production first and no drift between them?
  Triggers when work is done directly in production, or sandboxes are stale/drifted from prod.

## What it emits
- `findings[]` — one per discipline gap. `what_we_found` states the gap, `why_it_blocks_ai`
  ties it to the keystone argument (RevOps cannot credibly govern AI it can't reproduce or
  roll back), and `the_fix` is the concrete, ordered remediation. Open the narrative and the
  findings with the framing "before you govern others' AI, your own practice needs these."
- `summary` — `headline` names the gap to close first; `stats` = disciplines assessed, gaps
  found, blocking gaps.

## Recommendation patterns
- Put metadata and config under source control with peer review before anything else — it is
  the foundation the other two disciplines rest on.
- Make deployment reproducible from that source, with a tested rollback path.
- Separate environments and forbid direct production edits; validate in a clean sandbox first.
- Keep the tone self-directed and credible: this is RevOps holding itself to its own bar, not
  a critique of another team.

**Acceptance:** one finding per absent/partial discipline, each with an actionable `the_fix`,
framed as the RevOps practice getting its own house in order before it governs others' AI.
