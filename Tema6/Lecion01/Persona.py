# Las clases poseen atributos y metodos
# class Persona:
#     def __init__(self):
#         self.nombre = 'Juan' # atributos de una clase persona
#         self.apellido = 'Perez'
#         self.edad = 28
#
#
# # persona1 es nuestro objeto que podremos ver la informacion que se ha ido crando
# persona1 = Persona()  # se llamaria al metodo __init__
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)


# en el segundo ejemplo añadiremos parametros

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre # self.nombre es un atributo que lo igualamos a nuestro parametro
        self.apellido = apellido
        self.edad = edad


# persona1 es nuestro objeto que podremos ver la informacion que se ha ido crando
persona1 = Persona('Juan', 'Perez', 28)  # se llamaria al metodo __init__
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# Modificacion de valores de un objeto
persona1.nombre = 'Pepe'
persona1.apellido = 'Juarez'
persona1.edad = 29
print(f'Objeto persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# segundo objeto
persona2 = Persona('Laura', 'Gomez', 30)
# print(persona2.nombre)
# print(persona2.apellido)
# print(persona2.edad)
print(f'Objeto persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')
# Modificacion de los valores del segundo objeto
persona2.nombre = 'Andrea'
persona2.apellido = 'Gonzalez'
persona2.edad = 26
print(f'Objeto persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')