class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


base = float(input('Proporciona la base: '))
altura = float(input('Proporciona la altura: '))
rectangulo = Rectangulo(altura, base)
print(f'El area del rectangulo es: {rectangulo.calcular_area()}')