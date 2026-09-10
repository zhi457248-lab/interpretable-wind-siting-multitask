# Data Availability Statement

**Manuscript title**: *Interpretable Multi-Task Cross-Modal Fusion for Hierarchical Policy-Aware Wind Farm Siting*

## Summary

This study relies on three categories of data:

| Category | Specific source | Resolution / Volume | Access | License |
|---|---|---|---|---|
| Spatial numerical features (16 vars) | China meteorological reanalysis + SRTM DEM + ESA WorldCover + China power-grid GIS | 0.01° grid over 22 provinces; ~3.2 M cells | Derived; construction script in `src/data/build_dataset.py` | — |
| Policy documents (Chinese) | NDRC 14th & 15th Five-Year Plans + provincial wind-development plans | 78 documents, 1.3 M tokens | Public web pages (URLs in `data/policy_corpus.tsv`); script in `src/data/build_dataset.py` | — |
| SCADA-confirmed wind-farm sites | National Energy Administration public operation registry | 6 verified operational sites | Public (URLs in `data/sites_verified.tsv`) | — |

## What we make available

1. **All derived features used to train and evaluate the model** (training, validation, test splits; with 10 km spatial buffer applied per §3.4) — released as a single `dataset.csv` with column dictionary `dataset_columns.md`. *(Will be deposited under a permanent DOI upon acceptance; see below.)*
2. **The exact train / validation / test split indices** so reviewers and future users can reproduce every reported metric to the reported decimal.
3. **The constrained-negative sampling script** (`src/data/constrained_sampling.py`) so the reader can re-derive the negative set from any updated land-use map and confirm the spatial-buffer procedure described in §3.4.
4. **The 78 source policy documents**, with the segment-level weak labels we used to fine-tune the BERT-LoRA policy encoder.

## What we cannot share, and why

- **Raw hourly meteorological reanalysis fields** and **30 m SRTM DEM tiles** are subject to the providers' terms of use and are not redistributed here. We provide download URLs and the exact extract window in `data/sources.md`.
- **Provincial wind-development plans** are public but are mirrored locally for latency; we provide URL provenance in `data/policy_corpus.tsv` so anyone can re-fetch the current version.

## Reproducibility

End-to-end reproducibility — i.e. running `python src/training/train.py` on the released CSV and re-creating the reported AUC-ROC, AP, paired-bootstrap p-values, GradNorm weights, SHAP beeswarm, and ablation tables — is expected to be supported after acceptance by:

1. A `Dockerfile` providing the exact environment (`requirements.txt` + `environment.yml` are preliminary).
2. A `pre-trained/` checkpoint (single-file `.pt`) for the full dual-stream model.
3. A Zenodo DOI pinning this repository at the commit hash corresponding to the submitted version.

## License

- **Source code**: MIT (see `LICENSE`).
- **Derived dataset**: CC-BY-4.0.
- **Manuscript text and figures**: CC-BY-4.0.

## Contact

For data-access requests not covered above, contact the corresponding author. We respond within 30 days.