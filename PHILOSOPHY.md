# Teaching philosophy

This bootcamp is structured like a **Karpathy-tier** series: intuition first, library API second, **from scratch** third, and **limits** (where things break) last.

## Four acts per episode

| Act | Purpose |
|-----|---------|
| **Intuition** | Whiteboard-style: geometry, loss surfaces, what the algorithm is doing. Animations welcome. Minimal code. |
| **Library run** | sklearn / PyTorch / Hugging Face: minimal, clean code. Get a correct result and learn the API. |
| **From scratch** | NumPy for classical ML; raw autograd / tensors for deep learning. No `nn.Linear`-style shortcuts until the idea is clear. |
| **Limits** | Real failure modes: class imbalance, scaling, vanishing gradients, mode collapse, distribution shift—not vague warnings. |

## Non-negotiables

1. **Parity by construction**: The hand-rolled path should match the library path on the **same seeded data**; compare outputs in **Act 3** (and optionally with `common.testing` helpers)—no separate test suite required for the scaffold.
2. **Math ↔ code**: Every episode has `notes.md` mapping symbols in equations to **exact** variable names in code (`W` in the doc is `W` in the array).
3. **No magic numbers**: Hyperparameters are named, justified, and set in one place after explanation.
4. **Reproducibility**: `common.seeds.set_all(seed)` everywhere; pinned dependencies; fixed random seeds for demos and notebooks.

## Episode 0

**Episode 0** is standalone: NumPy, vectorisation, broadcasting, `einsum`, seeds, and profiling—skills that block learners before they touch algorithms.

## Presentations (RISE)

Intuition notebooks are **RISE-ready** in JupyterLab: use slideshow mode for classroom or self-study walkthroughs. See [docs/rise_guide.md](docs/rise_guide.md).

## Manim

Shared visual style and reusable diagram primitives live in **`bootcamp_manim/`** (named to avoid clashing with the installed **`manim`** package). Episode-specific scenes live in each episode’s `videos/` folder. See [docs/manim_guide.md](docs/manim_guide.md).
