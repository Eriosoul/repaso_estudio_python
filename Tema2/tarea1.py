"""
En el siguente ejercicio se solicita calcular el area de un perimetro de un rectanguo,
para ello debemos crear los siguentes variables:

alto
ancho
"""
alto = int(input("Introduzca la altura: "))
ancho = int(input("Introduzca el ancho: "))
# perimetro = (ancho + ancho) + (alto + alto)
perimetro = (alto + ancho) * 2
area = alto * ancho
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')