from ejercicio_tema11.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador: int = 0

    @classmethod
    def contador_teclados(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, marca, tipo_entrada):
        self._id_teclado = Teclado.contador_teclados()
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'


if __name__ == '__main__':
    telcado1 = Teclado('Hp', 'USB')
    print(telcado1)
    telcado2 = Teclado('Gamer', 'USB 3.0')
    print(telcado2)
