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


class Alumno:
    def __init__(self, nombre: str, edad: int):
        self.nombre: str = nombre
        self.edad: int = edad


class Curso:
    def __init__(self, nombre_curso: str):
        self.nombre_curso: str = nombre_curso
        self.lista_alumnos: list[Alumno] = []

    def agregar_alumno(self, alumno: Alumno):
        if len(self.lista_alumnos) <= 30:
            self.lista_alumnos.append(alumno)
        else:
            print('La lsta de los alumnos se encuentra llena')

    def mostrar_alumno(self):
        print(f'El curso: {self.nombre_curso}:')
        for alumno in self.lista_alumnos:
            print(alumno.nombre, alumno.edad)


if __name__ == '__main__':
    curso_1 = Curso('1º ESO')
    alumno_1 = Alumno("Ana", 13)
    alumno_2 = Alumno("Pepe", 12)
    alumno_3 = Alumno("Juan", 13)
    alumno_4 = Alumno("Andrea", 14)
    alumno_5 = Alumno("Luis", 14)
    alumno_6 = Alumno("Manuel", 14)

    curso_1.agregar_alumno(alumno_1)
    curso_1.agregar_alumno(alumno_2)
    curso_1.agregar_alumno(alumno_3)
    curso_1.agregar_alumno(alumno_4)
    curso_1.agregar_alumno(alumno_5)
    curso_1.agregar_alumno(alumno_6)

    curso_1.mostrar_alumno()

    curso_2 = Curso('2º ESO')
    alumno_1 = Alumno("Ana", 14)
    alumno_2 = Alumno("Pepe", 14)
    alumno_3 = Alumno("Juan", 15)
    alumno_4 = Alumno("Andrea", 16)
    alumno_5 = Alumno("Luis", 14)
    alumno_6 = Alumno("Manuel", 17)

    curso_2.agregar_alumno(alumno_1)
    curso_2.agregar_alumno(alumno_2)
    curso_2.agregar_alumno(alumno_3)
    curso_2.agregar_alumno(alumno_4)
    curso_2.agregar_alumno(alumno_5)
    curso_2.agregar_alumno(alumno_6)

    curso_2.mostrar_alumno()

    alumno_7 = Alumno("Manuel", 17)
    curso_2.agregar_alumno(alumno_7)
