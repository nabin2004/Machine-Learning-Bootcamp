"""Minimal network diagram stub (layers as labeled boxes)."""

from __future__ import annotations

from manim import ORIGIN, RIGHT, Rectangle, Text, VGroup


class NeuralNetDiagram(VGroup):
    """A row of boxes with placeholder labels (extend per episode)."""

    def __init__(self, layer_labels: list[str] | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        labels = layer_labels or ["x", "h", "y"]
        boxes: list[VGroup] = []
        for label in labels:
            rect = Rectangle(width=1.2, height=0.8, stroke_width=2)
            txt = Text(label, font_size=22).move_to(rect.get_center())
            grp = VGroup(rect, txt)
            boxes.append(grp)
        chain = VGroup(*boxes).arrange(RIGHT, buff=0.4)
        chain.move_to(ORIGIN)
        self.add(chain)
