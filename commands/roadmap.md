---
description: Synthesize every team's readiness JSON into one prioritised org-wide AI-readiness roadmap
argument-hint: [out-root]
---

The operator wants the capstone synthesis across all four teams.

**Optional output root:** `$ARGUMENTS` (defaults to `readiness-output`)

Do this:

1. Read `readiness-output/index.json` (or the given root). List every artifact found, grouped by team. If none exist, tell the operator which tools to run first and stop.
2. Invoke **revops-org-wide-roadmap**. It ingests every available tool JSON across all four teams, traces team-level symptoms back to root RevOps-level causes (the correlated-failure model), and emits a ranked, sequenced roadmap.
3. Note coverage gaps explicitly: name any team or tool that produced no JSON, since the roadmap is only as complete as its inputs.
4. Optionally offer to also run **revops-semantic-reconciler** (cross-team definition conflicts) and **revops-control-plane-blueprint** (unified governance) if their inputs are present, since they deepen the roadmap.
5. Report where the roadmap deliverable landed and read back the top 3 ranked actions with their root causes.

The roadmap recommends; it deploys nothing. Every action is owned by a human.
