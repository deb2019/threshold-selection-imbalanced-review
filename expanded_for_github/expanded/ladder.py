"""Guarantee ladder: empirical quantile -> expected-FNR control (CRC) -> high-probability control.
Uses only saved calibration/test scores (no refitting)."""
import sys
import numpy as np
import pandas as pd
sys.path.insert(0, '.')
from common import load_all, emp_threshold, os_threshold, crc_threshold, evaluate, OFFICIAL, ORDER

OUT = 'new_results/'
rows = []
S = load_all()
for (name, seed, model), g in S.groupby(['dataset', 'seed', 'model']):
    c = g[g.split == 'cal']; t = g[g.split == 'test']
    fault = np.sort(c.loc[c.label == 1, 'score'].to_numpy())
    s = t.score.to_numpy(); y = t.label.to_numpy()
    for r in (0.8, 0.9):
        tag = int(100 * r)
        rules = {f'Emp{tag}': emp_threshold(fault, r), f'CRC{tag}': crc_threshold(fault, r),
                 f'R{tag}': os_threshold(fault, r, 0.05)}
        for rule, th in rules.items():
            e = evaluate(s, y, th)
            rows.append(dict(dataset=name, seed=seed, model=model, target=r, rule=rule,
                             level=rule[:-2], m=len(fault), fallback=bool(np.isinf(th)), **e))
d = pd.DataFrame(rows)
d['hit'] = d.recall >= d.target
d['cap5'] = d.N // 20
d['joint'] = d.hit & (d.alerts <= d.cap5)
d.to_csv(OUT + 'ladder_rows.csv', index=False)

# Official Scania split
orow = []
o = pd.read_csv(OFFICIAL, float_precision='round_trip')
for model, g in o.groupby('model'):
    c = g[g.split == 'cal']; t = g[g.split == 'test']
    fault = np.sort(c.loc[c.label == 1, 'score'].to_numpy())
    for r in (0.8, 0.9):
        tag = int(100 * r)
        for rule, th in {f'Emp{tag}': emp_threshold(fault, r), f'CRC{tag}': crc_threshold(fault, r),
                         f'R{tag}': os_threshold(fault, r)}.items():
            orow.append(dict(model=model, rule=rule, m=len(fault), threshold=th,
                             **evaluate(t.score.to_numpy(), t.label.to_numpy(), th)))
od = pd.DataFrame(orow)
od.to_csv(OUT + 'ladder_official.csv', index=False)

pd.set_option('display.width', 220)
for mdl in ('RF', 'LR'):
    q = d[(d.model == mdl) & (d.target == 0.8)]
    summ = q.groupby(['dataset', 'level']).agg(rec=('recall', 'median'), wl=('workload', 'median'),
                                               hit=('hit', 'sum'), joint=('joint', 'sum'),
                                               fb=('fallback', 'sum'), m=('m', 'median'))
    print(f'\n=== {mdl}, 80% target ===')
    print(summ.unstack('level').loc[ORDER].round(3).to_string())
    q9 = d[(d.model == mdl) & (d.target == 0.9)]
    s9 = q9.groupby(['dataset', 'level']).agg(rec=('recall', 'median'), wl=('workload', 'median'), hit=('hit', 'sum'), fb=('fallback', 'sum'))
    print(f'--- {mdl}, 90% target ---')
    print(s9.unstack('level').loc[ORDER].round(3).to_string())
# within-split extra workload
w = d[(d.model == 'RF') & (d.target == 0.8)].pivot_table(index=['dataset', 'seed'], columns='level', values='workload')
print('\nRF median within-split extra inspections per 1000:')
print(pd.DataFrame({'CRC-Emp': (w.CRC - w.Emp).groupby('dataset').median(),
                    'R-CRC': (w.R - w.CRC).groupby('dataset').median()}).loc[ORDER].round(1))
print('\nOfficial:'); print(od.round(4).to_string(index=False))
