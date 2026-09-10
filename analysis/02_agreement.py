from pathlib import Path
import csv, math

ROOT = Path(__file__).resolve().parents[1]
a = list(csv.DictReader(open(ROOT/"coders/coder_A.csv", encoding="utf-8")))
b = list(csv.DictReader(open(ROOT/"coders/coder_B.csv", encoding="utf-8")))

def key(r): return (r["framework_id"], r["layer_id"])
A={key(r):r["coverage"] for r in a if r["coverage"]}
B={key(r):r["coverage"] for r in b if r["coverage"]}
keys=sorted(set(A)&set(B))
if not keys:
    print("No overlapping completed coder decisions yet; agreement not computed.")
    raise SystemExit

labels=["P","S","N"]
agree=sum(A[k]==B[k] for k in keys)
po=agree/len(keys)
pe=sum((sum(A[k]==x for k in keys)/len(keys))*(sum(B[k]==x for k in keys)/len(keys)) for x in labels)
kappa=(po-pe)/(1-pe) if (1-pe) else float("nan")

out=ROOT/"outputs/statistics/agreement.txt"
out.write_text(
    f"Decisions compared: {len(keys)}\nRaw agreement: {po:.4f}\nCohen kappa: {kappa:.4f}\n",
    encoding="utf-8")
print(out.read_text())
