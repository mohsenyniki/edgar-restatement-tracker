# 0002. SEC companyfacts API as the data source

**Status:** Accepted
**Date:** 2026-10-09

## Context
Detecting restatements requires seeing the same financial value as it was reported in *different* filings over time.

## Decision
Use `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`.

## Consequences
- One request returns every XBRL fact a company has reported, and each value carries the filing it came from (`accn`, `form`, `filed`). That filing-level history is exactly what change detection needs.
- One file per company (Apple ≈ 4 MB), so fetching many companies is many requests; SEC's fair-access limit is 10 requests/second.

## Alternatives considered
- **Parsing full XBRL filings:** complete, but far heavier to download and parse.
- **`frames` API:** one value per period across companies, but only the latest value, so revisions are invisible.
