"""
* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""

import time
import asyncio


# Función que realiza una tarea de larga duración de manera síncrona
def tarea_larga_sincrona(nombre):
    print(f"Iniciando tarea larga síncrona '{nombre}'")
    time.sleep(2)  # Simula una tarea que tarda 2 segundos en completarse
    print(f"Tarea larga síncrona '{nombre}' completada")


# Llamada a la función síncrona
tarea_larga_sincrona("A")
tarea_larga_sincrona("B")

"""
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""

async def func_C(num):
    print(f"Iniciando tarea larga síncrona 'C'")
    await asyncio.sleep(num)
    print(f"Tarea larga síncrona 'C' completada")

async def func_B(num):
    print(f"Iniciando tarea larga síncrona 'B'")
    await asyncio.sleep(num)
    print(f"Tarea larga síncrona 'B' completada")

async def func_A(num):
    print(f"Iniciando tarea larga síncrona 'A'")
    await asyncio.sleep(num)
    print(f"Tarea larga síncrona 'A' completada")

async def func_D(num):
    print(f"Iniciando tarea larga síncrona 'D'")
    await asyncio.sleep(num)
    print(f"Tarea larga síncrona 'D' completada")


async def ejecutar_func():
    await asyncio.gather(
        func_C(num=3),
        func_B(num=2),
        func_A(num=1)
    )
    await func_D(num=1)

asyncio.run(ejecutar_func())
