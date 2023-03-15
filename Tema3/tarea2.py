# dada la siguente tupla,
# crea una lista que solo incluya los numero menores a 5
menor: int = 5
tuple = (13, 1, 8, 3, 2, 5, 8)
lista = []
lista2 = []

for element in tuple:
    if element < 5:
        lista.append(element)
for element2 in tuple:
    if element2 == 13:
        lista2.append(element2)

print(lista)
print(lista2)