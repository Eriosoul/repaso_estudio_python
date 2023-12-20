"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""


def calcular_area_poligono():
    lado1 = 6
    lado2 = 6
    tiangulo = (lado1 * lado2) / 2
    cuadrado = lado1 * lado2
    rectangulo = lado1 * lado2
    print(tiangulo, cuadrado, rectangulo)


calcular_area_poligono()
