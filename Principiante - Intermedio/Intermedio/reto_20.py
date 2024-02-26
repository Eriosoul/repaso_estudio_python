"""
24 máximo común divisor (MCD) y mínimo común múltiplo (mcm)
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""


def func_mcd(num: int, num2: int):
    while num2 != 0:
        num, num2 = num2, num % num2
    return num


def func_mcm(num: int, num2: int):
    return (num * num2) / func_mcd(num, num2)


num1 = 152
num2 = 180

mcd = func_mcd(num1, num2)
mcm = func_mcm(num1, num2)

print("MCD:", mcd)
print("MCM:", mcm)
