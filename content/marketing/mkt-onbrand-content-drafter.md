# Logic layer — On-Brand Content Drafter (activation)

**Purpose.** Produce the **first safe market-facing draft** — the proof that the upstream
readiness work pays off. The draft is **grounded in the brand codex** and **auto-checked
against the claims list and the distinctiveness guard before it is emitted**, so the first
AI-assisted content a team sees is already on-voice and claim-safe. It either fills a
content gap or repurposes an existing blog. **Drafts and proposes only — it never sends,
schedules, or publishes. A human owns every publish.**

**Dependencies.** Loads the brand codex at
`readiness-output/marketing/mkt-brand-codex-builder.json` (grounding + voice). Applies the
logic of `mkt-claims-compliance-guardrails` and `mkt-distinctiveness-guard` to the draft
before emitting. If the codex is absent, offer to run the codex builder first.

**Minimum inputs.** A content brief — the gap to fill or the blog to repurpose (uploaded,
pasted, or a URL). Plus the codex artifact.

## How to draft (and self-check)
1. **Draft in codex voice** — we→you address, signature metaphor, approved language, every
   promise tied to a concrete deliverable.
2. **Claims self-check** — scan the draft for unsubstantiated superlatives, comparative
   claims, and pricing/guarantee promises (the claims-guardrails checks). Strip or qualify
   any that appear; never invent proof.
3. **Distinctiveness self-check** — measure the draft against the codex (the
   distinctiveness-guard checks); revise any line drifting to generic LLM-voice or banned filler.
4. **Record avoided claims** — list in `flags` any claim the draft deliberately avoided
   (e.g. "did not claim #1 / best-in-class — no substantiation on file").

## Output
`kind: "activation"`. One `drafts[]` entry (`kind:"on-brand-content"`): `title`, `content`
(the on-brand draft, clearly a draft), `grounded_on` (the codex + the brief/source),
`flags` (claims deliberately avoided and the human-review reminder). `summary.headline` =
one line on what was drafted; `summary.ai_ready` = `null`. Standard CTA. No findings.

## Fix / safety patterns
- The draft is a proposal, never a publish — say so in the flags and the handback.
- If the brief would require a risky claim, draft around it and flag the gap rather than
  fabricate substantiation.
- Re-run the claims and distinctiveness checks on any human edit before publish.
