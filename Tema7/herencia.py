class Persona(object):  # clase padre object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # sobrescritura en la clase padre
        return f'Persona: Nombre {self.nombre}, Edad {self.edad}'


class Empleado(Persona):  # hereda de la clase object
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()}  Gana: {self.sueldo}'
