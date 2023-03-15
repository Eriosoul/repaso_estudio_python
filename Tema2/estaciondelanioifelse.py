mes = int(input("Introduce el numero del mes(1 / 12) y se le indicara la estacion: "))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif estacion == 9 or estacion == 10 or estacion == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estación es: {estacion}')