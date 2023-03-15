"""
Lista es un conjunto de elementos
"""

nombres = ['Juan', 'Karla', 'Karlo', 'Didi']
print(nombres)  # printera nuestra lista
print(nombres[0])
print(nombres[3])  # acceder a una celada
print(nombres[-1])  # acceder de manera inversa a una celda de nuestra lista

# Imprimir un rango
print(nombres[2:4])
print(nombres[0:3])

# Ir del inicio de la lista al indice ( sin incluirlo )
print(nombres [:3])
print(nombres [-3:])

# cambiar el valor
nombres[2] = 'Pepe'
print(nombres)
# interar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No hay mas nombres en la lista')

# preguntar el largo de una lista
# vemos la cantidad de elementos de una lista
print(len(nombres))

# agregar nuevo elemento
nombres.append('Lorena')
print(nombres)
# insertar un elemento en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# eliminar un elemento
nombres.remove('Juan')
print(nombres)
# eliminar el ultimo valor agregado
nombres.pop()
print(nombres)

# del para eliminar un indice
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)