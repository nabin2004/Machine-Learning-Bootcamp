"""Manim entrypoint for: Episode 0 — ML from the bottom up.

Render (from ``videos/``): ``manim -ql scene.py EpisodeTitle``
"""

from __future__ import annotations

from manim import Scene, Text


class EpisodeTitle(Scene):
    """Title card / placeholder scene — replace with episode-specific animations."""

    def construct(self) -> None:
        self.add(Text("Episode 0 — ML from the bottom up", font_size=36))
