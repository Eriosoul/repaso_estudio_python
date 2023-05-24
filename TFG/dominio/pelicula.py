class Pelicula:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return f'El nombre de la pelicula es {self.nombre}'
