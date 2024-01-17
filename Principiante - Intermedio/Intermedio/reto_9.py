"""
Reto: Calculadora de Descuentos
Crea una calculadora de descuentos en Python. La aplicación debe permitir al usuario ingresar el precio original de un
producto y el porcentaje de descuento, y luego mostrar:

 - El monto del descuento.
 - El precio final después del descuento.
Estructura el programa en funciones para cada cálculo. Asegúrate de manejar casos especiales, como descuentos mayores
al 100% o descuentos negativos.

"""


def get_price():
    while True:
        try:
            price = float(input("Por favor, Introduczca el precio del producto: "))
            return price
        except ValueError:
            print("Por favor, ingrese un valor numerico valido.")


def get_discount():
    while True:
        try:
            discount = float(input("Por favor, Introduczca el descuento: "))
            return discount
        except ValueError:
            print("Por favor, ingrese un valor numérico valido.")


def calculate_discount(discount, price):
    final_discount = price * (discount / 100)
    return final_discount


def final_price(price, final_discount):
    final = price - final_discount
    print("El precio final despues del descuento es:", final)


if __name__ == '__main__':
    try:
        price = get_price()
        discount = get_discount()
        final_discount = calculate_discount(discount, price)
        final_price(price, final_discount)
    except Exception as e:
        print("Error: ", e)
