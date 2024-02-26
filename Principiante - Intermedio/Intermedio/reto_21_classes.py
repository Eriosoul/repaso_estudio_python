"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
"""


class Programmer:
    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def mostrar_datos(self):
        print(f"Nombre: {self.name} {self.surname}| Edad: {self.age} | Lenguajes: {self.languages}")


my_programer = Programmer("Erio", 26, ["Python", "Java", "C++"])
my_programer.mostrar_datos()
my_programer.surname = "Soul"
my_programer.mostrar_datos()
my_programer.age = 27
my_programer.mostrar_datos()


class Stack:
    def __init__(self):
        self.stack: list = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def show_data(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
my_stack.count()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO first in first out


class Queue:
    def __init__(self):
        self.queue: list = []

    def equeue(self, item):
        self.queue.append(item)

    def deequeue(self):
        # se hace pop a 0 que es el primer elemento
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

    def show_data(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
my_queue.equeue("D")
my_queue.show_data()
print(my_queue.count())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.count())
