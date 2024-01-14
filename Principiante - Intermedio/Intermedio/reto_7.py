"""
Reto: Calculadora de Estadísticas

Crea una calculadora de estadísticas básicas. La aplicación debe permitir al usuario ingresar una lista de números y luego mostrar:

La media (promedio) de los números.
La mediana de los números.
La moda de los números.
El rango (diferencia entre el número más grande y el más pequeño).
"""


def max_num():
    numbers_list = []
    num = int(input("¿Cuantos numeros desea introducir?"))
    for _ in range(num):
        num_to_list = int(input("Introduce el numero: "))
        numbers_list.append(num_to_list)

    print(numbers_list)
    suma_total = sum(numbers_list)
    print(f"La suma total de los números es: {suma_total}")
    div_promedio = suma_total / num
    print(f"El promedio es : {div_promedio}")
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    dif_num = max_num - min_num
    print(f"El numer maximo es {max_num}, El numero minimo es {min_num} -- El rango entre los numeros es {dif_num}")

if __name__ == '__main__':
    max_num()
