from ex7_helper import *


def mult(x: N, y: int) -> N:
    if y > 0:
        return add(x, mult(x, subtract_1(y)))
    return 0


def is_even(n: int) -> bool:
    if n > 1:
        return is_even(subtract_1(subtract_1(n)))
    return True if n == 0 else False


def log_mult(x: N, y: int) -> N:
    if y == 0:
        return 0

    if is_odd(y):
        return add(x, log_mult(x, divide_by_2(y)) * 2)

    return log_mult(x, divide_by_2(y)) * 2


def log_div(x: N, y: int) -> N:
    if is_odd(y):
        return add(x, log_mult(log_div(x, subtract_1(y)), 2))

    return log_mult(log_div(x, divide_by_2(y)), 2)


def is_power(b: int, x: int, power=1) -> bool:
    if b == 0:
        return True if x == 1 else False
    if power == x:
        return True
    if power > x:
        return False
    return is_power(b, x, log_mult(power, b))


def reverse(s, index=None, reversed_string=""):
    if index is None:
        index = len(s) - 1
    if index < 0:
        return reversed_string
    return reverse(s, index - 1, append_to_end(reversed_string, s[index]))


def count_ones_in_number(n: int) -> int:
    if n == 0:
        return 0
    if n % 10 == 1:
        return 1 + count_ones_in_number(n // 10)
    return count_ones_in_number(n // 10)


def number_of_ones(n: int) -> int:
    return 0 if n == 0 else count_ones_in_number(n) + number_of_ones(n - 1)


def compare_2d_lists(l1, l2) -> bool:
    if not l1 and not l2:
        return True
    if not l1 or not l2 or len(l1) != len(l2):
        return False
    return False if l1[0] != l2[0] else compare_2d_lists(l1[1:], l2[1:])


def deep_copy_list(lst) -> list[any]:
    if not lst:
        return []
    elif isinstance(lst[0], list):
        return [deep_copy_list(lst[0])] + deep_copy_list(lst[1:])
    else:
        return lst


def magic_list(n) -> list[any]:
    if n == 0:
        return []
    return magic_list(n - 1) + [deep_copy_list(magic_list(n - 1))]


def play_hanoi(hanoi, n, src, dest, temp):
    if n <= 0:
        return None
    if n == 1:
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)
