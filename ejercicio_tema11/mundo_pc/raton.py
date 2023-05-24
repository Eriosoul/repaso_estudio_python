from ejercicio_tema11.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contado: int = 0

    @classmethod
    def contador_ratones(cls):
        cls.contado += 1
        return cls.contado

    def __init__(self, marca, tipo_entrada):
        self._id_raton = Raton.contador_ratones()
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
    raton2 = Raton('Acer', 'Inalambrico')
    print(raton2)
