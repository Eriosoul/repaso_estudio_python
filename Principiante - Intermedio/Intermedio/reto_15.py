"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
*/
"""


def carrera():
    word = ["run", "jump", "run", "run", "run", "jump", "run", "jump"]
    road = ["_", "|", "_", "_", "_", "|", "_", "|"]
    passed = True
    # zip(road, word) para iterar sobre ambas listas al mismo tiempo.
    for w, r in zip(road, word):
        if r == "jump" and w == "_":
            print("Atleta salto sin valla y se torcio el tobillo \n choco")
            passed = False
        elif r == "run" and w == "|":
            print("Atleta corrio contra la valla y se partio el pecho \n choco ")
            passed = False
        if r == "jump" and w == "|":
            print("Atleta saltó la valla")
        elif r == "run" and w == "_":
            print("Atleta corrió en el suelo")
        else:
            print("Condición no definida")
    return passed

carrera()

if __name__ == '__main__':
    if carrera():
        print("El atleta ha superado la carrera correctamente.")
    else:
        print("El atleta no ha superado la carrera.")
