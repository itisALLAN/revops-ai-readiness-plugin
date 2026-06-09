# Logic layer — KB-Grounded Reply Drafter (★ flagship, activation)

**Purpose.** Given a customer question and the KB (article URLs or the supplied corpus),
draft a cited, grounded reply — and explicitly flag when the current KB cannot answer.
Doubles as live proof of the coverage gaps the Intent & Scope Mapper finds. **Assist
only — never sends.**

**Minimum inputs.** One customer question (text). KB source: article URLs to fetch, or
an uploaded KB export / the fixture corpus.

## How to draft
1. **Retrieve, don't invent.** Identify the KB article(s) that actually address the
   question. Quote/paraphrase only what those articles say. If nothing grounds a part of
   the question, say so — do not fill the gap from general knowledge.
2. **Cite every claim.** Each substantive sentence in the draft maps to a source article
   (title or URL). Put the sources in `grounded_on`.
3. **Flag the gaps.** For any part the KB can't answer, add a `flags` entry naming the
   missing coverage (e.g. "Current KB has no article on API rate limits — this part is
   unanswerable from the KB as it stands."). This is the proof-of-gap behavior.
4. **Stay in safe scope.** If the question is in a sensitive class (billing dispute,
   account security, legal/regulated), do **not** draft a resolving answer — draft a
   safe acknowledgement + escalation and flag it as out-of-scope for AI self-serve.
5. **Voice.** Helpful, plain, professional. No invented policy, no promises, no pricing.

## Output
`kind: "activation"`, one `drafts[]` entry: `kind: "kb-grounded-reply"`, `title` = short
question summary, `content` = the draft reply, `grounded_on` = cited articles,
`flags` = every gap and any out-of-scope routing. Add a `summary.headline` stating
whether the KB could fully ground the answer. Include the standard CTA. No `findings`.

## Severity / readiness signal
Set `summary.ai_ready` false when any part of the answer is ungrounded or the question is
out-of-scope; true only when the KB fully and safely grounds the whole reply.
