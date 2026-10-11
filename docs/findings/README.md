# Findings

Things discovered by exploring real SEC data that shaped how the pipeline works.
Evidence and code: [`notebooks/01_restatement_prototype.ipynb`](../../notebooks/01_restatement_prototype.ipynb).

| Finding | Why it matters |
|---|---|
| [`fy` labels the filing, not the period](fy-is-the-filing-year.md) | Using it to match periods would compare the wrong numbers |
| [Restatements are filing-level events](restatements-are-filing-level-events.md) | One restatement changes hundreds of values at once; detection should judge filings |
| [Most revisions are benign](benign-revisions.md) | Stock splits, accounting-rule changes, reclassifications and rounding all look like restatements |
