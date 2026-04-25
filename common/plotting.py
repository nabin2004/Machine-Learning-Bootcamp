"""Consistent matplotlib defaults and small teaching plots."""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure
    from numpy.typing import NDArray


def apply_style() -> None:
    """Set a clean default style for all bootcamp figures."""
    plt.rcParams.update(
        {
            "figure.figsize": (6, 4),
            "figure.dpi": 120,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.size": 11,
        }
    )


def scatter_classes(
    x: NDArray,
    y: NDArray,
    *,
    ax: Axes | None = None,
    title: str | None = None,
) -> tuple[Figure, Axes]:
    """Scatter 2D points coloured by class label."""
    apply_style()
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    for label in np.unique(y):
        mask = y == label
        ax.scatter(x[mask, 0], x[mask, 1], s=18, alpha=0.85, label=str(int(label)))
    ax.set_xlabel("x0")
    ax.set_ylabel("x1")
    if title:
        ax.set_title(title)
    ax.legend(title="class")
    fig.tight_layout()
    return fig, ax


def loss_curve(losses: list[float] | NDArray, *, ax: Axes | None = None) -> tuple[Figure, Axes]:
    """Plot a simple training loss curve."""
    apply_style()
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure
    ax.plot(np.asarray(losses, dtype=float))
    ax.set_xlabel("step")
    ax.set_ylabel("loss")
    ax.set_title("Training loss")
    fig.tight_layout()
    return fig, ax
