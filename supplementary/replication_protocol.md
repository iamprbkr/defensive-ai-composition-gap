# Replication Protocol

## Objective
Reproduce the seven-layer coverage analysis, cross-framework composition
analysis, incident mapping, and 13-point audit construction.

## Corpus
Freeze exactly 35 instruments using `data/corpus_manifest.csv`. Each included
instrument must have a stable bibliographic identity and documented inclusion
reason.

## Coding
Two independent coders each complete all 245 framework-layer decisions.
Every non-`N` decision must have source evidence. Ambiguous decisions receive
a confidence code and notes.

## Agreement
Compute:
- total decisions
- raw agreement
- Cohen's kappa
- per-layer agreement
- confusion matrix

## Adjudication
Resolve disagreements using the coding manual and preserve the original coder
values. The final analysis uses adjudicated values.

## Sensitivity
Compare the main, conservative, and expanded analyses defined in the coding
manual.

## Table generation
All manuscript counts and percentages must be generated from the final data.

## Release
Tag the exact repository commit used for submission and archive the release
with a DOI. Record software version and execution date.
