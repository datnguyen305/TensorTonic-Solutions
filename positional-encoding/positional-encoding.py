import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos_vector = np.arange(seq_len).reshape(seq_len, 1)
    row_vector = np.arange(d_model).reshape(1, d_model)
    angle = pos_vector / np.power(base, (row_vector//2)*2/d_model)
    angle[:, 0::2] = np.sin(angle[:, 0::2])
    angle[:, 1::2] = np.cos(angle[:, 1::2])
    return angle