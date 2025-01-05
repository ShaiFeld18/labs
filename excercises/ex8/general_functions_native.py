from typing import List


def list_equal(A: List[List[float]], B: List[List[float]], eps=1e-6) -> bool:
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for row in range(len(A)):
        for col in range(len(A[0])):
            if not abs(A[row][col] - B[row][col]) < eps:
                return False
    return True


def sum_matrix_native(A: List[List[float]], axis: int) -> List[float]:
    if axis == 0:
        return [sum([row[col] for row in A]) for col in range(len(A[0]))]
    elif axis == 1:
        return [sum(row) for row in A]


def mul_mat_native(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
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
    multiplication = mul_mat_native(A, B)
    print(multiplication)
    for row in range(len(multiplication)):
        for col in range(len(multiplication[row])):
            if (row != col and multiplication[row][col] != 0) or (row == col and multiplication[row][col] != 1):
                return False
    return True
