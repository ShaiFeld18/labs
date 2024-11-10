import math


def circle_area(radius: float):
    return math.pi * radius ** 2


def rectangle_area(width: float, height: float):
    return width * height


def equilateral_triangle_area(side: float):
    return math.sqrt(3) / 4 * side ** 2


def shape_area():
    shape_index = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape_index not in [1, 2, 3]:
        return None
    if shape_index == 1:
        area = circle_area(float(input()))
    elif shape_index == 2:
        area = rectangle_area(float(input()), float(input()))
    elif shape_index == 3:
        area = equilateral_triangle_area(float(input()))
    return area
