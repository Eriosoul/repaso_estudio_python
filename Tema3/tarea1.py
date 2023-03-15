# sintaxixs en range
# ejercicio 1 interar de 0 a 10 e imprimier numeros divisibles 3
# ejercicio 2 crear rango de numeros de 2 a 6
# ejercicio 3 crear rando de 3 a 10 interar de 2 en 2
ejercicio1 = 0
while ejercicio1 <= 10:
    if ejercicio1 % 3 == 0:
        print(ejercicio1)
    ejercicio1 += 1
print("Rango con valores de inicio a fin")

ejercicio2 = 2
while ejercicio2 <= 6:
    print(ejercicio2)
    ejercicio2 += 1
print("fin de ejercicio 2")

ejercicio3 = 3
while ejercicio3 <= 10:
    print(ejercicio3)
    ejercicio3 += 2
print("fin de ejercicio 3")

# ====================================================
# Ahora con for - if
print('=================================================')
print('Rango de 0 a 10 con numeros')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2 numero de 2 a 6
print('Rango de 2 a 6 con numeros')
rango = range(2, 7)
for i in rango:
    print(i)

print('Rango de 3 a 10 con numeros')
rango2 = range(3, 11, 2) # del 3 al 10 con incrementos de 2
for a in rango2:
    print(a)

for palabra in ["palabra1", "palabra2"]:
    print(palabra)

palabras: list[str] = ["palabra1", "palabra2"]
for i in range(len(palabras)):
    print(palabras[i])