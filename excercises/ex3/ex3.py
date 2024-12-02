def input_list():
    """Receives numbers from the user until an empty string is received and returns a list containing them"""
    numbers = []
    inputs_sum = 0
    user_input = input()
    while user_input != "":
        number = float(user_input)
        numbers.append(number)
        inputs_sum += number
        user_input = input()
    return numbers + [inputs_sum]


def inner_product(vec_1, vec_2):
    """Input: two vectors. Output: inner product of the vectors"""
    inner_product = 0
    if len(vec_1) != len(vec_2):
        return None
    for i in range(len(vec_1)):
        inner_product += vec_1[i] * vec_2[i]
    return inner_product


def sequence_monotonicity(sequence):
    """
    Returns a boolean value for each of the next definitions:
    1) Increasing
    2) Strictly Increasing
    3) Decreasing
    4) Strictly Decreasing
    """
    monotonicities = [True, True, True, True]
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            monotonicities[0] = False
        if sequence[i] >= sequence[i + 1]:
            monotonicities[1] = False
        if sequence[i] < sequence[i + 1]:
            monotonicities[2] = False
        if sequence[i] <= sequence[i + 1]:
            monotonicities[3] = False
    return monotonicities


def filter_list(num_list, operator, number):
    """
    Gets a list of numbers, an operator (=, <, >) and a number.
    returns a filtered list with the numbers that satisfy the operator
    """
    filtered_list = []
    for i in num_list:
        if operator == "=":
            condition = i == number
        elif operator == ">":
            condition = i > number
        elif operator == "<":
            condition = i < number
        if condition:
            filtered_list.append(i)
    return filtered_list


def cycle_sublist(lst, start, step):
    """
    Returns a sublist with values from the original list base on the starting index and steps until
    it passes the initial index once.
    """
    sublist = []
    index = start
    while index < len(lst):
        sublist.append(lst[index])
        index += step
    index = index % len(lst)
    while index < start:
        sublist.append(lst[index])
        index += step
    return sublist


def convolve(mat: list[list[float]]):
    """Receives a matrix and returns the convolution of the matrix"""
    if not mat:
        return None
    conv = []
    for row in range(len(mat) - 2):
        conv.append([])
        for col in range(len(mat[0]) - 2):
            conv[row].append(
                mat[row][col] + mat[row][col + 1] + mat[row][col + 2] +
                mat[row + 1][col] + mat[row + 1][col + 1] + mat[row + 1][col + 2] +
                mat[row + 2][col] + mat[row + 2][col + 1] + mat[row + 2][col + 2]
            )
    return conv


def num_of_orthogonal(vectors: list[list[float]]):
    """Receives a list of vectors and returns the number of orthogonal vectors"""
    orthogonal_vectors_counter = 0
    for first_vector_index in range(len(vectors)):
        for other_vector in vectors[first_vector_index + 1:]:
            if inner_product(vectors[first_vector_index], other_vector) == 0:
                orthogonal_vectors_counter += 1
    return orthogonal_vectors_counter


if __name__ == '__main__':
    print(
        num_of_orthogonal([[1,1,1,1], [2,1,3,3], [0, 0, 100, 33], [8, 8, 8, 1.5], [9,9,9,9]])
    )
