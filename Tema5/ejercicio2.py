"""
Ejercicio: calculadora de ipuestos
crea una funcion para calcular el total del pago incluyendo un impuesto aplicado.
# Formula: paga_total = paga_sin_impuesto + paga_sin_impuesto * (impuesto/100)
"""


def calcular_total_pago(paga_sin_impuesto: float, impuesto: float):
    pago_total = paga_sin_impuesto + paga_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutar funcion
paga_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))
pago_con_impuesto = calcular_total_pago(paga_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
