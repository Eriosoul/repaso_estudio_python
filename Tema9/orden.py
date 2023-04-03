from Tema9.productos import Productos


class Orden:
    contador: int = 0

    @classmethod
    def contador_ordenes(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, products):
        self._id_orden: int = Orden.contador_ordenes()
        self._productos = list(products)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def total_precio(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'El orden es:[{self._id_orden} \n Productos: {productos_str}]'


if __name__ == '__main__':
    producto1 = Productos('Camisa', 100.00)
    producto2 = Productos('Tenis', 45.35)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    print(f'El total de la orden: {orden1.total_precio()}')
