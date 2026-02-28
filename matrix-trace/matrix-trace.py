import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    H = len(A)
    W = len(A[0])
    trace = 0
    for i in range(H):
        for j in range(W):
            if i == j:
                trace += A[i][j]
    return trace
