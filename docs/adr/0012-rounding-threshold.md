# 0012. Treat changes under 0.1% as rounding

**Status:** Proposed
**Date:** 2026-10-09

## Context
Some changes are rounding differences between filings, e.g. Apple FY2007 net income $3,495M → $3,496M.

## Decision
Label value changes with |% change| < 0.1% as rounding noise.

## Consequences
- Affects 20 Apple and 64 Kraft Heinz changes.
- The threshold is deliberately low: real restatements are also small per line. Kraft Heinz's FY2016 net income moved 0.99%, so a 1% threshold would have hidden it.
- The filing-level view (0010) is the safeguard: a small change inside a broad revision event is still visible.

## Alternatives considered
- **1% threshold:** removes far more noise (272 Kraft Heinz changes) but also hides the known restatement.
- **Absolute dollar threshold:** doesn't scale across company sizes.
