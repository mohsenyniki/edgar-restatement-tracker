# 0014. Shared SEC client module with one small script per dataset

**Status:** Accepted
**Date:** 2026-10-10

## Context
Validating the detector against 8-K Item 4.02 filings needs a second SEC endpoint, `submissions/CIK##########.json`. Downloading it requires the same steps as `fetch_companyfacts.py` (validate the CIK, load the User-Agent, request with error handling, save raw JSON); only the URL and output folder differ.

## Decision
- Move the shared steps into `ingestion/sec_client.py` as functions: `normalize_cik`, `get_user_agent`, `fetch_json`, `save_json`.
- Keep one small entry-point script per dataset: `fetch_companyfacts.py` and a new `fetch_submissions.py`.
- Functions in the module **raise** exceptions; only the scripts print an error and exit with code 1. The module doesn't know whether it's called by a script, a notebook, a test or Airflow, so it shouldn't end the process itself.
- Two error types: `ValueError` for bad input (invalid CIK, missing User-Agent; retrying won't help) and a custom `SECError` for failures talking to SEC (network, 403, 404; a retry might help). Callers such as Airflow can treat them differently.

- The module stays **dataset-agnostic**. It can be extended with anything every SEC download benefits from (rate limiting, retries, pagination helpers), but nothing specific to one dataset: URLs, output folders and parsing (e.g. finding Item 4.02) live in the scripts and steps that use them.

## Consequences
- Request and error-handling logic exists once; a fix applies to every dataset.
- File names say what each script fetches, and each future Airflow task maps to one script.
- The functions can be unit-tested without running a script.

## Alternatives considered
- **Copy the script to `fetch_submissions.py`:** fastest, but duplicates ~50 lines that would drift apart.
- **One script with a `--dataset` argument (renamed `fetch_sec.py`):** no duplication, but one file doing several jobs, and the existing name would no longer fit.
