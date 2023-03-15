"""
    Ejercicio: Convertidor de Temperatura
    Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""

# Mi codigo
def conversor_de_grados(opcion: int, grados: float):
    if opcion == 1:
        calendar_celsius = (grados * 9 / 5) + 32
        return calendar_celsius
    elif opcion == 2:
        calendar_fahrenheit = (grados - 32) * 5 / 9
        return calendar_fahrenheit
    else:
        print('Error dichos datos no pueden ser')
        return


opcion = int(input("Si desea calcular celsius pulse 1 si dese calcular fahrenheit pulse 2 : "))
grados = float(input('Introduzca lso grados: '))
opcionselcionada = conversor_de_grados(opcion, grados)
print(f'Ha selecionado: {opcionselcionada:.02f}')


# RESPUESTA DEL PROFESOR
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius = float(input('Proporcione el valor en celsius: '))
resultado =  celsius_fahrenheit(celsius)
print(f'{celsius} C a F: {resultado:.02f}')

fahrenheit = float(input('Proporcione el valor en fahrenheit: '))
resultado =  celsius_fahrenheit(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.02f}')