"""
Promedio de una lista:
Escribe un programa que calcule el promedio de una lista de números.
"""

numeros = [4, 8, 15, 16, 23, 42]
count = 0
suma = 0
for i in numeros:
    count += 1
    suma += i
    num = count

print(f"La lsita tine: {num} numeros y la suma de todos ellos es: {suma}")
print(f"El promedio de la lista es  {suma / num}")


# simplificado

numeros = [4, 8, 15, 16, 23, 42]
suma = sum(numeros)
num = len(numeros)

print(f"La lista tiene: {num} números y la suma de todos ellos es: {suma}")
print(f"El promedio de la lista es {suma / num}")
