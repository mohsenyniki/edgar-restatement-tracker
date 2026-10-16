# EDGAR Restatement Tracker

A daily pipeline that detects when US public companies revise financial numbers they already reported to the SEC, measures how much changed, and classifies each revision as an error or benign.

> **Status:** 🚧 Ingestion and a working detection prototype are done. Detection has been checked against SEC 8-K Item 4.02 filings for Kraft Heinz and Apple. Next: load into PostgreSQL and move the logic into dbt.

## Why
Every 10-Q and 10-K repeats figures from earlier periods. When those figures quietly change between filings, it can signal an accounting error, or just a benign change like a reclassification or stock split. This project tracks those changes using real SEC EDGAR data.

## How it works
1. **Ingest:** pull company financial data (companyfacts) and filing history (submissions) from SEC EDGAR
2. **Compare:** match each reported figure against earlier reports for the same period
3. **Flag & classify:** group changes by the filing that made them, then separate error restatements from benign revisions (splits, accounting changes, reclassifications, sign flips, rounding)
4. **Validate:** check flagged filings against 8-K Item 4.02 (non-reliance) filings, SEC's own record of material-error restatements
5. **Serve:** dashboard with a watchlist, company pages, and a restatement alerts feed *(planned)*

## What's built so far
| Piece | What it does |
|---|---|
| [`ingestion/sec_client.py`](ingestion/sec_client.py) | Shared SEC client: CIK validation, User-Agent from `.env`, JSON fetch with clear errors for 403/404/network failures, save to disk |
| [`ingestion/fetch_companyfacts.py`](ingestion/fetch_companyfacts.py) | Downloads a company's XBRL financial data to `data/raw/companyfacts/` |
| [`ingestion/fetch_submissions.py`](ingestion/fetch_submissions.py) | Downloads a company's full filing history to `data/raw/submissions/`, including the older pages SEC keeps outside the main file |
| [`ingestion/flatten_companyfacts.py`](ingestion/flatten_companyfacts.py) | Flattens nested companyfacts JSON into one row per reported value |
| [`notebooks/01_restatement_prototype.ipynb`](notebooks/01_restatement_prototype.ipynb) | Pandas prototype: change detection, filing-level revision events, stock-split detection, and validation against Item 4.02 filings |

## Key findings
From running the prototype on Kraft Heinz (a known restater) and Apple (a noise case). Full write-ups in [`docs/findings/`](docs/findings/).

- **Restatements are filing-level events.** Kraft Heinz's 817 changed values collapse into 44 filings; its 2019 restatement 10-K alone changed 519 values across 119 concepts, with a median change of only ~1.2%.
- **Restatements don't share one shape.** Kraft Heinz's 2017 cash-flow restatement changed just 14 values, with a median change of ~200%.
- **Most revisions are benign.** Apple has 449 changed values but no error restatements in its XBRL era. Stock splits alone account for 111 of them.
- **`fy` labels the filing, not the period.** Values are matched by `start`/`end` dates, never by `fy`/`fp`.
- **Item 4.02 is the answer key, but only where the data reaches.** Both of Kraft Heinz's 4.02 filings line up with detected revisions. Apple's 2006 4.02 predates its XBRL data, so the detector can't see it.

## Design decisions
Every technical choice is recorded as an Architecture Decision Record in [`docs/adr/`](docs/adr/) (14 so far), from ELT with dbt and an immutable raw layer to stock-split detection and the rounding threshold.

## Quickstart
Requires Python 3.

```bash
pip install -r requirements.txt
cp .env.example .env   # set SEC_USER_AGENT to your name and email (SEC requires it)

python ingestion/fetch_companyfacts.py 1637459    # Kraft Heinz
python ingestion/fetch_submissions.py 1637459
python ingestion/flatten_companyfacts.py 1637459
```

Then open the notebook in `notebooks/` to run the detection prototype. Raw data is saved under `data/raw/` and is not committed.

## Stack
Python · pandas · Airflow · dbt · PostgreSQL · AWS (kept to a few dollars/month)

## Repo layout
| Folder | Purpose |
|---|---|
| `ingestion/` | EDGAR data pulls |
| `airflow/` | DAGs for scheduling |
| `dbt/`, `warehouse/` | Models and warehouse setup |
| `dashboard/` | Front end |
| `infra/` | Infrastructure config |
| `notebooks/` | Data exploration and prototyping |
| `tests/` | Tests |
| `docs/` | Architecture decisions (`adr/`) and data findings (`findings/`) |

## Roadmap
- [x] Repo structure
- [x] EDGAR ingestion (companyfacts and submissions)
- [x] Restatement detection prototype (pandas)
- [x] Validation against 8-K Item 4.02 filings (Kraft Heinz, Apple)
- [ ] Load raw data into PostgreSQL
- [ ] Detection and classification models in dbt
- [ ] Error vs. benign classification (accounting changes, reclassifications)
- [ ] Validation against Item 4.02 at scale
- [ ] Scheduled Airflow runs
- [ ] Dashboard
