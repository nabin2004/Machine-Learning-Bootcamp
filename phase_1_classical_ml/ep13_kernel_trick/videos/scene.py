"""Manim entrypoint for: Kernel trick.

Render (from ``videos/``): ``manim -ql scene.py EpisodeTitle``
"""

from __future__ import annotations

from manim import Scene, Text


class EpisodeTitle(Scene):
    """Title card / placeholder scene — replace with episode-specific animations."""

    def construct(self) -> None:
        self.add(Text("Kernel trick", font_size=36))
