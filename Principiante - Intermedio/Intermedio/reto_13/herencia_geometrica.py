"""
Ejercicio: Clases de Geometría

Crea una clase base llamada Figura con un método area que simplemente imprima "Área de la figura".
Luego, crea dos clases derivadas llamadas Cuadrado y Circulo que hereden de Figura.
Cada una de estas clases debe tener su propio método area que calcule
y muestre el área específica de un cuadrado o un círculo, respectivamente.

Puedes utilizar la fórmula del área del cuadrado (lado * lado) y la fórmula del área del círculo (pi * radio * radio).
"""
import math


class Figura:
    def __init__(self):
        pass

    def area_figura(self):
        print("Área de la figura")


class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular(self):
        area = self.lado * self.lado
        return print(area)


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular(self):
        area = math.pi * (self.radio * self.radio)
        return print(area)


if __name__ == '__main__':
    cuadrado = Cuadrado(lado=6)
    cuadrado.calcular()
    cuadrado.area_figura()

    circulo = Circulo(radio=12.56)
    circulo.calcular()
    circulo.area_figura()
