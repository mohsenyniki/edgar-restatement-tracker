# 0011. Detect stock splits by whole-number ratio

**Status:** Accepted
**Date:** 2026-10-09

## Context
After a stock split, companies re-report every prior period's per-share values and share counts. These changes are large (75–86% for Apple) and would dominate any "biggest change" ranking, but they aren't errors.

## Decision
Flag a change as split-like when:
- the unit is `shares` or `USD/shares`, and
- the ratio between the larger and smaller absolute value is a whole number ≥ 2, within ±0.05.

## Consequences
- Flags 111 of Apple's 449 changes, all filed right after its 2014 (7-for-1) and 2020 (4-for-1) splits; flags only 1 of Kraft Heinz's 817.
- The ±0.05 tolerance absorbs per-share rounding (e.g. $44.15 → $6.31 is 6.997×).
- May miss reverse splits with unusual ratios, or catch a coincidental 2× change in a share count.

## Alternatives considered
- **Use the company's reported split ratio** (`StockholdersEquityNoteStockSplitConversionRatio1`, which Apple reports as 7 in 2014 and 4 in 2020): more exact, but not every company tags it. A good cross-check for a later version.
