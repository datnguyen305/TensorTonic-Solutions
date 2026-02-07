import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    m_np = np.array(m)
    v_np = np.array(v)
    grad_np = np.array(grad)
    w_np = np.array(w)
    # Write code here
    m_t = beta1*m_np + (1-beta1)*grad_np
    v_t = beta2*v_np + (1-beta2)*grad_np**2
    w_t = w_np - lr*(weight_decay*w_np) - lr*(m_t/(np.sqrt(v_t)+eps))
    return w_t, m_t, v_t