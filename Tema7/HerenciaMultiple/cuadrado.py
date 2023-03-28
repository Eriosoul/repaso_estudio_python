from Tema7.HerenciaMultiple.color import Color
from Tema7.HerenciaMultiple.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho
        