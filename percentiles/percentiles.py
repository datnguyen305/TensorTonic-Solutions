import numpy as np
import math
def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x_np = np.array(x)
    result = np.percentile(x_np, q, method="linear")
    return np.array(result)