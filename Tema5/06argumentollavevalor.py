# **kewords
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'La llave es: {llave}, su valor es: {valor}')


listarTerminos(IDE='Integrated Development Environment', PK='Primary key')
