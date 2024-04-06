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

"""
import json
import os
import xml.etree.ElementTree as xml


data = {
    "name": "pepe",
    "age": 27,
    "birthday": "01/01/1990",
    "dev_lang": ["Python", "Java", "C++", "C"]
}

xml_file = "fichero.xml"
json_file = "fichero.json"

def create_xml():
    # posibilidad 1
    # root = xml.ElementTree("data user")
    # child = xml.SubElement(root, "name")
    # child.text = name

    root = xml.Element("data")
    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


create_xml()


def create_json():
    with open(xml_file) as file:
        print(file.read())

    # os.remove(xml_file)

    with open(json_file, "w") as file:
        json.dump(data, file)

    with open(json_file, "r") as file:
        print(file.read())

    # os.remove(json_file)


create_json()
# Dificultad extra
"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 """


class CustomData:
    def __init__(self, name, age, birthday, dev_lang):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.dev_lang = dev_lang


with open(xml_file) as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("name").text
    birthday = root.find("birthday").text
    dev_lang = [item.text for item in root.find("dev_lang")]

    data_from_xml = CustomData(name, age, birthday, dev_lang)
    print(data_from_xml.__dict__)

with open(json_file, "r") as json_data:
    data_dict = json.load(json_data)
    json_class = CustomData(
        data_dict["name"],
        data_dict["age"],
        data_dict["birthday"],
        data_dict["dev_lang"],
    )

    print(json_class.__dict__)


os.remove(xml_file)
os.remove(json_file)
