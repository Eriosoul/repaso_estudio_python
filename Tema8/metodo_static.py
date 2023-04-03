class MiClase:

    variable_calse = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod  # no pueden acceder a variables de instancia
    def metodo_estatic():  # no recibe el parametro sel
        print(f'Llamado desde el metodo static: {MiClase.variable_calse}')

    @classmethod
    def metodo_clase(cls):
        print(f'Llamado desde el metodo clase: {cls.variable_calse}')

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatic()
        print(self.variable_calse, self.variable_instancia)

# print metodo statinc
MiClase.metodo_estatic()
MiClase.metodo_clase()

miObjeto1 = MiClase('Variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

print(MiClase.variable_calse)

miclase = MiClase('Valor variable instancia')
print(miclase.variable_instancia)
print(miclase.variable_calse)
