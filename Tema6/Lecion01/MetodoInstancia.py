class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Los metos inician con minuscila
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()  # Lo comun
# Persona.mostrar_detalle(persona1)  # No es lo comun
persona1.telefono = '555444111'
print(persona1.telefono)

persona2 = Persona('Lola', 'Gomez', 29)
persona2.mostrar_detalle()
