#!/usr/bin/python3
from typing import List


def prime(n: int) -> bool:
    """a function that detects prime number"""
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def minOperations(n: int) -> int:
    """a function that calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    counter = 0
    if not prime(n):
        while n > 1:
            if n % 2 == 0:
                n /= 2
                counter += 2
            else:
                n -= 1
                counter += 1
    else:
        return n
    return counter
