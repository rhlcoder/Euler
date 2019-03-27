from functools import reduce
from itertools import accumulate


# Gracias a este genio: https://stackoverflow.com/a/6800214/4775210
# Da la descripcion detallada de la funcion
def factors(n):
    """ Returns a set of factors of n """
    return set(
        reduce(list.__add__,
               ([i, n // i]
                for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


x = 1
y = 1

while len(factors(y)) < 500:
    y = list(accumulate(range(x + 1)))[-1]
    x += 1

print("number:", y)
