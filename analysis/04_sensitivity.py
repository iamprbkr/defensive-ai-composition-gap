from pathlib import Path
import csv
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"data/coding_matrix_adjudicated.csv"
rows=list(csv.DictReader(open(p,encoding="utf-8")))
if not rows:
    print("No adjudicated coding data yet.")
    raise SystemExit

def summarize(name, keep):
    rr=[r for r in rows if r["coverage"] in keep]
    counts=Counter(r["layer_id"] for r in rr)
    return {"analysis":name, **{f"L{i}":counts[f"L{i}"] for i in range(1,8)}}

# Conservative = Primary + High confidence only.
con=[r for r in rows if r["coverage"]=="P" and r["confidence"]=="H"]
expanded=[r for r in rows if r["coverage"] in {"P","S"} and r["confidence"] in {"H","M"}]
main=[r for r in rows if r["coverage"] in {"P","S"}]
results=[
    summarize("main", {"P","S"}),
    {"analysis":"conservative", **{f"L{i}":sum(r["layer_id"]==f"L{i}" for r in con) for i in range(1,8)}},
    {"analysis":"expanded", **{f"L{i}":sum(r["layer_id"]==f"L{i}" for r in expanded) for i in range(1,8)}},
]
with open(ROOT/"outputs/statistics/sensitivity.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=results[0].keys()); w.writeheader(); w.writerows(results)
print("Wrote sensitivity analysis.")
