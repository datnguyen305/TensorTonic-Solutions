import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    x_t = np.asarray(x_t)
    h_prev = np.asarray(h_prev)
    Wx = np.asarray(Wx)
    Wh = np.asarray(Wh)
    b = np.asarray(b)
    pre_act = x_t@Wx + h_prev@Wh + b 
    h_t = np.tanh(pre_act)
    return h_t

