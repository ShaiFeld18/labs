import numpy as np


def ndarray_equal(A: np.ndarray, B: np.ndarray, eps=1e-6) -> bool:
    if A.shape != B.shape or not (abs(A - B) < eps).all():
        return False
    return True


def sum_matrix_vec(A: np.ndarray, axis: int) -> np.ndarray:
    return A.sum(axis=axis)


def mul_mat_vec(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    if A.shape[1] != B.shape[0]:
        raise ValueError('Matrix dimensions are incompatible')
    return np.dot(A, B)


def is_inverse_vec(A: np.ndarray, B: np.ndarray) -> bool:
    multiplied = mul_mat_vec(A, B)
    if ndarray_equal(multiplied, np.identity(multiplied.shape[0])):
        return True
    return False
