def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.asarray(X)
    y2 = np.asarray(y)
    lam = np.asarray(lam)
    x, y2 = X.shape
    
    I = np.eye(y2,y2)
    
    score = np.linalg.inv(X.T @ X + lam * I) @ X.T @ y
    return score
    