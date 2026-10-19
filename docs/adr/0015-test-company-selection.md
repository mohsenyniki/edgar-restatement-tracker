# 0015. Test set: verified restaters paired with matched controls

**Status:** Accepted
**Date:** 2026-10-19

## Context
The detector is validated on two companies (Kraft Heinz, Apple). Before scaling to hundreds, it needs a test set large enough to show the rules work beyond one example, with known answers: companies that restated and companies that didn't.

## Decision
**Restaters (~10):** companies with an 8-K Item 4.02 filed after 2009, verified in SEC's filing list (all pages), not taken from news reports alone. Picked to spread across industries.

**Controls:** one per restater, matched on:
1. **Industry:** same 4-digit SIC code; same 3-digit code if no match exists.
2. **Size:** revenue between 0.5× and 2× the restater's, in the fiscal year before its 4.02 (before any correction).
3. **Coverage:** companyfacts data for that year.
4. **Clean history:** no 8-K Item 4.02 since 2009.

Companies are identified by CIK, not name: names change (Viad → Pursuit Attractions & Hospitality), CIKs don't. Dates come from SEC filing dates, not announcement dates.

## Consequences
- Every candidate passes or fails on checkable facts; nothing is chosen by impression.
- Matched pairs mean a difference in what the detector flags comes from the restatement, not from industry reporting habits or company size.
- Most verified restaters are small companies, so this test set says little about the largest firms; the S&P 500 phase covers those.

## Alternatives considered
- **Controls from the S&P 500 only:** rejected after verification showed most restaters are small caps. A giant isn't a fair comparison for a company like Sypris Solutions.
- **Restaters from news reports alone:** fact-checking 17 candidates found 3 that couldn't be confirmed (an unidentifiable company, a name clash, a company no longer listed). Two Lucid- and Mirion-type cases were also excluded: the 2021 warrant restatements hit SPAC shells with almost no financial history.
