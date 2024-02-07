import os
from dotenv import load_dotenv
import requests
from requests import Response


class GlobalSongs:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde .env
        self.url = os.getenv("LINK")

    def get_status(self):
        try:
            r: Response = requests.get(self.url)
            if r.status_code != 200:
                print("Error al obtener los datos de la web", r)
            else:
                print("Conexion exitosa")
        except Exception as e:
            print("Error al obtener los datos: ", e)


if __name__ == '__main__':
    g: GlobalSongs = GlobalSongs()
    g.get_status()

