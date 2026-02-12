import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    x_input = np.asarray(x)
    if len(x_input.shape) == 3:
        H = x_input.shape[1]
        W = x_input.shape[2]
        score = np.sum(x_input, axis = (1,2))
        return score / (H*W)
    elif len(x_input.shape) == 4: 
        H = x_input.shape[2]
        W = x_input.shape[3]
        score = np.sum(x_input, axis = (2,3))
        return score / (H*W)    
    else: 
        raise ValueError("Invalid value")