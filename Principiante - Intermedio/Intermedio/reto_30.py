"""
Crea un programa en Python que simule un sistema de gestión de tareas.
Deberías tener una clase Tarea que represente una tarea en el sistema. La clase Tarea debe tener los siguientes atributos:

nombre: El nombre de la tarea.
descripcion: Una descripción de la tarea.
fecha_limite: La fecha límite para completar la tarea.
Además, la clase Tarea debe tener métodos para:

Mostrar la información de la tarea en un formato legible.
Crea una clase principal llamada GestorTareas que tenga los siguientes métodos:

agregar_tarea(): Para agregar una nueva tarea al sistema. Debe tomar el nombre, la descripción y la fecha límite como entrada y crear un nuevo objeto Tarea.
mostrar_tareas(): Para mostrar la información de todas las tareas en el sistema.

"""


class Tarea:
    def __init__(self, nombre, descripcion, fecha_limite):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Fecha límite: {self.fecha_limite}")


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion, fecha_limite):
        tarea = Tarea(nombre, descripcion, fecha_limite)
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            print("Lista de tareas:")
            for tarea in self.tareas:
                tarea.mostrar_informacion()


if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre de la tarea: ")
            descripcion = input("Breve descripción de la tarea: ")
            fecha_limite = input("Fecha límite de la tarea: ")
            gestor.agregar_tarea(nombre, descripcion, fecha_limite)
            print("Tarea agregada exitosamente.")
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
