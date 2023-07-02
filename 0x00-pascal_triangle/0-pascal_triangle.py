#!/usr/bin/python3


def factorial(n: int) -> int:
    """Returns the factorial of a given integer n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def combination(n: int) -> list:
    """Returns a list of combinations up to a given integer n."""
    comb_list = []
    for r in range(n + 1):
        comb = factorial(n) // (factorial(n - r) * factorial(r))
        comb_list.append(comb)
    return comb_list


def pascal_triangle(n: int):
    """Returns Pascal's Triangle up to a given integer n."""
    pascal = []
    if not isinstance(n, int) or n <= 0:
        return pascal
    for k in range(n):
        pascal.append(combination(k))
    return pascal
