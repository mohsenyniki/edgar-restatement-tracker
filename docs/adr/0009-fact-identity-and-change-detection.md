# 0009. Fact identity and change detection across filings

**Status:** Accepted
**Date:** 2026-10-09

## Context
Each 10-K and 10-Q repeats earlier periods as comparatives, so the same value is reported several times. A revision is a value that differs between two of those reports. That requires defining when two rows describe "the same fact".

## Decision
- A fact is identified by `(taxonomy, concept, unit, start, end)`.
- A fact's reports are ordered by `filed`, with `accn` as a tiebreaker; each value is compared with the **previous** report's value (`groupby` + `shift(1)`).
- Any difference is a **candidate** revision. Deciding whether it's a restatement happens in later steps.

## Consequences
- `unit` is part of the key because one concept can be reported in several units (USD, shares).
- `fy` is **not** used: it's the fiscal year of the *filing*, not of the period (see [finding](../findings/fy-is-the-filing-year.md)).
- Comparing with the previous report attributes each change to the filing that made it.
- `accn` as tiebreaker keeps the order deterministic when two filings share a date.
- Instant facts have no `start`; grouping uses `dropna=False`, otherwise pandas silently drops them.
- `% change` is left empty when the old value is 0.
- Checked on both test companies: no filing reports two different values for the same fact, so no deduplication is needed yet.

## Alternatives considered
- **Compare each report with the first report:** loses which filing made the change when a value is revised more than once.
