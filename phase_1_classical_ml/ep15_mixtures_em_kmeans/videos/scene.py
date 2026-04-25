"""Manim entrypoint for: Mixtures, EM, and k-means.

Render (from ``videos/``): ``manim -ql scene.py EpisodeTitle``
"""

from __future__ import annotations

from manim import Scene, Text


class EpisodeTitle(Scene):
    """Title card / placeholder scene — replace with episode-specific animations."""

    def construct(self) -> None:
        self.add(Text("Mixtures, EM, and k-means", font_size=36))
