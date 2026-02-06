import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    if rng is None:
        rng = np.random

    q = 1 - p

    # random values in [0, 1)
    r = rng.random(x.shape)

    # pattern: 0 (drop) or 1/q (keep + scale)
    pattern = np.where(r < q, 1 / q, 0)

    # apply pattern
    output = x * pattern

    return output, pattern
