# 0005. CLI scripts with exit codes and explicit failure handling

**Status:** Accepted
**Date:** 2026-10-09

## Context
Each pipeline step will eventually run unattended under Airflow, which needs to know whether a step succeeded. When a step fails, whoever reads the logs needs to know why.

## Decision
- Each step is a command-line script, e.g. `python ingestion/fetch_companyfacts.py 320193`.
- Success exits with code 0. Any failure prints one clear line to **stderr** and exits with code 1.
- Input is validated before any network call: the CIK must be 1–10 digits, then it is zero-padded to 10. Validation comes first because `"apple".zfill(10)` silently returns `"00000apple"`.
- Every HTTP request has a timeout.

| Failure | Detected by | Message tells the user to |
|---|---|---|
| Invalid CIK | input validation | pass 1–10 digits |
| Missing User-Agent | empty `os.getenv` | set `SEC_USER_AGENT` |
| No network / timeout | `requests.RequestException` | retry |
| 403 | status code | check `SEC_USER_AGENT` |
| 404 | status code | check the CIK |
| Other non-200 | status code | report the unexpected status |

## Consequences
- Airflow (or any shell) can rely on the exit code.
- Errors are one readable line, not a traceback; tracebacks are reserved for actual bugs.
- 403 handling couldn't be triggered in testing (SEC accepted a placeholder User-Agent), so it is untested against the live API.
