import os
import json


class CheckBookData:
    def __init__(self):
        self.library_book = "library_book.json"

    def exist(self):
        if os.path.exists(self.library_book):
            try:
                with open(self.library_book, 'r') as file:
                    json.load(file)
            except ValueError as err:
                print("Error:", err)
                return False
            return True
        else:
            # Si el archivo no existe, créalo
            with open(self.library_book, 'w') as file:
                json.dump({}, file)
            print(f"Archivo {self.library_book} creado.")
            return True


if __name__ == '__main__':
    c = CheckBookData()
    c.exist()
