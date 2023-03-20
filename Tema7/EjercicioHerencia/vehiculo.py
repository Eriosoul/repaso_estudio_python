class Vehiculo(object):  # clase padre
    def __init__(self, color: str, ruedas: int):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: color {self.color}, ruedas {str(self.ruedas)}'


class Coche(Vehiculo):
    def __init__(self, velocidad, color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, tipo, color, ruedas):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} tipo {self.tipo}'