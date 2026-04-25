"""Loss-surface visual stub (extend with 3D scenes in specific episodes)."""

from __future__ import annotations

from manim import Text, VGroup


class LossSurface(VGroup):
    """Placeholder group; swap for a real surface / wireframe in the episode."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.add(Text("Loss surface (stub)", font_size=32))
