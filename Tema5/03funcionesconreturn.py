# opcion A - > tipamos la funcion
def sumar(a: int = 0, b: int = 0) -> int:
    return a + b


resultado = sumar()
print(f'Resultado de la suma: {resultado}')
print(f'El resultado directo es : {sumar(6, 6)}')
