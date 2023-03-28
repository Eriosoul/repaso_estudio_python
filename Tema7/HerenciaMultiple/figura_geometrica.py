class FiguraGeometrica(object):
    def __init__(self, ancho: float, alto: float):
        if 0 < ancho < 10:
            self.ancho = ancho
        else:
            self._ancho = 0
        if 0 < alto < 10:
            self.alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self.ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self.alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'FiguraGeometrica[Alto:{self._alto}, Ancho{self._ancho}]'
