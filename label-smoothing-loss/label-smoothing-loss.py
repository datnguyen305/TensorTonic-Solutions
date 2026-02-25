import numpy as np 
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    predictions = np.asarray(predictions)
    epsilon = np.asarray(epsilon)

    K = len(predictions)

    q = np.full(K,epsilon/K)
    q[target] = (1-epsilon) + epsilon/K

    L = - np.sum(q * np.log(predictions))
    return L 