import os
from dotenv import load_dotenv
import requests
from requests import Response
from bs4 import BeautifulSoup


class GlobalSongs:
    def __init__(self):
        load_dotenv()  # Cargar variables de entorno desde .env
        self.url = os.getenv("LINK")

    def get_status(self):
        try:
            self.r: Response = requests.get(self.url)
            if self.r.status_code != 200:
                self.r.raise_for_status()
                print("Error al obtener los datos de la web", self.r)
            else:
                print("Conexion exitosa")
                print(self.r.text)
                self.get_data()
        except requests.exceptions.HTTPError as err:
            print(f"Error HTTP: {err}")
        except Exception as e:
            print("Error al obtener los datos: ", e)

    def get_data(self):
        soup: BeautifulSoup = BeautifulSoup(self.r.text, "html.parser")
        data = soup.find('div', class_='h4HgbO_Uu1JYg5UGANeQ.wTUruPetkKdWAR1dd6w4')
        print(data.text)


if __name__ == '__main__':
    g: GlobalSongs = GlobalSongs()
    g.get_status()

