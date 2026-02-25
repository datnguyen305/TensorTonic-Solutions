import math 
def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    H = len(X)
    W = len(X[0])
    p = pool_size
    H_out = math.floor(H/pool_size)
    W_out = math.floor(W/pool_size)
    result = [[0 for _ in range(W_out)] for _ in range(H_out)]
    
    for i in range(H_out):
        for j in range(W_out):
            total = 0
            for a in range(p):
                for b in range(p):
                    total += X[i*p + a][j*p +b]
            result[i][j] = 1/p**2 * total

    return result 
    