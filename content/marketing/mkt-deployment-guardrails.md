# Logic layer — Deployment Guardrails (readiness)

**Purpose.** Produce the governance blueprint that must exist before any AI marketing
capability is turned on: the **assist-vs-act** boundary, **approval-gate tiers**,
**sign-off requirements**, and an **audit-trail spec**. The core principle: **assist** (the
AI drafts, suggests, summarizes) is low-risk; **act** (the AI publishes, sends, or changes
live state) is high-risk and should be **auto-allowed almost nowhere early**. **Blueprint
and guidance only — it provisions nothing, publishes nothing, and is not legal advice.**

**Minimum inputs.** None required. Optionally a list of intended AI marketing use cases so
the tiers can be tailored.

## Named checks
1. **ASSIST_VS_ACT_UNDEFINED** — there is no explicit, written boundary between AI actions
   that only assist (draft, suggest, summarize) and actions that act on the world (publish,
   send, schedule, edit live audiences). Severity **high**. Without the boundary every
   capability defaults to ambiguous risk.
2. **APPROVAL_TIER_MISSING** — no tiered approval model exists. The blueprint defines tiers,
   e.g. **Tier 0 (assist-only, auto):** draft/summarize, never reaches an audience.
   **Tier 1 (review-then-publish):** human approves each artifact before publish.
   **Tier 2 (act, restricted):** narrow auto-publish only after a sustained track record,
   reversible, low-blast-radius. Early on, **auto-publish almost nothing.** Severity
   **high** per missing tier.
3. **SIGNOFF_UNDEFINED** — named human sign-off roles per tier are not defined (who approves
   a Tier 1 publish, who authorizes any Tier 2 auto-publish, who can pause the system).
   Severity **high**.
4. **NO_AUDIT_TRAIL** — there is no spec for logging what the AI proposed, what a human
   approved or edited, who signed off, and when. Severity **critical**. Without an audit
   trail no AI marketing action is defensible or reversible.

## Definitions emitted
None — this tool does not touch the shared semantic layer.

## Fix patterns
- Write the assist-vs-act boundary explicitly; classify every intended use case as assist or act.
- Adopt the tiered approval model; place every act-class capability at Tier 1
  (review-then-publish) until it earns a Tier 2 exception — auto-publish almost nothing early.
- Name a human owner and sign-off authority per tier, plus a single owner who can pause everything.
- Specify the audit trail: prompt/input, AI proposal, human edit, approver, timestamp,
  publish target — immutable and reviewable.
- Label the blueprint **guidance, not legal advice**; recommend counsel review for
  regulated content.
