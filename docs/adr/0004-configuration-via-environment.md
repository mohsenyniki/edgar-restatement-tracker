# 0004. Configuration through environment variables

**Status:** Accepted
**Date:** 2026-10-09

## Context
SEC requires a User-Agent with a name and contact email. Later the pipeline will need database credentials and AWS settings. None of these belong in the code or the repo.

## Decision
Read settings with `os.getenv`. Locally, `python-dotenv` loads them from `.env` (gitignored); `.env.example` documents every variable.

## Consequences
- No secrets or personal details in git.
- In production (Airflow, AWS) the same code reads real environment variables; `load_dotenv()` finds no file and does nothing.
- Missing settings are checked at startup and fail with a clear message before any request is made.

## Alternatives considered
- **Hardcoding:** leaks personal info and secrets into git history.
- **A config file in the repo:** same problem for secrets; environment variables are the standard for containerized jobs.
