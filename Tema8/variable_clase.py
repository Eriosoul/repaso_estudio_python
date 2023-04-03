class MiClase:

    variable_calse = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_calse)

miclase = MiClase('Valor variable instancia')
print(miclase.variable_instancia)
print(miclase.variable_calse)
