edad = int(input("Que edad tienes: "))

if edad <= 17:
    print(f"Usted es menor de edad : {edad}")
else:
    print(f"Usted es mayor de edad : {edad}")

edad2 = int(input('Introduce tu edad: '))
veintes = edad2 >= 20 and edad2 < 30
print(veintes)
treintas = edad2 >= 30 and edad2 <40
print(treintas)
# if anidado
# if (edad2 >= 20 and edad2 < 30) or (edad2 >= 30 and edad2 <40) pero se pierde detalle del if
if veintes or treintas:
    # print(f'Dentro de rango (20s) o (30s) ')
    if veintes:
        print("Dentro de los 20s")
    elif treintas:
        print("Dentro de los 30s")
else:
    print('fuera de rango')
