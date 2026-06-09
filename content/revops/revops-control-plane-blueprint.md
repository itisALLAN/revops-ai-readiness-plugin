# Logic layer — Control Plane Blueprint (RevOps synthesis)

**Purpose.** Each team has authored its own deployment-guardrails pack for the AI work it
wants to do. Left separate, those packs produce three inconsistent identity models, three
audit trails, and three views of what counts as sensitive data — exactly the fragmentation
an attacker or an auditor exploits. This tool synthesizes the three packs into ONE central
control-plane blueprint a human can implement: a single least-privilege identity model, one
unified audit-trail spec, one context/data governance policy, and one central guardrail
catalog. It is a blueprint — it deploys, configures, and provisions nothing.

**Inputs (minimum).** The three teams' deployment-guardrails JSON artifacts:
- `cs-deployment-guardrails` (customer-success)
- `sales-deployment-guardrails` (sales)
- `mkt-deployment-guardrails` (marketing)

Read from `readiness-output/index.json`. No new client data. No credentials. If a pack is
missing, the blueprint proceeds on what is present and names the gap.

## Named synthesis elements (each becomes a finding)
- **CP-IDENTITY** — Least-privilege identity model. Reconcile the access each pack requests
  into per-agent service identities scoped to the minimum objects/fields/actions that team's
  AI needs. No shared "god" credential; read vs write separated; human-in-the-loop required
  for any write or send. Trigger to raise it: any pack requesting broad or write access, or
  the three packs requesting overlapping-but-inconsistent scopes.
- **CP-AUDIT** — Unified audit-trail spec. One append-only log schema every agent writes to:
  who/what identity, which action, on which record, with which inputs/grounding, timestamp,
  and outcome. Trigger: packs that log differently or do not specify an audit trail at all.
- **CP-GOVERNANCE** — Context/data governance: PII handling, retention windows, and privacy
  rules for what an agent may read into context and how long anything is kept. Reconcile the
  strictest stance across the three packs as the floor. Trigger: any pack touching PII or
  customer content without a retention/redaction rule.
- **CP-CATALOG** — Central guardrail catalog: the union of the three packs' guardrails,
  de-duplicated and reconciled, with conflicts resolved to the stricter rule. The single
  place a human looks to see every guardrail any agent must honor. Trigger: always — this is
  the consolidating element.

## What it emits
- `findings[]` — one per blueprint element above; `what_we_found` summarizes what the packs
  said, `why_it_blocks_ai` explains the risk of leaving it fragmented, and `the_fix` gives
  concrete build steps a human follows to stand up that element.
- `consumed_artifacts[]` — the three guardrail packs that were present.
- `disclaimers[]` — must include **"Guidance, not legal advice."** (privacy/retention content).
- `summary` — `headline` names the central blueprint outcome; `narrative` must state which
  packs were ingested and explicitly name any pack that was missing; `stats` = packs
  ingested, guardrails catalogued, gaps.

## Recommendation patterns
- Default to least privilege and human-in-the-loop for every write/send action.
- Resolve guardrail conflicts to the stricter rule, and record that a human owns final
  ratification.
- Frame retention/PII guidance as guidance to validate with counsel — never as legal advice.
- State plainly, in the narrative and in CP-CATALOG's fix, that the blueprint is implemented
  by a human; this tool deploys nothing.

**Acceptance:** four blueprint elements present as findings, the three guardrail packs (those
available) in consumed_artifacts, a "Guidance, not legal advice." disclaimer, and any missing
pack named in the narrative.
