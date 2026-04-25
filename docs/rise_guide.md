# RISE (slideshow) in JupyterLab

We use **jupyterlab-rise** for turning intuition notebooks into slide decks.

## Install

Already included in `requirements.txt` (`jupyterlab-rise`). After `make setup`, launch:

```bash
make lab
```

## Using RISE

1. Open `01_intuition.ipynb`.
2. Enable the RISE extension from the JupyterLab launcher / right sidebar (depending on JL version).
3. Enter **slideshow mode** and step through cells.

## Cell metadata

Slides use notebook / cell metadata (`slideshow.slide_type`):

- `slide` — new slide
- `subslide` — continuation full slide
- `fragment` — reveal step
- `skip` — skipped in presentation
- `notes` — speaker notes

The template notebooks include basic metadata you can copy.

## Exporting static slides

```bash
make slides EP=phase_1_classical_ml/ep01_linear_regression
```

This runs `jupyter nbconvert --to slides` on `01_intuition.ipynb`. Host the generated HTML
or open it locally.

## Tips

- Keep **code cells** tiny in intuition decks; move heavy code to other acts.
- Use large fonts and high-contrast figures (`common.plotting.apply_style()`).
