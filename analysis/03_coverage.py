from pathlib import Path
import csv
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"data/coding_matrix_adjudicated.csv"
rows=list(csv.DictReader(open(p,encoding="utf-8")))
if not rows:
    print("No adjudicated coding data yet.")
    raise SystemExit

out=[]
for layer in [f"L{i}" for i in range(1,8)]:
    r=[x for x in rows if x["layer_id"]==layer]
    c=Counter(x["coverage"] for x in r)
    n=len(r)
    out.append({
        "layer_id":layer,"P":c["P"],"S":c["S"],"N":c["N"],
        "any_coverage":c["P"]+c["S"],
        "P_pct":round(100*c["P"]/n,2) if n else 0,
        "any_pct":round(100*(c["P"]+c["S"])/n,2) if n else 0
    })
with open(ROOT/"outputs/tables/coverage_summary.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
print("Wrote coverage summary.")
