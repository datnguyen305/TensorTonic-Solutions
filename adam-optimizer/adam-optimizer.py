import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    m_t = beta1 * m + (1 - beta1) * grad
    v_t = beta2 * v + (1 - beta2) * grad**2
    m_hat_t = m_t/(1-beta1**t)
    v_hat_t = v_t/(1-beta2**t)
    score = m_hat_t/(np.sqrt(v_hat_t) + eps)
    param_new = param - lr * score
    return param_new, m_t, v_t 

     