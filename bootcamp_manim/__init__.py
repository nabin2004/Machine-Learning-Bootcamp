"""Shared Manim helpers and reusable diagram primitives.

This package is named ``bootcamp_manim`` so it does **not** shadow the PyPI
``manim`` library when both are installed.
"""

from bootcamp_manim.styles import COLORS, apply_mpl_style

__all__ = ["COLORS", "apply_mpl_style"]
