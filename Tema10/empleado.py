class Empleado:
    def __init__(self, nombre: str, sueldo: float):
        self.nombre: str = nombre
        self.sueldo: float = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()
