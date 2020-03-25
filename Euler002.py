from functools import reduce
from itertools import takewhile


def fib(n):
	''' Clasica funcion recursiva de fibonacci '''
	if n in (1, 2):
		return 1
	else:
		return fib(n - 2) + fib(n - 1)


def crear_lista_fibonacci_hasta_valor(n):
	''' Crea una lista de fibonaccis con valor maximo n '''
	lista = []
	i = 1
	while (fib(i) < n):
		lista.append(fib(i))
		i += 1
	return lista


# otra manera usando un generador con yield este esta mas bueno porque luego
# decido si necesito una lista o prefiero generar otra estructura de datos (como set())
def crear_generador_fibonacci_hasta_valor(n):
	''' Crea una generador de fibonaccis con valor maximo n '''
	i = 1
	while (fib(i) < n):
		yield fib(i)
		i += 1


print(list(crear_generador_fibonacci_hasta_valor(1000)))

# El set no sirve porque elimina el "1" duplicado al principio
print(set(crear_generador_fibonacci_hasta_valor(1000)))

lista_valores = crear_lista_fibonacci_hasta_valor(1000)
lista_valores_pares = list(filter(lambda x: x % 2 == 0, lista_valores))
suma_valores_pares = reduce(lambda a, b: a + b, lista_valores_pares)

print(lista_valores)
print("El resultado de sumar todos los valores pares es:", suma_valores_pares)

# Usando numpy, dicen que es la mejor forma, igual no entiendo nada
from numpy import matrix

def fibo(n):
  return (matrix('0 1; 1 1' if n >= 0 else '-1 1; 1 0', object) ** abs(n))[0, 1]
    
print(fibo(16))
