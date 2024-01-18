"""
Ejercicio: Calculadora de Propinas

Crea una calculadora de propinas que solicite al usuario el monto de la factura y el porcentaje de propina que
 desea dejar. La aplicación debe calcular la propina y mostrar el monto total, incluida la propina.

Requisitos:
Propina= 100 Factura×Porcentaje
                ​



La aplicación debe manejar excepciones para garantizar que el usuario ingrese valores numéricos válidos.
Asegúrate de que el porcentaje de propina esté en el rango de 0% a 100%.
Muestra el resultado de una manera clara y legible.
"""


def get_factura():
    while True:
        try:
            factura = float(input("Introduzca la factura: "))
            return factura
        except ValueError:
            print("Se debe introducir un numero, puede contener decimales")


def get_procentaje_propina():
    while True:
        try:
            porcentaje = float(input("Introduzca el porcentaje de propina: "))
            if 0.00 < porcentaje <= 100.00:
                print(porcentaje)
                return porcentaje
            else:
                print("Error al introducir el porcentaje de propina")
        except ValueError:
            print("Se debe introducir un numero, puede contener decimales")


def calcular_poropina(factura, porcentaje):
    propina = (factura * porcentaje) / 100
    print("La propina es: ", propina)
    return propina


def monoto_total(propina, factura):
    total = factura + propina
    print("El total es: ", total)
    return total


if __name__ == '__main__':
    try:
        factura = get_factura()
        porcentaje = get_procentaje_propina()
        propina = calcular_poropina(factura, porcentaje)
        monoto_total(factura, propina)
    except Exception as e:
        print(e)
