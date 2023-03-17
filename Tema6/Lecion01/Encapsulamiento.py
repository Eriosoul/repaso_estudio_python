class Persona:
    """
    _nombre no deberian de poder acceder y modificar el contenido
    __nombre no acceden (menos comun)
    """
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Pesona: {self._nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()