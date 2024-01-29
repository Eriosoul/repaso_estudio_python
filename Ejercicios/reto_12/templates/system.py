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
        except Exception as e:
            print(e)


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
    else:
        print("error")
