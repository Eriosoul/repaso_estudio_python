class Persona:
    """
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
    *args = lo utilizamos para pasar una tupla de valores tipo variable
    **kwargs = pasar un diccionario de datos tras esa tupla de valores
    """
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Pesona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()

persona2 = Persona('Lola', 'Gomez', 30)
persona2.mostrar_detalle()