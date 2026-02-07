import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    try:
        if x is None or y is None:
            return None

        if len(x) != len(y):
            return None

        x_array = np.asarray(x, dtype=float)
        y_array = np.asarray(y, dtype=float)

        if x_array.ndim != 1 or y_array.ndim != 1:
            return None

        return float(np.sum(np.abs(x_array - y_array)))

    except Exception:
        return None

def _manhattan_distance_ref(x, y): 
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    try:
        if x is None or y is None:
            return None

        if len(x) != len(y):
            return None

        x_array = np.asarray(x, dtype=float)
        y_array = np.asarray(y, dtype=float)

        if x_array.ndim != 1 or y_array.ndim != 1:
            return None

        return float(np.sum(np.abs(x_array - y_array)))

    except Exception:
        return None