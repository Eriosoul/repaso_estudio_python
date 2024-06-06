# Pedir al usaurio que introduzca la base y altura del triangulo
class GetWidthHeight:
    def __init__(self, width=0.0, height=0.0):
        self.width: float = width
        self.height: float = height

    def get_data(self):
        try:
            self.width = float(input("Introduce la ancho del trinagulo: "))
            self.height = float(input("Introduce la alto del triangulo: "))
            return self.width, self.height
        except SyntaxError as ex:
            print("La sintaxix esta mal escrita se espera un numero", ex)
        except Exception as ex:
            print(ex)


# Calcular el area del triangulo
class CalculateArea(GetWidthHeight):
    def __init__(self, width=0.0, height=0.0):
        super().__init__(width, height)

    def calculate_area(self):
        area = (self.width * self.height) / 2
        return area


# Mostrar el resultado
if __name__ == '__main__':
    G: GetWidthHeight = GetWidthHeight()
    width, height = G.get_data()
    ca = CalculateArea(width, height)
    area = ca.calculate_area()
    print(f"El area del triangulo es {area}")
