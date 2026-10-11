# `fy` labels the filing, not the period

## What I expected
Each companyfacts value has an `fy` (fiscal year) field. I expected it to say which fiscal year the value describes.

## What the data shows
`fy` is the fiscal year of the **filing** the value appeared in. Kraft Heinz's FY2016 net income appears in three 10-Ks, each time with a different `fy`:

| Period (`start` – `end`) | `val` | `fy` | Filed |
|---|---|---|---|
| 2016-01-04 – 2016-12-31 | $3,632M | 2016 | 2017-02-23 |
| 2016-01-04 – 2016-12-31 | $3,632M | 2017 | 2018-02-16 |
| 2016-01-04 – 2016-12-31 | $3,596M | 2018 | 2019-06-07 |

Same period, three `fy` values, because each 10-K repeats prior years as comparatives.

## How I handled it
The period a value describes is identified only by `start` and `end` (just `end` for balance-sheet values). `fy` and `fp` are never used to match values across filings ([ADR 0009](../adr/0009-fact-identity-and-change-detection.md)).

## Why it matters
Grouping by `fy` would treat the FY2016 figure in the FY2018 10-K as an FY2018 value and compare it with the wrong numbers, both hiding real revisions and inventing fake ones.
