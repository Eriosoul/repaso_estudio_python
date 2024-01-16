"""
Reto: Conversor de Temperaturas

Crea un programa que permita al usuario convertir temperaturas entre grados Celsius y Fahrenheit. La aplicación debe realizar las siguientes acciones:

Pedir al usuario que elija entre convertir de Celsius a Fahrenheit o de Fahrenheit a Celsius.
Solicitar la temperatura a convertir.
Realizar la conversión y mostrar el resultado.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 9/5) + 32.

La fórmula para convertir de Fahrenheit a Celsius es: C = (F - 32) * 5/9.

Asegúrate de manejar cualquier entrada incorrecta del usuario y permite que pueda realizar varias conversiones en una sola ejecución.

¡Buena suerte! Si tienes alguna pregunta o necesitas ayuda, estoy aquí para ayudarte.
"""


def celsius_to_fahrenh(temperatura):
    F = (temperatura * 9/5) + 32
    print(F)
    return F


def fahrenh_to_celsius(temperatura):
    C = (temperatura - 32) * 5/9
    print(C)
    return C


def main():
    while True:
        print("=== Menu ===")
        print("Opcion 1: Celsius a Fahrenheit ")
        print("Opcion 2: Fahrenheit a Celsius")
        print("Opcion 3: Salir ")
        option = int(input("Seleciona una opcion:"))
        try:
            if option == 1:
                temperatura = float(input("Introude la temperatura que desea calcular: "))
                celsius_to_fahrenh(temperatura)
            elif option == 2:
                temperatura = float(input("Introude la temperatura que desea calcular: "))
                fahrenh_to_celsius(temperatura)
            elif option == 3:
                print("Gracias por confiar en nosotros ... ")
                break
            else:
                print("Opcion incorrecta ...")
        except TypeError as e:
            print("Error: ", e)
        except Exception as a:
            print(a)


if __name__ == '__main__':
    main()
