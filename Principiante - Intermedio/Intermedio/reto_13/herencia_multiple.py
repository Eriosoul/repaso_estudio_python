"""
Ejercicio 3: Herencia múltiple

Define tres clases: 'A', 'B' y 'C'. Luego, crea una clase 'D' que herede de 'A' y 'B'.
Finalmente, crea una clase 'E' que herede de 'C' y 'D'.
"""


class A:
    def message(self):
        print("class A")


class B:
    def message(self):
        print("class B")


class C:
    def message(self):
        print("class C")


class D(A, B):
    pass


class E(C, D):
    pass


object_e = E()
object_e.message()
