"""Figures sized for the CSJM A5 text block (118 mm wide), saved as EPS (no transparency)."""
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, '.')
from common import ORDER

OUT = 'new_figures/'
W = 118 / 25.4
plt.rcParams.update({'font.size': 7, 'axes.titlesize': 7, 'axes.labelsize': 7, 'legend.fontsize': 6.5,
                     'xtick.labelsize': 6.5, 'ytick.labelsize': 6.5, 'font.family': 'serif',
                     'axes.linewidth': 0.5, 'lines.linewidth': 1.0})
C = {'LR': '#1f5fa8', 'RF': '#c44e0f', 'Emp': '#1f5fa8', 'CRC': '#2a8a3e', 'R': '#c44e0f'}
FILL = {'LR': '#d7e3f3', 'RF': '#f6dccd', 'Emp': '#d7e3f3', 'CRC': '#d5ecd9', 'R': '#f6dccd'}

# Figure 1: recall vs inspection budget
d = pd.read_csv('expanded_results.csv')
fig, axes = plt.subplots(3, 3, figsize=(W, W * 0.92), sharex=True, sharey=True)
for ax, n in zip(axes.flat, ORDER):
    for model, sty in [('LR', '--'), ('RF', '-')]:
        v = d[(d.dataset == n) & (d.model == model) & d.rule.str.startswith('Top')].copy()
        v['b'] = v.rule.str[3:].astype(int)
        t = v.groupby('b').recall.agg(['median', 'min', 'max'])
        if model == 'RF':
            ax.fill_between(t.index, 100 * t['min'], 100 * t['max'], color=FILL[model], lw=0, zorder=1)
        else:
            ax.plot(t.index, 100 * t['min'], ':', color=C[model], lw=0.6, zorder=2)
            ax.plot(t.index, 100 * t['max'], ':', color=C[model], lw=0.6, zorder=2)
        ax.plot(t.index, 100 * t['median'], sty, color=C[model], label=model, zorder=3)
    ax.axhline(80, color='0.55', lw=0.5, zorder=2); ax.axvline(5, color='0.55', lw=0.5, zorder=2)
    ax.set_title(n, pad=2); ax.set_xticks([0, 10, 20, 30, 40]); ax.set_yticks([0, 20, 40, 60, 80, 100])
for ax in axes.flat[len(ORDER):]:
    ax.axis('off')
for ax in axes.flat[3:6]:
    ax.xaxis.set_tick_params(labelbottom=True)
axes.flat[0].legend(loc='lower right', frameon=False)
fig.supxlabel('Inspection budget (% of records)', fontsize=7)
fig.supylabel('Fault recall (%)', fontsize=7)
fig.tight_layout(pad=0.4, h_pad=0.6, w_pad=0.4)
fig.savefig(OUT + 'fig1_budget.eps'); fig.savefig(OUT + 'fig1_budget.pdf'); fig.savefig(OUT + 'fig1_budget.png', dpi=200); plt.close(fig)

# Figure 2: guarantee ladder workload (RF, 80% target)
L = pd.read_csv('new_results/ladder_rows.csv')
q = L[(L.model == 'RF') & (L.target == 0.8)]
fig, ax = plt.subplots(figsize=(W, W * 0.52))
y = np.arange(len(ORDER))
for i, (lev, mk, lab) in enumerate([('Emp', 'o', 'Emp80 (empirical)'), ('CRC', 'D', 'CRC80 (expected)'), ('R', 's', 'R80 (95% confidence)')]):
    v = q[q.level == lev].groupby('dataset').workload.agg(['median', 'min', 'max']).loc[ORDER]
    yy = y + (i - 1) * 0.24
    ax.hlines(yy, v['min'], v['max'], color=C[lev], lw=0.8)
    ax.plot(v['median'], yy, mk, color=C[lev], ms=3.5, label=lab, ls='none')
ax.set_xscale('log'); ax.set_xlim(10, 1100)
ax.set_xticks([10, 20, 50, 100, 200, 500, 1000]); ax.set_xticklabels(['10', '20', '50', '100', '200', '500', '1000'])
ax.set_yticks(y); ax.set_yticklabels(ORDER); ax.invert_yaxis()
ax.set_xlabel('Inspections per 1,000 records (median and observed range, log scale)')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.0), ncol=3, frameon=False, fontsize=6)
ax.grid(axis='x', color='0.9', lw=0.4); ax.set_axisbelow(True)
fig.tight_layout(pad=0.4)
fig.savefig(OUT + 'fig2_ladder.eps'); fig.savefig(OUT + 'fig2_ladder.pdf'); fig.savefig(OUT + 'fig2_ladder.png', dpi=200); plt.close(fig)

# Figure 3: calibration faults vs workload and attainment (official Scania, RF)
cs = pd.read_csv('new_results/calsize_rows.csv')
r = cs[cs.model == 'RF']
fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, W * 0.78), sharex=True, gridspec_kw={'height_ratios': [1.6, 1]})
for lev, mk, lab in [('Emp80', 'o', 'Emp80'), ('CRC80', 'D', 'CRC80'), ('R80', 's', 'R80')]:
    k = lev[:-2]
    g = r[r.rule == lev].groupby('m').workload
    med, lo, hi = g.median(), g.quantile(.1), g.quantile(.9)
    a1.fill_between(med.index, lo, hi, color=FILL[k], lw=0)
    a1.plot(med.index, med, '-', marker=mk, ms=2.8, color=C[k], label=lab)
    h = r[r.rule == lev].groupby('m').hit.mean() * 100
    a2.plot(h.index, h, '-', marker=mk, ms=2.8, color=C[k], label=lab)
a1.set_yscale('log'); a1.set_ylim(12, 1100)
a1.set_yticks([15, 20, 30, 50, 100, 300, 1000]); a1.set_yticklabels(['15', '20', '30', '50', '100', '300', '1000'])
a1.set_ylabel('Inspections per 1,000\n(median, 10th-90th pct.)')
a1.legend(frameon=False, ncol=3, loc='upper right')
a2.axhline(95, color='0.55', lw=0.5)
a2.set_ylabel('Subsamples with\n$\\geq$300 of 375 faults (%)')
a2.set_ylim(-5, 105); a2.set_xscale('log')
a2.set_xticks([10, 14, 20, 30, 50, 100, 250]); a2.set_xticklabels(['10', '14', '20', '30', '50', '100', '250'])
a2.set_xlabel('Calibration faults used to set the threshold (log scale)')
for a in (a1, a2):
    a.grid(color='0.9', lw=0.4); a.set_axisbelow(True)
fig.tight_layout(pad=0.4, h_pad=0.5)
fig.savefig(OUT + 'fig3_calsize.eps'); fig.savefig(OUT + 'fig3_calsize.pdf'); fig.savefig(OUT + 'fig3_calsize.png', dpi=200); plt.close(fig)
print('ok')
