from ejercicio_tema11.mundo_pc.teclado import Teclado
from ejercicio_tema11.mundo_pc.raton import Raton
from ejercicio_tema11.mundo_pc.monitor import Monitor


class Computadora:
    contador = 0

    @classmethod
    def contador_computadoras(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, nombre, monitor, teclado, raton):
        self._id_computadora = Computadora.contador_computadoras()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    teclado1 = Teclado('Hp', 'USB')
    raton1 = Raton('Gaming', 'USB')
    monitor1 = Monitor('AOC', 27)
    computadora1 = Computadora('Intel', monitor1, teclado1, raton1)
    print(computadora1)
