# Logic layer — Deployment Guardrails (readiness)

**Purpose.** Generate the guardrails a Customer Success AI must have in place before it
goes live: escalation/handoff trigger design, a context-handoff template, a read-only-first
permission posture, and a retrieval-plumbing checklist. Generated from best practice — no
client data needed. **Designs guardrails only; the suite never provisions or deploys an AI.**

**Minimum inputs.** None. Optionally the operator's stack names (CRM, KB platform) to
tailor wording. Never request credentials or live access.

## Named checks / guardrail areas
Emit one finding per area. These are prescriptive designs, so each "what_we_found" frames
the default gap the guardrail closes.

1. **Escalation & handoff triggers.** Triggers a finding always — every deployment needs
   explicit handoff rules. Define when the AI must stop and hand to a human: low retrieval
   confidence, sensitive intent (billing/security/legal), repeated failed turns, explicit
   customer request, or detected frustration/sentiment drop. **Severity: critical** — an AI
   with no handoff rule will answer things it shouldn't.
2. **Read-only-first permissions.** Triggers a finding always. The AI's first deployment
   should be read/draft only — it can retrieve and propose, but a human commits any write
   (record update, refund, status change). **Severity: high** — write access on day one
   turns a wrong answer into a wrong action.
3. **Retrieval-plumbing checklist.** Triggers a finding always. Before the AI can ground
   reliably, the retrieval path must be wired: Data Category Visibility on Knowledge,
   field-level security (FLS) on Knowledge objects/fields the AI reads, and sharing rules
   that expose only the intended articles. **Severity: high** — misconfigured visibility
   either starves retrieval or leaks internal-only content.

## Context-handoff template (drafts[])
Emit one `drafts[]` entry (`kind:"context-handoff-template"`) — a fill-in template the AI
hands to the human on escalation, capturing: customer + case id, intent, what the AI already
tried/answered, the grounding sources used, why it escalated, and the suggested next step.
Label it a template in `flags`.

## Definitions it may emit
None required.

## Fix patterns
- **Sequence** guardrails: retrieval plumbing → read-only-first → escalation rules →
  monitoring (handoff to the Test-Set & Observability tool).
- **Default deny** for sensitive intents — hard-gate, don't rely on the model.
- **Verify visibility** with a least-privilege review: the AI integration user sees exactly
  the public KB and nothing internal-only.
- **Stage** write access: enable only after a monitored read-only period passes review.

## Severity / readiness signal
Set `summary.ai_ready` false until escalation triggers, read-only-first posture, and the
retrieval-plumbing checklist are all in place. The headline names the single
highest-priority guardrail to stand up first (escalation/handoff design).

## Compliance
Any guardrail touching regulated handling is **guidance, not legal advice** — include a
`disclaimers[]` entry saying exactly that.
