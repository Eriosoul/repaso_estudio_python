# funcion imput
resultado = input("Escribe un mensaje: ")

print(resultado)
print("Fin del programa")

# Forma erronea de pedir datos int
# en este caso lo que hace nuestro codigo seria concatenar
print("Modo erroneo de hacer una suma")
n1 = input("Escribe un numer: ")
n2 = input("escribe el segundo numero: ")
resultado2 = n1 + n2
print("El resultado es:", resultado2)

# para evitar ese fallo deberiamos de hacer
print("Modo correcto de hacer una suma")
num1 = int(input("Ecribe el primer numero: "))
num2 = int(input("Ecribe el segundo numero: "))
resultado3 = num1 + num2
print(resultado3)
