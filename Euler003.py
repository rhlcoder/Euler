# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143
"""
How to Factor Numbers: Factorization

This factors calculator factors numbers by trial division.
Follow these steps to use trial division to find the factors of a number.

a- Find the square root of the integer number n and round down to the closest whole
    number. Let's call this number s.
b- Start with the number 1 and find the corresponding factor pair: n ÷ 1 = n.
    So 1 and n are a factor pair because division results in a whole number with
    zero remainder.
c- Do the same with the number 2 and proceed testing all integers
    (n ÷ 2, n ÷ 3, n ÷ 4... n ÷ s) up through the square root rounded to s.
    Record the factor pairs where division results in whole integer numbers with zero
    remainders.
d- When you reach n ÷ s and you have recorded all factor pairs you have successfully
    factored the number n.
"""
import math


NUM = 600851475143
raiz_cuadrada_nro = math.floor(math.sqrt(NUM))

def find_factors(num):
  ''' Generador pedorro que toma la variable global calculada arriba y va generando 
      numeros que dan 0 cuando los dividis por el numero ingresado'''
  # malisimo que agarre la variable global "raiz_cuadrada_nro", averiguar como evitarlo
  for i in range(1,raiz_cuadrada_nro+1):
    if num % i == 0:
      yield i

# Filtro los factores que son divisibles por mas de 2 nros (o sea que no son primos)
# Los dos nros serian el 1 y por si mismos
primos = filter(lambda x: len(list(find_factors(x))) == 2, list(find_factors(NUM)))

print('Factores primos:', list(primos))
