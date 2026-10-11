# Architecture Decision Records

Each file records one technical decision: the context, what was decided, and what it costs.
Records are numbered in the order they were made and are not rewritten later; a changed decision gets a new record that supersedes the old one.

| # | Decision | Status |
|---|---|---|
| [0001](0001-elt-with-dbt.md) | ELT: load raw data, transform in dbt | Accepted |
| [0002](0002-companyfacts-api-as-source.md) | SEC companyfacts API as the data source | Accepted |
| [0003](0003-immutable-raw-layer.md) | Keep raw responses untouched; local disk first, S3 later | Accepted |
| [0004](0004-configuration-via-environment.md) | Configuration through environment variables | Accepted |
| [0005](0005-cli-scripts-and-failure-handling.md) | CLI scripts with exit codes and explicit failure handling | Accepted |
| [0006](0006-flatten-in-python-before-load.md) | Flatten nested JSON in Python before loading | Accepted |
| [0007](0007-pinned-runtime-dependencies.md) | Pin runtime dependencies, keep dev tools out | Accepted |
| [0008](0008-prototype-in-pandas-first.md) | Prototype detection in pandas against a positive and a noise case | Accepted |
| [0009](0009-fact-identity-and-change-detection.md) | Fact identity and change detection across filings | Accepted |
| [0010](0010-revision-events.md) | Judge filings (revision events), not single values | Accepted |
| [0011](0011-stock-split-detection.md) | Detect stock splits by whole-number ratio | Accepted |
| [0012](0012-rounding-threshold.md) | Treat changes under 0.1% as rounding | Proposed |
| [0013](0013-accounting-changes-and-reclassifications.md) | Accounting-rule changes and reclassifications need more than values | Open |

## Template

```markdown
# NNNN. Title

**Status:** Proposed | Accepted | Superseded by NNNN
**Date:** YYYY-MM-DD

## Context
What problem or constraint forced a decision.

## Decision
What we chose.

## Consequences
What gets easier, what gets harder, what we gave up.

## Alternatives considered
- Option: why not.
```
