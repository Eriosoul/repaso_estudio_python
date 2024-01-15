"""
Reto: Calculadora de Estadísticas

Crea una calculadora de estadísticas básicas. La aplicación debe permitir al usuario ingresar una lista de números y luego mostrar:

La media (promedio) de los números.
La mediana de los números.
La moda de los números.
El rango (diferencia entre el número más grande y el más pequeño).
"""

# Mi respuesta
# def max_num():
#     numbers_list = []
#     num = int(input("¿Cuantos numeros desea introducir?"))
#     for _ in range(num):
#         num_to_list = int(input("Introduce el numero: "))
#         numbers_list.append(num_to_list)
#
#     print(numbers_list)
#     suma_total = sum(numbers_list)
#     print(f"La suma total de los números es: {suma_total}")
#     div_promedio = suma_total / num
#     print(f"El promedio es : {div_promedio}")
#     max_num = max(numbers_list)
#     min_num = min(numbers_list)
#     dif_num = max_num - min_num
#     print(f"El numer maximo es {max_num}, El numero minimo es {min_num} -- El rango entre los numeros es {dif_num}")
#
#
# if __name__ == '__main__':
#     max_num()


# Respiuesta del ejercicio

from statistics import mean, median, mode, StatisticsError


def calcular_estadisticas():
    numbers_list = []
    num = int(input("¿Cuántos números desea introducir?"))

    for _ in range(num):
        num_to_list = int(input("Introduce el número: "))
        numbers_list.append(num_to_list)

    # Calcular la media
    promedio = mean(numbers_list)
    print(f"La media (promedio) de los números es: {promedio}")

    # Calcular la mediana
    mediana = median(numbers_list)
    print(f"La mediana de los números es: {mediana}")

    # Calcular la moda
    try:
        moda = mode(numbers_list)
        print(f"La moda de los números es: {moda}")
    except StatisticsError:
        print("No hay una moda, todos los números son únicos.")

    # Calcular el rango
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    rango = max_num - min_num
    print(f"El número máximo es {max_num}, el número mínimo es {min_num}, y el rango es {rango}")


if __name__ == '__main__':
    calcular_estadisticas()
