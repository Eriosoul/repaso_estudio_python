"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""


# def incremento_numeros():
#     for number in range(2, 101):
#         if primos(number):
#             yield number
#
#
# for primo in incremento_numeros():
#     print(primo)


# def primos(num):
#     if num < 2:
#         return False
#     for _ in range(2, num):
#         if num % _ == 0:
#             return False
#     return True
#
#
# for num in range(2, 101):
#     if primos(num):
#         print(num)


def primos():
    for num in range(1, 101):
        if num >= 2:
            es_divisible = False
            for _ in range(2, num):
                if num % _ == 0:
                    es_divisible = True
            if not es_divisible:
                print(num)


primos()
