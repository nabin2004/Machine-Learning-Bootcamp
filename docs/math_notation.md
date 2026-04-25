# Math ↔ code notation

Every episode ships with `notes.md` containing a mapping table. Conventions:

## Rules

1. **Same symbol, same name**: If the doc uses \(W\), the code uses `W` (not `weights` unless
   you define that mapping explicitly once).
2. **Shapes in comments**: After each tensor, note shape, e.g. `# W: (d_out, d_in)`.
3. **Column vectors**: Prefer explicit shapes over ambiguous vector orientation; state whether
   \(x \in \mathbb{R}^{n}\) is row or column in code (`x` shape `(n,)` vs `(n, 1)`).
4. **Bias**: Use `b` if the doc uses \(b\); if you use Greek \(\beta\), still map to a code name
   in the table.

## Example `notes.md` snippet

| Symbol | Meaning | Code |
|--------|---------|------|
| \(X\) | Design matrix (samples as rows) | `X` `(n_samples, n_features)` |
| \(y\) | Targets | `y` `(n_samples,)` |
| \(W\) | Weights | `W` `(n_features,)` or `(n_features, n_out)` |
| \(b\) | Bias | `b` scalar or `(n_out,)` |
| \(\eta\) | Learning rate | `learning_rate` |

## Loss / objectives

Write the loss **exactly** as implemented (mean vs sum, log base, epsilon inside `log`).
Mismatch here is the #1 source of “parity test fails but both are correct” confusion.
