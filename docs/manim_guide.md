# Manim guide

## Layout

- **Episode scenes**: `<episode>/videos/scene.py` — one or more `Scene` subclasses.
- **Shared helpers**: [`bootcamp_manim/`](../bootcamp_manim/) — colours, small reusable
  groups (`LossSurface`, `GradientArrow`, `NeuralNetDiagram`).

We use the name **`bootcamp_manim`** so it never shadows the PyPI **`manim`** package.

## Install & CLI

Manim is installed from `requirements.txt`. Typical render:

```bash
cd phase_1_classical_ml/ep01_linear_regression/videos
manim -ql scene.py EpisodeTitle
```

Or from repo root:

```bash
make video EP=phase_1_classical_ml/ep01_linear_regression
```

Outputs go under `media/` (gitignored). Quality flags: `-ql` (480p15, fast), `-qh` (1080p60).

## Config

[`manim.cfg`](../manim.cfg) at the repository root sets default CLI quality. Override per
invocation as needed.

## Embedding in notebooks

Common workflow:

1. Render a clip to `media/videos/.../*.mp4`.
2. Use IPython `Video()` or HTML `<video>` in a markdown cell pointing at the relative path.

Keep large binaries out of git; commit **source** (`scene.py`) only unless you use Git LFS.

## LaTeX

Some systems lack a full LaTeX install. Prefer `Text` for stubs; use `MathTex` / `Tex` when
LaTeX is available and documented in the episode README.
