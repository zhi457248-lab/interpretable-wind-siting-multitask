# Interpretable Multi-Task Fusion Framework for Wind Farm Siting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LaTeX](https://img.shields.io/badge/source-LaTeX-blue.svg)](paper/paper_revised.tex)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)

> Companion repository for the manuscript *An Interpretable Multi-Task Fusion Framework for Wind Farm Siting Combining Policy Semantics and Meteorological Features*, targeting the **Energy Conversion and Management** (IF 11.0, Q1) submission.

This repository contains the LaTeX source, output figures, and a structural skeleton of the Python implementation of a **cross-modal, multi-task, interpretable** wind-farm siting framework that fuses:

1. **TabTransformer** for 16 meteorological / terrain / cost features,
2. **Chinese-BERT + LoRA** for 81 provincial and municipal policy documents,
3. **4-head cross-modal attention** to fuse the two streams,
4. **GradNorm** to balance three task heads (overall / encouraged-zone / restricted-zone siting scores),
5. **TreeSHAP + KernelSHAP** for local-to-global interpretability.

The framework is validated against nine SCADA-confirmed operational wind-farm sites across China (six from the training partition, three held out).

---

## Repository layout

```
.
├── paper/                      # LaTeX source and compiled PDF
│   ├── paper_revised.tex       # Manuscript (50 pp, 56 refs)
│   ├── paper_revised.pdf       # Latest compiled version
│   └── figures/                # All figures referenced in the manuscript
├── src/                        # Python implementation skeleton
│   ├── data/                   # ERA5 / OSM / policy-text preprocessing
│   ├── models/                 # TabTransformer + BERT-LoRA + cross-modal attention
│   ├── training/               # GradNorm multi-task trainer
│   ├── evaluation/             # AUC / AP / SHAP / ablation harness
│   └── README.md               # Per-module documentation
├── docs/                       # Methodology notes, derivation sketches
├── data/                       # Data availability statements and pointers
├── paper_revised.tex           # Top-level copy for backward compatibility
├── paper_revised.pdf
├── *.png / *.jpeg              # Top-level figures (legacy locations)
├── requirements.txt            # Python dependencies
├── environment.yml             # Conda environment specification
├── CITATION.cff                # Machine-readable citation metadata
└── README.md
```

---

## Key results

| Setting | AUC-ROC (μ ± 95% CI) | AP | Independent SCADA validation (n=9) |
|---|---|---|---|
| Full model (Exp. 4) | 0.8386 | 0.5279 | 0.7285 |
| −Policy stream (Exp. 4-Zero) | 0.7945 | — | — |
| −Permuted policy (Exp. 4-Permuted) | 0.8157 | — | — |
| Δ(Full − Zero) | +0.0441, *p*=0.005 | — | — |
| Δ(Full − Mean) | +0.0004, *p*=0.94 (n.s.) | — | — |

The headline finding is that the policy stream contributes almost entirely through **province-level priors**; the BERT+LoRA encoder's fine-grained semantic contribution is statistically indistinguishable from zero. We retain the full architecture because the contribution is the *cross-modal, end-to-end, interpretable pipeline* rather than the headline AUC. See §4.6 and §6 of the manuscript for the full paired-bootstrap analysis.

---

## Quick start

```bash
git clone https://github.com/<your-org>/interpretable-wind-siting-multitask.git
cd interpretable-wind-siting-multitask
conda env create -f environment.yml
conda activate wind-siting
```

To reproduce the PDF from LaTeX source:

```bash
cd paper
pdflatex -interaction=nonstopmode paper_revised.tex   # 3 passes required
pdflatex -interaction=nonstopmode paper_revised.tex
pdflatex -interaction=nonstopmode paper_revised.tex
```

---

## Data availability

- **ERA5 reanalysis** (Hersbach et al. 2020): publicly available via the Copernicus Climate Data Store.
- **OSM land-use tiles**: OpenStreetMap (ODbL).
- **Policy documents**: 81 Chinese national / provincial / municipal energy-policy documents; original sources publicly retrievable from official government portals (see Appendix A of the manuscript for the full list).
- **SCADA labels**: nine operational wind-farm sites. Aggregated, anonymised summary statistics are released; raw turbine-level SCADA traces are not redistributed due to commercial confidentiality — please contact the corresponding author for collaboration requests.

See [`data/README.md`](data/README.md) for the detailed statement.

---

## Citation

If you use this code or these results, please cite:

```bibtex
@article{wind_siting_policy_multitask_2026,
  title   = {An Interpretable Multi-Task Fusion Framework for Wind Farm Siting
             Combining Policy Semantics and Meteorological Features},
  author  = {Anonymous},
  journal  = {Energy Conversion and Management (under review)},
  year    = {2026},
  note    = {Companion repository: \url{https://github.com/<your-org>/interpretable-wind-siting-multitask}}
}
```

A machine-readable citation is also provided in [`CITATION.cff`](CITATION.cff).

---

## License

This repository is released under the **MIT License** (see [`LICENSE`](LICENSE)). Third-party data retain their original licences (Copernicus licence, ODbL, etc.).

---

## Reproducibility notes

The codebase is structured to enable independent reproduction of the headline ablation table, but several model checkpoints and intermediate tokenised datasets are intentionally withheld at the submission stage to preserve anonymised peer review. A full reproducibility release (data DOI + Zenodo archive + Docker image) will follow acceptance.