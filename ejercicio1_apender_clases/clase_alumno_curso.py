"""
Dos clases, una de alumno y una de curso
- alumno
    - contiene 2 atributos: edad y nombre
- curso
    - tiene un nombre de curso (1º, 2º, etc)
    - contiene una lista de alumnos
    - contiene una método en la que puedes añadir alumnos al curso
    - un curso no puede tener más de 30 alumnos
"""


class Alumno:  # Declaro la clase Alunmo con los atributos nombre y edad
    def __init__(self, nombre, edad):  # parametros
        self.nombre = nombre  # atributo nombre
        self.edad = edad  # atributo edad


class Curso:  # Declaro la clase Curso con el atributo nombre del curso y el listado
    def __init__(self, nombre_curso, id_curso):
        self.nombre_curso = nombre_curso  # atributo nombre del curso
        self.lista_alumnos = []  # atributo lista de alumnos que lo igualamos a un array / lista
        self.id_curso = id_curso  # atributo para diferenciar los alumnos segun su curso

    def agregar_alumno(self, alumno):  # metodo para agregar alumnos
        if len(self.lista_alumnos) < 30:  # comprobamos el contenido de la lista de los alumnos
            self.lista_alumnos.append(alumno)  # en caso de que la lista sea < 30 se añadira el alumno
        else:  # si es > 30 nos indicara un error
            print('La lista de los alumnos esta completa')

    def nuevos_alumnos(self):  # metodo pora mostrar la informacion
        print(f'Lista de alumnos del curso {self.nombre_curso} (Id:{self.id_curso}):')
        for alumno in self.lista_alumnos:  # Itero sobre la lista de alumnos del curso
            print(alumno.nombre, '-', alumno.edad)  # Accedo al objeto Alumno mediante la variable alumno


if __name__ == '__main__':
    cursos = []  # agregamos una lista para almacenar los cursos
    id_curso = 1  # agregamos un identificador para cada curso
    while True:  # bucle while para añadir mas de un alumno
        nombre_alumno = input('Introduce el nombre del alumno: ')
        edad_alumno = int(input('Introduce la edad del alumno: '))
        nuevo_alumno = Alumno(nombre_alumno, edad_alumno)
        nombre_curso = input('Introduce el nombre del curso: ')
        curso_existente = False  # agregamos una variable para indicar si el curso ya existe
        for curso in cursos:
            if curso.nombre_curso == nombre_curso:  # si el nombre del campo curso es el mismo
                curso.agregar_alumno(nuevo_alumno)  # añadimos a ese curso el alumno
                curso_existente = True  # indicamos que el curso existe
                break
        if not curso_existente:  # su el curso no esxixte
            curso = Curso(nombre_curso, id_curso)  # creamos un objeto el cual lamacenara el nombre y dicho id
            id_curso += 1  # aumnetamos el id del curso para que no se sobre escriba
            curso.agregar_alumno(nuevo_alumno)
            cursos.append(curso)
        opcion = input('Desea añadir un nuevo alumno s/n: ')
        if opcion == 'n':
            for curso in cursos:
                curso.nuevos_alumnos()
            break


# viejo codigo
# Creo el objeto de la clase del curso
# curso_1 = Curso("1º ESO")
#
# # Creo varios objetos de alumnos
# alumno_1 = Alumno("Ana", 13)
# alumno_2 = Alumno("Juan", 12)
# alumno_3 = Alumno("Luisa", 14)
#
# # añado los alumnos a la lista del curso ya que es curso_1 = eso hace que pertenezcan a la misma clase 1º
# curso_1.agregar_alumno(alumno_1)
# curso_1.agregar_alumno(alumno_2)
# curso_1.agregar_alumno(alumno_3)
#
# # Intentamos añadir un cuarto alumno a la lista, lo cual no debería ser posible
# alumno_4 = Alumno("Pedro", 13)
# curso_1.agregar_alumno(alumno_4)
#
# # Imprimimos la lista de alumnos del curso
# # curso = Curso("Programación en Python")
# # curso.agregar_alumno(alumno1)
# # curso.agregar_alumno(alumno2)
# print(curso.nuevos_alumnos()) # ('Programación en Python', [('Juan', 20), ('Ana', 22)])
