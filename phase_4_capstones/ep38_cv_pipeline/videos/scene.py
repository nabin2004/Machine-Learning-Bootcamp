"""Manim entrypoint for: End-to-end computer vision pipeline.

Render (from ``videos/``): ``manim -ql scene.py EpisodeTitle``
"""

from __future__ import annotations

from manim import Scene, Text


class EpisodeTitle(Scene):
    """Title card / placeholder scene — replace with episode-specific animations."""

    def construct(self) -> None:
        self.add(Text("End-to-end computer vision pipeline", font_size=36))
