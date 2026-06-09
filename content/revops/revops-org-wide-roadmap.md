# Logic layer — Org-Wide AI-Readiness Roadmap (★ capstone, synthesis)

**Purpose.** Ingest every tool's JSON across all four teams and produce ONE prioritised
roadmap that traces team-level symptoms back to root RevOps-level causes (the
correlated-failure model). This is what makes the suite a suite, not 25 separate tools.

**Inputs.** `readiness-output/index.json` and the artifacts it references
(`readiness-output/**/*.json`). No new client data required — it synthesizes existing
outputs.

## How to synthesize
1. **Ingest.** Load every available artifact. Record each in `consumed_artifacts[]`.
   Explicitly note which teams/tools produced nothing — the roadmap is only as complete
   as its inputs (no silent gaps).
2. **Cluster symptoms.** Group findings across teams by underlying cause. Look for the
   correlated-failure pattern: surface symptoms in CS/Sales/Marketing that share a single
   RevOps root.
   - Common roots: **no governed glossary** (definition conflicts everywhere),
     **broken object/handoff integrity** (orphans, broken seams), **no shared
     consent/identity model**, **no measurement feedback loop**, **no version-control /
     environment discipline** in RevOps itself.
3. **Trace.** For each root cause, list the team-level symptoms it explains (reference
   source tool ids), and the single action that resolves them.
4. **Rank & sequence.** Order by leverage (how many symptoms a fix retires) × blocking
   severity. Assign `sequence` now/next/later and `effort` S/M/L. The keystone insight:
   fix RevOps-level roots before team-level patches.

## Output
`kind: "synthesis"`. Fill `roadmap[]` (each item: rank, action, root_cause, symptoms[]
referencing source findings, teams[], effort, sequence) and `consumed_artifacts[]`.
`summary.headline` = the single highest-leverage move; `summary.narrative` = the
correlated-failure story in 2–3 sentences; `summary.stats` = artifacts ingested, teams
covered, total symptoms, root causes. Standard CTA.

**Acceptance:** must trace at least one team-level symptom to a root RevOps cause.
