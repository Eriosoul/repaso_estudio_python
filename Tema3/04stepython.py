# set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# largo de contenidos de nuestro set
print(len(planetas))
# revisar si un elemento esta presente
print('Marte' in planetas)  # si esta
print('Tierra' in planetas)  # no esta {'Marte', 'Jupiter', 'Venus'}
# agregar un elemento
planetas.add('Tierra')
print(planetas)

# no se puede duplicar elementos
planetas.add('Tierra')
print(planetas)

# eliminar elementos
planetas.remove('Marte')
print(planetas)
planetas.discard('Venus')  # si no se encuentra el elemento ni se borra ni manda error
print(planetas)

# para limirar el set
planetas.clear()
print(planetas)

# eliminar el set
del planetas
print(planetas)
