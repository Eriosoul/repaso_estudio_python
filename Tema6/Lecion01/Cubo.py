class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundo * self.alto


ancho = float(input('Proporciona el ancho: '))
profundo = float(input('Proporciona el profundo: '))
alto = float(input('Proporciona el ancho: '))

cubo = Cubo(ancho, profundo, alto)
print(f'El volumen es : {cubo.calcular_volumen()}')