"""Skeleton module — concrete implementation withheld at submission stage.

Maps to manuscript §4.6 (SHAP feature importance).

Two SHAP flavours:
1. TreeSHAP for the XGBoost / RandomForest baselines (fast, exact)
2. KernelSHAP for the deep multi-task model (slower, model-agnostic)

Outputs:
- Per-sample SHAP values for the top 16 features
- Beeswarm plot (SHAP value × feature value)
- Global feature importance ranking with bootstrap CI
- Per-task-head importance comparison
- Cross-scale shift in importance (overall → encouraged → restricted)
"""

from __future__ import annotations

# Concrete implementation deferred.