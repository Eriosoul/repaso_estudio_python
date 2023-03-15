nombre = str(input("Introduce el nombre del libro: "))
id = int(input("Introduce el id del libro: "))
precio = float(input("Introduce el precio del libro: "))
envio = input("Envio gratuito? True/False: ")

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto'

print(f"Nombre: {nombre}")
print(f"Id: {id}")
print(f"precio: {precio}")
print(f"Envio gratuito?: {envio}")
