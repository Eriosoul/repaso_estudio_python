class Aritmetica:
    """
    Clase Artimetica para relaizar las operaciones de sumar, restar, dividir etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def suma(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(8, 9)
aritmetica2 = Aritmetica(10, 2)
aritmetica3 = Aritmetica(15, 9)
aritmetica4 = Aritmetica(1789, 580)

print(f'El resultado de la suma es: {aritmetica1.suma()}')
print(f'El resultado de la resta es: {aritmetica2.restar()}')
print(f'El resultado de la multiplicacion es: {aritmetica3.multiplicar()}')
print(f'El resultado de la division es: {aritmetica4.dividir():.2f}')
