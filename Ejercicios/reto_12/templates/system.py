import json

from book import Book
from library_system import LibrarySystem
from Ejercicios.reto_12.check_book_data import CheckBookData


class SystemBook:
    def __init__(self, title, author, available=0):
        self.book = Book(title, author)
        self.library_system = LibrarySystem(available)
        self.check_book = CheckBookData()
        self.title_book = title
        self.author_book = author
        self.available_book = available

    def add_book(self):
        try:
            self.check_book.exist()
            self.title_book = str(input("Introduce el nombre del libro: "))
            self.author_book = str(input("Introduce el autor de dicho libro: "))
            self.available_book = int(input("Introduce la cantidad de libros nuevos: "))
            print(self.title_book, self.author_book, self.available_book)
            return self.title_book, self.author_book, self.available_book
        except Exception as e:
            print(e)

    def struct_add_book(self):
        my_struct = {
            "Nombre del libro": self.title_book,
            "Autor del libro": self.author_book,
            "Disponibilidad": self.available_book
        }
        try:
            # Verificar si el archivo JSON existe
            if not self.check_book.exist():
                print("No se pudo verificar la existencia del archivo JSON.")
                return

            # Obtener la lista de libros del archivo JSON
            with open(self.check_book.library_book, "r") as file:
                book_list = json.load(file)

            # Agregar el nuevo libro a la lista
            book_list.append(my_struct)

            # Escribir la lista actualizada al archivo JSON
            with open(self.check_book.library_book, "a") as file:
                json.dump(book_list, file, indent=4)

            print("¡Libro agregado correctamente!")

        except Exception as e:
            print("Error al agregar el libro:", e)


def menu():
    try:
        print("1.- Agregar libro ")
        print("2.- Buscar libro")
        print("3.- Prestar libro")
        print("4.- Devolver libro")
        print("5.- Mostrar lista de libros")
        print("6.- Salir del programa")
        option = int(input("Seleciona una opcion: "))
        if 1 <= option < 7:
            return option
        else:
            raise ValueError("Opcion invalida. Por favor sleecione una opcion")
    except ValueError as e:
        print("Error al introducir el valor: ", e)


if __name__ == '__main__':
    l = SystemBook(title="", author="", available=0)
    option = menu()
    if option == 1:
        l.add_book()
        print("mostramos informacion ")
        l.struct_add_book()
    else:
        print("error")
