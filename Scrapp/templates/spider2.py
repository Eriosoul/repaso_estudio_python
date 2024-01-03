import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import logging


class TenistaLider:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("URL")

    def check_url_status(self):
        if not self.url:
            logging.error("URL not defined.")
            return

        try:
            with requests.get(self.url) as r:
                r.raise_for_status()
                soup: BeautifulSoup = BeautifulSoup(r.text, "html.parser")
                print(soup)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error making HTTP request: {e}")

    def url_funciona(self):
        print("Super nice work")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    t: TenistaLider = TenistaLider()
    t.check_url_status()