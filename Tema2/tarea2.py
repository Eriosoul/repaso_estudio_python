"""
Solicitar al usuario dos valores y determinar cual es el mayor
"""
numero1 = int(input('Introduce el primer numero: '))
numero2 = int(input('Introduce el segundo numero: '))

if numero1 > numero2:
    print(f'El mayor numero es {numero1}')
elif numero2 > numero1:
    print(f'El mayor numero es {numero2}')
else:
    print(f'Los nummeros {numero1} {numero2} son iguales')