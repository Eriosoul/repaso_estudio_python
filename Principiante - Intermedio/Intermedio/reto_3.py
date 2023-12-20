"""
* Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…
# El 1 se obtiene sumando  0 + 1= 1   /  el 2 se calcula sumando 1+1  /  análogamente, el 3 es 1+2  /   el 5 es 2+3


def fibonacci():
    prev = 0
    next = 1

    for _ in range(0, 50):
        print(_, prev)
        # suma de los numeros prev y next
        fib = prev + next
        # pasamos el valor de next a prev
        prev = next
        # pasamos el valor de la suma a next
        next = fib



print(fibonacci())
