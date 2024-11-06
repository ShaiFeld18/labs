import math


def golden_ratio():
    """This function prints the golden ratio"""
    print((1 + math.sqrt(5)) / 2)


def six_squared():
    """This function prints the square of 6"""
    print(6 ** 2)


def hypotenuse():
    """This function prints the length of the hypotenuse in a 5*12 triangle"""
    print(math.sqrt((5 ** 2) + (12 ** 2)))


def pi():
    """This function prints pi"""
    print(math.pi)


def e():
    """This function prints e"""
    print(math.e)


def squares_area():
    """This function print the areas of the squares with sides from 1 to 10"""
    print(" ".join(f"{i ** 2}" for i in range(1, 11)))


if __name__ == '__main__':
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
