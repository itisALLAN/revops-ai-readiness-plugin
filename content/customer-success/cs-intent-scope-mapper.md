# Logic layer — Intent & Scope Mapper (readiness)

**Purpose.** Mine the real top customer intents from case history, map each to KB
coverage, and decide what an AI could safely be scoped to handle. Produces (a) findings
for every coverage gap and (b) a draft out-of-scope safety list of intents an AI must
never self-serve. Pairs with KB Retrieval Readiness (article quality) and the Reply
Drafter (live proof of a gap). **Diagnoses only — a human ratifies scope.**

**Minimum inputs.** A case/ticket export with at least a subject and a category per case
(the fixture `cases.csv` has `subject` and `reported_category`). A KB source: article
URLs, an export, or the fixture corpus `kb-articles.md`.

## Named checks
1. **Intent mining.** Cluster cases by subject + reported category into named intents
   (e.g. "password reset", "SSO setup", "billing dispute"). Rank by volume. This is the
   factual base — no finding on its own.
2. **Coverage match.** For each mined intent, find a KB article that actually answers it.
   An intent is *covered* only by a current, on-topic article; a stale or sprawl-only match
   counts as **partial**.
3. **Coverage gap.** Triggers when a common intent has **no** KB article at all. **Severity:
   high** for high-volume intents, medium for long-tail. State the org-wide gap rate:
   ~38% of common intents have no KB article (aligns with the org roadmap).
4. **Partial / stale-only coverage.** Triggers when the only matching article is stale or a
   sprawl page. **Severity: medium** — the intent is technically covered but not safely
   groundable; cross-reference KB Retrieval Readiness.
5. **Sensitive-intent classification.** Triggers when a mined intent falls in a regulated or
   high-risk class — it goes on the out-of-scope safety list regardless of KB coverage.
   Mandatory members: **billing disputes**, **account security**, and **legal/regulated
   (GDPR / data residency)**. **Severity: critical** if such an intent is currently
   unguarded.

## Out-of-scope safety list (drafts[])
Emit one `drafts[]` entry (`kind:"out-of-scope-safety-list"`) listing intents an AI must
not self-serve, each with the reason and the routing action (escalate to human / named
queue). Must include billing disputes, account security, and legal/regulated (GDPR).
Label it clearly as a draft for human ratification in `flags`.

## Definitions it may emit
Optionally emit a `definitions[]` entry for any intent label that doubles as a shared
business term. Not required for the core run.

## Fix patterns
- **Author** a single-topic KB article for each high-volume uncovered intent before it is
  put in AI scope.
- **Refresh** partial/stale coverage (hand to KB Retrieval Readiness) rather than scoping
  the intent in as-is.
- **Hard-gate** every sensitive intent to a human queue; never rely on the model to decline.
- **Prioritise** gap closure by intent volume × business risk.

## Severity / readiness signal
Set `summary.ai_ready` false whenever any high-volume intent is uncovered or any sensitive
intent is unguarded. The headline names the in-scope set as the safe starting point and the
out-of-scope list as the guardrail.
