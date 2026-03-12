import math
import sys


def add_numbers(a, b):
    result = a + b
    print("The result is:", result)
    return result


def circle_area(radius):
    area = math.pi * radius * radius
    print("Area:", area)
    return area


x = add_numbers(5, 10)
y = circle_area(7)