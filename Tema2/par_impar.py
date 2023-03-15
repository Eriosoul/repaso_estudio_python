numero = int(input("Introduzca un numero: "))
print(numero % 2)
# si el resto del numero que se ha dividio entre 2 es 0 es par
if numero % 2 == 0:
    print(f'El {numero} es par')
else:
    print(f'El {numero} es impar')