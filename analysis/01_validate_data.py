from pathlib import Path
import csv, sys

ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT/"data/corpus_manifest.csv"
coding = ROOT/"data/coding_matrix_adjudicated.csv"

errors = []
rows = list(csv.DictReader(open(manifest, encoding="utf-8")))
included = [r for r in rows if r.get("included","").upper()=="Y"]
ids = [r["framework_id"] for r in included]
if len(ids) != len(set(ids)): errors.append("Duplicate framework IDs.")
if len(included) != 35: errors.append(f"Expected 35 included instruments; found {len(included)}.")

if coding.exists():
    crows = list(csv.DictReader(open(coding, encoding="utf-8")))
    valid_layers = {f"L{i}" for i in range(1,8)}
    valid_codes = {"P","S","N"}
    for r in crows:
        if r["framework_id"] not in ids: errors.append("Coding contains unknown framework ID.")
        if r["layer_id"] not in valid_layers: errors.append("Invalid layer ID.")
        if r["coverage"] not in valid_codes: errors.append("Invalid coverage code.")
    if crows:
        expected = 35*7
        if len(crows) != expected:
            errors.append(f"Expected {expected} adjudicated decisions; found {len(crows)}.")

if errors:
    print("VALIDATION FAILED")
    print("\n".join("- "+e for e in errors))
    sys.exit(1)
print("VALIDATION PASSED")
