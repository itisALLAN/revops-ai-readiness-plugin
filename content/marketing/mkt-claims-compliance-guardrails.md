# Logic layer — Claims & Compliance Guardrails (readiness)

**Purpose.** Scan published marketing content for risky claims **already live** —
unsubstantiated superlatives, comparative claims, and pricing/guarantee promises — before
an AI is allowed to repurpose or generate copy that would amplify them. Produce a
**substantiation standard**, a **banned-claims list**, and a **human review path**.
**Assessment and guidance only — it changes nothing, sends nothing, and is not legal advice.**

**Minimum inputs.** A handful of representative content/blog URLs (web-fetched) or an
uploaded content corpus. Each finding must cite the offending line verbatim. The fixture
`fixtures/marketing/content-corpus.md` contains one deliberately risky post ("The
Best-in-Class AI Platform for Revenue Teams") that trips every check.

## Named checks
1. **UNSUBSTANTIATED_SUPERLATIVE** — absolute superlatives with no cited proof:
   "best-in-class", "industry-leading", "#1", "the best", "never fails". Severity
   **high**. An AI trained on or repurposing this content will replicate unprovable
   claims at scale. Cite each phrase.
2. **COMPARATIVE_CLAIM** — claims positioning against competitors without substantiation:
   "unlike every competitor", "better than X", "outperforms all others". Severity
   **high**. Comparative advertising carries the highest substantiation burden.
3. **PRICING_GUARANTEE_PROMISE** — outcome guarantees or money-back/pricing promises:
   "guaranteed to double your pipeline", "or your money back", "30 days". Severity
   **critical**. An AI that echoes a guarantee creates contractual and regulatory exposure.
4. **NO_REVIEW_PATH** — there is no documented review/approval gate or substantiation file
   any claim must clear before publication. Severity **high**. Without a review path, an
   AI draft can reach market unchecked.

## Definitions emitted
None — this tool does not touch the shared semantic layer.

## Fix patterns
- **Substantiation standard:** every comparative or superlative claim must link to a
  dated, sourced proof artifact (benchmark, customer data, third-party study) on file
  before it may appear in any draft, human- or AI-authored.
- **Banned-claims list:** maintain an explicit deny-list ("best-in-class" without proof,
  "#1", "industry-leading", "guaranteed", "money back", "unlike every competitor") that
  the On-Brand Content Drafter and any AI step check against pre-publication.
- **Review path:** route every AI-assisted draft through a named human reviewer (Marketing
  Ops + Legal/Compliance sign-off for any guarantee, pricing, or comparative claim) before
  publish. Log the approval.
- Always label compliance output **guidance, not legal advice**; recommend counsel review
  for any guarantee or comparative claim.
