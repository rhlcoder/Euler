'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time
start = time.time()


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def collatz_length(n):
    result = 0
    length = 1
    while result != 1:
        result = collatz(n)
        n = result
        length += 1
    return length


lista = [(i, collatz_length(i)) for i in range(999, 0, -1)]
biggest = max(lista, key=lambda x: x[1])

print(  # Probando string formatting al modo python 3.6
    f"The longest chain is {biggest[1]}, produced by the number {biggest[0]}")

end = time.time()


def tiempo_transcurrido(start, end):
    tiempo = end - start
    if tiempo < 1:
        return f"{tiempo * 1000} ms"
    else:
        return f"{tiempo} s"


print(tiempo_transcurrido(start, end))
