"""
Tablas de multiplicar:
Escribe un programa que imprima la tabla de multiplicar del 5.
"""

num = 5
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in tabla:
    resultado = i * num
    print(resultado)


for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
