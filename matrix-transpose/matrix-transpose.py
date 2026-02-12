import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n = len(A)
    m = len(A[0])
    result = np.zeros(shape=(m, n))
    for i in range(m):
        for j in range(n):
            result[i, j] = A[j][i]

    return result
