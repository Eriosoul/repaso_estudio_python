'''
    Ciclo for
'''

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')

for letra in cadena:
    if letra == 'l':
        print(letra)
        break
    print(letra)
else:
    print('Fin ciclo for')

# ejemplo de continue
# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor par: {i}')

for i in range(6):
    if i % 2 != 0: # si el valor de i no es divisible entre 2 continua
        continue
    print(f'Valor: {i}') # solo se imprimira los pares
