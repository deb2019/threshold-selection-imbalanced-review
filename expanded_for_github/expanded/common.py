"""Shared helpers: load saved scores and compute decision thresholds.

Threshold rules (flag a record if score >= threshold):
  Emp80  : empirical 80% quantile of calibration fault scores
  CRCr   : conformal risk control, E[FNR] <= 1-r  (Angelopoulos et al.)
  Rr     : order-statistic rule, P(FNR <= 1-r) >= 1-delta (Tong et al. style)
"""
import math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import binom

SCORE_DIR = Path('scores')
OFFICIAL = Path('official_aps/official_scores.csv.gz')
ORDER = ['APS', 'AI4I', 'Conveyor', 'Bogie', 'Sensor', 'Machines', 'Helicopter']


def load_all():
    frames = []
    for f in sorted(SCORE_DIR.glob('*.csv.gz')):
        name, seed = f.name.split('.')[0].split('_')
        d = pd.read_csv(f, float_precision='round_trip')
        d['seed'] = int(seed)
        frames.append(d)
    return pd.concat(frames, ignore_index=True)


def emp_threshold(fault_sorted, r=0.8):
    m = len(fault_sorted)
    return fault_sorted[m - math.ceil(r * m)]


def os_threshold(fault_sorted, r=0.8, delta=0.05):
    """Largest rank k with P(Bin(m,1-r) >= k) >= 1-delta; flag s >= s_(k)."""
    m = len(fault_sorted)
    ranks = np.arange(1, m + 1)
    valid = ranks[binom.sf(ranks - 1, m, 1 - r) >= 1 - delta]
    return fault_sorted[valid[-1] - 1] if len(valid) else -np.inf


def crc_threshold(fault_sorted, r=0.8):
    """Conformal risk control for FNR loss (bounded by 1):
    choose largest k (misses allowed among calibration faults) with
    (k + 1) / (m + 1) <= 1 - r; threshold = s_(k+1) (1-based), i.e. index k.
    Gives E[FNR] <= 1 - r over calibration and test draws."""
    m = len(fault_sorted)
    kmax = math.floor((1 - r) * (m + 1) - 1 + 1e-12)
    if kmax < 0:
        return -np.inf
    return fault_sorted[kmax]


def evaluate(scores, labels, th):
    flag = scores >= th
    a = int(flag.sum())
    tp = int(labels[flag].sum())
    P = int(labels.sum())
    n = len(labels)
    return dict(alerts=a, tp=tp, recall=tp / P, workload=1000 * a / n,
                N=n, P=P)
