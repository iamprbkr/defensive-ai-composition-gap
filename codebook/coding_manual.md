# Coding Manual

## 1. Unit of analysis

The primary unit is one framework/instrument × one layer of the seven-layer
model. With 35 instruments and seven layers, the core matrix contains 245
decisions.

## 2. Seven layers

Use the layer definitions in the manuscript and keep their labels stable across
all coders and analysis scripts:

1. Infrastructure
2. Platform / supply chain
3. Data
4. Model
5. Orchestration / agent
6. Interface
7. Application / governance

If the manuscript's final terminology changes, update this manual and the
schema together before coding.

## 3. Coverage code

### P — Primary
Use when the layer is an explicit main subject of security controls,
assessment, attacks, mitigations, assurance, or equivalent guidance.

### S — Secondary
Use when the layer receives substantive security treatment but is not the
principal scope.

### N — None
Use when the instrument provides no substantive, layer-specific treatment.

## 4. Evidence rule

Every `P` or `S` decision must have a traceable source location, such as a page,
section, control identifier, table, or stable web heading.

Generic references to AI risk, security, lifecycle, trust, or governance do not
by themselves establish layer coverage.

## 5. Do not code effectiveness

Coverage is not effectiveness. A framework can receive `P` coverage even if the
paper finds no empirical evidence that its recommended control is effective.

## 6. Control-type coding

Where evidence permits, classify the relevant control as one or more of:

- Preventive
- Detective
- Corrective
- Governance
- Assurance / testing
- Monitoring
- Incident response
- Identity / authorization
- Data / provenance
- Supply chain
- Privacy

Leave blank when the source does not support a reliable classification.

## 7. Assurance-evidence coding

Record whether the instrument specifies or requires evidence such as:

- Test results
- Logs / audit trails
- Provenance / lineage
- SBOM or dependency inventory
- Model evaluation
- Red-team results
- Access-control records
- Incident records
- Monitoring evidence
- Deployment attestation

Do not infer evidence requirements that are not documented.

## 8. Confidence

Use:

- `H` — high confidence: explicit layer/control evidence.
- `M` — medium confidence: substantive but boundary interpretation is needed.
- `L` — low confidence: ambiguous evidence requiring adjudication.

Confidence is a coding aid, not a statistical confidence interval.

## 9. Independence

Two coders should code the same corpus independently before seeing each
other's classifications. Record coder identity in the raw files and keep
adjudication separate from initial decisions.

## 10. Agreement

For the three-category nominal outcome (`P`, `S`, `N`), calculate raw agreement
and Cohen's kappa. Report overall agreement and agreement by layer. Do not
report kappa until two complete independent coding files are available.

## 11. Adjudication

When coders disagree, preserve both original decisions and record the final
decision plus a concise rule-based reason in `coders/adjudication_log.csv`.

## 12. Sensitivity analysis

Run at least:

- Main analysis: all final classifications.
- Conservative analysis: retain only `P` classifications supported by high
  confidence.
- Expanded analysis: include `P` and `S` classifications with high/medium
  confidence.

The purpose is to test whether conclusions depend on ambiguous coding.

## 13. Reproducibility requirement

No percentage, count, agreement statistic, or manuscript table should be
manually typed into the final analysis. Generate it from the machine-readable
data.
