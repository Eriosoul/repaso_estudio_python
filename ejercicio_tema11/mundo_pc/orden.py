class Orden:
    contador = 0

    @classmethod
    def contador_ordenes(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, computadoras):
        self._id_orden = Orden.contador_ordenes()
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        # almacenar todo tipo de computadoras
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''Id Orden: {self._id_orden} 
        Compuradoras {computadoras_str}
        '''  # contiene toda la informacion de los ordenadores
