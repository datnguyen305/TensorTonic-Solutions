import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x, dtype=float)
    score = np.where(
        x <= 0,
        0,
        x
    )
    return score