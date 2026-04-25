# bootcamp_manim

Shared **style** and **reusable diagram primitives** for episode videos.

> **Why not `manim/`?** A folder named `manim` at the repo root would shadow the
> installed Manim library when Python resolves imports. This package is intentionally
> named `bootcamp_manim`.

## Usage in an episode

From `…/your_episode/videos/scene.py`:

```python
from manim import *

from bootcamp_manim.styles import COLORS
from bootcamp_manim.scenes import NeuralNetDiagram


class EpisodeTitle(Scene):
    def construct(self):
        self.camera.background_color = COLORS["bg"]
        self.add(NeuralNetDiagram())
```

Render from the episode’s `videos/` directory (see root `Makefile` `make video`).

## Primitives

| Class | Role |
|-------|------|
| `LossSurface` | Placeholder for loss landscapes (replace per episode as needed). |
| `GradientArrow` | Gradient step arrow between two points. |
| `NeuralNetDiagram` | Simple layer boxes for architecture sketches. |

## Config

Project-wide Manim defaults live in [`../manim.cfg`](../manim.cfg) at the repository root.
