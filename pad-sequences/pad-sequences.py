import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.empty((0,0))
    N = len(seqs)
    L = max_len if max_len is not None else max(len(seq) for seq in seqs)
    result = np.full((N, L), pad_value, dtype=np.int32)
    for i, seq in enumerate(seqs):
        result[i, :len(seq)] = seq[:L]
    return result 