# Most revisions are benign

## Observation
Apple has no error restatements, yet change detection finds **449** values that changed between filings. "A value changed" is not the same as "a restatement". Four benign types account for the noise found so far.

## Stock splits
After a split, every prior per-share value and share count is re-reported. Apple's diluted EPS for FY2012 went from $44.15 to $6.31, a ratio of 6.997, after the 2014 7-for-1 split.

- 111 of Apple's 449 changes are split-like, all filed right after the 2014 (7:1) and 2020 (4:1) splits.
- Detected by a whole-number old/new ratio on `shares` and `USD/shares` values ([ADR 0011](../adr/0011-stock-split-detection.md)); only 1 of Kraft Heinz's 817 changes matches.
- Apple also reports the ratio itself (`StockholdersEquityNoteStockSplitConversionRatio1`: 7 in 2014, 4 in 2020).

## Retrospective accounting changes
Apple's 10-K/A of 2010-01-25 changed 62 values across 32 concepts, median ~27%, after adopting new revenue-recognition rules for iPhone. Allowed by accounting standards, not an error, but numerically it looks like a large restatement ([ADR 0013](../adr/0013-accounting-changes-and-reclassifications.md)).

## Reclassifications
Kraft Heinz's most frequently changed concepts are "Other…" line items (`OtherOperatingActivitiesCashFlowStatement`, `OtherNonoperatingIncomeExpense`), which absorb amounts moved between lines.

## Rounding
Apple's FY2007 net income: $3,495M → $3,496M. Changes under 0.1%: 20 for Apple, 64 for Kraft Heinz ([ADR 0012](../adr/0012-rounding-threshold.md)).

## Why it matters
Without filtering, a detector would flag Apple's split filings as its biggest "restatements". Separating these types is the core problem the pipeline solves.
