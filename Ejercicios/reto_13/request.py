import os
from dotenv import load_dotenv
import requests
from requests import Response


class GlobalSongs:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde .env
        self.url = os.getenv("LINK")

    def get_status(self):
        r: Response = requests.get(self.url)
        print(r)


if __name__ == '__main__':
    g: GlobalSongs = GlobalSongs()
    g.get_status()

