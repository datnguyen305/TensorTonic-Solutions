import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix_np = np.asarray(matrix, dtype=float)
        # must be 2D
        if matrix_np.ndim != 2:
            return None

        # reject empty matrices
        if matrix_np.size == 0:
            return None

        # axis validation
        if axis not in (None, 0, 1):
            return None
    
        if norm_type == "l2":
            norm = np.sqrt(np.sum(matrix_np ** 2, axis=axis, keepdims=True))
        elif norm_type == "l1":
            norm = np.sum(np.abs(matrix_np), axis=axis, keepdims=True)
        elif norm_type == "max":
            norm = np.max(np.abs(matrix_np), axis=axis, keepdims=True)
        else:
            raise ValueError

        norm = np.where(norm == 0, 1, norm)
        return np.round(matrix_np / norm, 2)
    except Exception:
        return None

def _matrix_normalization_ref(matrix, axis=None, norm_type="l2"):
    try:
        matrix_np = np.asarray(matrix, dtype=float)
        # must be 2D
        if matrix_np.ndim != 2:
            return None

        # reject empty matrices
        if matrix_np.size == 0:
            return None

        # axis validation
        if axis not in (None, 0, 1):
            return None
    
        if norm_type == "l2":
            norm = np.sqrt(np.sum(matrix_np ** 2, axis=axis, keepdims=True))
        elif norm_type == "l1":
            norm = np.sum(np.abs(matrix_np), axis=axis, keepdims=True)
        elif norm_type == "max":
            norm = np.max(np.abs(matrix_np), axis=axis, keepdims=True)
        else:
            raise ValueError

        norm = np.where(norm == 0, 1, norm)
        return np.round(matrix_np / norm, 2)
    except Exception:
        return None