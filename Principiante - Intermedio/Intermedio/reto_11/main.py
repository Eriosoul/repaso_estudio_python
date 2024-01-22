from pprint import pprint

"""
Ejercicio: Sistema de Gestión de Tareas
Crea un programa en Python para gestionar tareas. Debe permitir al usuario realizar las siguientes operaciones:

Agregar Tarea: El usuario puede agregar una nueva tarea. Cada tarea debe tener un nombre y una descripción.

Listar Tareas: Mostrar todas las tareas existentes.

Marcar Tarea como Completada: Permitir al usuario marcar una tarea como completada. Si una tarea está marcada como
completada, debería aparecer en la lista de tareas completadas.

Eliminar Tarea: Permitir al usuario eliminar una tarea.

Salir del Programa: Salir del programa.

Puedes estructurar el programa utilizando funciones para cada operación. Utiliza un diccionario para almacenar las
tareas, donde la clave sea el nombre de la tarea y el valor sea una tupla con la descripción y un indicador de si
está completada o no.
"""

work_system = [
    {
        "id": 1,
        "name_work": "Sistemas de procesamiento de transacciones",
        "description_work": "Los sistemas de procesamiento de transacciones (TPS por sus siglas en inglés) son los sistemas empresariales básicos que sirven al nivel operacional de la organización.",
        "status": "completada"
    },
    {
        "id": 2,
        "name_work": "Otra tarea",
        "description_work": "Descripción de otra tarea.",
        "status": "pendiente"
    },
]


def create_work():
    try:
        name_work = str(input("Introduce el nombre de la tarea: "))
        description_work = str(input("Introduce la descripcion de la tarea: "))
        status_work = str(input("Introduzca el estado de la tarea (Completada o Pendiente): "))
        print(name_work, ":", description_work, status_work)
        return name_work, description_work, status_work
    except ValueError as e:
        print("Error a la hora de introducir la informacion: ", e)


def add_data(name_work, description_work, status_work):
    last_id = max(task["id"] for task in work_system)
    new_id = last_id + 1
    print(last_id)
    print("nuevo id", new_id)
    new_task_data = {
        "id": new_id,
        "name_work": name_work,
        "description_work": description_work,
        "status": status_work
    }
    work_system.append(new_task_data)
    print("Nueva tarea añadida:")
    print(new_task_data)


def show_all_data():
    for task_id in work_system:
        print(task_id)


def menu():
    try:
        print("1. Para crear una tarea")
        print("2. Mostrar todas las tareas existentes ")
        print("3. Marcar Tarea como Completada")
        print("4. Permitir al usuario eliminar una tarea")
        print("5. Salir del programa")
        option = int(input("Seleccione su opcion: "))
        return option
    except ValueError as e:
        print("Error al introducir el valor: ", e)


if __name__ == '__main__':
    try:
        while True:
            option = menu()

            if option == 1:
                data = create_work()
                # Usar *data al llamar a add_data desempaqueta los elementos de la tupla y
                # los pasa como argumentos individuales a la función add_data.
                add_data(*data)
                print("Lista de tareas actualizada:")
                pprint(work_system)
            elif option == 2:
                show_all_data()
            elif option == 3:
                pass
            else:
                print("Error a la hora de selccionar la opcion...")
    except KeyboardInterrupt as interrupt:
        print("Se ha detenido el programa: ", interrupt)
    except Exception as e:
        print(e)
