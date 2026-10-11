# 0013. Accounting-rule changes and reclassifications need more than values

**Status:** Open
**Date:** 2026-10-09

## Context
Two benign revision types can't be reliably separated from error corrections by the numbers alone:
- **Retrospective accounting changes:** Apple's 10-K/A of 2010-01-25 changed 62 values across 32 concepts (median ~27%) after adopting new revenue-recognition rules.
- **Reclassifications:** amounts moved between line items; Kraft Heinz's most-changed concepts are "Other…" lines.

## Options under consideration
- **8-K Item 4.02 labels:** a non-reliance filing marks a Big R error restatement. The SEC submissions API (`data.sec.gov/submissions/CIK##########.json`) lists the item numbers of every 8-K, giving ground-truth labels to validate against. Kraft Heinz filed one on 2019-05-06, a month before its restated 10-K.
- **Offsetting changes:** within one filing, reclassified amounts should roughly net to zero across related line items.
- **Filing text:** restatement and accounting-change disclosures have characteristic language.

## Next step
Fetch submissions data and test whether Item 4.02 filings line up with detected revision events across more companies.
