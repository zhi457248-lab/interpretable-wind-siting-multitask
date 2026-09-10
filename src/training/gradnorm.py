"""Skeleton module — concrete implementation withheld at submission stage.

Maps to manuscript §4.5 (GradNorm multi-task loss balancing).

Reference: Chen, Badrinarayanan, Lee, Rabinovich (2018).
GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep
Multitask Networks. ICML 2018.

Implementation:
- Maintain per-task weight w_i(t) (sum normalised to T per step)
- Compute gradient norm of w_i(t) · L_i(t) w.r.t. last shared layer
- Optimise L_grad = Σ | G_W_i − Ḡ_W · r_i(t)^α |  on the weights w_i
- Use a separate optimiser for w_i (lr_w ≪ lr_main, e.g. 1e-3 vs 1e-4)
"""

from __future__ import annotations

# Concrete implementation deferred.