"""
/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */
"""
import asyncio


# async def sum_async(number=5, number2=2, seconds=10):
#     await asyncio.sleep(seconds)
#     return number + number2
#
#
# async def main():
#     result = await sum_async(seconds=3)  # Espera 3 segundos
#     print("Resultado:", result)
#
# if __name__ == '__main__':
#     asyncio.run(main())
#


async def sum(number, number2, seconds):
    await asyncio.sleep(seconds)
    return number + number2


async def main():
    # Definir las llamadas a la función sum con diferentes parámetros
    tasks = [
        sum(5, 2, 3),  # La suma de 5 y 2 después de 3 segundos
        sum(10, 20, 1),  # La suma de 10 y 20 después de 1 segundo
        sum(8, 4, 2)  # La suma de 8 y 4 después de 2 segundos
    ]

    # Ejecutar las corutinas concurrentemente
    results = await asyncio.gather(*tasks)
    print("Resultados:", results)

if __name__ == '__main__':
    asyncio.run(main())
