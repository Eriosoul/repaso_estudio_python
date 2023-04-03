class Productos:
    contador: int = 0

    @classmethod
    def contador_productos(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, nombre: str, precio: float):
        self._id_producto: int = Productos.contador_productos()
        self._nombre: str = nombre
        self._precio: float = precio

    # metodo get
    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'[{self._id_producto} Nombre: {self._nombre} Precio: {self._precio}]'


if __name__ == '__main__':
    producto1 = Productos('Camisa', 100.00)
    print(producto1)
    producto2 = Productos('Tenis', 45.35)
    print(producto2)
