import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    if rng is None: 
        rng = np.random
    
    test = rng.random(x.shape)

    pattern = np.where(test < (1-p), 1/(1-p), 0)

    output = x * pattern

    return output, pattern
