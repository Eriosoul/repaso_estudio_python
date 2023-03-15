"""
    Imprimir numeros de 5 a 1 de manera decendiente usando funciones recursivas
    Puede ser cualquier valor positivo
"""


def funcionRecursiva(numero):
    if numero >= 1:
        print(numero)
        funcionRecursiva(numero - 1)
    else:
        print('Valor incorrecto')


funcionRecursiva(5)