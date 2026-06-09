# Logic layer — Eval & Deployment Framework (RevOps readiness)

**Purpose.** Most orgs can stand up an AI agent faster than they can prove it works or roll
it back when it doesn't. This tool produces the framework that makes an agent safe to evaluate,
ship, and operate: how to test it (eval harness), how to change it without breaking it
(config versioning + dev/test/prod), and how to run it in production (ops runbook). It is a
framework — it builds, runs, and deploys nothing. A human implements it.

**Inputs.** None required — the framework is generated. Optionally the agent's intended job
and historical case/transcript samples, which let the eval test-set guidance be made concrete.

## Named framework components (each becomes a finding)
- **EVAL-HARNESS** — The eval harness design. A test set built from real historical cases
  (inputs + the known-good outcome), run two ways: **cold-start** (the agent with no prior
  context, to test baseline reasoning) and **accumulated-context** (the agent with the
  context it would have in production, to test it doesn't drift or over-rely on history).
  Plus **regression testing**: the full set re-runs on every config change and must not
  regress before the change ships.
- **CONFIG-DISCIPLINE** — Versioned, rollback-able configuration. Every prompt, tool
  definition, model choice, and guardrail lives in version control with a version tag; any
  deployed version can be rolled back atomically. No untracked, hand-edited production config.
- **ENV-MODEL** — A dev/test/prod model. Changes are authored in dev, validated against the
  eval harness in test, and only promoted to prod after passing. Prod is never edited directly;
  promotion is gated on eval results.
- **OPS-RUNBOOK** — The live-fleet ops runbook for agents already in production: monitoring
  (what signals to watch — output quality, escalation rate, latency, cost), tuning (how and
  when to adjust safely), incident response (how to detect, contain, and roll back a bad
  agent), and lifecycle (versioning, deprecation, retirement of agents).

## What it emits
- `findings[]` — one per component above. `what_we_found` frames the gap a typical org has,
  `why_it_blocks_ai` explains the risk of operating without it, and `the_fix` is the concrete,
  ordered recipe a human follows to build that component.
- `summary` — `headline` names the framework outcome; `stats` = framework components, eval
  gates, environments.

## Recommendation patterns
- Ground eval test sets in *real historical cases*, not invented prompts — the known outcome
  is what makes the test meaningful.
- Always run both cold-start and accumulated-context; a pass on one is not a pass on both.
- Make rollback a first-class capability, not an afterthought — if you can't roll back in
  minutes, you can't ship safely.
- Gate prod promotion on a clean regression run; never promote on a partial pass.
- State plainly that this is a framework a human implements; the tool deploys nothing.

**Acceptance:** all four framework components present as findings, each with an actionable
`the_fix` build recipe.
