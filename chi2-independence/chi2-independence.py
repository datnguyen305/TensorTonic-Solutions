import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.asarray(C)
    r, c = C.shape
    exp = np.zeros((r,c))
    total = np.sum(C)
    col = np.sum(C, axis = 1)
    row = np.sum(C, axis = 0)

    exp = np.outer(col, row)/total
    chi2 = np.sum((C-exp)**2/exp)
            

    return (chi2, exp)
