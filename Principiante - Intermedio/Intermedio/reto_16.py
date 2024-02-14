"""
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */
"""


def tres_en_raya():
    tablero = [
        ["0", "X", "X"],
        ["0", "X", "X"],
        ["X", "X", "0"]
    ]
    print(tablero)
    for fila in tablero:
        print("|".join(fila))
    for row in tablero:
        if all(igual == "X" for igual in row):
            print("X win the game")
            return
        elif all(igual == "0" for igual in row):
            print("0 win the game")
            return

    for col in range(3):
        if all(tablero[j][col] == "X" for j in range(3)):
            print("X win the game")
            return
        elif all(tablero[j][col] == "0" for j in range(3)):
            print("0 win the game")
            return

    if tablero[0][0] == tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] == tablero [2][0]:
        if tablero[1][1] == "X":
            print("X win the game")
        elif tablero[1][1] == "0":
            print("0 win the game")
        return

tres_en_raya()
