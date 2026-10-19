# Most revisions are benign

## Observation
Apple has no error restatements in the period its XBRL data covers (filings from July 2009), yet change detection finds **449** values that changed between filings. (Apple's one Item 4.02, filed 2006-08-04 for its stock-option backdating restatement, predates that data.) "A value changed" is not the same as "a restatement". Five benign types account for the noise found so far.

## Stock splits
After a split, every prior per-share value and share count is re-reported. Apple's diluted EPS for FY2012 went from $44.15 to $6.31, a ratio of 6.997, after the 2014 7-for-1 split.

- 111 of Apple's 449 changes are split-like, all filed right after the 2014 (7:1) and 2020 (4:1) splits.
- Detected by a whole-number old/new ratio on `shares` and `USD/shares` values ([ADR 0011](../adr/0011-stock-split-detection.md)); only 1 of Kraft Heinz's 817 changes matches.
- Apple also reports the ratio itself (`StockholdersEquityNoteStockSplitConversionRatio1`: 7 in 2014, 4 in 2020).

## Retrospective accounting changes
Apple's 10-K/A of 2010-01-25 changed 62 values across 32 concepts, median ~27%, after adopting new revenue-recognition rules for iPhone. Allowed by accounting standards, not an error, but numerically it looks like a large restatement ([ADR 0013](../adr/0013-accounting-changes-and-reclassifications.md)).

## Reclassifications
Kraft Heinz's most frequently changed concepts are "Other…" line items (`OtherOperatingActivitiesCashFlowStatement`, `OtherNonoperatingIncomeExpense`), which absorb amounts moved between lines.

## Sign flips
Same amount, opposite sign: a tagging correction, not an economic change. Kraft Heinz's 10-Q/A of 2017-11-07 changed `ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill` from −$48M to +$48M. Easy to detect (`new == −old`).

Noise also rides along inside real restatements: of the 14 changes in that 10-Q/A pair, 12 are the actual cash-flow correction and 2 are clean-ups (this sign flip, and a balance-sheet value going from a rounded $53,500M to an exact $53,496M).

## Rounding
Apple's FY2007 net income: $3,495M → $3,496M. Changes under 0.1%: 20 for Apple, 64 for Kraft Heinz ([ADR 0012](../adr/0012-rounding-threshold.md)).

## Odd but real values
- **Negative revenue:** Plug Power reported 2020 revenue of **−$93M**. Warrants (rights to buy shares cheaply) given to customers such as Amazon and Walmart are recorded as a reduction of revenue, and in 2020 that reduction exceeded sales. Any logic that divides by revenue or assumes it's positive must handle this.
- **Companies disappear:** acquired companies stop filing (Pivotal Software's last filing: Feb 2020), so their history ends mid-way through windows the pipeline may need.

## Why it matters
Without filtering, a detector would flag Apple's split filings as its biggest "restatements". Separating these types is the core problem the pipeline solves.
