import math


def quadratic_equation(a, b, c):
    """This function solves quadratic equation."""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        first_root, second_root = None, None
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        first_root = (-b + sqrt_discriminant) / (2 * a)
        second_root = (-b - sqrt_discriminant) / (2 * a)
    if first_root == second_root:
        return first_root, None
    return first_root, second_root


def quadratic_equation_user_input():
    coefficients = input("Insert coefficients a, b, and c: ").split(' ')
    if coefficients[0] == '0':
        print("The parameter 'a' may not equal 0")
    else:
        sol_1, sol_2 = quadratic_equation(*map(float, coefficients))
        if sol_1 and sol_2:
            print(f"The equation has 2 solutions: {sol_1} and {sol_2}")
        elif sol_1 and not sol_2:
            print(f"The equation has 1 solution: {sol_1}")
        else:
            print("The equation has no solutions")
