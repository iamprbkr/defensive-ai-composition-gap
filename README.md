# AI Composition Gap — Reproducibility Package

This repository contains the reproducibility infrastructure for the study of
AI-security frameworks across a seven-layer AI stack and the analysis of
cross-layer composition gaps.

## What this package contains

- A versioned 35-instrument corpus manifest.
- A formal coding manual for seven-layer coverage.
- Machine-readable coding schemas.
- An evidence matrix linking every classification to a source location.
- Independent-coder templates and an adjudication log.
- Analysis scripts for coverage, inter-coder agreement, sensitivity analysis,
  and manuscript-table generation.
- Incident-to-boundary mapping.
- A machine-readable specification of the 13-point audit.
- The manuscript source used for the current paper version.

## Important status note

The repository is intentionally structured so that the empirical coding can be
completed and independently reproduced. The coder files are templates until
actual independent coding is performed. No inter-rater agreement statistic
should be reported until two independent completed coding files exist.

The 35 instruments are treated as a purposive corpus rather than a probability
sample of all AI-security frameworks. Coverage labels describe documented
scope, not control effectiveness.

## Reproduction workflow

1. Freeze the corpus in `data/corpus_manifest.csv`.
2. Complete `codebook/coding_manual.md` review before coding.
3. Independently code all 35 × 7 = 245 framework-layer decisions.
4. Record source evidence for each decision in `data/evidence_matrix.csv`.
5. Export coder A and coder B decisions to:
   - `coders/coder_A.csv`
   - `coders/coder_B.csv`
6. Resolve disagreements in `coders/adjudication_log.csv`.
7. Run:
   - `python analysis/01_validate_data.py`
   - `python analysis/02_agreement.py`
   - `python analysis/03_coverage.py`
   - `python analysis/04_sensitivity.py`
   - `python analysis/05_generate_tables.py`
8. Regenerate the manuscript tables/statistics from the resulting outputs.
9. Tag a release and archive the release with a DOI (for example, Zenodo).

## Coding categories

- `P` = Primary: the layer is an explicit main subject of the instrument's
  security control, assessment, attack, mitigation, assurance, or equivalent
  guidance.
- `S` = Secondary: the layer receives substantive treatment but is not the
  principal scope.
- `N` = None: no substantive layer-specific control or guidance is documented.

Do not infer layer coverage merely because an instrument mentions "AI risk",
"lifecycle", "security", or "governance" in generic terms.

## Data provenance

For each instrument, preserve issuer, exact title, version/revision, release
date, access date, canonical URL or DOI, and (where lawful and feasible) a
revision/snapshot identifier or cryptographic hash.

Do not redistribute copyrighted standards in full. Store bibliographic metadata,
source locations, and short evidence excerpts only where legally permissible.

## Research integrity

This package does not attempt to optimize for or evade AI/plagiarism detectors.
The goal is transparent provenance, independently checkable coding, original
analysis, and proper attribution.
