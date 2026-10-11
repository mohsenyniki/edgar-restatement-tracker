# 0001. ELT: load raw data, transform in dbt

**Status:** Accepted
**Date:** 2026-10-09

## Context
The pipeline extracts SEC filings data, stores it, and applies restatement-detection logic that will change often as we learn what real restatements look like.

## Decision
Use ELT. Python extracts raw data and loads it into Postgres with minimal reshaping; all business logic (cleaning, change detection, classification) lives in dbt SQL models.

## Consequences
- Logic is versioned, testable with dbt tests, and visible as lineage.
- Raw data stays in the warehouse, so a logic change is a re-run of dbt, not a re-extract from SEC.
- Python code stays small: fetch, flatten, load.

## Alternatives considered
- **ETL (transform in Python before loading):** logic gets buried in scripts, and every logic change means re-running extraction.
