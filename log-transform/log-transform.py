import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    values = np.asarray(values)
    return np.log(1+values)