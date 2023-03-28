from Tema7.TareaHerenciaMultiple.rectangulo import Rectangulo
from Tema7.TareaHerenciaMultiple.cuadrado import Cuadrado


print('Creacion Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(f'Caluclo del area: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=3, alto=8, color='verde')
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
