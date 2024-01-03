import os
import requests
import logging
from dotenv import load_dotenv
from bs4 import BeautifulSoup


class TenistaLider:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("URL")
        self.soup = None

    def check_url_status(self):
        if not self.url:
            logging.error("URL not defined.")
            return
        try:
            r = requests.get(self.url)
            if r.status_code != 200:
                print(r.status_code)
                raise
            self.soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error making HTTP request: {e}")

    def get_data_from_first_table(self):
        if self.soup:
            # Buscar la primera tabla en el documento
            table = self.soup.find("table")
            # Verificar si se encontró la tabla
            if table:
                # Buscar todas las filas en la tabla
                rows = table.find_all("tr")
                # Iterar sobre las filas e imprimir los datos
                for row in rows:
                    # Buscar todas las celdas en la fila
                    cells = row.find_all(["td", "th"])
                    print(cells)
                    # Imprimir el contenido de cada celda
                    cell_texts = [cell.text.strip() for cell in cells]
                    print(cell_texts)
                    flag_cell = row.find("span", class_="flagicon")
                    if flag_cell:
                        flag_link = flag_cell.find("a")["href"]
                        flag_title = flag_cell.find("a")["title"]
                        print(f"Enlace de la bandera: {flag_link}")
                        print(f"Título de la bandera: {flag_title}")
            else:
                print("No se encontró la tabla en la página.")
        else:
            print("No hay objeto soup disponible.")


if __name__ == '__main__':
    t: TenistaLider = TenistaLider()
    t.check_url_status()
    print("============================")
    t.get_data_from_first_table()
