#!/usr/bin/python3
"""0-minoperations.py"""

def minOperations(n):
    """ calculates the fewest number of operations needed to result
    in exactly n H characters in the file"""
    if n <= 1:
        return n
    min_ops = [0] * (n + 1)
    for i in range(2, n + 1):
        min_ops[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)
    return min_ops[n]
