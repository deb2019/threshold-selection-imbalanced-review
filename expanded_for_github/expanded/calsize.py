"""How many labelled calibration faults make a recall guarantee affordable?
(a) Official Scania split: subsample the 250 calibration faults without replacement
    and evaluate each rule on the fixed official test set (16,000 records, 375 faults).
(b) Confidence sensitivity: delta in {0.10, 0.05, 0.01} on repeated splits and official split.
Only saved scores are used."""
import sys
import numpy as np
import pandas as pd
sys.path.insert(0, '.')
from common import load_all, emp_threshold, os_threshold, crc_threshold, evaluate, OFFICIAL, ORDER

OUT = 'new_results/'
rng = np.random.default_rng(2026)
B = 500
SIZES = [10, 14, 20, 30, 50, 75, 100, 150, 200, 250]

o = pd.read_csv(OFFICIAL, float_precision='round_trip')
rows = []
for model, g in o.groupby('model'):
    c = g[g.split == 'cal']; t = g[g.split == 'test']
    allf = c.loc[c.label == 1, 'score'].to_numpy()
    s = t.score.to_numpy(); y = t.label.to_numpy()
    for msub in SIZES:
        reps = 1 if msub == len(allf) else B
        for b in range(reps):
            f = np.sort(rng.choice(allf, msub, replace=False)) if reps > 1 else np.sort(allf)
            for rule, th in {'Emp80': emp_threshold(f), 'CRC80': crc_threshold(f),
                             'R80': os_threshold(f, .8, .05)}.items():
                e = evaluate(s, y, th)
                rows.append(dict(model=model, m=msub, rep=b, rule=rule, fallback=bool(np.isinf(th)), **e))
d = pd.DataFrame(rows)
d['hit'] = d.tp >= 300
d.to_csv(OUT + 'calsize_rows.csv', index=False)
pd.set_option('display.width', 220)
summ = d.groupby(['model', 'm', 'rule']).agg(wl=('workload', 'median'), wl_q10=('workload', lambda x: x.quantile(.1)),
                                             wl_q90=('workload', lambda x: x.quantile(.9)),
                                             rec=('recall', 'median'), hit=('hit', 'mean'), fb=('fallback', 'mean'))
summ.to_csv(OUT + 'calsize_summary.csv')
print(summ.round(3).to_string())

# delta sensitivity
S = load_all()
drows = []
for (name, seed, model), g in S.groupby(['dataset', 'seed', 'model']):
    c = g[g.split == 'cal']; t = g[g.split == 'test']
    f = np.sort(c.loc[c.label == 1, 'score'].to_numpy())
    for delta in (0.10, 0.05, 0.01):
        e = evaluate(t.score.to_numpy(), t.label.to_numpy(), os_threshold(f, .8, delta))
        drows.append(dict(dataset=name, seed=seed, model=model, delta=delta, m=len(f), **e))
dd = pd.DataFrame(drows); dd['hit'] = dd.recall >= .8
dd.to_csv(OUT + 'delta_rows.csv', index=False)
print('\nRF R80 workload (median) and hits by delta:')
print(dd[dd.model == 'RF'].groupby(['dataset', 'delta']).agg(wl=('workload', 'median'), hit=('hit', 'sum')).unstack().loc[ORDER].round(1).to_string())
od = []
for model, g in o.groupby('model'):
    c = g[g.split == 'cal']; t = g[g.split == 'test']
    f = np.sort(c.loc[c.label == 1, 'score'].to_numpy())
    for delta in (0.10, 0.05, 0.01):
        od.append(dict(model=model, delta=delta, **evaluate(t.score.to_numpy(), t.label.to_numpy(), os_threshold(f, .8, delta))))
print(pd.DataFrame(od).round(4).to_string(index=False))
pd.DataFrame(od).to_csv(OUT + 'delta_official.csv', index=False)
# minimum calibration faults for a non-trivial order-statistic threshold
from scipy.stats import binom
for r in (.8, .9):
    for delta in (.10, .05, .01):
        m = 1
        while 1 - r ** m < 1 - delta:
            m += 1
        print(f'R{int(100*r)} delta={delta}: needs m >= {m}')
