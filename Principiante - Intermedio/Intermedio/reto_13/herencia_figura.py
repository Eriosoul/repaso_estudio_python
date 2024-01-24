"""
Ejercicio 2: Utilizar atributos de la clase base en la clase derivada

Define una clase base llamada 'Figura' con atributos 'base' y 'altura'.
Luego, crea una clase derivada llamada 'Rectangulo' que herede de 'Figura' y tenga un
método 'calcular_area' que devuelva el área del rectángulo.
"""


class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def calcular_area(self):
        self.area = self.base * self.altura
        return print(f"El area de un rectangulo es: {self.area}")


if __name__ == '__main__':
    r = Rectangulo(base=6, altura=9)
    r.calcular_area()
