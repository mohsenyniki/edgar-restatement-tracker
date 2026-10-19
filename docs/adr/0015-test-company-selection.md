# 0015. Test set: verified restaters paired with matched controls

**Status:** Accepted
**Date:** 2026-10-19

## Context
The detector is validated on two companies (Kraft Heinz, Apple). Before scaling to hundreds, it needs a test set large enough to show the rules work beyond one example, with known answers: companies that restated and companies that didn't.

## Decision
**Restaters (~10):** companies with an 8-K Item 4.02 filed after 2009, verified in SEC's filing list (all pages), not taken from news reports alone. Picked to spread across industries.

**Controls:** one per restater, matched on:
1. **Industry:** same 4-digit SIC code; if no candidate passes the other rules, widen to the 3-digit group, then the 2-digit group. Large restaters need the wider groups: no company in Kraft Heinz's SIC 2030 was within 0.5×–2× of its $26.3B revenue, while the 2-digit food group (20xx) had five.
2. **Size:** revenue between 0.5× and 2× the restater's, in the fiscal year before its 4.02 (before any correction).
3. **Coverage:** companyfacts data for that year.
4. **Clean history:** no 8-K Item 4.02 since 2009.
5. **Still filing:** the control's last SEC filing is at least 12 months after the restater's 4.02, so it covers the window in which the detector looks for corrections. (First run matched Guidewire to Pivotal Software, which was acquired and stopped filing nine months after Guidewire's 4.02.)

**Size year:** the fiscal year before the 4.02. If the restater's revenue that year is missing, zero or negative, use the year before. (Plug Power reported revenue of −$93M for 2020: warrants given to customers are recorded as a reduction of revenue, and that year they exceeded sales.)

Companies are identified by CIK, not name: names change (Viad → Pursuit Attractions & Hospitality), CIKs don't. Dates come from SEC filing dates, not announcement dates.

## Consequences
- Every candidate passes or fails on checkable facts; nothing is chosen by impression.
- Matched pairs mean a difference in what the detector flags comes from the restatement, not from industry reporting habits or company size.
- Most verified restaters are small companies, so this test set says little about the largest firms; the S&P 500 phase covers those.

- **Example:** Kraft Heinz (SIC 2030) is matched to Mondelez (SIC 2000): same food group, 2018 revenue $25.9B vs $26.3B (0.99×), no Item 4.02 ever. Among size-matched candidates the closest ratio is chosen.
- SEC's search-by-industry page returns at most 100 companies per request, so the selection code must request further pages when a result is full.
- **Candidate revenue comes from SEC's `frames` API** (one request per revenue tag returns every company's value for a calendar year) rather than each candidate's full companyfacts file. Kraft Heinz's search dropped from ~7 minutes to ~45 seconds with the same result. Trade-off: frames are calendar-year aligned (`CY2018`), while the restater's own revenue uses its fiscal year; close enough for a 0.5×–2× size band.

## Alternatives considered
- **Controls from the S&P 500 only:** rejected after verification showed most restaters are small caps. A giant isn't a fair comparison for a company like Sypris Solutions.
- **Restaters from news reports alone:** fact-checking 17 candidates found 3 that couldn't be confirmed (an unidentifiable company, a name clash, a company no longer listed). Two Lucid- and Mirion-type cases were also excluded: the 2021 warrant restatements hit SPAC shells with almost no financial history.
