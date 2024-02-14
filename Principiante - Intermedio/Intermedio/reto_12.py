"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
*/
"""


def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


countdown(100)


"""
/*
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
*/
"""


def calculate_factorial(numbrer: int) -> int:
    try:
        if numbrer < 0:
            return 0
        elif numbrer == 0:
            return 1
        else:
            return numbrer * calculate_factorial(numbrer - 1)
    except Exception as e:
        print(f"Ha ocurrido un error {e}")


print(calculate_factorial(10))


def calculate_fibonacci(number: int) -> int:
    if number <= 0:
        print("La información es 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        f = calculate_fibonacci(number - 1) + calculate_fibonacci(number - 2)
        print("calculando:", f)
        return f


calculate_fibonacci(10)
