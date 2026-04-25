"""Arrow along negative gradient (teaching stub)."""

from __future__ import annotations

from manim import Arrow, VGroup


class GradientArrow(VGroup):
    """A single arrow from *start* toward *end*."""

    def __init__(self, start, end, **kwargs) -> None:
        super().__init__(**kwargs)
        self.add(Arrow(start, end, buff=0.08, stroke_width=3, **kwargs))
