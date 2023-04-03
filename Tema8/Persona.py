class Persona:
    contado_personas = 0  # se encargara de dar un valor unico a cada persona

    @classmethod
    def generar_siguente_valor(cls):
        cls.contado_personas += 1
        return cls.contado_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Karla', 30)
print(persona2)
persona3 = Persona('Carlos', 35)
print(persona3)
Persona.generar_siguente_valor()
persona4 = Persona('Ana', 23)
print(persona4)
print(f'Valor contador personas: {Persona.contado_personas}')
