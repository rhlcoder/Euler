'''
https://en.wikipedia.org/wiki/Lattice_path
Combinations and NE lattice paths

NE lattice paths have close connections to the number of combinations,
which are counted by the binomial coefficient, (n+k n)
and arranged in Pascal's triangle.
'''
from functools import reduce


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def lattice_path_count(n, k):
    return int(combination(n + k, n))


print(lattice_path_count(20, 20))
