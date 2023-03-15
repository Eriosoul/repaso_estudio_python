valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5
# no puede ser menor que 0 y si el valor es <= 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro de rango')

# operador or
vacaciones = True
diaDescanso = False
if vacaciones or diaDescanso:
    print('puede asistir al juego')
else:
    print('tiene deberes de hacer')

# operador not
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print('tiene deberes de hacer')
else:
    print('puede asistir al juego')