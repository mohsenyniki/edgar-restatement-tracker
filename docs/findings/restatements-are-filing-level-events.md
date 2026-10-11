# Restatements are filing-level events

## Observation
Change detection found 817 candidate revisions for Kraft Heinz. Grouped by the filing that made them, they collapse into 44 filings, and one filing dominates:

| Filing | Filed | Changed values | Concepts | Median change |
|---|---|---|---|---|
| 10-K (FY2018) | 2019-06-07 | **519** | **119** | **~1.2%** |
| 10-K (FY2017) | 2018-02-16 | 27 | 18 | ~27% |
| 10-Q | 2016-08-05 | 20 | 15 | ~9% |

A correction ripples through every line it touches (cost of sales → gross profit → operating income → net income, across several years), so an error restatement is **broad** (many concepts) and **small** (each value moves a little). FY2016 net income moved only 0.99%: as a single number it looks like noise, but in context it's part of the largest revision event in the company's history.

## Confirmed as a "Big R" restatement
SEC's filing index (`data.sec.gov/submissions/CIK0001637459.json`) shows the sequence:

| Date | Filing | Meaning |
|---|---|---|
| 2019-02-28 | NT 10-K | annual report will be late |
| 2019-03-15 | 8-K Item 3.01 | exchange notice about the late filing |
| 2019-05-06 | 8-K Item 4.02 | non-reliance: previously issued financials can't be relied on |
| 2019-06-07 | 10-K | restated figures, the 519-change event above |

An 8-K Item 4.02 is filed only for material errors, which makes it a ground-truth label for "Big R" restatements.

## Impact on the design
- Classification works at the filing level ([ADR 0010](../adr/0010-revision-events.md)).
- Item 4.02 filings are a candidate source of labels for validating the detector at scale ([ADR 0013](../adr/0013-accounting-changes-and-reclassifications.md)).

## Open questions
- Kraft Heinz filed another Item 4.02 on 2017-11-06; not yet examined.
- The FY2017 10-K (27 changes, median ~27%) is unexplained.
