"""Skeleton module — concrete implementation withheld at submission stage.

Maps to manuscript §4.1 (numerical-feature stream: TabTransformer).

Architecture (Huang et al. 2020):
- Per-feature linear embedding: 16 scalars → 16 × d_model tokens
- 4-head self-attention stack over feature tokens
- CLS-style aggregation
- Output: d_model-dim representation F_num

This module is framework-agnostic (pure PyTorch). For the manuscript's
reported runs, d_model = 32, n_heads = 4, n_layers = 3, dropout = 0.1.
"""

from __future__ import annotations

# Concrete implementation deferred to publication of the full
# reproducibility release.