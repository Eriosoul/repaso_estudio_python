import json
import pprint
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
        self.book_list = []
        self._id = 0

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

    def read_data(self):
        try:
            with open(self.check_book.library_book, 'r') as file:
                existing_data = json.load(file)
                self.data = existing_data
        except FileNotFoundError:
            self.data = {"Library": []}

    def add_data_to_json(self):
        self.read_data()
        try:
            # Verifica si hay libros en la lista, si no, inicializa la lista
            if "Library" not in self.data:
                self.data["Library"] = []

            # Incrementa el id para cada nuevo libro agregado
            if not self.data["Library"]:
                self._id = 1
            else:
                self._id = self.data["Library"][-1]["Id"] + 1  # Usa el id del último libro como base

            # Crea el diccionario de datos para el nuevo libro
            data = {
                "Id": self._id,
                "Titulo": self.title_book,
                "Autor": self.author_book,
                "Disponibilidad": self.available_book
            }

            # Agrega el nuevo libro a la lista de libros
            self.data["Library"].append(data)

            # Guarda los datos actualizados en el archivo JSON
            with open(self.check_book.library_book, 'w') as file:
                json.dump(self.data, file, indent=4)

            print("¡Libro agregado correctamente!")
        except Exception as e:
            print("Error al agregar el libro:", e)

    def search_book(self):
        self.read_data()
        title = str(input("¿Que libro desea buscar, introduzca su titulo?: "))
        try:
            with open(self.check_book.library_book) as file:
                data = json.load(file)
                library = data.get("Library", [])
                found_books = [book for book in library if book.get("Titulo") == title]
                if found_books:
                    print("\n")
                    for book in found_books:
                        print("Libro encontrado: ")
                        print(f"ID: {book['Id']}")
                        print(f"Título: {book['Titulo']}")
                        print(f"Autor: {book['Autor']}")
                        print(f"Disponibilidad: {book['Disponibilidad']}")
                        print("\n")
                else:
                    print(f"No se encontró ningún libro con el título '{title}'.")
        except Exception as e:
            print("Error:", e)

    def get_book(self):
        self.read_data()
        title = str(input("¿Que libro te quieres llevar, introduce su titulo?: "))
        try:
            with open(self.check_book.library_book) as file:
                data = json.load(file)
                library = data.get("Library", [])

                # Verifica la disponibilidad de los libros
                check_available = [book for book in library if
                                   book.get("Titulo") == title and book.get("Disponibilidad") > 0]
                if check_available:
                    # Actualiza la disponibilidad del libro
                    for book in library:
                        if book.get("Titulo") == title:
                            book["Disponibilidad"] -= 1
                    # Guarda los datos actualizados en el archivo JSON
                    with open(self.check_book.library_book, 'w') as file:
                        json.dump(data, file, indent=4)

                    # Muestra la información del libro retirado
                    for book in check_available:
                        print("¡Libro encontrado!")
                        print(f"ID: {book['Id']}")
                        print(f"Título: {book['Titulo']}")
                        print(f"Autor: {book['Autor']}")
                        print(f"Disponibilidad restante: {book['Disponibilidad']}")
                else:
                    print(f"El libro '{title}' no está disponible.")
        except Exception as e:
            print("Error:", e)

    def get_book_back(self):
        self.read_data()
        try:
            title = str(input("¿Que libro te quieres devolver, introduce su titulo?: "))
            with open(self.check_book.library_book) as file:
                data = json.load(file)
                library = data.get("Library", [])
                check_available =[book for book in library if book.get("Titulo") == title]
                if check_available:
                    for book in library:
                        if book.get("Titulo") == title:
                            book["Disponibilidad"] += 1
                        with open(self.check_book.library_book, 'w') as file:
                            json.dump(data, file, indent=4)
                        for book in check_available:
                            print("¡Libro devuelto correctamente!")
                            print(f"ID: {book['Id']}")
                            print(f"Título: {book['Titulo']}")
                            print(f"Autor: {book['Autor']}")
                            print(f"Disponibilidad restante: {book['Disponibilidad']}")
                else:
                    print(f"El libro '{title}' no se ha podido devolver.")
        except Exception as e:
            print(e)

    def show_all_data(self):
        pp = pprint.PrettyPrinter(indent=4)
        self.read_data()
        try:
            with open(self.check_book.library_book) as file:
                data = json.load(file)
                all_data = data["Library"]
                pp.pprint(all_data)
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
    try:
        while True:
            option = menu()
            if option == 1:
                l.add_book()
                print("mostramos informacion ")
                l.read_data()
                l.add_data_to_json()
            if option == 2:
                l.search_book()
            if option == 3:
                l.get_book()
            if option == 4:
                l.get_book_back()
            if option == 5:
                l.show_all_data()
            if option == 6:
                print("Gracias por visitarnos, vuelva pronto :D")
                break
            else:
                print("Error, no se ha elegido bien la informacion de nuestro menu")
    except KeyboardInterrupt as interrupt:
        print("Se ha interrumpido del programa", interrupt)
    except Exception as e:
        print("Error: ", e)
