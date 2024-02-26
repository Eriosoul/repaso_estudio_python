"""
Define una función download_file que tome una URL como argumento y utilice aiohttp para descargar el contenido
de la URL de forma asíncrona. La función debe devolver el contenido descargado como una cadena de texto.

Define una función download_files que tome una lista de URLs como argumento y utilice asyncio.gather para descargar
cada archivo de forma asíncrona. La función debe devolver una lista con el contenido descargado de cada archivo en el
mismo orden que las URLs de entrada.

En la función main, define una lista de URLs de archivos para descargar.

Llama a la función download_files con la lista de URLs y muestra el contenido descargado de cada archivo.
"""

import asyncio
import aiohttp


async def fetchresource(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except ConnectionError as e:
        print(e)


async def downloadfile(urls):
    try:
        async with aiohttp.ClientSession() as session:
            tasks = [fetchresource(session, url) for url in urls]
            return await asyncio.gather(*tasks)
    except Exception as ef:
        print("Error download file: ", ef)


async def main():
    try:
        urls = [
            "https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2",
            'https://jsonplaceholder.typicode.com/posts/3'
        ]

        results = await downloadfile(urls)
        for result in results:
            print(result)
    except Exception as es:
        print("Error en la vida", es)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()
