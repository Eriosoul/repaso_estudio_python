"""
/* # 23 CONJUNTOS
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""


def func(arr1: list, arr2: list, bolean: bool) -> list:
    if bolean:
        # busqueda de elementos comundes
        common_elements = [item for item in arr1 if item in arr2]
        return common_elements
    else:
        unique_elements = [item for item in arr1 if item not in arr2] + [item for item in arr2 if item not in arr1]
        return unique_elements


arr1 = ["alfa", "omega", "beta"]
arr2 = ["beta", "omega", "chocolate"]
print("Elementos comunes:", func(arr1, arr2, True))
# print("Elementos no comunes:", func(arr1, arr2, False)) se duplica alfa en los 2

unique_elements = list(set(arr1) ^ set(arr2))
print("Elementos no comunes:", unique_elements)
