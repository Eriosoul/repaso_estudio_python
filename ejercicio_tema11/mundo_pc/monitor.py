class Monitor:
    contador = 0

    @classmethod
    def contador_monitores(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, marca, tamaño: int):
        self._id_monitor = Monitor.contador_monitores()
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitor1 = Monitor('HP', 27)
    print(monitor1)
    monitor2 = Monitor('AOC', 27)
    print(monitor2)
