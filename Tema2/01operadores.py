# SUMA
operadorA = 3
operadorB = 2
suma = operadorA + operadorB
print("El resultado de la suma: ", suma)
print(f'Resultado suma: {suma}') # aqui se hace una incorporacion de variables en una cadena

# RESTA
resta = operadorA - operadorB
print(f'Resultado resta: {resta}')

# MULTIPLICACIÓN
multiplicacion = operadorA * operadorB
print(f'Resultado multiplicacion: {multiplicacion}')

# DIVISIÓN
division = operadorA / operadorB
print(f'Resultado de la division (float): {division}')
division = operadorA // operadorB
print(f'Resultado division (int): {division}')

# RESATO = modulo
modulo = operadorA % operadorB
print(f'Resultado del moduo: {modulo}')

# exponente 3 al cuadrado
exponente  = operadorA ** operadorB
print(f'Resultaod del exponente: {exponente}')

# bool
a = True
b = False
resultado = a and b # tienen que ser los 2 verdaderos
print(resultado)
resultado = a or b # si uno es verdadero
print(resultado)
resultado = not a # Invierto el valor de la variable a
print(resultado)