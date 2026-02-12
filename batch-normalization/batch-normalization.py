import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x_input = np.asarray(x)
    num_feats = len(x_input.shape)
    if num_feats == 2: 
        m = x_input.shape[0]
        lambda_b = np.mean(x_input, axis=0, keepdims=True)
        sigmoid_2 = 1/m * np.sum((x_input - lambda_b)**2, axis=0, keepdims=True)
        score = (x_input - lambda_b)/np.sqrt(sigmoid_2 + eps)
        return gamma * score + beta
    elif num_feats == 4: 
        m = x_input.shape[0]
        C = x_input.shape[1]
        gamma_res = np.asarray(gamma)
        beta_res = np.asarray(beta)
        gamma_res = gamma_res.reshape(1, C, 1, 1)
        beta_res = beta_res.reshape(1, C, 1, 1)
        lambda_b = np.mean(x_input, axis=(0,2,3), keepdims=True)
        sigmoid_2 = np.var(x_input, axis=(0,2,3), keepdims=True)
        score = (x_input - lambda_b)/np.sqrt(sigmoid_2 + eps)
        return gamma_res * score + beta_res
    else:
        return None
