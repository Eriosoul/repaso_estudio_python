# dict (key, value)
diccionario: dict = {
    '_id': '4561',
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
# largo de contenido
print(len(diccionario))
# acceder a elemento debemos proporcionar la Key
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
# recorrer elementos
for termino in diccionario:
    print(termino)
# regresa los elementos on key y valor
for t, valor in diccionario.items():
    print(t, valor)

# solo ver las key
for t in diccionario.keys():
    print(t)
# solo ver los valores
for valor in diccionario.values():
    print(valor)

# comprobar existencia de algun elemento
print('_id' in diccionario) # si se encuentra
print('id' in diccionario) # no existe

# agregar elemento a diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# eliminar un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar diccionario
diccionario.clear()
print(diccionario)

# eliminar la variable de diccionario
del diccionario
print(diccionario)