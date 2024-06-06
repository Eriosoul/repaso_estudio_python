# perdi al usuario que itnroduzca la distancia en kilometros

class Miles:
    def __init__(self):
        self.miles = 0.62137119


class GetKm:
    def __init__(self, km=0.0):
        self.km: float = km

    def get_km_user(self):
        try:
            self.km = float(input("Introduce el km que deseas pasar a millas: "))
            if self.km <= 0:
                print("Error: La distancia debe ser mayor que 0.")
                return None
            return self.km
        except ValueError as ex:
            print("Se espera un número. Error:", ex)
            return None
        except Exception as ex:
            print(ex)
            return None


# realizar la conversion a millas
class CalculateToMails(Miles, GetKm):
    def __init__(self, km=0.0):
        Miles.__init__(self)
        GetKm.__init__(self, km)

    def calculate(self):
        if self.km > 0:
            to_miles = self.km * self.miles
            print(f"{self.km} kilómetros son {to_miles} millas.")
        else:
            print("No se puede realizar la conversión. La distancia debe ser mayor que 0.")


# mostrar resultado
if __name__ == '__main__':
    try:
        km_instance = GetKm()
        km_value = km_instance.get_km_user()
        if km_value is not None:
            ca_instance = CalculateToMails(km_value)
            ca_instance.calculate()
    except KeyboardInterrupt as ex:
        print("Se ha detenido el programa...")
    except Exception as ex:
        print(ex)
