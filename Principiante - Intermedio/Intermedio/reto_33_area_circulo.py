# crear la constante pi
class Pi:
    def __init__(self):
        self.PI: float = 3.14159
# Pedi al usuario que introduzca el radio del circulo


class GetRCircle:
    def __init__(self):
        self.radio_circle = ""

    def get_circle_radio(self):
        n_radio = input("Introduce el radio del circulo: ")
        self.radio_circle = float(n_radio)
        return self.radio_circle


# Calcular el area del circulo
class CalculateArea(Pi, GetRCircle):
    def __init__(self):
        Pi.__init__(self)
        GetRCircle.__init__(self)

    def calculate_area(self):
        area = self.PI * (float(self.radio_circle) ** 2)
        return area


if __name__ == '__main__':
    pi: Pi = Pi()
    gr: GetRCircle = GetRCircle()
    gr.get_circle_radio()
    ca = CalculateArea()
    ca.radio_circle = gr.radio_circle  # Asegúrate de pasar el radio al objeto CalculateArea

    area = ca.calculate_area()
    print(f'El área del círculo es: {area}')