def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    L = np.sqrt(6/fan_in)
    H = len(W)
    wid = len(W[0])
    result = [[0 for _ in range(wid)] for _ in range(H)]
    for i in range(H):
        for j in range(wid):
            result[i][j] = W[i][j] * (2 * L) - L
    return result
        