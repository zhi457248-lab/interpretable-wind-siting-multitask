"""Skeleton module — concrete implementation withheld at submission stage.

Maps to manuscript §5.4 (Exp. 4 ablation).

Four policy-stream variants:
1. Full:        F_policy = BERT+LoRA(doc)               (proposed)
2. Mean:        F_policy = mean over training corpus    (province prior only)
3. Permuted:    F_policy = BERT+LoRA(doc) with random doc-shuffle per batch
4. Zero:        F_policy = 0                              (no policy)

Paired bootstrap (10,000 resamples) gives ΔAUC and p-value for every pair.
The key result (manuscript §6) is that Δ(Full − Mean) is +0.0004 with p=0.94,
proving that BERT+LoRA's fine-grained semantic contribution is statistically
indistinguishable from zero; the policy stream's value is dominated by
province-level priors.
"""

from __future__ import annotations

# Concrete implementation deferred.