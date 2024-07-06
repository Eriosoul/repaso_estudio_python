"""
Números pares en un rango:
Escribe un programa que imprima todos los números pares del 1 al 20.
"""

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


for i in range(2, 21, 2):
    print(i)
