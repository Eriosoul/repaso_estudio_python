"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

import re


def capitalize():
    palabra = "hola, ¿cómo estás?"
    print(palabra.title())


capitalize()


def capitalize_text(text):
    words = re.findall(r'[A-Za-zÀ-ú]+', text)
    capitalized_text = ' '.join(word.capitalize() for word in words)
    return capitalized_text


text = "hola, ¿cómo estás?"
capitalized_text = capitalize_text(text)
print(capitalized_text)
