import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0, 1].
    If X is 2D and axis=0: scale per column.
    If X is 2D and axis=1: scale per row.
    """
    X = np.asarray(X, dtype=float)

    min_val = np.min(X, axis=axis, keepdims=True)
    max_val = np.max(X, axis=axis, keepdims=True)

    return (X - min_val) / (max_val - min_val + eps)