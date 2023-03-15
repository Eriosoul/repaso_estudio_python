# como no sabemos la cantidad de nombres se pone el *
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


# se creara una tupla con dichos nombres
listarNombres('Juan', 'Laura', 'Karla', 'Didi', 'Lucy')
listarNombres('Laura', 'Carlos')

"""
    suma de varios valores recibidos de tipo numerico,
    utilizando argumentos variables *args como parametro de la funcion
    y regresa como resultado la suma de todo los valores pasados como argumento
"""


def miSuma(*args) -> int:
    resultado = 0
    for valor in args:
        # print(valor)
        resultado += valor
    return resultado


print(miSuma(1, 5, 6, 7, 89, 100))


def miMultiplicacion(*args) -> int:
    resultado = 1
    for valor in args:
        # print(valor)
        resultado *= valor
    return resultado


print(miMultiplicacion(1, 5, 6, 7, 89, 100))
