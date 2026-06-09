# Logic layer — KB Retrieval Readiness (readiness)

**Purpose.** Review a knowledge base article-by-article and flag the articles an AI
agent cannot safely ground on. Each finding names the article and prescribes a concrete
split, fix, or retire action. Pairs with the Intent & Scope Mapper (which finds *missing*
coverage); this tool grades the *quality* of what exists for retrieval. **Diagnoses only.**

**Minimum inputs.** A KB source: article URLs to fetch, an uploaded KB export, or the
fixture corpus `fixtures/customer-success/kb-articles.md`. Per article, the tool needs
title, last-updated date, and body text.

## Named checks
Run each check against every article. One finding per article that fails one or more checks.

1. **Multi-topic sprawl.** Triggers when a single article spans 3+ unrelated topics or
   exceeds ~1,500 words covering distinct intents. An AI retriever returns the whole page
   and cannot isolate the answer. **Severity: high** (critical if the page is the only
   source for several intents).
2. **Staleness.** Triggers when `last_updated` is older than ~18 months, or the body
   references an outdated artifact (old package/API version, deprecated UI). The AI grounds
   on facts that are no longer true. **Severity: high** when it asserts a stale fact (e.g. a
   version number); medium when merely old but still accurate.
3. **Dangling reference.** Triggers when the body cross-references an article, section, or
   anchor that does not exist in the corpus. The AI follows a broken pointer and either
   hallucinates the target or returns an incomplete answer. **Severity: high.**
4. **Bad chunking / structure.** Triggers when an article lacks headings, mixes prose and
   steps without structure, or buries the answer such that a chunker would split mid-thought.
   Retrieval returns a fragment that doesn't stand alone. **Severity: medium.**

A clean, single-topic, current, well-structured article produces **no finding** and is
noted as a good grounding source in the narrative.

## Definitions it may emit
None required. Emit a `definitions[]` entry only if an article defines a shared business
term (e.g. "customer", "churn") that downstream teams reuse.

## Fix patterns
- **Split** a sprawl page into one single-topic article per intent; link them, don't nest.
- **Refresh** a stale article: correct the version/fact, update `last_updated`, or retire
  if the feature is gone.
- **Repair** a dangling reference: create the missing target article, or remove the
  cross-reference and inline the needed steps.
- **Restructure** for chunking: add H2/H3 headings per sub-topic, lead with the answer,
  keep each section self-contained.
- **Retire** any article that is both stale and superseded — leaving it invites the AI to
  ground on dead content.

## Severity / readiness signal
Set `summary.ai_ready` false when any high-severity finding exists (sprawl, stale fact, or
dangling reference) — the KB is not safe to ground on as-is. true only when every article
passes all four checks.
