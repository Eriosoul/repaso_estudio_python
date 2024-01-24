"""
Ejercicio: Sistema de Gestión de Biblioteca
Crea un sistema de gestión de biblioteca en Python. Aquí hay algunas funciones que puedes implementar:

Agregar Libro:

Permite al usuario agregar un nuevo libro a la biblioteca. Cada libro debe tener un título, autor y número de copias disponibles.
Buscar Libro:

Permite al usuario buscar un libro por título o autor y mostrar la información disponible.
Prestar Libro:

Permite al usuario prestar un libro. Debes tener en cuenta el número de copias disponibles.
Devolver Libro:

Permite al usuario devolver un libro. Asegúrate de manejar correctamente las devoluciones y actualizar la cantidad de copias disponibles.
Mostrar Lista de Libros:

Muestra una lista de todos los libros disponibles en la biblioteca.
Salir del Programa:

Proporciona una opción para que el usuario salga del programa.
"""


def menu():
    try:
        print("1.- Agregar libro ")
        print("2.- Buscar libro")
        print("3.- Prestar libro")
        print("4.- Devolver libro")
        print("5.- Mostrar lista de libros")
        print("6.- Salir del programa")
        option = int(input("Seleciona una opcion: "))
        if 1 < option < 7:
            return option
        else:
            raise ValueError("Opcion invalida. Por favor sleecione una opcion")
    except ValueError as e:
        print("Error al introducir el valor: ", e)


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt as interrupt:
        print("\nSe ha detenido el programa: ", interrupt)
    except Exception as e:
        print(e)
