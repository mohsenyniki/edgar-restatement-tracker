# 0008. Prototype detection in pandas against a positive and a noise case

**Status:** Accepted
**Date:** 2026-10-09

## Context
Before this work it was unknown what restatements and benign revisions look like in companyfacts data. Designing dbt models from guesses would mean redesigning them later.

## Decision
- Prototype detection in a notebook ([`notebooks/01_restatement_prototype.ipynb`](../../notebooks/01_restatement_prototype.ipynb)), then port the validated logic to dbt.
- Validate against two companies:
  - **Kraft Heinz (CIK 1637459), the positive case:** a confirmed restatement (FY2016 net income $3,632M → $3,596M in the 10-K filed 2019-06-07). Detection must flag it; an `assert` in the notebook fails if it doesn't.
  - **Apple (CIK 320193), the noise case:** no error restatements, so its value changes show what benign revisions look like and should not be flagged.

## Consequences
- Rules are designed from evidence (see [findings](../findings/)).
- A detector is only useful if it flags real restatements *and* ignores noise; the pair tests both.
- Two companies is a small sample; rules must be re-validated on more companies.
