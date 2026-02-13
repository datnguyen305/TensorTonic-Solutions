import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.asarray(x)
    n = len(x)
    mean = np.mean(x)

    # sample standard deviation
    s = np.sqrt(np.sum((x - mean)**2) / (n - 1))

    t = (mean - mu0) / (s / np.sqrt(n))
    return t