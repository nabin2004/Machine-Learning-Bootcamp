"""Consistent colours and typography hooks for Manim + matplotlib."""

from __future__ import annotations

from manim import ManimColor

# Palette (ManimColor for Manim, hex for matplotlib)
COLORS = {
    "intuition": ManimColor("#4C9AFF"),
    "library": ManimColor("#3DDC84"),
    "scratch": ManimColor("#FFD54A"),
    "limits": ManimColor("#FF6B6B"),
    "ink": ManimColor("#E8E8E8"),
    "muted": ManimColor("#9AA0A6"),
    "bg": ManimColor("#1E1E1E"),
}


def apply_mpl_style() -> None:
    """Optional matplotlib style aligned with bootcamp visuals (for static frames)."""
    import matplotlib as mpl

    mpl.rcParams.update(
        {
            "figure.facecolor": "#1E1E1E",
            "axes.facecolor": "#1E1E1E",
            "axes.edgecolor": "#9AA0A6",
            "axes.labelcolor": "#E8E8E8",
            "text.color": "#E8E8E8",
            "xtick.color": "#9AA0A6",
            "ytick.color": "#9AA0A6",
            "grid.color": "#3A3A3A",
        }
    )
