# The first edge case checks negative values and the second edge case check for equal values
def largest_and_smallest(num1: float, num2: float, num3: float):
    """Returns the largest and smallest numbers."""
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    return largest, smallest


def check_largest_and_smallest():
    if largest_and_smallest(17, 1, 11) != (17, 1):
        return False
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    if largest_and_smallest(1, -1, 0) != (1, -1):
        return False
    if largest_and_smallest(1, 1, 1) != (1, 1):
        return False
    return True
