"""
Ejercicio: Sistema de Empleados

Crea una clase base llamada Empleado con los siguientes atributos:

nombre: nombre del empleado.
salario: salario base del empleado.
Añade un método llamado calcular_salario que imprima el salario base.

Luego, crea dos clases derivadas llamadas Programador y Gerente que hereden de Empleado.
Cada una de estas clases debe tener atributos adicionales específicos y un método calcular_salario que calcule y
muestre el salario total de acuerdo con las siguientes reglas:

Para un Programador, el salario total es el salario base más un bono del 10%.
Para un Gerente, el salario total es el salario base más un bono del 20%.
"""


class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre: str = nombre
        self.salario: float = salario

    def calcular_salario(self):
        print(f"El empleado {self.nombre} dispone de un salario de {self.salario}")


class Programador(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_salario(self):
        salario_total = self.salario + (self.salario * 10) / 100
        print(f"El programador {self.nombre} tiene un salario total de ${salario_total:.2f}")


class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_salario(self):
        salario_total = self.salario + (self.salario * 20) / 100
        print(f"El gerente {self.nombre} tiene un salario total de ${salario_total:.2f}")


if __name__ == '__main__':
    p = Programador(nombre="Andrei", salario=1300.00)
    p.calcular_salario()

    g = Gerente(nombre="Andrei", salario=40750.90)
    g.calcular_salario()
