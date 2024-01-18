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

work_system: dict = {
    1: {
        "name_work": "Sistemas de procesamiento de transacciones",
        "description_work": "Los sistemas de procesamiento de transacciones (TPS por sus siglas en inglés) son los sistemas empresariales básicos que sirven al nivel operacional de la organización.",
        "status": "completada"
    },
}


def create_work():
    try:
        name_work = str(input("Introduce el nombre de la tarea: "))
        description_work = str(input("Introduce la descripcion de la tarea: "))
        print(name_work, ":", description_work)
        return name_work, description_work
    except ValueError as e:
        print("Error a la hora de introducir la informacion: ", e)


def show_data():
    for task_id, task_info in work_system.items():
        name_work = task_info["name_work"]
        description = task_info["description_work"]
        print(f"ID: {task_id}, Name: {name_work} = Description : {description}")


if __name__ == '__main__':
    create_work()
    show_data()
