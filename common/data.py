"""Small synthetic datasets for teaching and parity checks."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from sklearn.datasets import make_classification, make_moons

if TYPE_CHECKING:
    from numpy.typing import NDArray


def moons(n_samples: int = 300, noise: float = 0.15, seed: int = 0) -> tuple[NDArray, NDArray]:
    """Two interleaving half-moons (+ labels 0/1)."""
    x, y = make_moons(n_samples=n_samples, noise=noise, random_state=seed)
    return x.astype(np.float64), y.astype(np.int64)


def spirals(
    n_samples_per_class: int = 200,
    *,
    seed: int = 0,
) -> tuple[NDArray, NDArray]:
    """Toy 2D spiral dataset (binary), useful for non-linear decision boundaries."""
    rng = np.random.default_rng(seed)
    n = n_samples_per_class
    theta = np.sqrt(rng.random(n)) * 4 * np.pi
    r = 2 * theta + np.pi
    data1 = np.column_stack((r * np.cos(theta), r * np.sin(theta)))
    data2 = -data1 + 0.5 * rng.standard_normal(data1.shape)
    x = np.vstack((data1, data2)).astype(np.float64)
    y = np.concatenate((np.zeros(n, dtype=np.int64), np.ones(n, dtype=np.int64)))
    return x, y


def blobs_2d(
    n_samples: int = 400,
    *,
    seed: int = 0,
) -> tuple[NDArray, NDArray]:
    """Linearly separable-ish Gaussian blobs in 2D."""
    x, y = make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        n_clusters_per_class=1,
        flip_y=0.02,
        class_sep=1.8,
        random_state=seed,
    )
    return x.astype(np.float64), y.astype(np.int64)
