# Methodology notes

This directory collects derivation sketches, design rationale, and
sensitivity analyses that supplement the manuscript but did not fit
into the main text.

## Planned documents (placeholder)

- `constrained-sampling-sensitivity.md` — sensitivity of headline AUC
  to buffer-radius choice (5 / 10 / 20 km) and slope threshold.
- `gradnorm-hyperparameter-sweep.md` — α ∈ {0.5, 1.0, 1.5, 2.0} sweep
  on multi-task balance stability.
- `paired-bootstrap-power-analysis.md` — minimum detectable ΔAUC
  at 10,000 resamples for various effect sizes.
- `chinese-bert-model-choice.md` — rationale for selecting
  chinese-roberta-wwm-ext over alternatives (RoBERTa-wwm-ext-large,
  ERNIE, MacBERT).
- `shap-computation-cost.md` — TreeSHAP vs KernelSHAP trade-off.

These documents are deferred to the post-acceptance release alongside
the full data and code release.