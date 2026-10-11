# 0006. Flatten nested JSON in Python before loading

**Status:** Accepted
**Date:** 2026-10-09

## Context
A companyfacts file is nested four levels deep: taxonomy → concept → unit → list of reported values. Change detection needs a flat table with one row per reported value.

## Decision
`ingestion/flatten_companyfacts.py` walks the nesting and emits one row per value, carrying the parent keys (`taxonomy`, `concept`, `unit`) as columns and parsing `start`, `end` and `filed` as dates. No business logic is added.

The flattened table is not saved as a file; it is rebuilt from raw JSON when needed (about a second) and will be persisted when loaded into Postgres.

## Consequences
- Reshaping happens in readable Python instead of nested Postgres `JSONB` functions.
- This is a deliberate, limited exception to ELT (0001): structure changes only, no logic.
- `start` is empty for instant facts such as balance-sheet values; that is expected, not a parsing error.

## Alternatives considered
- **Load raw JSON into a `JSONB` column and flatten in dbt:** purer ELT, but unnesting four levels in SQL is hard to read. Possible later if the warehouse should hold the exact payload.
- **Persist an intermediate Parquet file:** standard in data-lake stacks (Spark, Athena), redundant when Postgres is the warehouse.
