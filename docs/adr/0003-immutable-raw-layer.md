# 0003. Keep raw responses untouched; local disk first, S3 later

**Status:** Accepted
**Date:** 2026-10-09

## Context
Downstream logic (flattening, detection) will have bugs and will change. Re-downloading from SEC every time is slow and subject to rate limits.

## Decision
- The fetch step writes the API response unmodified to `data/raw/companyfacts/CIK##########.json`.
- During development, raw files live on local disk (gitignored). When the pipeline runs on AWS, `STORAGE_BACKEND=s3` switches the same layout to S3 keys (`raw/companyfacts/CIK....json`).

## Consequences
- The raw layer is the source of truth and an audit trail of exactly what SEC returned; everything downstream can be rebuilt from it.
- No cloud cost or setup while the data shape is still being explored.
- Switching to S3 only touches the save function; the path layout and downstream steps stay the same.

## Alternatives considered
- **Saving only cleaned data:** a bug in cleaning would require re-fetching, and the original response would be lost.
- **S3 from day one:** adds AWS setup and cost before it's needed.
