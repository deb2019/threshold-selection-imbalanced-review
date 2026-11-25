# Expanded inspection-workload analysis (CSJM manuscript)

Seven equipment datasets, ten split seeds (42-51), two classifiers (LR, RF), and the official
Scania APS train/test split. This folder supports the manuscript
"Inspection Workload at Target Recall in Imbalanced Equipment-Fault Screening".
The repository root contains the earlier three-dataset experiment.

## Contents
| Path | What it is |
|---|---|
| `scores/` | Calibration and test scores for every dataset, seed and model (`row` = row index of the prepared data after deduplication) |
| `official_aps/` | Official Scania split: scores, results, script and input hashes (see its README.txt) |
| `fit.py` | Refits both models and regenerates `scores/` from the prepared CSV files |
| `analyze.py` | Operating points for the score thresholds and inspection budgets -> `expanded_results.csv` |
| `figures.py` | Earlier figures (budget curves, workload ranges) |
| `common.py` | Shared threshold rules: empirical quantile, conformal risk control, order statistic |
| `ladder.py` | Guarantee ladder (Emp / CRC / R at 80% and 90% targets) -> `new_results/ladder_*.csv` |
| `calsize.py` | Calibration-fault subsampling on the official split and confidence-level sensitivity -> `new_results/calsize_*.csv`, `delta_*.csv` |
| `figures_csjm.py` | Figures 1-3 of the manuscript (EPS and PDF) -> `new_figures/` |
| `new_results/` | Outputs of `ladder.py` and `calsize.py` used in the manuscript |

## Reproduce
```
pip install -r requirements.txt
python analyze.py
mkdir -p new_results new_figures
python ladder.py
python calsize.py      # numpy seed 2026, 500 subsamples per calibration size
python figures_csjm.py
```
All analyses except `fit.py` use only the included score files; no model is refitted.

## Full retraining
Download the source datasets listed in the manuscript (Table 1), extract the prepared CSV files named
in `checksums.txt` into `data/`, check them with `sha256sum -c checksums.txt`, and run
`OPENBLAS_NUM_THREADS=1 python fit.py` (this overwrites `scores/`). The source datasets are not
redistributed here. For the official Scania split, see `official_aps/README.txt`.

## Decision rules (flag a record if its score >= threshold)
- Emp: empirical quantile of calibration fault scores (no guarantee).
- CRC: conformal risk control for the miss-rate loss; expected FNR <= 1 - r.
- R: order-statistic rule; P(FNR <= 1 - r) >= 1 - delta (delta = 0.05 unless stated).
- Top-b: inspect exactly floor(bN) highest-ranked test records; stable order resolves ties.
