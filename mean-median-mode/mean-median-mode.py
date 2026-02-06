import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    mean = float(np.mean(x))
    median = float(np.median(x))
    c = Counter(x)
    mode = float(c.most_common(1)[0][0])
    return (mean, median, mode)