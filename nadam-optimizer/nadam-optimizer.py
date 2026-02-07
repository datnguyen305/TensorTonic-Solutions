import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    m_np = np.array(m)
    v_np = np.array(v)
    grad_np = np.array(grad)
    w_np = np.array(w)
    
    m_t =  beta1 * m_np + (1-beta1)*grad_np
    v_t = beta2* v_np + (1-beta2)*grad_np**2
    score = (beta1*m_t + (1-beta1)*grad_np)/(np.sqrt(v_t)+eps)
    w_score = w_np - lr*score
    return w_score, m_t, v_t