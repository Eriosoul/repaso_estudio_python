import json


def read_data(json_name):
    with open(json_name, 'r') as file:
        data = json.load(file)
    return data

def show_data(data):
    for clave, valor in data.items():
        print(f"{clave}: {valor}")


if __name__ == '__main__':
    json_name = "person.json"
    data = read_data(json_name)
    show_data(data)
