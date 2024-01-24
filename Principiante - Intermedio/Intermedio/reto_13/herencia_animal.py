"""
Ejercicio 1: Crear una clase base y una clase derivada

Define una clase base llamada 'Animal' con un método 'hablar'.
Luego, crea una clase derivada llamada 'Perro' que herede de 'Animal'
y sobrescribe el método 'hablar' para que imprima "¡Guau!"
"""


class Animal:
    def hablar(self):
        print("Sonidos de un animal")


class Perro(Animal):
    def hablar(self):
        print("¡Guau!")


if __name__ == '__main__':
    animal_generico = Animal()
    animal_generico.hablar()

    perro = Perro()
    perro.hablar()
