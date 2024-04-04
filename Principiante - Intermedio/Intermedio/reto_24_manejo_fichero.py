"""
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""

import os


def first_file():
    filename = "primer_fichero.txt"
    if not os.path.exists(filename):
        with open(filename, 'a+'):
            print("Fichero creado")
    else:
        print(f"Fichero existente: {filename}")

    # name = input("Introduce el nombre: ")
    # age = input("Introduce la edad: ")
    # fav_dev_lang = input("Introduce tu lenguaje favorito: ")
    name = "pepe"
    age = 27
    fav_dev_lang = "Python"
    with open(filename, 'a+') as file:
        file.write(f"Nombre: {name}\n")
        file.write(f"Edad: {age}\n")
        file.write(f"Lenguaje Favorito: {fav_dev_lang}\n")

    with open(filename, 'r') as file:
        print(file.read())

    os.remove(filename)


first_file()

"""
* DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
"""

filename = "prueba24.txt"
open(filename, "a")


while True:
    print("1. Añadir producto ")
    print("2. Consultar producto ")
    print("3. Actualizar producto ")
    print("4. Borrar producto ")
    print("5. Calculo total ")
    print("6. Venta por producto ")
    print("7. Mostrar todos los productos ")
    print("8. Salir...")
    option = input("Seelcciona una opcion: ")
    if option == "1":
        name: str = input("Name: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(filename, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")
            print("Datos escritos")
    elif option == "2":
        name = input("Nombre del producto: ")
        with open(filename, 'r') as file:
            for line in file.readlines():
               if line.split(", ")[0] == name:
                   print(line)
    elif option == "3":
        name: str = input("Name: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, "w") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name: str = input("Name: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
            with open(filename, "w") as file:
                for line in file.readlines():
                    if line.split(", ")[0] != name:
                        file.write(line)

    elif option == "5":
        total = 0
        with open(filename, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = components[1]
                price = components[2]
                total += quantity * price
        print(total)
    elif option == "6":
        name = input("Nombre: ")
        total = 0
        with open(filename, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = components[1]
                    price = components[2]
                    total += quantity * price
                    break
        print(total)
    elif option == "7":
        with open(filename, "r") as file:
            print(file.read())
    elif option == "8":
        os.remove(filename)
        break
    else:
        print("La opcion selecionada no es valida")
