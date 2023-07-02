#!/usr/bin/python3
import math

""" another way using n!/((n-k)! * k!) to generate
coefficients but requires importing maths.
"""


def pascal_triangle(n):
    """
    a function that takes in an integer n

    parameters:
        n(int) - input number of rows to generate

    Return:
        triangle - pascals triangle of be generated
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            coefficient = (math.factorial(i) //
                           (math.factorial(j) * math.factorial(i - j)))

            row.append(coefficient)
            " add coeffient to that row empty array "
        triangle.append(row)

    return triangle