# Threshold Selection for Imbalanced Binary Classification

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24288576.svg)](https://doi.org/10.5281/zenodo.24288576)

Code, configuration and result records for the review article

> D. Roy, A. Roy and U. Roy, *Threshold Selection for Imbalanced Binary Classification: A Methodological Review with Synthetic and Real-Data Illustrations*, manuscript under review (2026).

The article organizes decision-threshold selection methods by decision objective, selection mechanism, score requirement, granularity, adaptation setting and guarantee type, and illustrates the framework with controlled simulations and real-data experiments. This repository contains the material needed to reproduce the empirical part of the article.

## Experimental layers

| Layer | Folder | Description | Units |
|---|---|---|---|
| S1 | `experiments/S1_synthetic` | Controlled synthetic factorial (linear and bimodal Gaussian geometries, separation, imbalance ratio, training size), threshold-selection support, label corruption, calibration and known-prior change | 720 base fits + 40 calibration fits |
| S2 | `experiments/S2_tolerance` | Post hoc tolerance analysis of saved exact-F1 outcomes (loss tolerance × required success fraction); no new fitting | 36,000 saved rows |
| R1 | `experiments/R1_focused_real` | Focused real-data analysis on 12 tasks with nested validation subsets and injected label corruption | 216 reused fitted score models |
| R2 | `experiments/R2_refit_calibration` | Refits on APS and Shoppers with a reserved calibration partition; raw versus sigmoid-calibrated scores; target-prior cost evaluation | 216 fits + 216 calibrators |
| B1 | `experiments/B1_broad_benchmark` | Broad benchmark of 59 prepared tasks in five domain categories (57 minority-positive) | 1,062 fits; 11,682 policy evaluations |

Common choices: logistic regression (liblinear, max 3,000 iterations) and random forest (100 trees, min leaf size 2); three training regimes (plain, inverse-frequency class weights, random oversampling of the training minority); seeds 42, 137 and 2026 for the real-data layers. No hyperparameter search was performed and models were not refitted after threshold selection.

## Threshold policies

Every empirical rule selects a threshold from selection-partition scores and labels only; test labels are never used for selection. Predictions use `score >= threshold`; tied scores are grouped and exact objective ties are resolved by the highest candidate threshold.

| Category | Representative rule |
|---|---|
| Default | Fixed cutoff 0.5 |
| Metric-driven | Exact search maximizing F1, F2, balanced accuracy (equivalently Youden's J) or MCC |
| Cost-driven | Empirical expected-cost minimization; analytical Bayes cutoff C_FP/(C_FP+C_FN), with and without prior adjustment |
| Prevalence | Cutoff at the training positive prevalence on learned scores |
| Constrained | Maximum recall subject to validation FPR ≤ α; fixed-recall rule |
| Stability | Bootstrap-aggregated F1 threshold |
| Baselines | All-negative and all-positive decisions |

The illustrative cost ratio is C_FN : C_FP = 10 : 1.

## Repository layout

```
src/                     shared code: data loading, preprocessing, training regimes, threshold policies, metrics
experiments/<layer>/     scripts and configuration for each experimental layer
data/raw/                original datasets (not tracked; see docs/datasets.md)
data/processed/          split and subset indices
results/tables/          per-run result records (CSV)
results/figures/         figures reported in the article
paper/                   manuscript source (LaTeX)
docs/datasets.md         dataset sources, positive-class definitions and split policies
```

## Installation

```bash
git clone https://github.com/deb2019/threshold-selection-imbalanced-review.git
cd threshold-selection-imbalanced-review
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The reported runs used Python 3.12, NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0 and scikit-learn 1.8.0.

## Reproducing the results

1. Download the datasets listed in `docs/datasets.md` into `data/raw/`.
2. Run each layer from its folder, for example:

```bash
python experiments/S1_synthetic/run.py
python experiments/B1_broad_benchmark/run.py
```

3. Result records are written to `results/tables/`, and figures to `results/figures/`.

Synthetic data are regenerated deterministically from the recorded seeds. For the real-data layers, the saved split and subset indices in `data/processed/` reproduce the partitions used in the article.

## Data

The real-data experiments use publicly available datasets. Their sources, positive-class definitions and split policies are listed in [`docs/datasets.md`](docs/datasets.md). Datasets are not redistributed here; please obtain them from the original sources and respect their licences.

## Citation

If you use this code, please cite the article (see `CITATION.cff`). The archived release of this repository is available on Zenodo: [https://doi.org/10.5281/zenodo.24288576](https://doi.org/10.5281/zenodo.24288576).

## License

Code is released under the MIT License (see `LICENSE`).

## Contact

Debashis Roy, Department of Computer and System Sciences, Visva-Bharati, Santiniketan, West Bengal 731235, India.
