from Tema10.empleado import Empleado
from Tema10.gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
