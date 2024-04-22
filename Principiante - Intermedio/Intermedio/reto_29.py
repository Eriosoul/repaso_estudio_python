"""" Generar tabala de multiplicacion de n numero"""

n: int = int(input("Introduce el numero: "))

for i in range(1, 11):
    print(f"{i} * {n} = {i*n}")
