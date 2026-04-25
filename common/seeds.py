"""Deterministic RNG for demos, notebooks, and tests."""

from __future__ import annotations

import os
import random


def set_all(seed: int) -> None:
    """Set seeds for ``random``, ``numpy``, ``torch`` (if installed), and hash randomization."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)

    import numpy as np

    np.random.seed(seed)

    try:
        import torch
    except ImportError:
        return

    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    # Best-effort determinism (full reproducibility may require Cudnn flags per workload).
    torch.use_deterministic_algorithms(False)
