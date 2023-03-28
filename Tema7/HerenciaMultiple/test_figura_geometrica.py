from Tema7.HerenciaMultiple.cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.area())


# MRO - Method Resoulution Order
# MRO es el meto de resolucion en orden
print(Cuadrado.mro())
