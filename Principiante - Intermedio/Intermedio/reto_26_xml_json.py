"""
* EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""

import os
import xml.etree.ElementTree as xml




data = {
    "name": "pepe",
    "age": 27,
    "birthday": "01/01/1990",
    "dev_lang": ["Python", "Java", "C++", "C"]
}

xml_file = "fichero.xml"

def save_xml():
    # posibilidad 1
    # root = xml.ElementTree("data user")
    # child = xml.SubElement(root, "name")
    # child.text = name

    root = xml.Element("data")
    for key, value in data.items():
        child = xml.SubElement(root, key)
        child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)

save_xml()
# xml_file = "fichero.xml"
# json_file = "fichero.json"
#
# open(xml_file, "a")
# open(json_file, "a")
#
#
# def generate_data(xml_file, json_file):
#     name = "pepe"
#     age = "27"
#     birthday = "01/01/1990"
#     dev_lang = ["Python", "Java", "C++", "C"]
#     with open(xml_file, "a") as file:
#         file.write(f"{name}, {age}, {birthday}, {dev_lang}")
#
#     with open(json_file, "a") as file:
#         file.write(f"{name}, {age}, {birthday}, {dev_lang}")
#
#
# generate_data(xml_file=xml_file, json_file=json_file)
