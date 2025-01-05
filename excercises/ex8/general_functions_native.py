from typing import List


def list_equal(A: List[List[float]], B: List[List[float]], eps=1e-6) -> bool:
    """
    Checks if two two-dimensional lists are the same size and if the diff between each value is lower than epsilon.
    :param A: first list.
    :param B: second list.
    :param eps: epsilon
    :return: bool
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for row in range(len(A)):
        for col in range(len(A[0])):
            if not abs(A[row][col] - B[row][col]) < eps:
                return False
    return True


def sum_matrix_native(A: List[List[float]], axis: int) -> List[float]:
    """
    Return the sum of all rows or columns.
    :param A: two-dimensional list
    :param axis: 0 for rows 1 for columns.
    :return: sum of values
    """
    if axis == 0:
        return [sum([row[col] for row in A]) for col in range(len(A[0]))]
    elif axis == 1:
        return [sum(row) for row in A]


def mul_mat_native(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.
    :param A: first matrix
    :param B: second matrix
    :return: multiplied matrix
    """
    if len(A[0]) != len(B):
        raise ValueError('Matrix dimensions are incompatible')
    res = []
    for a_row in range(len(A)):
        res.append([])
        for b_col in range(len(B[0])):
            res[a_row].append(0)
            for b_row in range(len(B)):
                res[a_row][b_col] += A[a_row][b_row] * B[b_row][b_col]
    return res


def is_inverse_native(A: List[List[float]], B: List[List[float]]) -> bool:
    """
    Checks if two matrices are inverse of each other.
    :param A: first matrix
    :param B: second matrix
    :return: True if the matrices are inverse False if aren't inverse
    """
    multiplication = mul_mat_native(A, B)
    print(multiplication)
    for row in range(len(multiplication)):
        for col in range(len(multiplication[row])):
            if (row != col and multiplication[row][col] != 0) or (row == col and multiplication[row][col] != 1):
                return False
    return True
