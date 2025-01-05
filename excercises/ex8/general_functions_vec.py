import numpy as np


def ndarray_equal(A: np.ndarray, B: np.ndarray, eps=1e-6) -> bool:
    """
    Checks if two two-dimensional lists are the same size and if the diff between each value is lower than epsilon.
    :param A: first list.
    :param B: second list.
    :param eps: epsilon
    :return: bool
    """
    if A.shape != B.shape or not (abs(A - B) < eps).all():
        return False
    return True


def sum_matrix_vec(A: np.ndarray, axis: int) -> np.ndarray:
    """
    Return the sum of all rows or columns.
    :param A: two-dimensional list
    :param axis: 0 for rows 1 for columns.
    :return: sum of values
    """
    return A.sum(axis=axis)


def mul_mat_vec(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Multiply two matrices.
    :param A: first matrix
    :param B: second matrix
    :return: multiplied matrix
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError('Matrix dimensions are incompatible')
    return np.dot(A, B)


def is_inverse_vec(A: np.ndarray, B: np.ndarray) -> bool:
    """
    Checks if two matrices are inverse of each other.
    :param A: first matrix
    :param B: second matrix
    :return: True if the matrices are inverse False if aren't inverse
    """
    multiplied = mul_mat_vec(A, B)
    if ndarray_equal(multiplied, np.identity(multiplied.shape[0])):
        return True
    return False
