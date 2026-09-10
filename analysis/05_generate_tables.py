from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"outputs/tables/coverage_summary.csv"
if not src.exists():
    print("Run 03_coverage.py first.")
    raise SystemExit

rows=list(csv.DictReader(open(src,encoding="utf-8")))
tex=[]
tex.append(r"\begin{tabular}{lrrrrrr}")
tex.append(r"\toprule")
tex.append(r"Layer & P & S & N & Any & P(\%) & Any(\%) \\")
tex.append(r"\midrule")
for r in rows:
    tex.append(f'{r["layer_id"]} & {r["P"]} & {r["S"]} & {r["N"]} & {r["any_coverage"]} & {r["P_pct"]:.2f} & {r["any_pct"]:.2f} \\\\')
tex.append(r"\bottomrule")
tex.append(r"\end{tabular}")
(ROOT/"outputs/tables/coverage_summary.tex").write_text("\n".join(tex),encoding="utf-8")
print("Wrote LaTeX coverage table.")
