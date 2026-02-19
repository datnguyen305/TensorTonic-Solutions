def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    for i in range(steps):
        x -= lr*(2*x*a + b + 0)
    return x 
    