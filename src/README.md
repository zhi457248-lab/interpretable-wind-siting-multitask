# `src/` — Implementation skeleton

This directory contains a structural skeleton of the implementation
described in the manuscript. Each module is documented at the
module-level docstring; concrete function signatures are sketched,
but the actual training loop and checkpoint-saving code is
intentionally withheld at the **submission stage** to preserve
anonymised peer review. A full release (data DOI, Zenodo archive,
Docker image) will follow acceptance.

## Layout

```
src/
├── data/
│   ├── era5_loader.py            # ERA5 reanalysis → 0.25° grid feature tensor
│   ├── osm_landuse.py            # OSM tiles → 16-dim engineering / land-use vector
│   ├── policy_corpus.py          # 81 docs → tokenised Chinese-BERT inputs (LoRA-ready)
│   ├── build_dataset.py          # End-to-end dataset builder (positive / constrained negative)
│   └── constrained_sampling.py   # Buffer-based negative sampling (≥10 km, slope ≤ 25°, etc.)
├── models/
│   ├── tab_transformer.py        # 16-feature stream: per-feature linear embed + 4-head self-attention
│   ├── policy_bert_lora.py       # hfl/chinese-roberta-wwm-ext + LoRA adapter (rank 8)
│   ├── cross_modal_fusion.py     # 4-head cross-modal attention (num as Q, policy as K/V) + sigmoid gate
│   └── multitask_heads.py        # Three task heads: overall, encouraged, restricted
├── training/
│   ├── gradnorm.py               # GradNorm loss-weight balancer (Chen et al. 2018, ICML)
│   ├── train.py                  # End-to-end training loop, paired-bootstrap evaluation harness
│   └── losses.py                 # BCE-with-logits per head + auxiliary regularisers
├── evaluation/
│   ├── metrics.py                # AUC-ROC (DeLong 1988 significance), AP, paired bootstrap
│   ├── shap_analysis.py          # TreeSHAP (XGBoost) + KernelSHAP (deep model)
│   └── ablation.py               # Four-variant policy ablation runner (Full/Mean/Permuted/Zero)
└── README.md
```

## Mapping to manuscript sections

| Source module | Manuscript section | Purpose |
|---|---|---|
| `data/build_dataset.py` | §3.1 Study area | 13,197-grid-cell feature assembly |
| `data/constrained_sampling.py` | §3.2 Constrained sampling | Negative-set definition with 10 km buffer |
| `models/tab_transformer.py` | §4.1 Numerical-feature stream | 16-feature TabTransformer |
| `models/policy_bert_lora.py` | §4.2 Policy-text stream | Chinese-BERT + LoRA encoder |
| `models/cross_modal_fusion.py` | §4.3 Cross-modal attention | 4-head attention + sigmoid gate |
| `training/gradnorm.py` | §4.5 Multi-task balance | Three-head loss balancing |
| `evaluation/shap_analysis.py` | §4.6 SHAP | TreeSHAP + KernelSHAP |
| `evaluation/ablation.py` | §5.4 Exp. 4 ablation | Full/Mean/Permuted/Zero variants |
| `evaluation/metrics.py` | §4.4 Coordinate inference | AUC + DeLong + paired bootstrap |

## Reproducing the headline ablation table

The full reproducibility instructions will be released alongside the
data DOI upon acceptance. Until then, please contact the corresponding
author with reproduction requests.