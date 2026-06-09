# Logic layer — Codified Brand Builder (★ flagship, activation)

**Purpose.** From content/blog URLs (or the supplied corpus), build a machine-usable
**brand codex**: voice/tone, positioning, messaging pillars, approved/banned language,
and visual notes. Its JSON `codex` is consumed by the Distinctiveness Guard and the
On-Brand Content Drafter.

**Minimum inputs.** A handful of representative content/blog URLs or an uploaded content
corpus. More is better (Marketing usually has the most data — take what's offered).

## How to codify
Read across the corpus and extract, with evidence quotes where possible:
1. **Voice & tone** — person (we/you), register, sentence shape, signature metaphors,
   emoji policy. Capture 2–4 verbatim examples that exemplify the voice.
2. **Positioning** — the one-line "who we help + how + the payoff."
3. **Messaging pillars** — 3–6 recurring themes, each with a sentence and a sample line.
4. **Approved language** — words/phrases the brand owns (e.g. "harmonize", "summit",
   "with intention").
5. **Banned / off-voice language** — filler and LLM-mean drift to avoid (e.g.
   "leverage synergies", "in today's fast-paced landscape", "best-in-class" without proof).
6. **Visual notes** — colors, type, imagery tone if discernible from the brand.

Distinguish on-voice exemplars from off-voice samples in the corpus (the corpus may
contain both — flag the generic one as a negative example).

## Output
`kind: "activation"`. Put the structured codex in the top-level `codex` object (free-form
but stable keys: `voice`, `tone`, `positioning`, `pillars[]`, `approved_language[]`,
`banned_language[]`, `visual_notes`, `examples[]`). Also emit one `drafts[]` entry
(`kind:"brand-codex"`) with a human-readable rendering of the codex so the HTML shows it.
`summary.headline` = a one-line statement of the codified voice. Standard CTA. No findings.

Downstream: `readiness-output/marketing/mkt-brand-codex-builder.json` is the codex other
marketing tools load.
