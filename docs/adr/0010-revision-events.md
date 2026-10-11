# 0010. Judge filings (revision events), not single values

**Status:** Accepted
**Date:** 2026-10-09

## Context
Change detection (0009) returns hundreds of candidate changes per company (Kraft Heinz 817, Apple 449). Looked at one by one, a real restatement line can look like rounding: Kraft Heinz's FY2016 net income moved only 0.99%.

## Decision
Group changes by the filing that made them (`accn`) and describe each filing: number of changed values, number of distinct concepts, and median absolute % change. Classification will happen at this filing level.

## Consequences
- Kraft Heinz's 817 changes collapse into 44 filings; the restatement 10-K alone holds 519 of them across 119 concepts, with a median change of ~1.2%.
- Error restatements and benign events have different shapes: **broad and small** (many line items, each moved a little) vs. fewer values moved by a lot (Apple's 2010 accounting change: median ~27%; splits: 75–86%). See [findings](../findings/restatements-are-filing-level-events.md).

## Alternatives considered
- **Classify each changed value on its own:** loses the context that makes a small change meaningful.
