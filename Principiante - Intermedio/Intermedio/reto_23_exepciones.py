"""
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""


def division():
    try:
        div = 10 / 0
        return div
    except Exception as e:
        print(f"Error: ({type(e).__name__})")
        return None


division()


class StrExeption(Exception):
    pass


def procesar_parametros(parametros: list):
    if len(parametros) < 6:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[2]) == str:
        raise StrExeption(
            "El elemento 3 disponde de una cadena de texto"
        )

    print(parametros[2])
    print(parametros[0]/parametros[2])
    print(parametros[2] + 5)


try:
    procesar_parametros([1, 2, "Erio", 4, 5, 6])
except IndexError as e:
    print("El numero debe ser mayor aque 2")
except ZeroDivisionError as e:
    print("No se puede dividir por 0", e)
except StrExeption as e:
    print(e)
except Exception as e:
    print("Error: ", e)
else:
    print("No se ha producido ningun error")
finally:
    print("El programa ha finalizado")
