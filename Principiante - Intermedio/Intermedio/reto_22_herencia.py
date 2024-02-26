"""
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Guaw!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Miau!"


my_dog = Dog("Rex")
my_cat = Cat("whiskas")

print(my_dog.name, ":", my_dog.sound())

print(my_cat.name, ":", my_cat.sound())

"""
* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""


# * Implementa la jerarquía de una empresa de desarrollo formada por Empleados
class Empleados:
    # Cada empleado tiene un identificador y un nombre.
    def __init__(self, identificador, nombre: str):
        self.identificador = identificador
        self.nombre = nombre


class Gerente(Empleados):
    def __init__(self, identificdor, nombre):
        super().__init__(identificdor, nombre)
        self.empleados_a_cargo: list = []

    def adjuntar_empleados(self, empleados):
        self.empleados_a_cargo.append(empleados)

    def empleados_a_cargo_del_gerente(self):
        if self.empleados_a_cargo == 0:
            print(f"El gerente {self.nombre} no dispone de ningun empleaod")
        else:
            print(f"Empleados a cargo del gerente {self.nombre}")
            for empleados in self.empleados_a_cargo:
                print(f"Empleados a cargao, nombre: {empleados.nombre}")


class GerenteDeProyectos(Gerente):
    def __init__(self, identificador, nombre):
        super().__init__(identificador, nombre)
        self.identificador = identificador
        self.nombre = nombre

    def gerente_de_pryectos(self):
        print(f"El gerente de los proyectos es {self.nombre}")


class Programadores(Empleados):
    def __init__(self, identificador, nombre: str, lenguajes: str):
        super().__init__(identificador, nombre)
        self.identificador = identificador
        self.nombre = nombre
        self.leguajes = lenguajes

    def tabajadores_dev(self):
        print(f"Los programaodres son: {self.nombre} y dominan el lenguajes de programación: {self.leguajes}")


manager1 = GerenteDeProyectos("M001", "Alice")
manager2 = Gerente("M002", "Bob")
programmer1 = Programadores("P001", "Charlie", "Python")
programmer2 = Programadores("P002", "David", "JavaScript")

# Añadir subordinados al gerente
manager1.adjuntar_empleados(manager2)
manager1.adjuntar_empleados(programmer1)
manager1.adjuntar_empleados(programmer2)

# Mostrar los subordinados del gerente
manager1.empleados_a_cargo_del_gerente()

# Realizar tareas específicas de cada tipo de empleado
manager1.gerente_de_pryectos()
programmer1.tabajadores_dev()
programmer2.tabajadores_dev()
