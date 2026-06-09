# Logic layer — Distinctiveness Guard (readiness)

**Purpose.** Use the **brand codex** as the yardstick to flag content drifting toward
generic LLM-voice / the mean. The risk an AI introduces: scaled content generation pulls a
distinctive brand toward bland, interchangeable filler. The guard measures each piece
against the codex's voice, signature elements, and banned language. **Assessment only — it
tells a human what to rewrite; it changes nothing.**

**Codex dependency.** This tool **loads the brand codex** at
`readiness-output/marketing/mkt-brand-codex-builder.json`. If it is absent, offer to run
`mkt-brand-codex-builder` first — the guard cannot measure drift without the yardstick.

**Minimum inputs.** The brand codex artifact, plus content/blog URLs (web-fetched) or an
uploaded corpus. The fixture `fixtures/marketing/content-corpus.md` contains one clearly
generic post ("Leveraging Synergies to Unlock Holistic Growth") that the guard must flag.

## Named checks (all measured against the loaded codex)
1. **GENERIC_LLM_VOICE** — a piece reads as interchangeable LLM filler: abstract,
   stakeholder-y, no point of view, no signature voice. Severity **high**. The
   "Leveraging Synergies to Unlock Holistic Growth" post is the canonical example and
   **must be flagged specifically**.
2. **MISSING_SIGNATURE_ELEMENTS** — the codex's signature elements are absent (e.g. the
   summit/climb metaphor, "we"→"you" address, a concrete deliverable). Severity **medium**.
3. **BANNED_FILLER_PRESENT** — phrases on the codex `banned_language` list appear
   verbatim ("leverage synergies", "in today's fast-paced landscape", "holistic,
   end-to-end", "robust, scalable" as filler). Severity **high**. Cite each.
4. **NO_CONCRETE_DELIVERABLE** — the codex requires every promise to land on a concrete
   deliverable; the piece stays purely aspirational. Severity **medium**.

## Definitions emitted
None — this tool does not touch the shared semantic layer.

## Fix patterns
- **Rewrite toward the codex voice:** replace banned filler with approved language, restore
  the signature metaphor and we→you address, and anchor every claim to a concrete
  deliverable. Show a before/after line where possible.
- Add the drifting piece to a watch-list for re-check after rewrite.
- Run this guard on every AI-assisted draft before publication, alongside the claims list.
