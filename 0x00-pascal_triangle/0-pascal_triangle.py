#!/bin/usr/python3


# factorial function definition
def factorial(n: int):
    value = 1
    while n > 0:
        value *= n
        n -= 1
    return value


# combination function definition
def combination(n: int):
    comb_list = []
    r = 0
    while n - r > 0 or r == n:
        comb = int(factorial(n) / (factorial(n - r) * factorial(r)))
        comb_list.append(comb)
        r += 1
    return comb_list


# pascal triangle definition
def pascal_triangle(n: int):
    pascal = []
    k = 0
    if n <= 0:
        return []
    while k < n:
        pascal.append(combination(k))
        k += 1
    return pascal
